from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from app import settings
from app.models import Operators, Products
from app.utils import Utils
from backend.forms.product_forms import ProductExcelImportForm


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
