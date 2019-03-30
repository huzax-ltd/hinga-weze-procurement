from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from app import settings
from app.models import Operators, Orders, Order_Items, Inventory, Inventory_Items, Products
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
            # try:
            order = Orders.objects.get(order_id=order_id)
            if request.method == 'POST':

                form = OrderItemCreateForm(request.POST)
                # noinspection PyArgumentList
                if form.is_valid():
                    model = Order_Items()
                    model.orders_order_id = order_id

                    title = 'unknown'
                    type = form.cleaned_data['type']
                    model.order_item_type_id = 0
                    if type == 'service':
                        title = form.cleaned_data['title_service']
                    if type == 'goods':
                        type_id = form.cleaned_data['title_goods']
                        model.order_item_type_id = type_id
                        product = Products.objects.get(product_id=type_id)
                        title = product.product_title
                    if type == 'asset':
                        type_id = form.cleaned_data['title_asset']
                        model.order_item_type_id = type_id
                        product = Products.objects.get(product_id=type_id)
                        title = product.product_title

                    model.order_item_type = type
                    model.order_item_title = title
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
                    'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                    'title': Order_Items.TITLE,
                    'name': Order_Items.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'form': form,
                }
            )
        # except(TypeError, ValueError, OverflowError, Orders.DoesNotExist, Order_Items.DoesNotExist):
        #     return HttpResponseNotFound('Not Found', content_type='text/plain')
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
            # try:
            model = Order_Items.objects.get(order_item_id=pk)
            order = Orders.objects.get(order_id=model.orders_order_id)
            if request.method == 'POST':

                form = OrderItemUpdateForm(request.POST)

                # noinspection PyArgumentList
                if form.is_valid():
                    title = 'unknown'
                    type = form.cleaned_data['type']
                    model.order_item_type_id = 0
                    if type == 'service':
                        title = form.cleaned_data['title_service']
                    if type == 'goods':
                        type_id = form.cleaned_data['title_goods']
                        model.order_item_type_id = type_id
                        product = Products.objects.get(product_id=type_id)
                        title = product.product_title
                    if type == 'asset':
                        type_id = form.cleaned_data['title_asset']
                        model.order_item_type_id = type_id
                        product = Products.objects.get(product_id=type_id)
                        title = product.product_title

                    model.order_item_type = type
                    model.order_item_title = title
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
                title = 'unknown'
                type = model.order_item_type
                if type == 'service':
                    title = model.order_item_title
                if type == 'goods':
                    title = model.order_item_type_id
                if type == 'asset':
                    title = model.order_item_type_id
                form = OrderItemUpdateForm(
                    initial={
                        'order_id': order.order_code,
                        'type': type,
                        'title_service': title,
                        'title_goods': title,
                        'title_asset': title,
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
                    'section': settings.BACKEND_SECTION_PROCUREMENT_ALL_REQUESTS,
                    'title': Order_Items.TITLE,
                    'name': Order_Items.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'form': form,
                    'model': model,
                }
            )
        # except(TypeError, ValueError, OverflowError, Orders.DoesNotExist, Order_Items.DoesNotExist):
        #     return HttpResponseNotFound('Not Found', content_type='text/plain')
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
                        except(TypeError, ValueError, OverflowError, Order_Items.DoesNotExist):
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
                if action == 'usaid-approve-yes':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        for id in ids:
                            try:
                                model = Order_Items.objects.get(order_item_id=id)
                                model.order_item_usaid_approval = True
                                model.save()
                            except(TypeError, ValueError, OverflowError, Order_Items.DoesNotExist):
                                continue
                        messages.success(request, 'Updated successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'usaid-approve-no':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        for id in ids:
                            try:
                                model = Order_Items.objects.get(order_item_id=id)
                                model.order_item_usaid_approval = False
                                model.save()
                            except(TypeError, ValueError, OverflowError, Order_Items.DoesNotExist):
                                continue
                        messages.success(request, 'Updated successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-item-received':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        for id in ids:
                            try:
                                model = Order_Items.objects.get(order_item_id=id)
                                if model.order_item_status == Order_Items.STATUS_PENDING:
                                    if model.order_item_type == Order_Items.TYPE_SERVICE:
                                        model.order_item_received_at = Utils.get_current_datetime_utc()
                                        model.order_item_received_id = operator.operator_id
                                        model.order_item_received_by = operator.operator_name
                                        model.order_item_received_department = operator.operator_department
                                        model.order_item_received_role = operator.operator_role
                                        model.order_item_status = Order_Items.STATUS_RECEIVED
                                        model.save()
                            except(TypeError, ValueError, OverflowError, Order_Items.DoesNotExist):
                                continue
                        messages.success(request, 'Updated successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-item-pending':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        for id in ids:
                            try:
                                model = Order_Items.objects.get(order_item_id=id)
                                if model.order_item_status == Order_Items.STATUS_RECEIVED:
                                    if model.order_item_type != Order_Items.TYPE_SERVICE:
                                        try:
                                            order = Orders.objects.get(order_id=model.orders_order_id)
                                            inventory = Inventory.objects.get(
                                                inventory_order_purchase_no=order.order_purchase_no)
                                            inventory_items = Inventory_Items.objects.filter(
                                                inventory_inventory_id=inventory.inventory_id)
                                            for inventory_item in inventory_items:
                                                try:
                                                    product = Products.objects.get(
                                                        product_id=inventory_item.products_product_id)
                                                    product.product_quantity_available = product.product_quantity_available - inventory_item.inventory_item_product_quantity_ordered
                                                    product.product_updated_at = Utils.get_current_datetime_utc()
                                                    product.product_updated_id = operator.operator_id
                                                    product.product_updated_by = operator.operator_name
                                                    product.product_updated_department = operator.operator_department
                                                    product.product_updated_role = operator.operator_role
                                                    product.save()
                                                    inventory_item.delete()
                                                except Products.DoesNotExist:
                                                    inventory_item.delete()
                                                    continue
                                        except (Orders.DoesNotExist, Inventory.DoesNotExist):
                                            print('Order or inventory does not exist.')
                                    model.order_item_received_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                                    model.order_item_received_id = ''
                                    model.order_item_received_by = ''
                                    model.order_item_received_department = ''
                                    model.order_item_received_role = ''
                                    model.order_item_status = Order_Items.STATUS_PENDING
                                    model.save()

                            except(TypeError, ValueError, OverflowError, Order_Items.DoesNotExist):
                                continue
                        messages.success(request, 'Updated successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                return HttpResponse('success', content_type='text/plain')
            else:
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')
    else:
        return HttpResponseForbidden('Forbidden', content_type='text/plain')
