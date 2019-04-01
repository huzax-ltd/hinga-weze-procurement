import json
import os

from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import defaultfilters
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt

from app import settings
from app.models import Operators, Orders, Order_Items, Order_Approvals, Order_Proposals, \
    Notifications, NotificationsTimeline, Emails, Attachments
from app.utils import Utils
from backend.forms.general_forms import SendEmailForm
from backend.forms.order_forms import OrderSearchIndexForm, OrderCreateForm, OrderUpdateForm, OrderProcurementForm, \
    OrderAssignmentForm, OrderSupplierForm, OrderEmailToSupplierForm, OrderUploadAttachmentForm, \
    OrderPurchaseUpdateForm, OrderInvoiceUpdateForm, OrderPaymentVoucherUpdateForm
from backend.forms.order_item_forms import OrderItemSearchIndexForm
from backend.forms.order_proposal_forms import OrderProposalCreateForm, OrderProposalViewForm
from backend.tables.order_item_tables import OrderItemsTable
from backend.tables.order_tables import OrdersTable, OrdersStockTable


# noinspection PyUnusedLocal
def index(request):
    template_url = 'orders/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            search_form = OrderSearchIndexForm(request.POST or None)
            objects = None

            objects = Orders.get_filtered_orders(operator)

            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                table = OrdersTable(objects)
            else:
                display_search = False
                table = OrdersTable(objects)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                    'title': Orders.TITLE,
                    'name': Orders.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'search_form': search_form,
                    'display_search': display_search,
                    'index_url': reverse("orders_index"),
                    'select_multiple_url': reverse("orders_select_multiple"),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal
def index_operator(request):
    template_url = 'orders/index-operator.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            search_form = OrderSearchIndexForm(request.POST or None)
            objects = None

            objects = Orders.objects.filter(order_created_id=operator.operator_id)

            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                table = OrdersTable(objects)
            else:
                display_search = False
                table = OrdersTable(objects)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_PROCUREMENT_MY_REQUESTS,
                    'title': Orders.TITLE,
                    'name': Orders.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'search_form': search_form,
                    'display_search': display_search,
                    'index_url': reverse("orders_index"),
                    'select_multiple_url': reverse("orders_select_multiple"),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal
