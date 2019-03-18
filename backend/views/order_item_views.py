from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from app import settings
from app.models import Operators, Orders, Order_Items
from app.utils import Utils
from backend.forms.order_item_forms import OrderItemCreateForm, OrderItemUpdateForm


# noinspection PyUnusedLocal
def json_order_items(request):
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            return HttpResponse(serializers.serialize("json", Order_Items.objects.all()),
                                content_type="application/json")
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def create(request, order_id):
    template_url = 'order-items/create.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_CREATE in auth_permissions.values():
            try:
                order = Orders.objects.get(order_id=order_id)
                if request.method == 'POST':

                    form = OrderItemCreateForm(request.POST)
                    # noinspection PyArgumentList
                    if form.is_valid():
                        model = Order_Items()
                        model.orders_order_id = order_id

                        model.order_item_title = form.cleaned_data['title']
                        model.order_item_sub_title = ''
                        model.order_item_quantity_ordered = form.cleaned_data['quantity_ordered']
                        model.order_item_quantity_unit = form.cleaned_data['quantity_unit']
                        model.order_item_unit_price = form.cleaned_data['unit_price']
                        model.order_item_total_price = model.order_item_quantity_ordered * model.order_item_unit_price
                        model.order_item_usaid_approval = 0

                        model.order_item_created_at = Utils.get_current_datetime_utc()
                        model.order_item_created_id = operator.operator_id
                        model.order_item_created_by = operator.operator_name
                        model.order_item_created_department = operator.operator_department
                        model.order_item_created_role = operator.operator_role

                        model.order_item_updated_at = Utils.get_current_datetime_utc()
                        model.order_item_updated_id = operator.operator_id
                        model.order_item_updated_by = operator.operator_name
                        model.order_item_updated_department = operator.operator_department
                        model.order_item_updated_role = operator.operator_role

                        model.order_item_received_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                        model.order_item_received_id = ''
                        model.order_item_received_by = ''
                        model.order_item_received_department = ''
                        model.order_item_received_role = ''

                        model.order_item_status = Orders.STATUS_PENDING
                        # noinspection PyCallByClass,PyTypeChecker
                        model.save('Created')

                        Orders.update_grand_total(request, order, operator)

                        messages.success(request, 'Item added successfully.')
                        return redirect(reverse("orders_view", args=[order_id]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("orders_view", args=[order_id]))

                else:
                    form = OrderItemCreateForm(
                        initial={
                            'order_id': order.order_code,
                            'title': '',
                            'duration': 0,
                            'unit_price': 0,
                            'currency': Order_Items.CURRENCY_RWF,
                            'quantity_ordered': 0,
                            'quantity_unit': '',
                        })

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_ORDERS,
                        'title': Order_Items.TITLE,
                        'name': Order_Items.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist, Order_Items.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update(request, pk):
    template_url = 'order-items/update.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            try:
                model = Order_Items.objects.get(order_item_id=pk)
                order = Orders.objects.get(order_id=model.orders_order_id)
                if request.method == 'POST':

                    form = OrderItemUpdateForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.order_item_title = form.cleaned_data['title']
                        model.order_item_sub_title = ''
                        model.order_item_quantity_ordered = form.cleaned_data['quantity_ordered']
                        model.order_item_quantity_unit = form.cleaned_data['quantity_unit']
                        model.order_item_unit_price = form.cleaned_data['unit_price']
                        model.order_item_total_price = model.order_item_quantity_ordered * model.order_item_unit_price

                        model.order_item_updated_at = Utils.get_current_datetime_utc()
                        model.order_item_updated_id = operator.operator_id
                        model.order_item_updated_by = operator.operator_name
                        model.order_item_updated_department = operator.operator_department
                        model.order_item_updated_role = operator.operator_role
                        model.save()

                        Orders.update_grand_total(request, order, operator)

                        messages.success(request, 'Item updated successfully.')
                        return redirect(reverse("orders_view", args=[order.order_id]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("orders_view", args=[order_id]))
                else:
                    form = OrderItemUpdateForm(
                        initial={
                            'order_id': order.order_code,
                            'title': model.order_item_title,
                            'duration': model.order_item_duration,
                            'unit_price': model.order_item_unit_price,
                            'currency': model.order_item_currency,
                            'quantity_ordered': model.order_item_quantity_ordered,
                            'quantity_unit': model.order_item_quantity_unit,
                        }
                    )

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_ORDERS,
                        'title': Order_Items.TITLE,
                        'name': Order_Items.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'model': model,
                    }
                )
            except(TypeError, ValueError, OverflowError, Orders.DoesNotExist, Order_Items.DoesNotExist):
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
                if action == 'delete':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Order_Items.objects.get(order_item_id=id)
                            order = Orders.objects.get(order_id=model.orders_order_id)

                            Order_Items.delete_order_item(request, model, operator)

                            Orders.update_grand_total(request, order, operator)

                            messages.success(request, 'Item removed successfully.')
                        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                return HttpResponse('success', content_type='text/plain')
            else:
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')
    else:
        return HttpResponseForbidden('Forbidden', content_type='text/plain')
