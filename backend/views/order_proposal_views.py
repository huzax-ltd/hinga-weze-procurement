import json
import os

from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import defaultfilters
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from app import settings
from app.models import Operators, Orders, Order_Attachments, Order_Proposals, Notifications
from app.utils import Utils
from backend.forms.order_forms import OrderUploadAttachmentForm
from backend.forms.order_proposal_forms import OrderProposalSearchIndexForm, OrderProposalCreateForm, \
    OrderProposalViewForm, OrderProposalEvaluateForm, OrderProposalSelectForm
from backend.tables.order_proposal_tables import Order_ProposalsTable


# noinspection PyUnusedLocal
def index(request, pk):
    template_url = 'order-proposals/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            try:
                model = Orders.objects.get(order_id=pk)
                search_form = OrderProposalSearchIndexForm(request.POST or None)
                objects = None

                objects = Order_Proposals.objects.filter(orders_order_id=model.order_id).exclude(
                    order_proposal_supplier_rf_number='').all()

                if request.method == 'POST' and search_form.is_valid():
                    display_search = True
                    table = Order_ProposalsTable(objects)
                else:
                    display_search = False
                    table = Order_ProposalsTable(objects)

                table.set_auth_permissions(auth_permissions)
                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                        'title': Order_Proposals.TITLE,
                        'name': Order_Proposals.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'table': table,
                        'search_form': search_form,
                        'display_search': display_search,
                        'model': model,
                        'index_url': reverse("orders_index"),
                        'view_url': reverse("orders_view", kwargs={'pk': pk}),
                        'reload_url': reverse("order_proposals_index", kwargs={'pk': pk}),
                        'select_single_url': reverse("order_proposals_select_single"),
                        'select_multiple_url': reverse("order_proposals_select_multiple"),
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


