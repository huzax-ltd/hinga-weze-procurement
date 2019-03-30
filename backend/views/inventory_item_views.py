from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from app import settings
from app.models import Operators, Orders, Order_Items, Order_Proposals, Inventory, Inventory_Items, Products
from app.utils import Utils
from backend.forms.inventory_item_forms import InventoryItemCreateForm


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
def create(request, pk, action, ids):
    template_url = 'inventory-items/create.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            # try:
            order = Orders.objects.get(order_id=pk)
            order_proposal = Order_Proposals.objects.get(order_proposal_id=order.order_proposal_id)
            try:
                print(ids)
                ids = ids.split("-")
                print(ids)
            except(TypeError, ValueError, OverflowError):
                ids = None
            if action != 'order-item-received' or ids is None:
                return HttpResponseNotFound('Not Found', content_type='text/plain')
            else:
                if request.method == 'POST':
                    form = InventoryItemCreateForm(request.POST)
                    # noinspection PyArgumentList
                    if form.is_valid():
                        inventory_item_voucher_reference = form.cleaned_data['inventory_item_voucher_reference']
                        inventory_item_location = form.cleaned_data['inventory_item_location']
                        inventory_item_equipment_holder_status = form.cleaned_data[
                            'inventory_item_equipment_holder_status']
                        inventory_item_staff_name = form.cleaned_data['inventory_item_staff_name']
                        inventory_item_room_number = form.cleaned_data['inventory_item_room_number']
                        inventory_item_disposal_date = form.cleaned_data['inventory_item_disposal_date']
                        inventory_item_verified_date = form.cleaned_data['inventory_item_verified_date']
                        inventory_item_present_condition = form.cleaned_data['inventory_item_present_condition']
                        inventory_item_remark = form.cleaned_data['inventory_item_remark']

                        try:
                            inventory = Inventory.objects.get(inventory_order_purchase_no=order.order_purchase_no)
                            inventory.inventory_order_proposal_id = order.order_proposal_id
                            inventory.inventory_order_proposal_supplier_title = order_proposal.order_proposal_supplier_title
                            inventory.inventory_updated_at = Utils.get_current_datetime_utc()
                            inventory.inventory_updated_id = operator.operator_id
                            inventory.inventory_updated_by = operator.operator_name
                            inventory.inventory_updated_department = operator.operator_department
                            inventory.inventory_updated_role = operator.operator_role
                            inventory.save()
                        except Inventory.DoesNotExist:
                            inventory = Inventory()
                            inventory.inventory_order_purchase_no = order.order_purchase_no
                            inventory.inventory_order_proposal_id = order.order_proposal_id
                            inventory.inventory_order_proposal_supplier_title = order_proposal.order_proposal_supplier_title
                            inventory.inventory_created_at = Utils.get_current_datetime_utc()
                            inventory.inventory_created_id = operator.operator_id
                            inventory.inventory_created_by = operator.operator_name
                            inventory.inventory_created_department = operator.operator_department
                            inventory.inventory_created_role = operator.operator_role
                            inventory.inventory_updated_at = Utils.get_current_datetime_utc()
                            inventory.inventory_updated_id = operator.operator_id
                            inventory.inventory_updated_by = operator.operator_name
                            inventory.inventory_updated_department = operator.operator_department
                            inventory.inventory_updated_role = operator.operator_role
                            inventory.save()

                        for id in ids:
                            try:
                                order_item = Order_Items.objects.get(order_item_id=id)
                                if order_item.order_item_type != Order_Items.TYPE_SERVICE:
                                    order_item.order_item_received_at = Utils.get_current_datetime_utc()
                                    order_item.order_item_received_id = operator.operator_id
                                    order_item.order_item_received_by = operator.operator_name
                                    order_item.order_item_received_department = operator.operator_department
                                    order_item.order_item_received_role = operator.operator_role
                                    order_item.order_item_status = Order_Items.STATUS_RECEIVED
                                    order_item.save()

                                    try:
                                        product = Products.objects.get(product_id=order_item.order_item_type_id)
                                        inventory_item = Inventory_Items()
                                        inventory_item.inventory_inventory_id = inventory.inventory_id
                                        inventory_item.products_product_id = order_item.order_item_type_id
                                        inventory_item.inventory_item_product_type = order_item.order_item_type
                                        inventory_item.inventory_item_product_code = product.product_code
                                        inventory_item.inventory_item_product_tag = product.product_tag
                                        inventory_item.inventory_item_product_category = product.product_category
                                        inventory_item.inventory_item_product_title = product.product_title
                                        inventory_item.inventory_item_product_sub_title = product.product_sub_title
                                        inventory_item.inventory_item_product_quantity_initial = product.product_quantity_available
                                        inventory_item.inventory_item_product_quantity_ordered = order_item.order_item_quantity_ordered
                                        inventory_item.inventory_item_product_quantity_balance = product.product_quantity_available + order_item.order_item_quantity_ordered
                                        inventory_item.inventory_item_product_quantity_unit = product.product_quantity_unit
                                        inventory_item.inventory_item_product_currency = order_item.order_item_currency
                                        inventory_item.inventory_item_product_unit_price = order_item.order_item_unit_price
                                        inventory_item.inventory_item_product_rate_price = 0
                                        inventory_item.inventory_item_product_usd_price = 0
                                        inventory_item.inventory_item_product_usaid_equipment_price = 0
                                        inventory_item.inventory_item_product_small_equipment_price = 0
                                        inventory_item.inventory_item_project = order.order_project_name
                                        inventory_item.inventory_item_voucher_reference = inventory_item_voucher_reference
                                        inventory_item.inventory_item_location = inventory_item_location
                                        inventory_item.inventory_item_equipment_holder_status = inventory_item_equipment_holder_status
                                        inventory_item.inventory_item_staff_name = inventory_item_staff_name
                                        inventory_item.inventory_item_room_number = inventory_item_room_number
                                        inventory_item.inventory_item_present_condition = inventory_item_present_condition
                                        inventory_item.inventory_item_disposal_date = inventory_item_disposal_date
                                        inventory_item.inventory_item_verified_date = inventory_item_verified_date
                                        inventory_item.inventory_item_remark = inventory_item_remark
                                        inventory_item.inventory_created_at = Utils.get_current_datetime_utc()
                                        inventory_item.inventory_created_id = operator.operator_id
                                        inventory_item.inventory_created_by = operator.operator_name
                                        inventory_item.inventory_created_department = operator.operator_department
                                        inventory_item.inventory_created_role = operator.operator_role
                                        inventory_item.inventory_updated_at = Utils.get_current_datetime_utc()
                                        inventory_item.inventory_updated_id = operator.operator_id
                                        inventory_item.inventory_updated_by = operator.operator_name
                                        inventory_item.inventory_updated_department = operator.operator_department
                                        inventory_item.inventory_updated_role = operator.operator_role
                                        inventory_item.save()

                                        product.product_quantity_available = product.product_quantity_available + order_item.order_item_quantity_ordered
                                        product.product_updated_at = Utils.get_current_datetime_utc()
                                        product.product_updated_id = operator.operator_id
                                        product.product_updated_by = operator.operator_name
                                        product.product_updated_department = operator.operator_department
                                        product.product_updated_role = operator.operator_role
                                        product.save()

                                    except Products.DoesNotExist:
                                        continue

                            except Order_Items.DoesNotExist:
                                continue

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("order_items_index", args=[order.order_id]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("order_items_index", args=[order.order_id]))
                else:
                    form = InventoryItemCreateForm(
                        initial={
                            'inventory_order_purchase_no': order.order_purchase_no,
                            'inventory_order_project_name': order.order_project_name,
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
                    }
                )
        # except(TypeError, ValueError, OverflowError, Orders.DoesNotExist, Order_Proposals.DoesNotExist,
        #        Order_Proposals.DoesNotExist):
        #     return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')
