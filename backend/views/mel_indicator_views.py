from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from app import settings
from app.models import Mel_Indicators
from app.models import Operators
from app.utils import Utils
from backend.forms.mel_indicator_forms import MelIndicatorSearchIndexForm, MelIndicatorCreateForm, \
    MelIndicatorUpdateForm, MelIndicatorItemUpdateForm
from backend.tables.mel_indicator_tables import MelIndicatorsTable


# noinspection PyUnusedLocal
def index(request, id):
    template_url = 'mel-indicators/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_INDICATORS_VIEW in auth_permissions.values():
            search_form = MelIndicatorSearchIndexForm(request.POST or None)
            try:
                mel_indicator = Mel_Indicators.objects.get(mel_indicator_id=id)
                search_form.fields['mel_indicator_id'].initial = id
            except Mel_Indicators.DoesNotExist:
                mel_indicator = Mel_Indicators()
                mel_indicator.mel_indicator_id = 0
                mel_indicator.mel_indicator_code = 0
                search_form.fields['mel_indicator_id'].initial = ''

            objects = None

            objects = Mel_Indicators.objects.all()
            objects = objects.filter(mel_indicator_code=mel_indicator.mel_indicator_code).order_by(
                'mel_indicator_number')

            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                table = MelIndicatorsTable(objects)
            else:
                display_search = False
                table = MelIndicatorsTable(objects)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_MEL_DEPARTMENT_INDICATORS,
                    'title': Mel_Indicators.TITLE,
                    'name': Mel_Indicators.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'indicators': objects,
                    'search_form': search_form,
                    'display_search': display_search,
                    'model': mel_indicator,
                    'index_url': reverse("mel_indicators_index", kwargs={'id': mel_indicator.mel_indicator_code}),
                    'select_multiple_url': reverse("mel_indicators_index",
                                                   kwargs={'id': mel_indicator.mel_indicator_code}),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def create(request):
    template_url = 'mel-indicators/create.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_INDICATORS_CREATE in auth_permissions.values():
            if request.method == 'POST':
                form = MelIndicatorCreateForm(request.POST)
                # noinspection PyArgumentList
                if form.is_valid():
                    model = Mel_Indicators()
                    mel_indicator_code = model.mel_indicator_code = Mel_Indicators.generate_random_number(
                        'mel_indicator_code', 8)
                    model.mel_indicator_number = 1
                    mel_indicator_name = model.mel_indicator_name = form.cleaned_data['mel_indicator_name']
                    model.mel_indicator_details = ''

                    model.mel_indicator_created_at = Utils.get_current_datetime_utc()
                    model.mel_indicator_created_id = operator.operator_id
                    model.mel_indicator_created_by = operator.operator_name
                    model.mel_indicator_created_department = operator.operator_department
                    model.mel_indicator_created_role = operator.operator_role

                    model.mel_indicator_updated_at = Utils.get_current_datetime_utc()
                    model.mel_indicator_updated_id = operator.operator_id
                    model.mel_indicator_updated_by = operator.operator_name
                    model.mel_indicator_updated_department = operator.operator_department
                    model.mel_indicator_updated_role = operator.operator_role

                    # noinspection PyCallByClass,PyTypeChecker
                    model.save('Created')

                    for i in range(2, 24):
                        item = Mel_Indicators()
                        item.mel_indicator_code = mel_indicator_code
                        item.mel_indicator_number = i
                        item.mel_indicator_name = mel_indicator_name
                        item.mel_indicator_details = ''

                        item.mel_indicator_created_at = Utils.get_current_datetime_utc()
                        item.mel_indicator_created_id = operator.operator_id
                        item.mel_indicator_created_by = operator.operator_name
                        item.mel_indicator_created_department = operator.operator_department
                        item.mel_indicator_created_role = operator.operator_role

                        item.mel_indicator_updated_at = Utils.get_current_datetime_utc()
                        item.mel_indicator_updated_id = operator.operator_id
                        item.mel_indicator_updated_by = operator.operator_name
                        item.mel_indicator_updated_department = operator.operator_department
                        item.mel_indicator_updated_role = operator.operator_role

                        # noinspection PyCallByClass,PyTypeChecker
                        item.save('Created')

                    messages.success(request, 'Added successfully.')
                    return redirect(reverse("mel_indicators_index", kwargs={'id': model.mel_indicator_id}))
                else:
                    error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                    messages.error(request, '' + error_string)
                    return redirect(reverse("mel_indicators_index", kwargs={'id': 0}))

            else:
                form = MelIndicatorCreateForm()

            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_MEL_DEPARTMENT_INDICATORS,
                    'title': Mel_Indicators.TITLE,
                    'name': Mel_Indicators.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'form': form,
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update(request, pk):
    template_url = 'mel-indicators/update.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_INDICATORS_UPDATE in auth_permissions.values():
            try:
                model = Mel_Indicators.objects.get(mel_indicator_id=pk)
                if request.method == 'POST':

                    form = MelIndicatorUpdateForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        mel_indicator_code = model.mel_indicator_code
                        mel_indicator_name = model.mel_indicator_name = form.cleaned_data['mel_indicator_name']

                        model.mel_indicator_updated_at = Utils.get_current_datetime_utc()
                        model.mel_indicator_updated_id = operator.operator_id
                        model.mel_indicator_updated_by = operator.operator_name
                        model.mel_indicator_updated_department = operator.operator_department
                        model.mel_indicator_updated_role = operator.operator_role

                        model.save()

                        for i in range(2, 24):
                            try:
                                item = Mel_Indicators.objects.get(mel_indicator_code=mel_indicator_code,
                                                                  mel_indicator_number=i)
                                item.mel_indicator_name = mel_indicator_name

                                item.mel_indicator_updated_at = Utils.get_current_datetime_utc()
                                item.mel_indicator_updated_id = operator.operator_id
                                item.mel_indicator_updated_by = operator.operator_name
                                item.mel_indicator_updated_department = operator.operator_department
                                item.mel_indicator_updated_role = operator.operator_role
                                # noinspection PyCallByClass,PyTypeChecker
                                item.save()
                            except Mel_Indicators.DoesNotExist:
                                continue

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("mel_indicators_index", kwargs={'id': model.mel_indicator_id}))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("mel_indicators_index", kwargs={'id': 0}))
                else:
                    form = MelIndicatorUpdateForm(
                        initial={
                            'mel_indicator_name': model.mel_indicator_name,
                        }
                    )

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_MEL_DEPARTMENT_INDICATORS,
                        'title': Mel_Indicators.TITLE,
                        'name': Mel_Indicators.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'model': model,
                    }
                )
            except(TypeError, ValueError, OverflowError, Mel_Indicators.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update_item(request, id, pk):
    template_url = 'mel-indicators/update-item.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_INDICATORS_UPDATE in auth_permissions.values():
            try:
                model = Mel_Indicators.objects.get(mel_indicator_id=pk)
                if request.method == 'POST':

                    form = MelIndicatorItemUpdateForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.mel_indicator_details = form.cleaned_data['mel_indicator_details']

                        model.mel_indicator_updated_at = Utils.get_current_datetime_utc()
                        model.mel_indicator_updated_id = operator.operator_id
                        model.mel_indicator_updated_by = operator.operator_name
                        model.mel_indicator_updated_department = operator.operator_department
                        model.mel_indicator_updated_role = operator.operator_role

                        model.save()

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("mel_indicators_index", kwargs={'id': id}))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("mel_indicators_index", kwargs={'id': id}))
                else:
                    form = MelIndicatorItemUpdateForm(
                        initial={
                            'mel_indicator_id': model.mel_indicator_id,
                            'mel_indicator_number': model.mel_indicator_number,
                            'mel_indicator_details': model.mel_indicator_details,
                        }
                    )

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_MEL_DEPARTMENT_INDICATORS,
                        'title': Mel_Indicators.TITLE,
                        'name': Mel_Indicators.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'model': model,
                    }
                )
            except(TypeError, ValueError, OverflowError, Mel_Indicators.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')