@csrf_exempt
# noinspection PyUnusedLocal
def select_single(request):
    if request.is_ajax():
        operator = Operators.login_required(request)
        if operator is None:
            # Operators.set_redirect_field_name(request, request.path)
            # return redirect(reverse("operators_signin"))
            return HttpResponse('signin', content_type='text/plain')
        else:
            auth_permissions = Operators.get_auth_permissions(operator)
            action = request.POST['action']
            id = request.POST['id']
            if action != '' and id is not None:
                if action == 'order-proposal-approve':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Order_Proposals.objects.get(order_proposal_id=id)

                            model.order_proposal_approval_updated_at = Utils.get_current_datetime_utc()
                            model.order_proposal_approval_updated_id = operator.operator_id
                            model.order_proposal_approval_updated_by = operator.operator_name
                            model.order_proposal_approval_updated_department = operator.operator_department
                            model.order_proposal_approval_updated_role = operator.operator_role
                            model.order_proposal_status = Order_Proposals.STATUS_APPROVED
                            model.save()

                            # sending notification to COP and OPM
                            operators = Operators.objects.filter(
                                Q(operator_role=Operators.ROLE_COP) |
                                Q(operator_role=Operators.ROLE_OPM))
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER_PROPOSAL,
                                    model.order_proposal_id,
                                    "Some vendors are selected to review.",
                                    "/backend/order-proposals/index/" + str(model.orders_order_id) + "/"
                                )

                            messages.success(request, 'Updated successfully.')
                        except(TypeError, ValueError, OverflowError, Order_Proposals.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-proposal-reject':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Order_Proposals.objects.get(order_proposal_id=id)

                            model.order_proposal_approval_updated_at = Utils.get_current_datetime_utc()
                            model.order_proposal_approval_updated_id = operator.operator_id
                            model.order_proposal_approval_updated_by = operator.operator_name
                            model.order_proposal_approval_updated_department = operator.operator_department
                            model.order_proposal_approval_updated_role = operator.operator_role
                            model.order_proposal_status = Order_Proposals.STATUS_REJECTED
                            model.save()

                            messages.success(request, 'Updated successfully.')
                        except(TypeError, ValueError, OverflowError, Order_Proposals.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                return HttpResponse('success', content_type='text/plain')
            else:
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')
    else:
        return HttpResponseForbidden('Forbidden', content_type='text/plain')


@csrf_exempt
# noinspection PyUnusedLocal
def select_multiple(request):
    if request.is_ajax():
        operator = Operators.login_required(request)
        if operator is None:
            # Operators.set_redirect_field_name(request, request.path)
            # return redirect(reverse("operators_signin"))
            return HttpResponse('signin', content_type='text/plain')
        else:
            auth_permissions = Operators.get_auth_permissions(operator)
            action = request.POST['action']
            ids = request.POST['ids']
            try:
                ids = ids.split(",")
            except(TypeError, ValueError, OverflowError):
                ids = None
            if action != '' and ids is not None:
                return HttpResponse('success', content_type='text/plain')
            else:
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')
    else:
        return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def create(request, pk, code):
    template_url = 'order-proposals/create.html'
    try:
        order = Orders.objects.get(order_id=pk)

        if code == str(0):
            model = Order_Proposals()
            model.order_proposal_code = Order_Proposals.generate_random_number('order_proposal_code', 8)
            model.orders_order_id = order.order_id
            model.order_proposal_supplier_category = order.order_supplier_category

            model.order_proposal_supplier_company_type = ''
            model.order_proposal_supplier_title = ''
            model.order_proposal_supplier_details = ''
            model.order_proposal_supplier_rf_number = ''
            model.order_proposal_supplier_proposal_title = ''
            model.order_proposal_supplier_legal_representatives = ''
            model.order_proposal_supplier_address_plot_no = ''
            model.order_proposal_supplier_address_street = ''
            model.order_proposal_supplier_address_av_no = ''
            model.order_proposal_supplier_address_sector = ''
            model.order_proposal_supplier_address_district = ''
            model.order_proposal_supplier_address_country = ''
            model.order_proposal_supplier_contact_phone_number = ''
            model.order_proposal_supplier_contact_email_id = ''
            model.order_proposal_supplier_tin_number = ''
            model.order_proposal_supplier_bank_account_details = ''
            model.order_proposal_supplier_previous_reference1_name = ''
            model.order_proposal_supplier_previous_reference1_contact_person = ''
            model.order_proposal_supplier_previous_reference1_contact_number = ''
            model.order_proposal_supplier_previous_reference1_contact_email_id = ''
            model.order_proposal_supplier_previous_reference2_name = ''
            model.order_proposal_supplier_previous_reference2_contact_person = ''
            model.order_proposal_supplier_previous_reference2_contact_number = ''
            model.order_proposal_supplier_previous_reference2_contact_email_id = ''
            model.order_proposal_supplier_previous_reference3_name = ''
            model.order_proposal_supplier_previous_reference3_contact_person = ''
            model.order_proposal_supplier_previous_reference3_contact_number = ''
            model.order_proposal_supplier_previous_reference3_contact_email_id = ''

            model.order_proposal_cost = 0
            model.order_proposal_evaluated_score = 0
            model.order_proposal_evaluation_details = ''

            model.order_proposal_created_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
            model.order_proposal_created_id = 0
            model.order_proposal_created_by = ''
            model.order_proposal_created_department = ''
            model.order_proposal_created_role = ''

            model.order_proposal_updated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
            model.order_proposal_updated_id = 0
            model.order_proposal_updated_by = ''
            model.order_proposal_updated_department = ''
            model.order_proposal_updated_role = ''

            model.order_proposal_evaluated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
            model.order_proposal_evaluated_id = ''
            model.order_proposal_evaluated_by = ''
            model.order_proposal_evaluated_department = ''
            model.order_proposal_evaluated_role = ''

            model.order_proposal_approval_updated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
            model.order_proposal_approval_updated_id = ''
            model.order_proposal_approval_updated_by = ''
            model.order_proposal_approval_updated_department = ''
            model.order_proposal_approval_updated_role = ''

            model.order_proposal_selected_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
            model.order_proposal_selected_id = 0
            model.order_proposal_selected_by = ''
            model.order_proposal_selected_department = ''
            model.order_proposal_selected_role = ''

            model.order_proposal_acknowledged_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
            model.order_proposal_acknowledged_id = ''
            model.order_proposal_acknowledged_by = ''
            model.order_proposal_acknowledged_department = ''
            model.order_proposal_acknowledged_role = ''

            model.order_proposal_status = Order_Proposals.STATUS_PENDING
            # noinspection PyCallByClass,PyTypeChecker
            model.save('Created')
        else:
            model = Order_Proposals.objects.get(order_proposal_code=code)

        order_attachments = Order_Attachments.objects.filter(
            Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_BUSINESS_LICENSE) &
            Q(order_attachment_type_id=model.order_proposal_code)
        ).order_by('-order_attachment_id').all()

        order_attachment1 = ''
        if order_attachments.count() != 0:
            order_attachment1 = order_attachments[0]

        order_attachments = Order_Attachments.objects.filter(
            Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_OFFER_LETTER) &
            Q(order_attachment_type_id=model.order_proposal_code)
        ).order_by('-order_attachment_id').all()

        order_attachment2 = ''
        if order_attachments.count() != 0:
            order_attachment2 = order_attachments[0]

        order_attachments = Order_Attachments.objects.filter(
            Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_QUOTATION) &
            Q(order_attachment_type_id=model.order_proposal_code)
        ).order_by('-order_attachment_id').all()

        order_attachment3 = ''
        if order_attachments.count() != 0:
            order_attachment3 = order_attachments[0]

        order_attachments = Order_Attachments.objects.filter(
            Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_VAT_REGISTRATION) &
            Q(order_attachment_type_id=model.order_proposal_code)
        ).order_by('-order_attachment_id').all()

        order_attachment4 = ''
        if order_attachments.count() != 0:
            order_attachment4 = order_attachments[0]

        order_attachments = Order_Attachments.objects.filter(
            Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_OTHER_DOCUMENT) &
            Q(order_attachment_type_id=model.order_proposal_code) &
            Q(order_attachment_file_id=1)
        ).order_by('-order_attachment_id').all()

        order_attachment5 = ''
        if order_attachments.count() != 0:
            order_attachment5 = order_attachments[0]

        order_attachments = Order_Attachments.objects.filter(
            Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_OTHER_DOCUMENT) &
            Q(order_attachment_type_id=model.order_proposal_code) &
            Q(order_attachment_file_id=2)
        ).order_by('-order_attachment_id').all()

        order_attachment6 = ''
        if order_attachments.count() != 0:
            order_attachment6 = order_attachments[0]

        order_attachments = Order_Attachments.objects.filter(
            Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT) &
            Q(order_attachment_type_id=model.order_proposal_code) &
            Q(order_attachment_file_id=1)
        ).order_by('-order_attachment_id').all()

        order_attachment7 = ''
        if order_attachments.count() != 0:
            order_attachment7 = order_attachments[0]

        order_attachments = Order_Attachments.objects.filter(
            Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT) &
            Q(order_attachment_type_id=model.order_proposal_code) &
            Q(order_attachment_file_id=2)
        ).order_by('-order_attachment_id').all()

        order_attachment8 = ''
        if order_attachments.count() != 0:
            order_attachment8 = order_attachments[0]

        order_attachments = Order_Attachments.objects.filter(
            Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT) &
            Q(order_attachment_type_id=model.order_proposal_code) &
            Q(order_attachment_file_id=3)
        ).order_by('-order_attachment_id').all()

        order_attachment9 = ''
        if order_attachments.count() != 0:
            order_attachment9 = order_attachments[0]

        if request.method == 'POST':

            form = OrderProposalCreateForm(request.POST)

            # noinspection PyArgumentList
            if form.is_valid():

                model.order_proposal_supplier_company_type = form.cleaned_data['company_type']
                model.order_proposal_supplier_title = form.cleaned_data['title']
                model.order_proposal_supplier_details = form.cleaned_data['details']
                model.order_proposal_supplier_rf_number = form.cleaned_data['rf_number']
                model.order_proposal_supplier_proposal_title = form.cleaned_data['proposal_title']
                model.order_proposal_supplier_legal_representatives = form.cleaned_data['legal_representatives']
                model.order_proposal_supplier_address_plot_no = form.cleaned_data['address_plot_no']
                model.order_proposal_supplier_address_street = form.cleaned_data['address_street']
                model.order_proposal_supplier_address_av_no = form.cleaned_data['address_av_no']
                model.order_proposal_supplier_address_sector = form.cleaned_data['address_sector']
                model.order_proposal_supplier_address_district = form.cleaned_data['address_district']
                model.order_proposal_supplier_address_country = form.cleaned_data['address_country']
                model.order_proposal_supplier_contact_phone_number = form.cleaned_data['contact_phone_number']
                model.order_proposal_supplier_contact_email_id = form.cleaned_data['contact_email_id']
                model.order_proposal_supplier_tin_number = form.cleaned_data['tin_number']
                model.order_proposal_supplier_bank_account_details = form.cleaned_data['bank_account_details']
                model.order_proposal_supplier_previous_reference1_name = form.cleaned_data['previous_reference1_name']
                model.order_proposal_supplier_previous_reference1_contact_person = form.cleaned_data[
                    'previous_reference1_contact_person']
                model.order_proposal_supplier_previous_reference1_contact_number = form.cleaned_data[
                    'previous_reference1_contact_number']
                model.order_proposal_supplier_previous_reference1_contact_email_id = form.cleaned_data[
                    'previous_reference1_contact_email_id']
                model.order_proposal_supplier_previous_reference2_name = form.cleaned_data['previous_reference2_name']
                model.order_proposal_supplier_previous_reference2_contact_person = form.cleaned_data[
                    'previous_reference2_contact_person']
                model.order_proposal_supplier_previous_reference2_contact_number = form.cleaned_data[
                    'previous_reference2_contact_number']
                model.order_proposal_supplier_previous_reference2_contact_email_id = form.cleaned_data[
                    'previous_reference2_contact_email_id']
                model.order_proposal_supplier_previous_reference3_name = form.cleaned_data['previous_reference3_name']
                model.order_proposal_supplier_previous_reference3_contact_person = form.cleaned_data[
                    'previous_reference3_contact_person']
                model.order_proposal_supplier_previous_reference3_contact_number = form.cleaned_data[
                    'previous_reference3_contact_number']
                model.order_proposal_supplier_previous_reference3_contact_email_id = form.cleaned_data[
                    'previous_reference3_contact_email_id']

                if model.order_proposal_created_at == settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE:
                    model.order_proposal_created_at = Utils.get_current_datetime_utc()
                    model.order_proposal_created_id = 0
                    model.order_proposal_created_by = ''
                    model.order_proposal_created_department = ''
                    model.order_proposal_created_role = ''

                    model.order_proposal_updated_at = Utils.get_current_datetime_utc()
                    model.order_proposal_updated_id = 0
                    model.order_proposal_updated_by = ''
                    model.order_proposal_updated_department = ''
                    model.order_proposal_updated_role = ''

                model.order_proposal_evaluated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                model.order_proposal_evaluated_id = ''
                model.order_proposal_evaluated_by = ''
                model.order_proposal_evaluated_department = ''
                model.order_proposal_evaluated_role = ''

                model.order_proposal_approval_updated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                model.order_proposal_approval_updated_id = ''
                model.order_proposal_approval_updated_by = ''
                model.order_proposal_approval_updated_department = ''
                model.order_proposal_approval_updated_role = ''

                model.order_proposal_acknowledged_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                model.order_proposal_acknowledged_id = ''
                model.order_proposal_acknowledged_by = ''
                model.order_proposal_acknowledged_department = ''
                model.order_proposal_acknowledged_role = ''

                model.order_proposal_status = Order_Proposals.STATUS_PENDING
                # noinspection PyCallByClass,PyTypeChecker
                model.save()

                # sending notification to Officer
                if order.order_assigned_to_id != str(0):
                    operators = Operators.objects.all().filter(
                        Q(operator_id=order.order_assigned_to_id)
                    )
                else:
                    operators = Operators.objects.all().filter(
                        Q(operator_department=Operators.DEPARTMENT_DAF) &
                        Q(operator_role=order.order_assigned_to_role)
                    )

                for item in operators:
                    Notifications.add_notification(
                        Notifications.TYPE_SUPPLIER,
                        model.order_proposal_id,
                        Notifications.TYPE_OPERATOR,
                        item.operator_id,
                        Notifications.TYPE_ORDER_PROPOSAL,
                        model.order_proposal_id,
                        "Submitted a proposal to evaluate.",
                        "/backend/order-proposals/view/internal/" + str(model.order_proposal_id) + "/"
                    )

                # sending email confirmation mail
                if settings.IS_LOCAL:
                    domain = settings.BACKEND_DOMAIN_LOCAL
                    logo_url = settings.STATIC_LOCAL + "app/logo-transparent-white.png"
                else:
                    domain = settings.BACKEND_DOMAIN_PROD
                    logo_url = settings.STATIC_PROD + "app/logo-transparent-white.png"

                # contact_url = '{domain}/{path}'.format(domain=domain, path=settings.CONTACT_URL)
                contact_url = settings.APP_CONSTANT_COMPANY_WEBSITE
                link_url = '{domain}/{path}'.format(
                    domain=domain,
                    path="order-proposals/create/" + str(model.orders_order_id) + "/" + str(
                        model.order_proposal_code) + "/"
                )
                link_name = "View Details"
                html_content = render_to_string(
                    'email/email-info-with-link.html',
                    {
                        'logo_url': logo_url,
                        'contact_url': contact_url,
                        'link_url': link_url,
                        'link_name': link_name,
                        'name': model.order_proposal_supplier_title,
                        'message': 'Thank you for submitting your proposal, we will review your proposal and get back to you soon.',
                    }
                )
                send_mail(
                    settings.EMAIL_NOTIFICATION_SUBJECT,
                    settings.EMAIL_NOTIFICATION_MESSAGE,
                    settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                    [model.order_proposal_supplier_contact_email_id],
                    fail_silently=False,
                    html_message=html_content,
                )

                messages.info(request,
                              'Your proposal request has been submitted successfully.')

                return redirect(
                    reverse("order_proposals_create", args=[model.orders_order_id, model.order_proposal_code]))
            else:
                messages.error(request, str(form.errors))
                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                        'title': Orders.TITLE,
                        'name': Orders.NAME,
                        'form': form,
                        'model': model,
                        'order': order,
                        'select_single_url': reverse("orders_select_single_external"),
                        'order_attachment1': order_attachment1,
                        'order_attachment2': order_attachment2,
                        'order_attachment3': order_attachment3,
                        'order_attachment4': order_attachment4,
                        'order_attachment5': order_attachment5,
                        'order_attachment6': order_attachment6,
                        'order_attachment7': order_attachment7,
                        'order_attachment8': order_attachment8,
                        'order_attachment9': order_attachment9,
                    }
                )
        else:
            if model.order_proposal_status == Order_Proposals.STATUS_PENDING:
                form = OrderProposalCreateForm(
                    initial={
                        'company_type': model.order_proposal_supplier_company_type,
                        'title': model.order_proposal_supplier_title,
                        'details': model.order_proposal_supplier_details,
                        'rf_number': model.order_proposal_supplier_rf_number,
                        'proposal_title': model.order_proposal_supplier_proposal_title,
                        'legal_representatives': model.order_proposal_supplier_legal_representatives,
                        'address_plot_no': model.order_proposal_supplier_address_plot_no,
                        'address_street': model.order_proposal_supplier_address_street,
                        'address_av_no': model.order_proposal_supplier_address_av_no,
                        'address_sector': model.order_proposal_supplier_address_sector,
                        'address_district': model.order_proposal_supplier_address_district,
                        'address_country': model.order_proposal_supplier_address_country,
                        'contact_phone_number': model.order_proposal_supplier_contact_phone_number,
                        'contact_email_id': model.order_proposal_supplier_contact_email_id,
                        'tin_number': model.order_proposal_supplier_tin_number,
                        'bank_account_details': model.order_proposal_supplier_bank_account_details,
                        'previous_reference1_name': model.order_proposal_supplier_previous_reference1_name,
                        'previous_reference1_contact_person': model.order_proposal_supplier_previous_reference1_contact_person,
                        'previous_reference1_contact_number': model.order_proposal_supplier_previous_reference1_contact_number,
                        'previous_reference1_contact_email_id': model.order_proposal_supplier_previous_reference1_contact_email_id,
                        'previous_reference2_name': model.order_proposal_supplier_previous_reference2_name,
                        'previous_reference2_contact_person': model.order_proposal_supplier_previous_reference2_contact_person,
                        'previous_reference2_contact_number': model.order_proposal_supplier_previous_reference2_contact_number,
                        'previous_reference2_contact_email_id': model.order_proposal_supplier_previous_reference2_contact_email_id,
                        'previous_reference3_name': model.order_proposal_supplier_previous_reference3_name,
                        'previous_reference3_contact_person': model.order_proposal_supplier_previous_reference3_contact_person,
                        'previous_reference3_contact_number': model.order_proposal_supplier_previous_reference3_contact_number,
                        'previous_reference3_contact_email_id': model.order_proposal_supplier_previous_reference3_contact_email_id,
                    }
                )
            else:
                template_url = 'order-proposals/view.html'
                form = OrderProposalViewForm(
                    initial={
                        'company_type': model.order_proposal_supplier_company_type,
                        'title': model.order_proposal_supplier_title,
                        'details': model.order_proposal_supplier_details,
                        'rf_number': model.order_proposal_supplier_rf_number,
                        'proposal_title': model.order_proposal_supplier_proposal_title,
                        'legal_representatives': model.order_proposal_supplier_legal_representatives,
                        'address_plot_no': model.order_proposal_supplier_address_plot_no,
                        'address_street': model.order_proposal_supplier_address_street,
                        'address_av_no': model.order_proposal_supplier_address_av_no,
                        'address_sector': model.order_proposal_supplier_address_sector,
                        'address_district': model.order_proposal_supplier_address_district,
                        'address_country': model.order_proposal_supplier_address_country,
                        'contact_phone_number': model.order_proposal_supplier_contact_phone_number,
                        'contact_email_id': model.order_proposal_supplier_contact_email_id,
                        'tin_number': model.order_proposal_supplier_tin_number,
                        'bank_account_details': model.order_proposal_supplier_bank_account_details,
                        'previous_reference1_name': model.order_proposal_supplier_previous_reference1_name,
                        'previous_reference1_contact_person': model.order_proposal_supplier_previous_reference1_contact_person,
                        'previous_reference1_contact_number': model.order_proposal_supplier_previous_reference1_contact_number,
                        'previous_reference1_contact_email_id': model.order_proposal_supplier_previous_reference1_contact_email_id,
                        'previous_reference2_name': model.order_proposal_supplier_previous_reference2_name,
                        'previous_reference2_contact_person': model.order_proposal_supplier_previous_reference2_contact_person,
                        'previous_reference2_contact_number': model.order_proposal_supplier_previous_reference2_contact_number,
                        'previous_reference2_contact_email_id': model.order_proposal_supplier_previous_reference2_contact_email_id,
                        'previous_reference3_name': model.order_proposal_supplier_previous_reference3_name,
                        'previous_reference3_contact_person': model.order_proposal_supplier_previous_reference3_contact_person,
                        'previous_reference3_contact_number': model.order_proposal_supplier_previous_reference3_contact_number,
                        'previous_reference3_contact_email_id': model.order_proposal_supplier_previous_reference3_contact_email_id,
                    }
                )

        return render(
            request, template_url,
            {
                'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                'title': Orders.TITLE,
                'name': Orders.NAME,
                'form': form,
                'model': model,
                'order': order,
                'select_single_url': reverse("orders_select_single_external"),
                'order_attachment1': order_attachment1,
                'order_attachment2': order_attachment2,
                'order_attachment3': order_attachment3,
                'order_attachment4': order_attachment4,
                'order_attachment5': order_attachment5,
                'order_attachment6': order_attachment6,
                'order_attachment7': order_attachment7,
                'order_attachment8': order_attachment8,
                'order_attachment9': order_attachment9,
            }
        )
    except(TypeError, ValueError, OverflowError, Orders.DoesNotExist, Order_Proposals.DoesNotExist):
        return HttpResponseNotFound('Not Found', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def view_internal(request, pk):
    template_url = 'order-proposals/view-internal.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            try:
                model = Order_Proposals.objects.get(order_proposal_id=pk)
                order = Orders.objects.get(order_id=model.orders_order_id)

                order_attachments = Order_Attachments.objects.filter(
                    Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_BUSINESS_LICENSE) &
                    Q(order_attachment_type_id=model.order_proposal_code)
                ).order_by('-order_attachment_id').all()

                order_attachment1 = ''
                if order_attachments.count() != 0:
                    order_attachment1 = order_attachments[0]

                order_attachments = Order_Attachments.objects.filter(
                    Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_OFFER_LETTER) &
                    Q(order_attachment_type_id=model.order_proposal_code)
                ).order_by('-order_attachment_id').all()

                order_attachment2 = ''
                if order_attachments.count() != 0:
                    order_attachment2 = order_attachments[0]

                order_attachments = Order_Attachments.objects.filter(
                    Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_QUOTATION) &
                    Q(order_attachment_type_id=model.order_proposal_code)
                ).order_by('-order_attachment_id').all()

                order_attachment3 = ''
                if order_attachments.count() != 0:
                    order_attachment3 = order_attachments[0]

                order_attachments = Order_Attachments.objects.filter(
                    Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_VAT_REGISTRATION) &
                    Q(order_attachment_type_id=model.order_proposal_code)
                ).order_by('-order_attachment_id').all()

                order_attachment4 = ''
                if order_attachments.count() != 0:
                    order_attachment4 = order_attachments[0]

                order_attachments = Order_Attachments.objects.filter(
                    Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_OTHER_DOCUMENT) &
                    Q(order_attachment_type_id=model.order_proposal_code) &
                    Q(order_attachment_file_id=1)
                ).order_by('-order_attachment_id').all()

                order_attachment5 = ''
                if order_attachments.count() != 0:
                    order_attachment5 = order_attachments[0]

                order_attachments = Order_Attachments.objects.filter(
                    Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_OTHER_DOCUMENT) &
                    Q(order_attachment_type_id=model.order_proposal_code) &
                    Q(order_attachment_file_id=2)
                ).order_by('-order_attachment_id').all()

                order_attachment6 = ''
                if order_attachments.count() != 0:
                    order_attachment6 = order_attachments[0]

                order_attachments = Order_Attachments.objects.filter(
                    Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT) &
                    Q(order_attachment_type_id=model.order_proposal_code) &
                    Q(order_attachment_file_id=1)
                ).order_by('-order_attachment_id').all()

                order_attachment7 = ''
                if order_attachments.count() != 0:
                    order_attachment7 = order_attachments[0]

                order_attachments = Order_Attachments.objects.filter(
                    Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT) &
                    Q(order_attachment_type_id=model.order_proposal_code) &
                    Q(order_attachment_file_id=2)
                ).order_by('-order_attachment_id').all()

                order_attachment8 = ''
                if order_attachments.count() != 0:
                    order_attachment8 = order_attachments[0]

                order_attachments = Order_Attachments.objects.filter(
                    Q(order_attachment_type=Order_Attachments.TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT) &
                    Q(order_attachment_type_id=model.order_proposal_code) &
                    Q(order_attachment_file_id=3)
                ).order_by('-order_attachment_id').all()

                order_attachment9 = ''
                if order_attachments.count() != 0:
                    order_attachment9 = order_attachments[0]

                form = OrderProposalViewForm(
                    initial={
                        'company_type': model.order_proposal_supplier_company_type,
                        'title': model.order_proposal_supplier_title,
                        'details': model.order_proposal_supplier_details,
                        'rf_number': model.order_proposal_supplier_rf_number,
                        'proposal_title': model.order_proposal_supplier_proposal_title,
                        'legal_representatives': model.order_proposal_supplier_legal_representatives,
                        'address_plot_no': model.order_proposal_supplier_address_plot_no,
                        'address_street': model.order_proposal_supplier_address_street,
                        'address_av_no': model.order_proposal_supplier_address_av_no,
                        'address_sector': model.order_proposal_supplier_address_sector,
                        'address_district': model.order_proposal_supplier_address_district,
                        'address_country': model.order_proposal_supplier_address_country,
                        'contact_phone_number': model.order_proposal_supplier_contact_phone_number,
                        'contact_email_id': model.order_proposal_supplier_contact_email_id,
                        'tin_number': model.order_proposal_supplier_tin_number,
                        'bank_account_details': model.order_proposal_supplier_bank_account_details,
                        'previous_reference1_name': model.order_proposal_supplier_previous_reference1_name,
                        'previous_reference1_contact_person': model.order_proposal_supplier_previous_reference1_contact_person,
                        'previous_reference1_contact_number': model.order_proposal_supplier_previous_reference1_contact_number,
                        'previous_reference1_contact_email_id': model.order_proposal_supplier_previous_reference1_contact_email_id,
                        'previous_reference2_name': model.order_proposal_supplier_previous_reference2_name,
                        'previous_reference2_contact_person': model.order_proposal_supplier_previous_reference2_contact_person,
                        'previous_reference2_contact_number': model.order_proposal_supplier_previous_reference2_contact_number,
                        'previous_reference2_contact_email_id': model.order_proposal_supplier_previous_reference2_contact_email_id,
                        'previous_reference3_name': model.order_proposal_supplier_previous_reference3_name,
                        'previous_reference3_contact_person': model.order_proposal_supplier_previous_reference3_contact_person,
                        'previous_reference3_contact_number': model.order_proposal_supplier_previous_reference3_contact_number,
                        'previous_reference3_contact_email_id': model.order_proposal_supplier_previous_reference3_contact_email_id,
                    }
                )

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                        'title': Orders.TITLE,
                        'name': Orders.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'model': model,
                        'order': order,
                        'index_url': reverse("order_proposals_index", kwargs={'pk': order.order_id}),
                        'select_single_url': reverse("order_proposals_select_single"),
                        'order_attachment1': order_attachment1,
                        'order_attachment2': order_attachment2,
                        'order_attachment3': order_attachment3,
                        'order_attachment4': order_attachment4,
                        'order_attachment5': order_attachment5,
                        'order_attachment6': order_attachment6,
                        'order_attachment7': order_attachment7,
                        'order_attachment8': order_attachment8,
                        'order_attachment9': order_attachment9,
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist, Order_Proposals.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


