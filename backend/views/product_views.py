from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from app import settings
from app.models import Operators, Products, Inventory_Items, Product_Request_Items
from app.utils import Utils
from backend.forms.product_forms import ProductExcelImportForm, ProductSearchIndexForm, ProductInventorySearchIndexForm
from backend.tables.product_tables import ProductGoodsTable, ProductAssetsTable, ProductGoodsInventoryTable, \
    ProductAssetsInventoryTable


# noinspection PyUnusedLocal, PyShadowingBuiltins
def import_excel(request):
    template_url = 'products/import-excel.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
            if operator.operator_type != Operators.TYPE_SUPER_ADMIN:
                return HttpResponseForbidden('Forbidden', content_type='text/plain')
            else:
                if request.method == 'POST':
                    form = ProductExcelImportForm(request.POST, request.FILES)
                    if form.is_valid():
                        if 'excel_file' in request.FILES and \
                                request.FILES['excel_file']:
                            excel_file = form.cleaned_data['excel_file']
                            import pandas as pd
                            df = pd.read_excel(excel_file)
                            matrix = df.values
                            df = pd.DataFrame(df)
                            error = ''
                            success = 0
                            failed = 0
                            for index, row in df.iterrows():
                                print(index, row)
                                try:
                                    type = row['type']
                                    tag = row['tag']
                                    title = row['title']
                                    category = row['category']

                                    fail = False

                                    try:
                                        product = Products.objects.get(product_tag=tag)
                                    except Products.DoesNotExist:
                                        product = None

                                    if product is None:
                                        product = Products()
                                        product.product_code = Products.generate_random_number('product_code',
                                                                                               8)
                                        product.product_sub_title = ''
                                        product.product_quantity_available = 0
                                        product.product_quantity_unit = ''

                                    product.product_type = type
                                    product.product_tag = tag
                                    product.product_category = category
                                    product.product_title = title

                                    product.product_updated_at = Utils.get_current_datetime_utc()
                                    product.product_updated_id = operator.operator_id
                                    product.product_updated_by = operator.operator_name
                                    product.product_updated_department = operator.operator_department
                                    product.product_updated_role = operator.operator_role
                                    product.save()

                                    success = success + 1

                                except Exception as e:
                                    failed = failed + 1
                                    error = error + " <br> " + 'Error - [Row: ' + str(index) + '] ' + str(e)

                            message = 'Success: ' + str(success) + ', Failed: ' + str(failed)
                            message = message + error
                            messages.warning(request, message)

                            form = ProductExcelImportForm()

                            return render(
                                request, template_url,
                                {
                                    'section': settings.BACKEND_SECTION_SETTINGS,
                                    'title': Products.TITLE,
                                    'name': Products.NAME,
                                    'operator': operator,
                                    'auth_permissions': auth_permissions,
                                    'form': form,
                                }
                            )
                        else:
                            messages.error(request, 'Error: Select excel file to import.')
                            return render(
                                request, template_url,
                                {
                                    'section': settings.BACKEND_SECTION_SETTINGS,
                                    'title': Products.TITLE,
                                    'name': Products.NAME,
                                    'operator': operator,
                                    'auth_permissions': auth_permissions,
                                    'form': form,
                                }
                            )
                    else:
                        messages.error(request, 'Error: invalid form inputs.')
                        return render(
                            request, template_url,
                            {
                                'section': settings.BACKEND_SECTION_SETTINGS,
                                'title': Products.TITLE,
                                'name': Products.NAME,
                                'operator': operator,
                                'auth_permissions': auth_permissions,
                                'form': form,
                            }
                        )
                else:
                    form = ProductExcelImportForm()

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_SETTINGS,
                        'title': Products.TITLE,
                        'name': Products.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                    }
                )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal
