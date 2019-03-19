from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from app import settings
from app.models import Operators, Orders, Order_Items
from app.utils import Utils
from backend.forms.order_forms import OrderSearchIndexForm, OrderCreateForm, OrderUpdateForm
from backend.tables.order_tables import OrdersTable


# noinspection PyUnusedLocal
def json_orders(request):
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            return HttpResponse(serializers.serialize("json", Orders.objects.all()),
                                content_type="application/json")
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


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
                    'section': settings.BACKEND_SECTION_ORDERS,
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
                                Orders.request_order(request, model, operator)
                                messages.success(request, 'Order requested successfully.')
                            else:
                                messages.success(request, 'Forbidden')
                        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
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
                    model.order_proposal_id = 0
                    model.order_proposal_due_date = settings.APP_CONSTANT_DEFAULT_DATE_VALUE
                    model.order_purchase_no = 0
                    model.order_invoice_no = 0

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

                    model.order_purchase_generated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.order_purchase_generated_id = ''
                    model.order_purchase_generated_by = ''
                    model.order_purchase_generated_department = ''
                    model.order_purchase_generated_role = ''

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
                            'section': settings.BACKEND_SECTION_ORDERS,
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
                    'section': settings.BACKEND_SECTION_ORDERS,
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
                                'section': settings.BACKEND_SECTION_ORDERS,
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
                    model.order_anticipated_start_date = Utils.get_us_format_date(
                        str(model.order_anticipated_start_date))
                    model.order_anticipated_end_date = Utils.get_us_format_date(str(model.order_anticipated_end_date))
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
                        'section': settings.BACKEND_SECTION_ORDERS,
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

                if model.order_created_id == Operators.operator_id and model.order_status == Orders.STATUS_PENDING:
                    template_url = 'orders/view-edit.html'

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_ORDERS,
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
                        'item_select_single_url': reverse("order_item_select_single"),
                        'status_html_tag': Orders.get_status_html_tag(model)
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')
