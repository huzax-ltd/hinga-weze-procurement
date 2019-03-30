from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from app import settings
from app.models import Operators, Product_Requests, Product_Request_Items, Products
from app.utils import Utils
from backend.forms.product_request_item_forms import ProductRequestItemCreateForm, ProductRequestItemUpdateForm


# noinspection PyUnusedLocal, PyShadowingBuiltins
def create(request, id):
    template_url = 'product-request-items/create.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_CREATE in auth_permissions.values():
            try:
                product_request = Product_Requests.objects.get(product_request_id=id)
                if request.method == 'POST':

                    form = ProductRequestItemCreateForm(request.POST)
                    # noinspection PyArgumentList
                    if form.is_valid():
                        model = Product_Request_Items()
                        model.product_requests_product_request_id = product_request.product_request_id
                        model.products_product_id = form.cleaned_data['products_product_id']

                        product = Products.objects.get(product_id=model.products_product_id)

                        model.product_request_item_product_type = product.product_type
                        model.product_request_item_product_code = product.product_code
                        model.product_request_item_product_tag = product.product_tag
                        model.product_request_item_product_category = product.product_category
                        model.product_request_item_product_title = product.product_title
                        model.product_request_item_product_sub_title = product.product_sub_title
                        model.product_request_item_product_quantity_initial = 0
                        model.product_request_item_product_quantity_ordered = form.cleaned_data[
                            'product_request_item_product_quantity_ordered']
                        model.product_request_item_product_quantity_balance = 0
                        model.product_request_item_product_quantity_unit = product.product_quantity_unit

                        model.product_request_item_created_at = Utils.get_current_datetime_utc()
                        model.product_request_item_created_id = operator.operator_id
                        model.product_request_item_created_by = operator.operator_name
                        model.product_request_item_created_department = operator.operator_department
                        model.product_request_item_created_role = operator.operator_role

                        model.product_request_item_updated_at = Utils.get_current_datetime_utc()
                        model.product_request_item_updated_id = operator.operator_id
                        model.product_request_item_updated_by = operator.operator_name
                        model.product_request_item_updated_department = operator.operator_department
                        model.product_request_item_updated_role = operator.operator_role

                        model.product_request_item_received_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                        model.product_request_item_received_id = ''
                        model.product_request_item_received_by = ''
                        model.product_request_item_received_department = ''
                        model.product_request_item_received_role = ''

                        model.product_request_item_status = Product_Requests.STATUS_PENDING
                        # noinspection PyCallByClass,PyTypeChecker
                        model.save('Created')

                        Product_Requests.update_grand_total(request, product_request, operator)

                        messages.success(request, 'Item added successfully.')
                        return redirect(reverse("product_requests_view", args=[product_request.product_request_id]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("product_requests_view", args=[product_request.product_request_id]))

                else:
                    form = ProductRequestItemCreateForm(
                        initial={
                            'product_request_id': product_request.product_request_code,
                            'products_product_id': '',
                            'product_request_item_product_quantity_ordered': 0,
                        })

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_STOCK_ALL_REQUESTS,
                        'title': Product_Request_Items.TITLE,
                        'name': Product_Request_Items.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                    }
                )
            except(TypeError, ValueError, OverflowError,
                   Product_Requests.DoesNotExist, Product_Request_Items.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update(request, pk):
    template_url = 'product-request-items/update.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            try:
                model = Product_Request_Items.objects.get(product_request_item_id=pk)
                product_request = Product_Requests.objects.get(
                    product_request_id=model.product_requests_product_request_id)
                if request.method == 'POST':

                    form = ProductRequestItemUpdateForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.products_product_id = form.cleaned_data['products_product_id']

                        product = Products.objects.get(product_id=model.products_product_id)

                        model.product_request_item_product_type = product.product_type
                        model.product_request_item_product_code = product.product_code
                        model.product_request_item_product_tag = product.product_tag
                        model.product_request_item_product_category = product.product_category
                        model.product_request_item_product_title = product.product_title
                        model.product_request_item_product_sub_title = product.product_sub_title
                        model.product_request_item_product_quantity_initial = 0
                        model.product_request_item_product_quantity_ordered = form.cleaned_data[
                            'product_request_item_product_quantity_ordered']
                        model.product_request_item_product_quantity_balance = 0
                        model.product_request_item_product_quantity_unit = product.product_quantity_unit

                        model.product_request_item_updated_at = Utils.get_current_datetime_utc()
                        model.product_request_item_updated_id = operator.operator_id
                        model.product_request_item_updated_by = operator.operator_name
                        model.product_request_item_updated_department = operator.operator_department
                        model.product_request_item_updated_role = operator.operator_role
                        model.save()

                        Product_Requests.update_grand_total(request, product_request, operator)

                        messages.success(request, 'Item updated successfully.')
                        return redirect(reverse("product_requests_view", args=[product_request.product_request_id]))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("product_requests_view", args=[product_request.product_request_id]))
                else:
                    form = ProductRequestItemUpdateForm(
                        initial={
                            'product_request_id': product_request.product_request_code,
                            'products_product_id': model.products_product_id,
                            'product_request_item_product_quantity_ordered': model.product_request_item_product_quantity_ordered,
                        }
                    )

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_STOCK_ALL_REQUESTS,
                        'title': Product_Request_Items.TITLE,
                        'name': Product_Request_Items.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'model': model,
                    }
                )
            except(
                    TypeError, ValueError, OverflowError, Product_Requests.DoesNotExist,
                    Product_Request_Items.DoesNotExist):
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
                            model = Product_Request_Items.objects.get(product_request_item_id=id)
                            product_request = Product_Requests.objects.get(
                                product_request_id=model.product_requests_product_request_id)

                            Product_Request_Items.delete_product_request_item(request, model, operator)

                            Product_Requests.update_grand_total(request, product_request, operator)

                            messages.success(request, 'Item removed successfully.')
                        except(TypeError, ValueError, OverflowError, Product_Request_Items.DoesNotExist):
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
                if action == 'order-item-received':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        for id in ids:
                            try:
                                model = Product_Request_Items.objects.get(product_request_item_id=id)
                                if model.product_request_item_status == Product_Request_Items.STATUS_PENDING:
                                    try:
                                        product = Products.objects.get(product_id=model.products_product_id)

                                        model.product_request_item_product_quantity_initial = product.product_quantity_available

                                        product.product_quantity_available = product.product_quantity_available - model.product_request_item_product_quantity_ordered

                                        model.product_request_item_product_quantity_balance = product.product_quantity_available

                                        product.product_updated_at = Utils.get_current_datetime_utc()
                                        product.product_updated_id = operator.operator_id
                                        product.product_updated_by = operator.operator_name
                                        product.product_updated_department = operator.operator_department
                                        product.product_updated_role = operator.operator_role
                                        product.save()
                                    except (Product_Requests.DoesNotExist, Products.DoesNotExist):
                                        print('Product Request does not exist.')

                                    model.product_request_item_received_at = Utils.get_current_datetime_utc()
                                    model.product_request_item_received_id = operator.operator_id
                                    model.product_request_item_received_by = operator.operator_name
                                    model.product_request_item_received_department = operator.operator_department
                                    model.product_request_item_received_role = operator.operator_role
                                    model.product_request_item_status = Product_Request_Items.STATUS_RECEIVED
                                    model.save()

                            except(TypeError, ValueError, OverflowError, Product_Request_Items.DoesNotExist):
                                continue
                        messages.success(request, 'Updated successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-item-pending':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        for id in ids:
                            try:
                                model = Product_Request_Items.objects.get(product_request_item_id=id)
                                if model.product_request_item_status == Product_Request_Items.STATUS_RECEIVED:
                                    try:
                                        product = Products.objects.get(product_id=model.products_product_id)

                                        model.product_request_item_product_quantity_initial = 0

                                        product.product_quantity_available = product.product_quantity_available + model.product_request_item_product_quantity_ordered

                                        model.product_request_item_product_quantity_balance = 0

                                        product.product_updated_at = Utils.get_current_datetime_utc()
                                        product.product_updated_id = operator.operator_id
                                        product.product_updated_by = operator.operator_name
                                        product.product_updated_department = operator.operator_department
                                        product.product_updated_role = operator.operator_role
                                        product.save()
                                    except (Product_Requests.DoesNotExist, Products.DoesNotExist):
                                        print('Product Request not exist.')

                                    model.product_request_item_received_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                                    model.product_request_item_received_id = ''
                                    model.product_request_item_received_by = ''
                                    model.product_request_item_received_department = ''
                                    model.product_request_item_received_role = ''
                                    model.product_request_item_status = Product_Request_Items.STATUS_PENDING
                                    model.save()

                            except(TypeError, ValueError, OverflowError, Product_Request_Items.DoesNotExist):
                                continue
                        messages.success(request, 'Updated successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                return HttpResponse('success', content_type='text/plain')
            else:
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')
    else:
        return HttpResponseForbidden('Forbidden', content_type='text/plain')