@csrf_exempt
# noinspection PyUnusedLocal, PyShadowingBuiltins
def upload_attachments_external(request):
    action = request.POST['action']
    id = request.POST['id']
    if action != '' and id is not None:
        if action == 'upload-order-proposal-business-license' or \
                action == 'upload-order-proposal-offer-letter' or \
                action == 'upload-order-proposal-quotation' or \
                action == 'upload-order-proposal-vat-registration' or \
                action == 'upload-order-proposal-other-document' or \
                action == 'upload-order-proposal-reference-document':
            order = Orders.objects.get(order_id=id)
            if order is not None:

                model = Order_Attachments()
                model.orders_order_id = order.order_id

                model.order_attachment_type_id = 0
                model.order_attachment_file_id = 0

                if action == 'upload-order-proposal-business-license':
                    model.order_attachment_type = Order_Attachments.TYPE_ORDER_PROPOSAL_BUSINESS_LICENSE

                if action == 'upload-order-proposal-offer-letter':
                    model.order_attachment_type = Order_Attachments.TYPE_ORDER_PROPOSAL_OFFER_LETTER

                if action == 'upload-order-proposal-quotation':
                    model.order_attachment_type = Order_Attachments.TYPE_ORDER_PROPOSAL_QUOTATION

                if action == 'upload-order-proposal-vat-registration':
                    model.order_attachment_type = Order_Attachments.TYPE_ORDER_PROPOSAL_VAT_REGISTRATION

                if action == 'upload-order-proposal-other-document':
                    model.order_attachment_type = Order_Attachments.TYPE_ORDER_PROPOSAL_OTHER_DOCUMENT

                if action == 'upload-order-proposal-reference-document':
                    model.order_attachment_type = Order_Attachments.TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT

                if action == 'upload-order-proposal-business-license' or \
                        action == 'upload-order-proposal-offer-letter' or \
                        action == 'upload-order-proposal-quotation' or \
                        action == 'upload-order-proposal-vat-registration' or \
                        action == 'upload-order-proposal-other-document' or \
                        action == 'upload-order-proposal-reference-document':
                    code = request.POST['code']
                    model.order_attachment_type_id = code

                if action == 'upload-order-proposal-other-document' or \
                        action == 'upload-order-proposal-reference-document':
                    number = request.POST['number']
                    model.order_attachment_file_id = number

                model.order_attachment_file_uploaded_at = Utils.get_current_datetime_utc()
                model.order_attachment_file_uploaded_id = ''
                model.order_attachment_file_uploaded_by = ''
                model.order_attachment_file_uploaded_department = ''
                model.order_attachment_file_uploaded_role = ''

                import magic
                mime = magic.Magic(mime=True)
                # for file in request.FILES.getlist('order_attachment_file_path'):
                form = OrderUploadAttachmentForm(request.POST, request.FILES)
                if form.is_valid():
                    try:
                        original_filename = form.cleaned_data['order_attachment_file_path']

                        ext = original_filename.split('.')[-1]
                        new_filename = 'order_email_' + str(order.order_code) + '_' + str(
                            Utils.get_epochtime_ms()) + '.' + str(ext)
                        temp_file_path = settings.MEDIA_ROOT + 'temp/' + str(original_filename)
                        order_attachment_file_path = settings.MEDIA_ROOT + Order_Attachments.UPLOAD_PATH + str(
                            new_filename)
                        os.rename(temp_file_path, order_attachment_file_path)
                        url = Order_Attachments.UPLOAD_PATH + new_filename
                        size = str(os.path.getsize(order_attachment_file_path))
                        model.order_attachment_file_name = original_filename
                        model.order_attachment_file_path = url
                        model.order_attachment_file_type = str(mime.from_file(order_attachment_file_path))
                        model.order_attachment_file_size = size
                        model.save()

                        # return HttpResponse('success', content_type='text/plain')
                        response = json.dumps({
                            'error': False,
                            'message': 'success',
                            'name': original_filename,
                            'url': model.order_attachment_file_path.url,
                            'size': defaultfilters.filesizeformat(size),
                            'id': model.order_attachment_id,
                        })
                        return HttpResponse(str(response), content_type='text/plain')

                    except Exception as e:
                        print('Exception: ' + str(e))
                        response = json.dumps({
                            'error': True,
                            'message': str(e),
                        })
                        return HttpResponse(str(response), content_type='text/plain')
                else:
                    print(form.errors)
                    response = json.dumps({
                        'error': True,
                        'message': str(form.errors),
                    })
                    return HttpResponse(str(response), content_type='text/plain')
            else:
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        response = json.dumps({
            'error': True,
            'message': 'Invalid action',
        })
        return HttpResponse(str(response), content_type='text/plain')
    else:
        return HttpResponseBadRequest('Bad Request', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def evaluate_proposal(request, pk):
    template_url = 'order-proposals/proposal-evaluate.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            try:
                model = Order_Proposals.objects.get(order_proposal_id=pk)
                if request.method == 'POST':

                    form = OrderProposalEvaluateForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.order_proposal_cost = form.cleaned_data['order_proposal_cost']
                        model.order_proposal_cost_currency = form.cleaned_data['order_proposal_cost_currency']
                        model.order_proposal_evaluated_score = form.cleaned_data['order_proposal_evaluated_score']
                        model.order_proposal_evaluation_details = form.cleaned_data['order_proposal_evaluation_details']

                        model.order_proposal_evaluated_at = Utils.get_current_datetime_utc()
                        model.order_proposal_evaluated_id = operator.operator_id
                        model.order_proposal_evaluated_by = operator.operator_name
                        model.order_proposal_evaluated_department = operator.operator_department
                        model.order_proposal_evaluated_role = operator.operator_role
                        model.order_proposal_status = Order_Proposals.STATUS_EVALUATED
                        model.save()

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("order_proposals_view_internal", args=[model.order_proposal_id]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("order_proposals_view_internal", args=[model.order_proposal_id]))
                else:
                    form = OrderProposalEvaluateForm(
                        initial={
                            'order_proposal_code': model.order_proposal_code,
                            'order_proposal_supplier_title': model.order_proposal_supplier_title,
                            'order_proposal_cost': model.order_proposal_cost,
                            'order_proposal_cost_currency': model.order_proposal_cost_currency,
                            'order_proposal_evaluated_score': model.order_proposal_evaluated_score,
                            'order_proposal_evaluation_details': model.order_proposal_evaluation_details,
                        }
                    )

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                        'title': Order_Proposals.TITLE,
                        'name': Order_Proposals.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'model': model,
                    }
                )
            except(TypeError, ValueError, OverflowError, Order_Proposals.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal
def api_dropdown_approved_proposals(request, code):
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        proposals = ""
        proposals += "<option value=''>--select--</option>"
        order = Orders.objects.get(order_code=code)
        objects = Order_Proposals.objects.filter(
            Q(orders_order_id=order.order_id) &
            (Q(order_proposal_status=Order_Proposals.STATUS_APPROVED) |
             Q(order_proposal_status=Order_Proposals.STATUS_SELECTED))
        )
        for item in objects:
            proposals += "<option value='" + str(
                item.order_proposal_id) + "'>" + str(item.order_proposal_code) + " (" + str(
                item.order_proposal_supplier_title) + ")</option>"

        return HttpResponse(proposals, content_type="text/plain")


# noinspection PyUnusedLocal, PyShadowingBuiltins
def select_proposal(request, pk):
    template_url = 'order-proposals/proposal-select.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            try:
                order = Orders.objects.get(order_id=pk)
                if request.method == 'POST':

                    form = OrderProposalSelectForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():

                        order_proposals = Order_Proposals.objects.filter(orders_order_id=pk,
                                                                         order_proposal_status=Order_Proposals.STATUS_SELECTED)
                        for order_proposal in order_proposals:
                            order_proposal.order_proposal_selected_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                            order_proposal.order_proposal_selected_id = ''
                            order_proposal.order_proposal_selected_by = ''
                            order_proposal.order_proposal_selected_department = ''
                            order_proposal.order_proposal_selected_role = ''
                            order_proposal.order_proposal_status = Order_Proposals.STATUS_APPROVED
                            order_proposal.save()

                        order_proposal_id = form.cleaned_data['order_proposal_id']
                        model = Order_Proposals.objects.get(order_proposal_id=order_proposal_id)

                        model.order_proposal_selected_at = Utils.get_current_datetime_utc()
                        model.order_proposal_selected_id = operator.operator_id
                        model.order_proposal_selected_by = operator.operator_name
                        model.order_proposal_selected_department = operator.operator_department
                        model.order_proposal_selected_role = operator.operator_role
                        model.order_proposal_status = Order_Proposals.STATUS_SELECTED
                        model.save()

                        order.order_proposal_id = model.order_proposal_id
                        order.order_proposal_selected_at = Utils.get_current_datetime_utc()
                        order.order_proposal_selected_id = operator.operator_id
                        order.order_proposal_selected_by = operator.operator_name
                        order.order_proposal_selected_department = operator.operator_department
                        order.order_proposal_selected_role = operator.operator_role
                        order.order_status = Orders.STATUS_PROPOSAL_SELECTED
                        order.save()

                        # sending email confirmation mail
                        if settings.IS_LOCAL:
                            domain = settings.BACKEND_DOMAIN_LOCAL
                            logo_url = settings.STATIC_LOCAL + "app/logo-transparent-white.png"
                        else:
                            domain = settings.BACKEND_DOMAIN_PROD
                            logo_url = settings.STATIC_PROD + "app/logo-transparent-white.png"

                        contact_url = settings.APP_CONSTANT_COMPANY_WEBSITE
                        link_url = '{domain}/{path}'.format(
                            domain=domain,
                            path="order-proposals/create/" + str(model.orders_order_id) + "/" + str(
                                model.order_proposal_code) + "/"
                        )
                        link_name = "View Details"

                        acknowledge_url = '/order-proposals/update/acknowledge/' + str(pk) + '/'
                        acknowledge_url = "<a title=\"link\" href=\"" + str(
                            domain) + acknowledge_url + "\" target=\"_blank\" rel=\"noopener\">link</a>"

                        message = "Congratulations your proposal has been approved. Please acknowledge by clicking on this " + acknowledge_url + "."
                        html_content = render_to_string(
                            'email/email-info-with-link.html',
                            {
                                'logo_url': logo_url,
                                'contact_url': contact_url,
                                'link_url': link_url,
                                'link_name': link_name,
                                'name': model.order_proposal_supplier_title,
                                'message': defaultfilters.safe(message),
                            }
                        )
                        send_mail(
                            settings.EMAIL_NOTIFICATION_SUBJECT,
                            settings.EMAIL_NOTIFICATION_MESSAGE,
                            settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                            [model.order_proposal_supplier_contact_email_id],
                            fail_silently=False,
                            html_message=html_content,
                        )

                        order_proposals = Order_Proposals.objects.filter(orders_order_id=pk).exclude(
                            order_proposal_status=Order_Proposals.STATUS_SELECTED)
                        for model in order_proposals:
                            # sending email confirmation mail
                            if settings.IS_LOCAL:
                                domain = settings.BACKEND_DOMAIN_LOCAL
                                logo_url = settings.STATIC_LOCAL + "app/logo-transparent-white.png"
                            else:
                                domain = settings.BACKEND_DOMAIN_PROD
                                logo_url = settings.STATIC_PROD + "app/logo-transparent-white.png"

                            contact_url = settings.APP_CONSTANT_COMPANY_WEBSITE
                            link_url = '{domain}/{path}'.format(
                                domain=domain,
                                path="order-proposals/create/" + str(model.orders_order_id) + "/" + str(
                                    model.order_proposal_code) + "/"
                            )
                            link_name = "View Details"
                            message = "Sorry, your proposal has been rejected."
                            html_content = render_to_string(
                                'email/email-info-with-link.html',
                                {
                                    'logo_url': logo_url,
                                    'contact_url': contact_url,
                                    'link_url': link_url,
                                    'link_name': link_name,
                                    'name': model.order_proposal_supplier_title,
                                    'message': defaultfilters.safe(message),
                                }
                            )
                            send_mail(
                                settings.EMAIL_NOTIFICATION_SUBJECT,
                                settings.EMAIL_NOTIFICATION_MESSAGE,
                                settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                                [model.order_proposal_supplier_contact_email_id],
                                fail_silently=False,
                                html_message=html_content,
                            )

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("order_proposals_index", args=[pk]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("order_proposals_index", args=[pk]))
                else:
                    form = OrderProposalSelectForm(
                        initial={
                            'order_id': order.order_code,
                            'order_proposal_id': '',
                        }
                    )

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                        'title': Order_Proposals.TITLE,
                        'name': Order_Proposals.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist, Order_Proposals.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


@csrf_exempt
# noinspection PyUnusedLocal, PyShadowingBuiltins
def acknowledge_proposal_external(request, pk):
    try:
        model = Order_Proposals.objects.get(order_proposal_id=pk)
        order = Orders.objects.get(order_id=model.orders_order_id)
        if model.order_proposal_status == Order_Proposals.STATUS_SELECTED:
            model.order_proposal_acknowledged_at = Utils.get_current_datetime_utc()
            model.order_proposal_acknowledged_id = ''
            model.order_proposal_acknowledged_by = ''
            model.order_proposal_acknowledged_department = ''
            model.order_proposal_acknowledged_role = ''
            model.order_proposal_status = Order_Proposals.STATUS_ACKNOWLEDGED
            model.save()

        # sending notification to Officer
        if order.order_assigned_to_id != str(0):
            operators = Operators.objects.all().filter(
                Q(operator_id=order.order_assigned_to_id)
            )
        else:
            operators = Operators.objects.all().filter(
                Q(operator_department=Operators.DEPARTMENT_DAF) &
                Q(operator_role=order.order_assigned_to_role)
            )

        for item in operators:
            Notifications.add_notification(
                Notifications.TYPE_SUPPLIER,
                model.order_proposal_id,
                Notifications.TYPE_OPERATOR,
                item.operator_id,
                Notifications.TYPE_ORDER_PROPOSAL,
                model.order_proposal_id,
                "Acknowledged proposal to generate purchase order.",
                "/backend/order-proposals/view/internal/" + str(model.order_proposal_id) + "/"
            )

        messages.success(request, 'Acknowledged successfully.')
        return redirect(reverse("order_proposals_create", args=[pk, model.order_proposal_code]))

    except(TypeError, ValueError, OverflowError, Orders.DoesNotExist, Order_Proposals.DoesNotExist):
        return HttpResponseNotFound('Not Found', content_type='text/plain')