def index_goods(request):
    template_url = 'products/index-goods.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_PRODUCT_VIEW in auth_permissions.values():
            search_form = ProductSearchIndexForm(request.POST or None)
            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                objects = Products.objects.filter(product_type=Products.TYPE_GOODS).order_by('product_tag',
                                                                                             'product_title')
                table = ProductGoodsTable(objects)
            else:
                display_search = False
                objects = Products.objects.filter(product_type=Products.TYPE_GOODS).order_by('product_tag',
                                                                                             'product_title')
                table = ProductGoodsTable(objects)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_STOCK_ALL_GOODS,
                    'title': Products.TITLE,
                    'name': Products.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'search_form': search_form,
                    'display_search': display_search,
                    'index_url': reverse("products_index_goods"),
                    'select_multiple_url': '#',
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal
def index_assets(request):
    template_url = 'products/index-assets.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_PRODUCT_VIEW in auth_permissions.values():
            search_form = ProductSearchIndexForm(request.POST or None)
            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                objects = Products.objects.filter(product_type=Products.TYPE_ASSET).order_by('product_tag',
                                                                                             'product_title')
                table = ProductAssetsTable(objects)
            else:
                display_search = False
                objects = Products.objects.filter(product_type=Products.TYPE_ASSET).order_by('product_tag',
                                                                                             'product_title')
                table = ProductAssetsTable(objects)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_STOCK_ALL_ASSETS,
                    'title': Products.TITLE,
                    'name': Products.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'search_form': search_form,
                    'display_search': display_search,
                    'index_url': reverse("products_index_assets"),
                    'select_multiple_url': '#',
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal
def index_inventory_goods(request):
    template_url = 'products/index-inventory-goods.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_INVENTORY_VIEW in auth_permissions.values():
            search_form = ProductInventorySearchIndexForm(request.POST or None)
            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                objects = Products.objects.all()
                objects = objects.filter(product_type=Products.TYPE_GOODS)
                objects = objects.order_by('product_tag', 'product_title')

                results = []
                for item in objects:
                    item.product_quantity_initial = 0

                    item.product_quantity_in = 0
                    inventory_items = Inventory_Items.objects.filter(products_product_id=item.product_id)
                    for inventory_item in inventory_items:
                        item.product_quantity_in = item.product_quantity_in + inventory_item.inventory_item_product_quantity_ordered

                    item.product_quantity_out = 0
                    product_request_items = Product_Request_Items.objects.all()
                    product_request_items = product_request_items.filter(products_product_id=item.product_id,
                                                                         product_request_item_status=Product_Request_Items.STATUS_RECEIVED)
                    for product_request_item in product_request_items:
                        item.product_quantity_out = item.product_quantity_out + product_request_item.product_request_item_product_quantity_ordered

                    item.product_quantity_final = item.product_quantity_available
                    results.append(item)

                table = ProductGoodsInventoryTable(objects)
            else:
                display_search = False
                objects = Products.objects.all()
                objects = objects.filter(product_type=Products.TYPE_GOODS)
                objects = objects.order_by('product_tag', 'product_title')

                results = []
                for item in objects:
                    item.product_quantity_initial = 0

                    item.product_quantity_in = 0
                    inventory_items = Inventory_Items.objects.filter(products_product_id=item.product_id)
                    for inventory_item in inventory_items:
                        item.product_quantity_in = item.product_quantity_in + inventory_item.inventory_item_product_quantity_ordered

                    item.product_quantity_out = 0
                    product_request_items = Product_Request_Items.objects.all()
                    product_request_items = product_request_items.filter(products_product_id=item.product_id,
                                                                         product_request_item_status=Product_Request_Items.STATUS_RECEIVED)
                    for product_request_item in product_request_items:
                        item.product_quantity_out = item.product_quantity_out + product_request_item.product_request_item_product_quantity_ordered

                    item.product_quantity_final = item.product_quantity_available
                    results.append(item)

                table = ProductGoodsInventoryTable(objects)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_INVENTORY_GOODS,
                    'title': Products.TITLE,
                    'name': Products.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'search_form': search_form,
                    'display_search': display_search,
                    'index_url': reverse("products_index_inventory_goods"),
                    'select_multiple_url': '#',
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal
def index_inventory_assets(request):
    template_url = 'products/index-inventory-assets.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_INVENTORY_VIEW in auth_permissions.values():
            search_form = ProductInventorySearchIndexForm(request.POST or None)
            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                objects = Products.objects.all()
                objects = objects.filter(product_type=Products.TYPE_ASSET)
                objects = objects.order_by('product_tag', 'product_title')

                results = []
                for item in objects:
                    item.product_quantity_initial = 0

                    item.product_quantity_in = 0
                    inventory_items = Inventory_Items.objects.filter(products_product_id=item.product_id)
                    for inventory_item in inventory_items:
                        item.product_quantity_in = item.product_quantity_in + inventory_item.inventory_item_product_quantity_ordered

                    item.product_quantity_out = 0
                    product_request_items = Product_Request_Items.objects.all()
                    product_request_items = product_request_items.filter(products_product_id=item.product_id,
                                                                         product_request_item_status=Product_Request_Items.STATUS_RECEIVED)
                    for product_request_item in product_request_items:
                        item.product_quantity_out = item.product_quantity_out + product_request_item.product_request_item_product_quantity_ordered

                    item.product_quantity_final = item.product_quantity_available
                    results.append(item)

                table = ProductAssetsInventoryTable(objects)
            else:
                display_search = False
                objects = Products.objects.all()
                objects = objects.filter(product_type=Products.TYPE_ASSET)
                objects = objects.order_by('product_tag', 'product_title')

                results = []
                for item in objects:
                    item.product_quantity_initial = 0

                    item.product_quantity_in = 0
                    inventory_items = Inventory_Items.objects.filter(products_product_id=item.product_id)
                    for inventory_item in inventory_items:
                        item.product_quantity_in = item.product_quantity_in + inventory_item.inventory_item_product_quantity_ordered

                    item.product_quantity_out = 0
                    product_request_items = Product_Request_Items.objects.all()
                    product_request_items = product_request_items.filter(products_product_id=item.product_id,
                                                                         product_request_item_status=Product_Request_Items.STATUS_RECEIVED)
                    for product_request_item in product_request_items:
                        item.product_quantity_out = item.product_quantity_out + product_request_item.product_request_item_product_quantity_ordered

                    item.product_quantity_final = item.product_quantity_available
                    results.append(item)

                table = ProductAssetsInventoryTable(results)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_INVENTORY_ASSETS,
                    'title': Products.TITLE,
                    'name': Products.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'search_form': search_form,
                    'display_search': display_search,
                    'index_url': reverse("products_index_inventory_assets"),
                    'select_multiple_url': '#',
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')