def index_stock(request):
    template_url = 'orders/index-stock.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            search_form = OrderSearchIndexForm(request.POST or None)
            objects = None

            objects = Orders.objects.all()
            objects.filter(order_status=Orders.STATUS_ACKNOWLEDGED)

            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                table = OrdersStockTable(objects)
            else:
                display_search = False
                table = OrdersStockTable(objects)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_PROCUREMENT_PO_REQUESTS,
                    'title': Orders.TITLE,
                    'name': Orders.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'search_form': search_form,
                    'display_search': display_search,
                    'index_url': reverse("orders_index_stock"),
                    'select_multiple_url': reverse("orders_select_multiple"),
                }
            )
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
                if action == 'order-request':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)
                            if model.order_created_id == str(operator.operator_id):
                                Orders.request_or_level_approval_order(request, 'request', model, operator)
                                messages.success(request, 'Requested successfully.')
                            else:
                                messages.success(request, 'Forbidden')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-level-approve':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)
                            Orders.request_or_level_approval_order(request, 'approve', model, operator)
                            messages.success(request, 'Approved successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-level-reject':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)
                            Orders.request_or_level_approval_order(request, 'reject', model, operator)
                            messages.success(request, 'Rejected successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-review':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)

                            model.order_reviewed_at = Utils.get_current_datetime_utc()
                            model.order_reviewed_id = operator.operator_id
                            model.order_reviewed_by = operator.operator_name
                            model.order_reviewed_department = operator.operator_department
                            model.order_reviewed_role = operator.operator_role
                            model.order_status = Orders.STATUS_REVIEWED
                            model.save()

                            # sending notification to COP
                            operators = Operators.objects.filter(operator_role=Operators.ROLE_COP)
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "A purchase request has been sent for approval.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            messages.success(request, 'Reviewed successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-approve':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)

                            model.order_approved_at = Utils.get_current_datetime_utc()
                            model.order_approved_id = operator.operator_id
                            model.order_approved_by = operator.operator_name
                            model.order_approved_department = operator.operator_department
                            model.order_approved_role = operator.operator_role
                            model.order_status = Orders.STATUS_APPROVED
                            model.save()

                            # sending notification to all
                            order_approvals = Order_Approvals.objects.filter(orders_order_id=model.order_id)
                            for item in order_approvals:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.order_approval_created_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "Your purchase order request has been approved by COP.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            # sending notification to OPM
                            operators = Operators.objects.filter(operator_role=Operators.ROLE_OPM)
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "A purchase request has been sent by COP to process ahead.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            messages.success(request, 'Approved successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-reject':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)

                            model.order_approved_at = Utils.get_current_datetime_utc()
                            model.order_approved_id = operator.operator_id
                            model.order_approved_by = operator.operator_name
                            model.order_approved_department = operator.operator_department
                            model.order_approved_role = operator.operator_role
                            model.order_status = Orders.STATUS_REJECTED
                            model.save()

                            # sending notification to all
                            order_approvals = Order_Approvals.objects.filter(orders_order_id=model.order_id)
                            for item in order_approvals:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.order_approval_created_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "Your purchase order request has been rejeted by COP.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            messages.success(request, 'Rejected successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'attachment-delete':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Attachments.objects.get(attachment_id=id)
                            if model.attachment_file_path:
                                Utils.delete_file(model.attachment_file_path.path)
                            model.delete()
                        except(TypeError, ValueError, OverflowError, Attachments.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-email-attachment-delete-all':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)
                            attachments = Attachments.objects.filter(
                                attachment_model=Attachments.MODEL_ORDERS,
                                attachment_model_id=model.order_id,
                                attachment_type=Attachments.TYPE_ORDER_EMAIL,
                            )
                            for attachment in attachments:
                                if attachment.attachment_file_path:
                                    Utils.delete_file(attachment.attachment_file_path.path)
                                attachment.delete()
                            messages.success(request, 'Attachments deleted successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-invoice-review':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)

                            model.order_invoice_reviewed_at = Utils.get_current_datetime_utc()
                            model.order_invoice_reviewed_id = operator.operator_id
                            model.order_invoice_reviewed_by = operator.operator_name
                            model.order_invoice_reviewed_department = operator.operator_department
                            model.order_invoice_reviewed_role = operator.operator_role
                            model.order_status = Orders.STATUS_INVOICE_REVIEWED
                            model.save()

                            # sending notification to Accountant
                            operators = Operators.objects.filter(
                                Q(operator_department=Operators.DEPARTMENT_DAF) &
                                (Q(operator_role=Operators.ROLE_ACCOUNTANT_MANAGER) |
                                 Q(operator_role=Operators.ROLE_ACCOUNTANT_OFFICER))
                            )
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "An invoice has been reviewed and sent for generating payment voucher.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            messages.success(request, 'Invoice reviewed successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-invoice-approve':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)

                            model.order_invoice_approval_updated_at = Utils.get_current_datetime_utc()
                            model.order_invoice_approval_updated_id = operator.operator_id
                            model.order_invoice_approval_updated_by = operator.operator_name
                            model.order_invoice_approval_updated_department = operator.operator_department
                            model.order_invoice_approval_updated_role = operator.operator_role
                            model.order_status = Orders.STATUS_INVOICE_APPROVED
                            model.save()

                            # sending notification to DAF
                            operators = Operators.objects.filter(
                                Q(operator_department=Operators.DEPARTMENT_DAF) &
                                (Q(operator_role=Operators.ROLE_DIRECTOR))
                            )
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "An invoice has been sent for approval.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            messages.success(request, 'Updated successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-invoice-reject':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)

                            model.order_invoice_approval_updated_at = Utils.get_current_datetime_utc()
                            model.order_invoice_approval_updated_id = operator.operator_id
                            model.order_invoice_approval_updated_by = operator.operator_name
                            model.order_invoice_approval_updated_department = operator.operator_department
                            model.order_invoice_approval_updated_role = operator.operator_role
                            model.order_status = Orders.STATUS_INVOICE_REJECTED
                            model.save()

                            # sending notification to Accountants
                            operators = Operators.objects.filter(
                                Q(operator_department=Operators.DEPARTMENT_DAF) &
                                (Q(operator_role=Operators.ROLE_ACCOUNTANT_MANAGER) |
                                 Q(operator_role=Operators.ROLE_ACCOUNTANT_OFFICER))
                            )
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "Your invoice has been rejected.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            messages.success(request, 'Updated successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-invoice-approve-daf':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)

                            model.order_invoice_daf_approval_updated_at = Utils.get_current_datetime_utc()
                            model.order_invoice_daf_approval_updated_id = operator.operator_id
                            model.order_invoice_daf_approval_updated_by = operator.operator_name
                            model.order_invoice_daf_approval_updated_department = operator.operator_department
                            model.order_invoice_daf_approval_updated_role = operator.operator_role
                            model.order_status = Orders.STATUS_INVOICE_DAF_APPROVED
                            model.save()

                            # sending notification to COP
                            operators = Operators.objects.filter(operator_role=Operators.ROLE_COP)
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "An invoice has been sent for approval.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            messages.success(request, 'Updated successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-invoice-reject-daf':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)

                            model.order_invoice_daf_approval_updated_at = Utils.get_current_datetime_utc()
                            model.order_invoice_daf_approval_updated_id = operator.operator_id
                            model.order_invoice_daf_approval_updated_by = operator.operator_name
                            model.order_invoice_daf_approval_updated_department = operator.operator_department
                            model.order_invoice_daf_approval_updated_role = operator.operator_role
                            model.order_status = Orders.STATUS_INVOICE_DAF_REJECTED
                            model.save()

                            # sending notification to Accountants
                            operators = Operators.objects.filter(
                                Q(operator_department=Operators.DEPARTMENT_DAF) &
                                (Q(operator_role=Operators.ROLE_ACCOUNTANT_MANAGER) |
                                 Q(operator_role=Operators.ROLE_ACCOUNTANT_OFFICER))
                            )
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "Your invoice has been rejected.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            messages.success(request, 'Updated successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-invoice-approve-cop':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)

                            model.order_invoice_cop_approval_updated_at = Utils.get_current_datetime_utc()
                            model.order_invoice_cop_approval_updated_id = operator.operator_id
                            model.order_invoice_cop_approval_updated_by = operator.operator_name
                            model.order_invoice_cop_approval_updated_department = operator.operator_department
                            model.order_invoice_cop_approval_updated_role = operator.operator_role
                            model.order_status = Orders.STATUS_INVOICE_COP_APPROVED
                            model.save()

                            # sending notification to DAF
                            operators = Operators.objects.filter(
                                Q(operator_department=Operators.DEPARTMENT_DAF) &
                                (Q(operator_role=Operators.ROLE_DIRECTOR) |
                                 Q(operator_role=Operators.ROLE_ACCOUNTANT_MANAGER) |
                                 Q(operator_role=Operators.ROLE_ACCOUNTANT_OFFICER))
                            )
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "Your invoice has been approved.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            messages.success(request, 'Updated successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-invoice-reject-cop':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)

                            model.order_invoice_cop_approval_updated_at = Utils.get_current_datetime_utc()
                            model.order_invoice_cop_approval_updated_id = operator.operator_id
                            model.order_invoice_cop_approval_updated_by = operator.operator_name
                            model.order_invoice_cop_approval_updated_department = operator.operator_department
                            model.order_invoice_cop_approval_updated_role = operator.operator_role
                            model.order_status = Orders.STATUS_INVOICE_COP_REJECTED
                            model.save()

                            # sending notification to Accountants
                            operators = Operators.objects.filter(
                                Q(operator_department=Operators.DEPARTMENT_DAF) &
                                (Q(operator_role=Operators.ROLE_DIRECTOR) |
                                 Q(operator_role=Operators.ROLE_ACCOUNTANT_MANAGER) |
                                 Q(operator_role=Operators.ROLE_ACCOUNTANT_OFFICER))
                            )
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "Your invoice has been rejected.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            messages.success(request, 'Updated successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-paid':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)

                            model.order_paid_at = Utils.get_current_datetime_utc()
                            model.order_paid_id = operator.operator_id
                            model.order_paid_by = operator.operator_name
                            model.order_paid_department = operator.operator_department
                            model.order_paid_role = operator.operator_role
                            model.order_status = Orders.STATUS_PAID
                            model.save()

                            messages.success(request, 'Updated successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-close':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Orders.objects.get(order_id=id)

                            model.order_closed_at = Utils.get_current_datetime_utc()
                            model.order_closed_id = operator.operator_id
                            model.order_closed_by = operator.operator_name
                            model.order_closed_department = operator.operator_department
                            model.order_closed_role = operator.operator_role
                            model.order_status = Orders.STATUS_CLOSED
                            model.save()

                            messages.success(request, 'Updated successfully.')
                        except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
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
def select_single_external(request):
    action = request.POST['action']
    id = request.POST['id']
    if action != '' and id is not None:
        if action == 'attachment-delete-external':
            try:
                model = Attachments.objects.get(attachment_id=id)
                if model.attachment_file_path:
                    Utils.delete_file(model.attachment_file_path.path)
                model.delete()
            except(TypeError, ValueError, OverflowError, Attachments.DoesNotExist):
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')
        return HttpResponse('success', content_type='text/plain')
    else:
        return HttpResponseBadRequest('Bad Request', content_type='text/plain')


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
def create(request):
    template_url = 'orders/create.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_CREATE in auth_permissions.values():
            if request.method == 'POST':

                form = OrderCreateForm(request.POST)
                # noinspection PyArgumentList
                if form.is_valid():
                    model = Orders()
                    model.order_code = Orders.generate_random_number('order_code', 8)

                    model.order_requester_name = form.cleaned_data['requester_name']
                    model.order_project_name = form.cleaned_data['project_name']
                    model.order_project_code = form.cleaned_data['project_code']
                    model.order_project_geo_code = form.cleaned_data['project_geo_code']
                    model.order_charge_code = form.cleaned_data['charge_code']
                    model.order_award_number = form.cleaned_data['award_number']
                    model.order_requisition_number = form.cleaned_data['requisition_number']
                    model.order_donor = form.cleaned_data['donor']
                    model.order_description = form.cleaned_data['description']
                    model.order_anticipated_award_mechanism = form.cleaned_data['anticipated_award_mechanism']
                    model.order_anticipated_start_date = form.cleaned_data['anticipated_start_date']
                    model.order_anticipated_end_date = form.cleaned_data['anticipated_end_date']
                    model.order_special_considerations = form.cleaned_data['special_considerations']

                    model.order_procurement_method = ''
                    model.order_procurement_method_updated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_procurement_method_updated_id = ''
                    model.order_procurement_method_updated_by = ''
                    model.order_procurement_method_updated_department = ''
                    model.order_procurement_method_updated_role = ''

                    model.order_no_of_items = 0
                    model.order_total_price = 0
                    model.order_equipment_price = 0
                    model.order_tax_price = 0
                    model.order_grand_total_price = model.order_total_price + model.order_equipment_price + model.order_tax_price
                    model.order_currency = Orders.CURRENCY_RWF

                    model.order_supplier_category = ''
                    model.order_supplier_updated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_supplier_updated_id = ''
                    model.order_supplier_updated_by = ''
                    model.order_supplier_updated_department = ''
                    model.order_supplier_updated_role = ''

                    model.order_proposal_id = 0
                    model.order_proposal_due_date = settings.APP_CONSTANT_DEFAULT_DATE_VALUE
                    model.order_purchase_no = 0
                    model.order_invoice_no = 0
                    model.order_payment_voucher_no = 0

                    model.order_created_at = Utils.get_current_datetime_utc()
                    model.order_created_id = operator.operator_id
                    model.order_created_by = operator.operator_name
                    model.order_created_department = operator.operator_department
                    model.order_created_role = operator.operator_role

                    model.order_updated_at = Utils.get_current_datetime_utc()
                    model.order_updated_id = operator.operator_id
                    model.order_updated_by = operator.operator_name
                    model.order_updated_department = operator.operator_department
                    model.order_updated_role = operator.operator_role

                    model.order_requested_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_requested_id = ''
                    model.order_requested_by = ''
                    model.order_requested_department = ''
                    model.order_requested_role = ''

                    model.order_approval_no_of_levels = 0

                    model.order_reviewed_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_reviewed_id = ''
                    model.order_reviewed_by = ''
                    model.order_reviewed_department = ''
                    model.order_reviewed_role = ''

                    model.order_approved_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_approved_id = ''
                    model.order_approved_by = ''
                    model.order_approved_department = ''
                    model.order_approved_role = ''

                    model.order_assigned_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_assigned_id = ''
                    model.order_assigned_by = ''
                    model.order_assigned_department = ''
                    model.order_assigned_role = ''

                    model.order_assigned_to_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_assigned_to_id = ''
                    model.order_assigned_to_by = ''
                    model.order_assigned_to_department = ''
                    model.order_assigned_to_role = ''

                    model.order_proposal_generated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_proposal_generated_id = ''
                    model.order_proposal_generated_by = ''
                    model.order_proposal_generated_department = ''
                    model.order_proposal_generated_role = ''

                    model.order_proposal_requested_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_proposal_requested_id = ''
                    model.order_proposal_requested_by = ''
                    model.order_proposal_requested_department = ''
                    model.order_proposal_requested_role = ''

                    model.order_proposal_selected_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_proposal_selected_id = ''
                    model.order_proposal_selected_by = ''
                    model.order_proposal_selected_department = ''
                    model.order_proposal_selected_role = ''

                    model.order_purchase_generated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_purchase_generated_id = ''
                    model.order_purchase_generated_by = ''
                    model.order_purchase_generated_department = ''
                    model.order_purchase_generated_role = ''

                    model.order_acknowledged_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_acknowledged_id = ''
                    model.order_acknowledged_by = ''
                    model.order_acknowledged_department = ''
                    model.order_acknowledged_role = ''

                    model.order_invoice_uploaded_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_invoice_uploaded_id = ''
                    model.order_invoice_uploaded_by = ''
                    model.order_invoice_uploaded_department = ''
                    model.order_invoice_uploaded_role = ''

                    model.order_invoice_reviewed_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_invoice_reviewed_id = ''
                    model.order_invoice_reviewed_by = ''
                    model.order_invoice_reviewed_department = ''
                    model.order_invoice_reviewed_role = ''

                    model.order_invoice_payment_voucher_uploaded_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_invoice_payment_voucher_uploaded_id = ''
                    model.order_invoice_payment_voucher_uploaded_by = ''
                    model.order_invoice_payment_voucher_uploaded_department = ''
                    model.order_invoice_payment_voucher_uploaded_role = ''

                    model.order_invoice_approval_updated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_invoice_approval_updated_id = ''
                    model.order_invoice_approval_updated_by = ''
                    model.order_invoice_approval_updated_department = ''
                    model.order_invoice_approval_updated_role = ''

                    model.order_invoice_daf_approval_updated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_invoice_daf_approval_updated_id = ''
                    model.order_invoice_daf_approval_updated_by = ''
                    model.order_invoice_daf_approval_updated_department = ''
                    model.order_invoice_daf_approval_updated_role = ''

                    model.order_invoice_cop_approval_updated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_invoice_cop_approval_updated_id = ''
                    model.order_invoice_cop_approval_updated_by = ''
                    model.order_invoice_cop_approval_updated_department = ''
                    model.order_invoice_cop_approval_updated_role = ''

                    model.order_paid_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_paid_id = ''
                    model.order_paid_by = ''
                    model.order_paid_department = ''
                    model.order_paid_role = ''

                    model.order_closed_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_closed_id = ''
                    model.order_closed_by = ''
                    model.order_closed_department = ''
                    model.order_closed_role = ''

                    model.order_cancelled_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_cancelled_id = ''
                    model.order_cancelled_by = ''
                    model.order_cancelled_department = ''
                    model.order_cancelled_role = ''

                    model.order_status = Orders.STATUS_PENDING
                    # noinspection PyCallByClass,PyTypeChecker
                    model.save('Created')

                    messages.info(request,
                                  'Your procurement request has been created successfully.')
                    return redirect(reverse("orders_view", args=[model.order_id]))
                else:
                    return render(
                        request, template_url,
                        {
                            'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                            'title': Orders.TITLE,
                            'name': Orders.NAME,
                            'operator': operator,
                            'auth_permissions': auth_permissions,
                            'form': form,
                            'index_url': reverse("orders_index"),
                        }
                    )
            else:
                form = OrderCreateForm()

            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                    'title': Orders.TITLE,
                    'name': Orders.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'form': form,
                    'index_url': reverse("orders_index"),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update(request, pk):
    template_url = 'orders/update.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            try:
                model = Orders.objects.get(order_id=pk)
                if request.method == 'POST':

                    form = OrderUpdateForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.order_requester_name = form.cleaned_data['requester_name']
                        model.order_project_name = form.cleaned_data['project_name']
                        model.order_project_code = form.cleaned_data['project_code']
                        model.order_project_geo_code = form.cleaned_data['project_geo_code']
                        model.order_charge_code = form.cleaned_data['charge_code']
                        model.order_award_number = form.cleaned_data['award_number']
                        model.order_requisition_number = form.cleaned_data['requisition_number']
                        model.order_donor = form.cleaned_data['donor']
                        model.order_description = form.cleaned_data['description']
                        model.order_anticipated_award_mechanism = form.cleaned_data['anticipated_award_mechanism']
                        model.order_anticipated_start_date = form.cleaned_data['anticipated_start_date']
                        model.order_anticipated_end_date = form.cleaned_data['anticipated_end_date']
                        model.order_special_considerations = form.cleaned_data['special_considerations']

                        model.order_updated_at = Utils.get_current_datetime_utc()
                        model.order_updated_id = operator.operator_id
                        model.order_updated_by = operator.operator_name
                        model.order_updated_department = operator.operator_department
                        model.order_updated_role = operator.operator_role
                        model.save()

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("orders_view", args=[model.order_id]))
                    else:
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
                                'index_url': reverse("orders_index"),
                            }
                        )
                else:
                    model.order_anticipated_start_date = Utils.get_fuse_format_date(
                        str(model.order_anticipated_start_date))
                    model.order_anticipated_end_date = Utils.get_fuse_format_date(str(model.order_anticipated_end_date))
                    form = OrderUpdateForm(
                        initial={
                            'requester_name': model.order_requester_name,
                            'project_name': model.order_project_name,
                            'project_code': model.order_project_code,
                            'project_geo_code': model.order_project_geo_code,
                            'charge_code': model.order_charge_code,
                            'award_number': model.order_award_number,
                            'requisition_number': model.order_requisition_number,
                            'donor': model.order_donor,
                            'description': model.order_description,
                            'anticipated_award_mechanism': model.order_anticipated_award_mechanism,
                            'anticipated_start_date': model.order_anticipated_start_date,
                            'anticipated_end_date': model.order_anticipated_end_date,
                            'special_considerations': model.order_special_considerations,
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
                        'index_url': reverse("orders_index"),
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def view(request, pk):
    template_url = 'orders/view.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            try:
                model = Orders.objects.get(order_id=pk)
                model.order_created_at = Utils.get_convert_datetime(model.order_created_at,
                                                                    settings.TIME_ZONE,
                                                                    settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                model.order_updated_at = Utils.get_convert_datetime(model.order_updated_at,
                                                                    settings.TIME_ZONE,
                                                                    settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO

                order_items = Order_Items.objects.filter(orders_order_id=pk).all()

                if model.order_created_id == str(operator.operator_id) and model.order_status == Orders.STATUS_PENDING:
                    template_url = 'orders/view-edit.html'

                display_level_approval = False
                if operator.operator_role != Operators.ROLE_OPM:
                    order_approvals = Order_Approvals.objects.filter(
                        Q(orders_order_id=model.order_id) &
                        Q(order_approval_updated_id=operator.operator_id) &
                        Q(order_approval_status=Order_Approvals.STATUS_PENDING)
                    )
                    if order_approvals.count() == 1:
                        display_level_approval = True

                timeline_notifications = []
                counter = -1
                if model.order_requested_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Requested <small>by ' + model.order_requested_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_requested_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_approval_no_of_levels != 0:
                    order_approvals = Order_Approvals.objects.filter(orders_order_id=model.order_id).order_by(
                        'order_approval_level')
                    for order_approval in order_approvals:
                        message = ''
                        if order_approval.order_approval_status == Order_Approvals.STATUS_APPROVED:
                            message = 'Level Approved <small>by ' + order_approval.order_approval_updated_role + '</small>'
                        if order_approval.order_approval_status == Order_Approvals.STATUS_REJECTED:
                            message = 'Level Rejected <small>by ' + order_approval.order_approval_updated_role + '</small>'

                        if message != '':
                            notification_timeline = NotificationsTimeline()
                            notification_timeline.message = message
                            notification_timeline.datetime = Utils.get_convert_datetime(
                                order_approval.order_approval_updated_at,
                                settings.TIME_ZONE,
                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                            timeline_notifications.append(notification_timeline)

                if model.order_procurement_method_updated_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Added procurement method<small>by ' + model.order_procurement_method_updated_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(
                        model.order_procurement_method_updated_at,
                        settings.TIME_ZONE,
                        settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_reviewed_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Reviewed <small>by DAF</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_reviewed_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_approved_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Approved <small>by ' + model.order_approved_role + '</small>'
                    if model.order_status == Orders.STATUS_REJECTED:
                        notification_timeline.message = 'Rejected <small>by ' + model.order_approved_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_approved_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_assigned_to_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Assigned <small>to ' + model.order_assigned_to_role + ' by ' + model.order_assigned_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_assigned_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_supplier_updated_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Selected Vendor Category <small>by ' + model.order_supplier_updated_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_supplier_updated_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_proposal_generated_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Updated proposal request <small>by ' + model.order_proposal_generated_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_proposal_generated_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_proposal_requested_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Published proposal request <small>by ' + model.order_proposal_requested_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_proposal_requested_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_proposal_selected_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Selected vendor <small>by ' + model.order_proposal_selected_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_proposal_selected_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_purchase_generated_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Purchase order generated <small>by ' + model.order_purchase_generated_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_purchase_generated_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if str(model.order_acknowledged_at)[0:19] != settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE:
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Acknowledged order <small>by vendor</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_acknowledged_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_invoice_uploaded_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Invoice uploaded <small>by ' + model.order_invoice_uploaded_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_invoice_uploaded_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_invoice_reviewed_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Invoice reviewed <small>by ' + model.order_invoice_reviewed_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_invoice_reviewed_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_invoice_payment_voucher_uploaded_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Invoice payment voucher uploaded <small>by ' + model.order_invoice_payment_voucher_uploaded_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(
                        model.order_invoice_payment_voucher_uploaded_at,
                        settings.TIME_ZONE,
                        settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_invoice_approval_updated_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Invoice approved <small>by ' + model.order_invoice_approval_updated_role + '</small>'
                    if model.order_status == Orders.STATUS_INVOICE_REJECTED:
                        notification_timeline.message = 'Invoice rejected <small>by ' + model.order_invoice_approval_updated_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_invoice_approval_updated_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_invoice_daf_approval_updated_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Invoice approved <small>by ' + model.order_invoice_daf_approval_updated_role + '</small>'
                    if model.order_status == Orders.STATUS_INVOICE_DAF_REJECTED:
                        notification_timeline.message = 'Invoice rejected <small>by ' + model.order_invoice_daf_approval_updated_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(
                        model.order_invoice_daf_approval_updated_at,
                        settings.TIME_ZONE,
                        settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_invoice_cop_approval_updated_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Invoice approved <small>by ' + model.order_invoice_cop_approval_updated_role + '</small>'
                    if model.order_status == Orders.STATUS_INVOICE_COP_REJECTED:
                        notification_timeline.message = 'Invoice rejected <small>by ' + model.order_invoice_cop_approval_updated_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(
                        model.order_invoice_cop_approval_updated_at,
                        settings.TIME_ZONE,
                        settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_paid_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Paid <small>by ' + model.order_paid_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_paid_at, settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_closed_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Closed <small>by ' + model.order_closed_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_closed_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_cancelled_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Closed <small>by ' + model.order_cancelled_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.order_cancelled_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_REQUESTED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Level approval pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL1_APPROVED and model.order_approval_no_of_levels > 1:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Level approval pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL1_REJECTED and model.order_approval_no_of_levels >= 1:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Rejected at level 1</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL2_APPROVED and model.order_approval_no_of_levels > 2:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Level approval pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL2_REJECTED and model.order_approval_no_of_levels >= 2:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Rejected at level 2</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL3_APPROVED and model.order_approval_no_of_levels > 3:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Level approval pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL3_REJECTED and model.order_approval_no_of_levels >= 3:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Rejected at level 3</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL4_APPROVED and model.order_approval_no_of_levels > 4:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Level approval pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL4_REJECTED and model.order_approval_no_of_levels >= 4:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Rejected at level 4</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL5_APPROVED and model.order_approval_no_of_levels > 5:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Level approval pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL5_REJECTED and model.order_approval_no_of_levels >= 5:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Rejected at level 5</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL6_APPROVED and model.order_approval_no_of_levels > 6:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Level approval pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL6_REJECTED and model.order_approval_no_of_levels >= 6:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Rejected at level 6</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL0_APPROVED and model.order_procurement_method_updated_id == '':
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Procurement method pending from OPM</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_LEVEL0_APPROVED and model.order_procurement_method_updated_id != '':
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Review pending from DAF</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_REVIEWED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Approval pending from COP</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_APPROVED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Assign pending from OPM</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_REJECTED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Rejected from COP</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_ASSIGNED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Pending vendor category selection</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_SUPPLIER_UPDATED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Email draft to vendors is pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_PROPOSAL_GENERATED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Requesting for proposals to vendors is pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_PROPOSAL_REQUESTED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Evaluating vendors' proposals is pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_PROPOSAL_SELECTED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Generating purchase order is pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_PURCHASE_GENERATED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Vendor acknowledgement is pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_ACKNOWLEDGED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>In Progress</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_INVOICE_UPLOADED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Invoice review is pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_INVOICE_REVIEWED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Generate payment voucher is pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_INVOICE_PAYMENT_VOUCHER_GENERATED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Approval pending from Sr. Accountant</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_INVOICE_APPROVED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Approval pending from DAF</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_INVOICE_REJECTED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Invoice rejected by Sr. Accountant</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_INVOICE_DAF_APPROVED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Approval pending from COP</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_INVOICE_DAF_REJECTED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Invoice rejected by DAF</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_INVOICE_COP_APPROVED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Payment pending</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_INVOICE_COP_REJECTED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Invoice rejected by COP</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_PAID:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Payment Done</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_CLOSED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-success'>Completed</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.order_status == Orders.STATUS_CANCELLED:
                    notification_timeline = NotificationsTimeline()
                    model.order_readable_status = notification_timeline.message = "<b class='text-red'>Cancelled</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                try:
                    attachment_order_purchase_no = Attachments.objects.get(
                        attachment_model=Attachments.MODEL_ORDERS,
                        attachment_model_id=model.order_id,
                        attachment_type=Attachments.TYPE_ORDER_PURCHASE,
                    )
                except Attachments.DoesNotExist:
                    attachment_order_purchase_no = ''

                try:
                    attachment_order_invoice_no = Attachments.objects.get(
                        attachment_model=Attachments.MODEL_ORDERS,
                        attachment_model_id=model.order_id,
                        attachment_type=Attachments.TYPE_ORDER_INVOICE,
                    )
                except Attachments.DoesNotExist:
                    attachment_order_invoice_no = ''

                try:
                    attachment_order_payment_voucher = Attachments.objects.get(
                        attachment_model=Attachments.MODEL_ORDERS,
                        attachment_model_id=model.order_id,
                        attachment_type=Attachments.TYPE_ORDER_PAYMENT_VOUCHER,
                    )
                except Attachments.DoesNotExist:
                    attachment_order_payment_voucher = ''

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                        'title': Orders.TITLE,
                        'name': Orders.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'model': model,
                        'index_url': reverse("orders_index"),
                        'select_single_url': reverse("orders_select_single"),
                        'order_items': order_items,
                        'order_items_size': order_items,
                        'item_index_url': reverse("orders_view", kwargs={'pk': pk}),
                        'item_select_single_url': reverse("order_items_select_single"),
                        'status_html_tag': Orders.get_status_html_tag(model),
                        'display_level_approval': display_level_approval,
                        'timeline_notifications': timeline_notifications,
                        'attachment_order_purchase_no': attachment_order_purchase_no,
                        'attachment_order_invoice_no': attachment_order_invoice_no,
                        'attachment_order_payment_voucher': attachment_order_payment_voucher,
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update_procurement_method(request, pk):
    template_url = 'orders/update-procurement-method.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values() and operator.operator_role == Operators.ROLE_OPM:
            try:
                model = Orders.objects.get(order_id=pk)
                if request.method == 'POST':

                    form = OrderProcurementForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.order_procurement_method = form.cleaned_data['procurement_method']
                        model.order_procurement_method_updated_at = Utils.get_current_datetime_utc()
                        model.order_procurement_method_updated_id = operator.operator_id
                        model.order_procurement_method_updated_by = operator.operator_name
                        model.order_procurement_method_updated_department = operator.operator_department
                        model.order_procurement_method_updated_role = operator.operator_role
                        model.save()

                        # sending notification to Director of DFA
                        operators = Operators.objects.all().filter(
                            Q(operator_department=Operators.DEPARTMENT_DAF) &
                            Q(operator_role=Operators.ROLE_DIRECTOR)
                        )
                        for item in operators:
                            Notifications.add_notification(
                                Notifications.TYPE_OPERATOR,
                                operator.operator_id,
                                Notifications.TYPE_OPERATOR,
                                item.operator_id,
                                Notifications.TYPE_ORDER,
                                model.order_id,
                                "Created a purchase request to review.",
                                "/backend/orders/view/" + str(model.order_id) + "/"
                            )

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("orders_view", args=[model.order_id]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("orders_view", args=[model.order_id]))
                else:
                    form = OrderProcurementForm(
                        initial={
                            'order_id': model.order_code,
                            'procurement_method': model.order_procurement_method,
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
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def view_order_items(request, pk):
    template_url = 'order-items/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            try:
                model = Orders.objects.get(order_id=pk)

                search_form = OrderItemSearchIndexForm(request.POST or None)
                objects = Order_Items.objects.filter(orders_order_id=model.order_id)

                if request.method == 'POST' and search_form.is_valid():
                    display_search = True
                    table = OrderItemsTable(objects)
                else:
                    display_search = False
                    table = OrderItemsTable(objects)

                table.set_auth_permissions(auth_permissions)
                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                        'title': Orders.TITLE,
                        'name': Orders.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'table': table,
                        'search_form': search_form,
                        'display_search': display_search,
                        'index_url': reverse("order_items_index", kwargs={'pk': pk}),
                        'select_multiple_url': reverse("order_items_select_multiple"),
                        'model': model,
                        'item_index_url': reverse("orders_view", kwargs={'pk': pk}),
                    }
                )

            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update_order_assignment(request, pk):
    template_url = 'orders/update-order-assignment.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values() and operator.operator_role == Operators.ROLE_OPM:
            try:
                model = Orders.objects.get(order_id=pk)
                if request.method == 'POST':

                    form = OrderAssignmentForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():

                        # assign from
                        model.order_assigned_at = Utils.get_current_datetime_utc()
                        model.order_assigned_id = operator.operator_id
                        model.order_assigned_by = operator.operator_name
                        model.order_assigned_department = operator.operator_department
                        model.order_assigned_role = operator.operator_role

                        # assign to
                        model.order_assigned_to_at = Utils.get_current_datetime_utc()
                        assign_id = form.cleaned_data['order_assigned_id']

                        item_operator = None
                        if assign_id != str(0):
                            item_operator = Operators.objects.get(operator_id=assign_id)

                        if item_operator is None:
                            model.order_assigned_to_id = 0
                            model.order_assigned_to_by = ''
                        else:
                            model.order_assigned_to_id = item_operator.operator_id
                            model.order_assigned_to_by = item_operator.operator_name
                        model.order_assigned_to_department = Operators.DEPARTMENT_DAF
                        model.order_assigned_to_role = form.cleaned_data['order_assigned_role']
                        model.order_status = Orders.STATUS_ASSIGNED
                        model.save()

                        if item_operator is None:
                            # sending notification to Director of DFA
                            operators = Operators.objects.all().filter(
                                Q(operator_role=model.order_assigned_to_role)
                            )
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "Assigned a purchase request to process ahead.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )
                        else:
                            Notifications.add_notification(
                                Notifications.TYPE_OPERATOR,
                                operator.operator_id,
                                Notifications.TYPE_OPERATOR,
                                item_operator.operator_id,
                                Notifications.TYPE_ORDER,
                                model.order_id,
                                "Assigned a purchase request to process ahead.",
                                "/backend/orders/view/" + str(model.order_id) + "/"
                            )

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("orders_view", args=[model.order_id]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("orders_view", args=[model.order_id]))
                else:
                    form = OrderAssignmentForm(
                        initial={
                            'order_id': model.order_code,
                            'order_assigned_role': model.order_assigned_role,
                            'order_assigned_id': model.order_assigned_id,
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
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update_supplier(request, pk):
    template_url = 'orders/update-supplier.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            try:
                model = Orders.objects.get(order_id=pk)
                if request.method == 'POST':

                    form = OrderSupplierForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.order_supplier_category = form.cleaned_data['order_supplier_category']
                        model.order_supplier_updated_at = Utils.get_current_datetime_utc()
                        model.order_supplier_updated_id = operator.operator_id
                        model.order_supplier_updated_by = operator.operator_name
                        model.order_supplier_updated_department = operator.operator_department
                        model.order_supplier_updated_role = operator.operator_role
                        model.order_status = Orders.STATUS_SUPPLIER_UPDATED
                        model.save()

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("orders_view", args=[model.order_id]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("orders_view", args=[model.order_id]))
                else:
                    form = OrderSupplierForm(
                        initial={
                            'order_id': model.order_code,
                            'order_supplier_category': model.order_supplier_category,
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
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update_email_to_supplier(request, pk):
    template_url = 'orders/update-email-to-supplier.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            try:
                model = Orders.objects.get(order_id=pk)

                # sending email
                if settings.IS_LOCAL:
                    domain = settings.BACKEND_DOMAIN_LOCAL
                else:
                    domain = settings.BACKEND_DOMAIN_PROD

                create_url = '/order-proposals/create/' + str(pk) + '/0/'
                url = "<a title=\"Submit your proposal\" href=\"" + str(
                    domain) + create_url + "\" target=\"_blank\" rel=\"noopener\">Submit your proposal</a>"

                if create_url not in model.order_email_to_supplier_message:
                    model.order_email_to_supplier_message = model.order_email_to_supplier_message + "<br><p>Link to submit your proposals:&nbsp;" + url + "</p>"

                attachment_form = OrderUploadAttachmentForm()
                attachments = Attachments.objects.filter(
                    attachment_model=Attachments.MODEL_ORDERS,
                    attachment_model_id=model.order_id,
                    attachment_type=Attachments.TYPE_ORDER_EMAIL
                ).order_by('-attachment_id').all()

                if request.method == 'POST':

                    form = OrderEmailToSupplierForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.order_email_to_supplier_subject = form.cleaned_data['order_email_to_supplier_subject']
                        model.order_email_to_supplier_message = form.cleaned_data['order_email_to_supplier_message']

                        model.order_email_to_supplier_updated_id = Utils.get_current_datetime_utc()
                        model.order_email_to_supplier_updated_id = operator.operator_id
                        model.order_email_to_supplier_updated_by = operator.operator_name
                        model.order_email_to_supplier_updated_department = operator.operator_department
                        model.order_email_to_supplier_updated_role = operator.operator_role

                        # extra unneeded
                        model.order_proposal_generated_at = Utils.get_current_datetime_utc()
                        model.order_proposal_generated_id = operator.operator_id
                        model.order_proposal_generated_by = operator.operator_name
                        model.order_proposal_generated_department = operator.operator_department
                        model.order_proposal_generated_role = operator.operator_role
                        model.order_status = Orders.STATUS_PROPOSAL_GENERATED
                        model.save()

                        model.order_proposal_requested_at = Utils.get_current_datetime_utc()
                        model.order_proposal_requested_id = operator.operator_id
                        model.order_proposal_requested_by = operator.operator_name
                        model.order_proposal_requested_department = operator.operator_department
                        model.order_proposal_requested_role = operator.operator_role
                        model.order_status = Orders.STATUS_PROPOSAL_REQUESTED
                        model.save()

                        messages.success(request, 'Updated and proposal generated successfully.')
                        return redirect(reverse("orders_view", args=[model.order_id]))
                    else:
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
                                'index_url': reverse("orders_index"),
                                'select_single_url': reverse("orders_select_single"),
                                'attachment_form': attachment_form,
                                'attachments': attachments,
                            }
                        )
                else:
                    form = OrderEmailToSupplierForm(
                        initial={
                            'order_email_to_supplier_subject': model.order_email_to_supplier_subject,
                            'order_email_to_supplier_message': model.order_email_to_supplier_message,
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
                        'index_url': reverse("orders_index"),
                        'select_single_url': reverse("orders_select_single"),
                        'attachment_form': attachment_form,
                        'attachments': attachments,
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def send_email_to_supplier(request, pk):
    template_url = 'orders/send-email-to-supplier.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            # try:
            order = Orders.objects.get(order_id=pk)
            model = Emails()
            model.email_from = settings.EMAIL_HOST_USER
            model.email_from_name = settings.EMAIL_HOST_NAME

            model.email_subject = order.order_email_to_supplier_subject
            model.email_message = order.order_email_to_supplier_message

            attachments = Attachments.objects.filter(
                attachment_model=Attachments.MODEL_ORDERS,
                attachment_model_id=order.order_id,
                attachment_type=Attachments.TYPE_ORDER_EMAIL,
            ).order_by('-attachment_id').all()

            if request.method == 'POST':

                form = SendEmailForm(request.POST)

                # noinspection PyArgumentList
                if form.is_valid():

                    model.email_to = form.cleaned_data['email_to']
                    model.email_cc = form.cleaned_data['email_cc']

                    model.email_created_at = Utils.get_current_datetime_utc()
                    model.email_created_id = operator.operator_id
                    model.email_created_by = operator.operator_name
                    model.email_created_department = operator.operator_department
                    model.email_created_role = operator.operator_role

                    model.email_updated_at = Utils.get_current_datetime_utc()
                    model.email_updated_id = operator.operator_id
                    model.email_updated_by = operator.operator_name
                    model.email_updated_department = operator.operator_department
                    model.email_updated_role = operator.operator_role

                    model.email_status = Emails.STATUS_PENDING
                    model.save()

                    # sending email
                    if settings.IS_LOCAL:
                        domain = settings.BACKEND_DOMAIN_LOCAL
                        logo_url = settings.LOGO_URL_LOCAL
                    else:
                        domain = settings.BACKEND_DOMAIN_PROD
                        logo_url = settings.LOGO_URL_PROD

                    # contact_url = '{domain}/{path}'.format(domain=domain, path=settings.CONTACT_URL)
                    contact_url = settings.APP_CONSTANT_COMPANY_WEBSITE

                    if settings.IS_LOCAL:
                        domain = settings.BACKEND_DOMAIN_LOCAL
                    else:
                        domain = settings.BACKEND_DOMAIN_PROD
                    message = model.email_message.replace("../../../../", str(domain) + "/")
                    html_content = render_to_string(
                        'email/email-app.html',
                        {
                            'logo_url': logo_url,
                            'contact_url': contact_url,
                            'message': defaultfilters.safe(message),
                        }
                    )
                    text_content = strip_tags(html_content)

                    email_message = EmailMultiAlternatives(
                        subject=model.email_subject,
                        body=text_content,
                        from_email=settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                        to=[model.email_to],
                        cc=[settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID, model.email_cc],
                        reply_to=[settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID],
                    )
                    email_message.attach_alternative(html_content, "text/html")

                    counter = 0
                    for attachment in attachments:
                        counter = counter + 1
                        app_attachment = Attachments()
                        app_attachment.UPLOAD_PATH = Attachments.EMAILS_UPLOAD_PATH
                        app_attachment.attachment_model = Attachments.MODEL_EMAILS
                        app_attachment.attachment_model_id = model.email_id
                        app_attachment.attachment_type = Attachments.MODEL_EMAILS
                        app_attachment.attachment_type_id = model.email_id
                        app_attachment.attachment_number = counter
                        app_attachment.attachment_file_name = attachment.attachment_file_name
                        app_attachment.attachment_file_path = attachment.attachment_file_path
                        app_attachment.attachment_file_size = attachment.attachment_file_size
                        app_attachment.attachment_file_type = attachment.attachment_file_type

                        app_attachment.attachment_file_uploaded_at = Utils.get_current_datetime_utc()
                        app_attachment.attachment_file_uploaded_id = operator.operator_id
                        app_attachment.attachment_file_uploaded_by = operator.operator_name
                        app_attachment.attachment_file_uploaded_department = operator.operator_department
                        app_attachment.attachment_file_uploaded_role = operator.operator_role

                        app_attachment.save()

                        email_message.attach_file(attachment.attachment_file_path.path)

                    email_message.send(fail_silently=False)

                    model.email_sent_at = Utils.get_current_datetime_utc()
                    model.email_status = Emails.STATUS_SENT
                    model.save()

                    model.email_delivered_at = Utils.get_current_datetime_utc()
                    model.email_status = Emails.STATUS_DELIVERED
                    model.save()

                    messages.success(request, 'Email sent successfully.')
                    return redirect(reverse("orders_view", args=[order.order_id]))
                else:
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
                            'index_url': reverse("orders_index"),
                            'select_single_url': reverse("orders_select_single"),
                            'attachments': attachments,
                        }
                    )
            else:
                form = SendEmailForm(
                    initial={
                        'email_to': '',
                        'email_cc': '',
                        'email_subject': model.email_subject,
                        'email_message': model.email_message,
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
                    'index_url': reverse("orders_index"),
                    'select_single_url': reverse("orders_select_single"),
                    'attachments': attachments,
                }
            )
        # except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
        #     return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def upload_attachments(request):
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
            if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                if action == 'upload-order-email':
                    order = Orders.objects.get(order_id=id)
                    if order is not None:

                        model = Attachments()
                        model.UPLOAD_PATH = Attachments.ORDERS_UPLOAD_PATH
                        model.attachment_model = Attachments.MODEL_ORDERS
                        model.attachment_model_id = order.order_id
                        model.attachment_type = Attachments.TYPE_ORDER_EMAIL
                        model.attachment_type_id = 0
                        model.attachment_number = 0

                        if action == 'upload-order-email':
                            model.attachment_type = Attachments.TYPE_ORDER_EMAIL

                        model.attachment_file_uploaded_at = Utils.get_current_datetime_utc()
                        model.attachment_file_uploaded_id = operator.operator_id
                        model.attachment_file_uploaded_by = operator.operator_name
                        model.attachment_file_uploaded_department = operator.operator_department
                        model.attachment_file_uploaded_role = operator.operator_role

                        import magic
                        mime = magic.Magic(mime=True)
                        # for file in request.FILES.getlist('attachment_file_path'):
                        form = OrderUploadAttachmentForm(request.POST, request.FILES)
                        if form.is_valid():
                            try:
                                original_filename = form.cleaned_data['attachment_file_path']
                                ext = original_filename.split('.')[-1]
                                new_filename = 'order_email_' + str(order.order_code) + '_' + str(
                                    Utils.get_epochtime_ms()) + '.' + str(ext)
                                temp_file_path = settings.MEDIA_ROOT + 'temp/' + str(original_filename)
                                attachment_file_path = settings.MEDIA_ROOT + model.UPLOAD_PATH + str(
                                    new_filename)
                                os.rename(temp_file_path, attachment_file_path)
                                url = model.UPLOAD_PATH + new_filename
                                size = str(os.path.getsize(attachment_file_path))
                                model.attachment_file_name = original_filename
                                model.attachment_file_path = url
                                model.attachment_file_type = str(mime.from_file(attachment_file_path))
                                model.attachment_file_size = size
                                model.save()

                                # return HttpResponse('success', content_type='text/plain')
                                response = json.dumps({
                                    'error': False,
                                    'message': 'success',
                                    'name': original_filename,
                                    'url': model.attachment_file_path.url,
                                    'size': defaultfilters.filesizeformat(size),
                                    'id': model.attachment_id,
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
                return HttpResponseForbidden('Forbidden', content_type='text/plain')
        else:
            return HttpResponseBadRequest('Bad Request', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def order_proposal_create(request, pk, code):
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

            if model.order_proposal_status != Order_Proposals.STATUS_PENDING:
                return HttpResponseForbidden('Forbidden', content_type='text/plain')

        attachments = Attachments.objects.filter(
            attachment_model=Attachments.MODEL_ORDERS,
            attachment_model_id=model.order_id,
            attachment_type=Attachments.TYPE_ORDER_PROPOSAL_BUSINESS_LICENSE,
        ).order_by('-attachment_id').all()

        attachment1 = ''
        if attachments.count() != 0:
            attachment1 = attachments[0]

        attachments = Attachments.objects.filter(
            attachment_model=Attachments.MODEL_ORDERS,
            attachment_model_id=model.order_id,
            attachment_type=Attachments.TYPE_ORDER_PROPOSAL_OFFER_LETTER,
        ).order_by('-attachment_id').all()

        attachment2 = ''
        if attachments.count() != 0:
            attachment2 = attachments[0]

        attachments = Attachments.objects.filter(
            attachment_model=Attachments.MODEL_ORDERS,
            attachment_model_id=model.order_id,
            attachment_type=Attachments.TYPE_ORDER_PROPOSAL_QUOTATION,
        ).order_by('-attachment_id').all()

        attachment3 = ''
        if attachments.count() != 0:
            attachment3 = attachments[0]

        attachments = Attachments.objects.filter(
            attachment_model=Attachments.MODEL_ORDERS,
            attachment_model_id=model.order_id,
            attachment_type=Attachments.TYPE_ORDER_PROPOSAL_VAT_REGISTRATION,
        ).order_by('-attachment_id').all()

        attachment4 = ''
        if attachments.count() != 0:
            attachment4 = attachments[0]

        attachments = Attachments.objects.filter(
            attachment_model=Attachments.MODEL_ORDERS,
            attachment_model_id=model.order_id,
            attachment_type=Attachments.TYPE_ORDER_PROPOSAL_OTHER_DOCUMENT,
            attachment_number=1,
        ).order_by('-attachment_id').all()

        attachment5 = ''
        if attachments.count() != 0:
            attachment5 = attachments[0]

        attachments = Attachments.objects.filter(
            attachment_model=Attachments.MODEL_ORDERS,
            attachment_model_id=model.order_id,
            attachment_type=Attachments.TYPE_ORDER_PROPOSAL_OTHER_DOCUMENT,
            attachment_number=2,
        ).order_by('-attachment_id').all()

        attachment6 = ''
        if attachments.count() != 0:
            attachment6 = attachments[0]

        attachments = Attachments.objects.filter(
            attachment_model=Attachments.MODEL_ORDERS,
            attachment_model_id=model.order_id,
            attachment_type=Attachments.TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT,
            attachment_number=1,
        ).order_by('-attachment_id').all()

        attachment7 = ''
        if attachments.count() != 0:
            attachment7 = attachments[0]

        attachments = Attachments.objects.filter(
            attachment_model=Attachments.MODEL_ORDERS,
            attachment_model_id=model.order_id,
            attachment_type=Attachments.TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT,
            attachment_number=2,
        ).order_by('-attachment_id').all()

        attachment8 = ''
        if attachments.count() != 0:
            attachment8 = attachments[0]

        attachments = Attachments.objects.filter(
            attachment_model=Attachments.MODEL_ORDERS,
            attachment_model_id=model.order_id,
            attachment_type=Attachments.TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT,
            attachment_number=3,
        ).order_by('-attachment_id').all()

        attachment9 = ''
        if attachments.count() != 0:
            attachment9 = attachments[0]

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

                # sending email confirmation mail
                if settings.IS_LOCAL:
                    domain = settings.BACKEND_DOMAIN_LOCAL
                    logo_url = settings.LOGO_URL_LOCAL
                else:
                    domain = settings.BACKEND_DOMAIN_PROD
                    logo_url = settings.LOGO_URL_PROD

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
                        'attachment1': attachment1,
                        'attachment2': attachment2,
                        'attachment3': attachment3,
                        'attachment4': attachment4,
                        'attachment5': attachment5,
                        'attachment6': attachment6,
                        'attachment7': attachment7,
                        'attachment8': attachment8,
                        'attachment9': attachment9,
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
                'attachment1': attachment1,
                'attachment2': attachment2,
                'attachment3': attachment3,
                'attachment4': attachment4,
                'attachment5': attachment5,
                'attachment6': attachment6,
                'attachment7': attachment7,
                'attachment8': attachment8,
                'attachment9': attachment9,
            }
        )
    except(TypeError, ValueError, OverflowError, Orders.DoesNotExist, Order_Proposals.DoesNotExist):
        return HttpResponseNotFound('Not Found', content_type='text/plain')


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

                model = Attachments()
                model.UPLOAD_PATH = Attachments.ORDERS_UPLOAD_PATH
                model.attachment_model = Attachments.MODEL_ORDERS
                model.attachment_model_id = order.order_id

                model.attachment_type_id = 0
                model.attachment_number = 0

                new_filename_prefix = 'order_email_'

                if action == 'upload-order-proposal-business-license':
                    model.attachment_type = Attachments.TYPE_ORDER_PROPOSAL_BUSINESS_LICENSE
                    new_filename_prefix = 'order_proposal_business_license_'

                if action == 'upload-order-proposal-offer-letter':
                    model.attachment_type = Attachments.TYPE_ORDER_PROPOSAL_OFFER_LETTER
                    new_filename_prefix = 'order_proposal_offer_letter_'

                if action == 'upload-order-proposal-quotation':
                    model.attachment_type = Attachments.TYPE_ORDER_PROPOSAL_QUOTATION
                    new_filename_prefix = 'order_proposal_quotation_'

                if action == 'upload-order-proposal-vat-registration':
                    model.attachment_type = Attachments.TYPE_ORDER_PROPOSAL_VAT_REGISTRATION
                    new_filename_prefix = 'order_proposal_vat_registration_'

                if action == 'upload-order-proposal-other-document':
                    model.attachment_type = Attachments.TYPE_ORDER_PROPOSAL_OTHER_DOCUMENT
                    new_filename_prefix = 'order_proposal_other_document_'

                if action == 'upload-order-proposal-reference-document':
                    model.attachment_type = Attachments.TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT
                    new_filename_prefix = 'order_proposal_reference_document_'

                if action == 'upload-order-proposal-business-license' or \
                        action == 'upload-order-proposal-offer-letter' or \
                        action == 'upload-order-proposal-quotation' or \
                        action == 'upload-order-proposal-vat-registration' or \
                        action == 'upload-order-proposal-other-document' or \
                        action == 'upload-order-proposal-reference-document':
                    code = request.POST['code']
                    model.attachment_type_id = code

                if action == 'upload-order-proposal-other-document' or \
                        action == 'upload-order-proposal-reference-document':
                    number = request.POST['number']
                    model.attachment_number = number

                model.attachment_file_uploaded_at = Utils.get_current_datetime_utc()
                model.attachment_file_uploaded_id = ''
                model.attachment_file_uploaded_by = ''
                model.attachment_file_uploaded_department = ''
                model.attachment_file_uploaded_role = ''

                import magic
                mime = magic.Magic(mime=True)
                # for file in request.FILES.getlist('attachment_file_path'):
                form = OrderUploadAttachmentForm(request.POST, request.FILES)
                if form.is_valid():
                    try:
                        original_filename = form.cleaned_data['attachment_file_path']

                        ext = original_filename.split('.')[-1]
                        new_filename = new_filename_prefix + str(order.order_code) + '_' + str(
                            Utils.get_epochtime_ms()) + '.' + str(ext)
                        temp_file_path = settings.MEDIA_ROOT + 'temp/' + str(original_filename)
                        attachment_file_path = settings.MEDIA_ROOT + model.UPLOAD_PATH + str(
                            new_filename)
                        os.rename(temp_file_path, attachment_file_path)
                        url = model.UPLOAD_PATH + new_filename
                        size = str(os.path.getsize(attachment_file_path))
                        model.attachment_file_name = original_filename
                        model.attachment_file_path = url
                        model.attachment_file_type = str(mime.from_file(attachment_file_path))
                        model.attachment_file_size = size
                        model.save()

                        # return HttpResponse('success', content_type='text/plain')
                        response = json.dumps({
                            'error': False,
                            'message': 'success',
                            'name': original_filename,
                            'url': model.attachment_file_path.url,
                            'size': defaultfilters.filesizeformat(size),
                            'id': model.attachment_id,
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
def update_purchase_order(request, pk):
    template_url = 'orders/update-purchase.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            try:
                model = Orders.objects.get(order_id=pk)
                if request.method == 'POST':

                    form = OrderPurchaseUpdateForm(request.POST, request.FILES)

                    import magic
                    mime = magic.Magic(mime=True)
                    # noinspection PyArgumentList
                    if form.is_valid():
                        try:
                            attachments = Attachments.objects.filter(
                                attachment_model=Attachments.MODEL_ORDERS,
                                attachment_model_id=model.order_id,
                                attachment_type=Attachments.TYPE_ORDER_PURCHASE,
                            ).all()

                            for attachment in attachments:
                                if attachment.attachment_file_path:
                                    Utils.delete_file(attachment.attachment_file_path.path)
                                attachment.delete()

                            attachment = Attachments()
                            attachment.UPLOAD_PATH = Attachments.ORDERS_UPLOAD_PATH
                            attachment.attachment_model = Attachments.MODEL_ORDERS
                            attachment.attachment_model_id = model.order_id
                            attachment.attachment_type_id = 0
                            attachment.attachment_number = 0
                            attachment.attachment_type = Attachments.TYPE_ORDER_PURCHASE
                            attachment.attachment_file_uploaded_at = Utils.get_current_datetime_utc()
                            attachment.attachment_file_uploaded_id = operator.operator_id
                            attachment.attachment_file_uploaded_by = operator.operator_name
                            attachment.attachment_file_uploaded_department = operator.operator_department
                            attachment.attachment_file_uploaded_role = operator.operator_role

                            original_filename = form.cleaned_data['attachment_file_path']

                            ext = original_filename.split('.')[-1]
                            new_filename = 'order_purchase_' + str(model.order_code) + '_' + str(
                                Utils.get_epochtime_ms()) + '.' + str(ext)
                            temp_file_path = settings.MEDIA_ROOT + 'temp/' + str(original_filename)
                            attachment_file_path = settings.MEDIA_ROOT + attachment.UPLOAD_PATH + str(
                                new_filename)
                            os.rename(temp_file_path, attachment_file_path)
                            url = attachment.UPLOAD_PATH + new_filename
                            size = str(os.path.getsize(attachment_file_path))
                            attachment.attachment_file_name = original_filename
                            attachment.attachment_file_path = url
                            attachment.attachment_file_type = str(mime.from_file(attachment_file_path))
                            attachment.attachment_file_size = size
                            attachment.save()

                            model.order_purchase_no = form.cleaned_data['order_purchase_no']

                            model.order_purchase_generated_at = Utils.get_current_datetime_utc()
                            model.order_purchase_generated_id = operator.operator_id
                            model.order_purchase_generated_by = operator.operator_name
                            model.order_purchase_generated_department = operator.operator_department
                            model.order_purchase_generated_role = operator.operator_role

                            model.order_status = Orders.STATUS_PURCHASE_GENERATED
                            model.save()

                            messages.success(request, 'Updated successfully.')
                            return redirect(reverse("orders_view", args=[model.order_id]))
                        except Exception as e:
                            print('Exception: ' + str(e))
                            messages.error(request, '' + str(e))
                            return redirect(reverse("orders_view", args=[model.order_id]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("orders_view", args=[model.order_id]))
                else:
                    form = OrderPurchaseUpdateForm(
                        initial={
                            'order_id': model.order_code,
                            'order_purchase_no': model.order_purchase_no,
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
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update_invoice_order(request, pk):
    template_url = 'orders/update-invoice.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            try:
                model = Orders.objects.get(order_id=pk)
                if request.method == 'POST':

                    form = OrderInvoiceUpdateForm(request.POST, request.FILES)

                    import magic
                    mime = magic.Magic(mime=True)
                    # noinspection PyArgumentList
                    if form.is_valid():
                        try:
                            attachments = Attachments.objects.filter(
                                attachment_model=Attachments.MODEL_ORDERS,
                                attachment_model_id=model.order_id,
                                attachment_type=Attachments.TYPE_ORDER_INVOICE,
                            ).all()

                            for attachment in attachments:
                                if attachment.attachment_file_path:
                                    Utils.delete_file(attachment.attachment_file_path.path)
                                attachment.delete()

                            attachment = Attachments()
                            attachment.UPLOAD_PATH = Attachments.ORDERS_UPLOAD_PATH
                            attachment.attachment_model = Attachments.MODEL_ORDERS
                            attachment.attachment_model_id = model.order_id
                            attachment.attachment_type_id = 0
                            attachment.attachment_number = 0
                            attachment.attachment_type = Attachments.TYPE_ORDER_INVOICE
                            attachment.attachment_file_uploaded_at = Utils.get_current_datetime_utc()
                            attachment.attachment_file_uploaded_id = operator.operator_id
                            attachment.attachment_file_uploaded_by = operator.operator_name
                            attachment.attachment_file_uploaded_department = operator.operator_department
                            attachment.attachment_file_uploaded_role = operator.operator_role

                            original_filename = form.cleaned_data['attachment_file_path']

                            ext = original_filename.split('.')[-1]
                            new_filename = 'order_invoice_' + str(model.order_code) + '_' + str(
                                Utils.get_epochtime_ms()) + '.' + str(ext)
                            temp_file_path = settings.MEDIA_ROOT + 'temp/' + str(original_filename)
                            attachment_file_path = settings.MEDIA_ROOT + attachment.UPLOAD_PATH + str(
                                new_filename)
                            os.rename(temp_file_path, attachment_file_path)
                            url = attachment.UPLOAD_PATH + new_filename
                            size = str(os.path.getsize(attachment_file_path))
                            attachment.attachment_file_name = original_filename
                            attachment.attachment_file_path = url
                            attachment.attachment_file_type = str(mime.from_file(attachment_file_path))
                            attachment.attachment_file_size = size
                            attachment.save()

                            model.order_invoice_no = form.cleaned_data['order_invoice_no']

                            model.order_invoice_uploaded_at = Utils.get_current_datetime_utc()
                            model.order_invoice_uploaded_id = operator.operator_id
                            model.order_invoice_uploaded_by = operator.operator_name
                            model.order_invoice_uploaded_department = operator.operator_department
                            model.order_invoice_uploaded_role = operator.operator_role

                            model.order_status = Orders.STATUS_INVOICE_UPLOADED
                            model.save()

                            # sending notification to OPM
                            operators = Operators.objects.all().filter(
                                Q(operator_department=Operators.DEPARTMENT_DAF) &
                                Q(operator_role=Operators.ROLE_OPM)
                            )

                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_SUPPLIER,
                                    model.order_proposal_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "Invoice uploaded to review.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            messages.success(request, 'Updated successfully.')
                            return redirect(reverse("orders_view", args=[model.order_id]))
                        except Exception as e:
                            print('Exception: ' + str(e))
                            messages.error(request, '' + str(e))
                            return redirect(reverse("orders_view", args=[model.order_id]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("orders_view", args=[model.order_id]))
                else:
                    form = OrderInvoiceUpdateForm(
                        initial={
                            'order_purchase_no': model.order_purchase_no,
                            'order_invoice_no': model.order_invoice_no,
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
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update_payment_voucher_order(request, pk):
    template_url = 'orders/update-payment-voucher.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            try:
                model = Orders.objects.get(order_id=pk)
                if request.method == 'POST':

                    form = OrderPaymentVoucherUpdateForm(request.POST, request.FILES)

                    import magic
                    mime = magic.Magic(mime=True)
                    # noinspection PyArgumentList
                    if form.is_valid():
                        try:
                            attachments = Attachments.objects.filter(
                                attachment_model=Attachments.MODEL_ORDERS,
                                attachment_model_id=model.order_id,
                                attachment_type=Attachments.TYPE_ORDER_PAYMENT_VOUCHER,
                            ).all()

                            for attachment in attachments:
                                if attachment.attachment_file_path:
                                    Utils.delete_file(attachment.attachment_file_path.path)
                                attachment.delete()

                            attachment = Attachments()
                            attachment.UPLOAD_PATH = Attachments.ORDERS_UPLOAD_PATH
                            attachment.attachment_model = Attachments.MODEL_ORDERS
                            attachment.attachment_model_id = model.order_id
                            attachment.attachment_type_id = 0
                            attachment.attachment_number = 0
                            attachment.attachment_type = Attachments.TYPE_ORDER_PAYMENT_VOUCHER
                            attachment.attachment_file_uploaded_at = Utils.get_current_datetime_utc()
                            attachment.attachment_file_uploaded_id = operator.operator_id
                            attachment.attachment_file_uploaded_by = operator.operator_name
                            attachment.attachment_file_uploaded_department = operator.operator_department
                            attachment.attachment_file_uploaded_role = operator.operator_role

                            original_filename = form.cleaned_data['attachment_file_path']

                            ext = original_filename.split('.')[-1]
                            new_filename = 'order_payment_voucher_' + str(model.order_code) + '_' + str(
                                Utils.get_epochtime_ms()) + '.' + str(ext)
                            temp_file_path = settings.MEDIA_ROOT + 'temp/' + str(original_filename)
                            attachment_file_path = settings.MEDIA_ROOT + attachment.UPLOAD_PATH + str(
                                new_filename)
                            os.rename(temp_file_path, attachment_file_path)
                            url = attachment.UPLOAD_PATH + new_filename
                            size = str(os.path.getsize(attachment_file_path))
                            attachment.attachment_file_name = original_filename
                            attachment.attachment_file_path = url
                            attachment.attachment_file_type = str(mime.from_file(attachment_file_path))
                            attachment.attachment_file_size = size
                            attachment.save()

                            model.order_payment_voucher_no = form.cleaned_data['order_payment_voucher_no']

                            model.order_invoice_payment_voucher_uploaded_at = Utils.get_current_datetime_utc()
                            model.order_invoice_payment_voucher_uploaded_id = operator.operator_id
                            model.order_invoice_payment_voucher_uploaded_by = operator.operator_name
                            model.order_invoice_payment_voucher_uploaded_department = operator.operator_department
                            model.order_invoice_payment_voucher_uploaded_role = operator.operator_role

                            model.order_status = Orders.STATUS_INVOICE_PAYMENT_VOUCHER_GENERATED
                            model.save()

                            # sending notification to OPM
                            operators = Operators.objects.all().filter(
                                Q(operator_department=Operators.DEPARTMENT_DAF) &
                                Q(operator_role=Operators.ROLE_ACCOUNTANT_MANAGER)
                            )

                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_SUPPLIER,
                                    model.order_proposal_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_ORDER,
                                    model.order_id,
                                    "Invoice payment voucher uploaded for approval.",
                                    "/backend/orders/view/" + str(model.order_id) + "/"
                                )

                            messages.success(request, 'Updated successfully.')
                            return redirect(reverse("orders_view", args=[model.order_id]))
                        except Exception as e:
                            print('Exception: ' + str(e))
                            messages.error(request, '' + str(e))
                            return redirect(reverse("orders_view", args=[model.order_id]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("orders_view", args=[model.order_id]))
                else:
                    form = OrderPaymentVoucherUpdateForm(
                        initial={
                            'order_invoice_no': model.order_invoice_no,
                            'order_payment_voucher_no': model.order_payment_voucher_no,
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
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def send_purchase_order(request, pk):
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            try:
                model = Orders.objects.get(order_id=pk)

                attachment = Attachments.objects.get(
                    attachment_model=Attachments.MODEL_ORDERS,
                    attachment_model_id=model.order_id,
                    attachment_type=Attachments.TYPE_ORDER_PURCHASE,
                )

                order_proposal = Order_Proposals.objects.get(order_proposal_id=model.order_proposal_id)

                # sending email confirmation mail
                if settings.IS_LOCAL:
                    domain = settings.BACKEND_DOMAIN_LOCAL
                    logo_url = settings.LOGO_URL_LOCAL
                else:
                    domain = settings.BACKEND_DOMAIN_PROD
                    logo_url = settings.LOGO_URL_PROD

                contact_url = settings.APP_CONSTANT_COMPANY_WEBSITE
                link_url = '{domain}/{path}'.format(
                    domain=domain,
                    path="order-proposals/create/" + str(order_proposal.orders_order_id) + "/" + str(
                        order_proposal.order_proposal_code) + "/"
                )
                link_name = "View Details"

                acknowledge_url = '/orders/update/acknowledge/' + str(pk) + '/'
                acknowledge_url = "<a title=\"link\" href=\"" + str(
                    domain) + acknowledge_url + "\" target=\"_blank\" rel=\"noopener\">link</a>"

                message = "Please find the attachment for purchase order and acknowledge by clicking on this " + acknowledge_url + "."
                html_content = render_to_string(
                    'email/email-info-with-link.html',
                    {
                        'logo_url': logo_url,
                        'contact_url': contact_url,
                        'link_url': link_url,
                        'link_name': link_name,
                        'name': order_proposal.order_proposal_supplier_title,
                        'message': defaultfilters.safe(message),
                    }
                )
                text_content = strip_tags(html_content)

                email_message = EmailMultiAlternatives(
                    subject=settings.EMAIL_NOTIFICATION_SUBJECT,
                    body=text_content,
                    from_email=settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                    to=[order_proposal.order_proposal_supplier_contact_email_id],
                    cc=[settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID],
                    reply_to=[settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID],
                )
                email_message.attach_alternative(html_content, "text/html")

                email_message.attach_file(attachment.attachment_file_path.path)

                email_message.send(fail_silently=False)

                messages.success(request, 'Purchase order email sent successfully.')

                return redirect(reverse("orders_view", args=[model.order_id]))
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist, Attachments.DoesNotExist,
                   Order_Proposals.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


@csrf_exempt
# noinspection PyUnusedLocal, PyShadowingBuiltins
def acknowledge_proposal_external(request, pk):
    try:
        model = Orders.objects.get(order_id=pk)
        order_proposal = Order_Proposals.objects.get(order_proposal_id=model.order_proposal_id)

        if model.order_status == Orders.STATUS_PURCHASE_GENERATED:
            model.order_acknowledged_at = Utils.get_current_datetime_utc()
            model.order_acknowledged_id = ''
            model.order_acknowledged_by = ''
            model.order_acknowledged_department = ''
            model.order_acknowledged_role = ''
            model.order_status = Orders.STATUS_ACKNOWLEDGED
            model.save()

        # sending notification to Officer
        if model.order_assigned_to_id != str(0):
            operators = Operators.objects.all().filter(
                Q(operator_id=model.order_assigned_to_id)
            )
        else:
            operators = Operators.objects.all().filter(
                Q(operator_department=Operators.DEPARTMENT_DAF) &
                Q(operator_role=model.order_assigned_to_role)
            )

        for item in operators:
            Notifications.add_notification(
                Notifications.TYPE_SUPPLIER,
                model.order_proposal_id,
                Notifications.TYPE_OPERATOR,
                item.operator_id,
                Notifications.TYPE_ORDER,
                model.order_id,
                "Acknowledged purchase order.",
                "/backend/orders/view/" + str(model.order_id) + "/",
            )

        messages.success(request, 'Acknowledged successfully.')
        return redirect(reverse("order_proposals_create", args=[pk, order_proposal.order_proposal_code]))

    except(TypeError, ValueError, OverflowError, Orders.DoesNotExist, Order_Proposals.DoesNotExist):
        return HttpResponseNotFound('Not Found', content_type='text/plain')
