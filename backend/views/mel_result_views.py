from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from app import settings
from app.models import Operators, Mel_Indicators, Mel_Results
from app.utils import Utils
from backend.forms.mel_result_forms import MelResultSearchIndexForm, MelResultCreateForm, MelResultUpdateForm
from backend.tables.mel_result_tables import MelResultsTable


# noinspection PyUnusedLocal
def api_dropdown_results(request, code):
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        try:
            mel_indicator = Mel_Indicators.objects.get(mel_indicator_id=code)
        except Mel_Indicators.DoesNotExist:
            mel_indicator = Mel_Indicators()
            mel_indicator.mel_indicator_id = 0
            mel_indicator.mel_indicator_code = 0

        results = ""
        results += "<option value=''>--select--</option>"
        mel_results = Mel_Results.objects.all()
        mel_results = mel_results.filter(mel_indicators_mel_indicator_code=mel_indicator.mel_indicator_code)
        for item in mel_results:
            results += "<option value='" + \
                       str(item.mel_result_id) + "'>" + str(item.mel_result_details) + "</option>"

        return HttpResponse(results, content_type="text/plain")


# noinspection PyUnusedLocal
def index(request, id):
    template_url = 'mel-results/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_RESULTS_VIEW in auth_permissions.values():
            search_form = MelResultSearchIndexForm(request.POST or None)
            try:
                mel_indicator = Mel_Indicators.objects.get(mel_indicator_id=id)
                search_form.fields['mel_indicator_id'].initial = id
            except Mel_Indicators.DoesNotExist:
                mel_indicator = Mel_Indicators()
                mel_indicator.mel_indicator_id = 0
                mel_indicator.mel_indicator_code = 0
                search_form.fields['mel_indicator_id'].initial = ''

            objects = None

            objects = Mel_Results.objects.all()
            objects = objects.filter(mel_indicators_mel_indicator_code=mel_indicator.mel_indicator_code)

            results = []
            for item in objects:
                li_mel_indicator_ids = item.mel_indicator_ids
                li_mel_indicator_ids = li_mel_indicator_ids.replace('[', '')
                li_mel_indicator_ids = li_mel_indicator_ids.replace(']', '')
                li_mel_indicator_ids = li_mel_indicator_ids.replace('\'', '')
                li_mel_indicator_ids = li_mel_indicator_ids.replace(',', '')
                li_mel_indicator_ids = li_mel_indicator_ids.split()
                item.indicators = '<ul class="li_mel_indicators">'
                for li_mel_indicator_id in li_mel_indicator_ids:
                    try:
                        li_mel_indicator = Mel_Indicators.objects.get(mel_indicator_id=li_mel_indicator_id)
                        item.indicators = item.indicators + '<li>' + str(
                            li_mel_indicator.mel_indicator_number) + '. ' + li_mel_indicator.mel_indicator_details + '</li>'
                    except Mel_Indicators.DoesNotExist:
                        continue
                item.indicators = item.indicators + '</ul>'

                item.sub_results = '<ul class="li_mel_indicators">'
                counter = 1
                item.sub_results = item.sub_results + '</ul>'

                results.append(item)

            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                table = MelResultsTable(results)
            else:
                display_search = False
                table = MelResultsTable(results)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_MEL_DEPARTMENT_RESULTS,
                    'title': Mel_Results.TITLE,
                    'name': Mel_Results.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'results': results,
                    'search_form': search_form,
                    'display_search': display_search,
                    'model': mel_indicator,
                    'index_url': reverse("mel_results_index", kwargs={'id': mel_indicator.mel_indicator_code}),
                    'select_multiple_url': reverse("mel_results_index",
                                                   kwargs={'id': mel_indicator.mel_indicator_code}),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def create(request, id):
    template_url = 'mel-results/create.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_RESULTS_CREATE in auth_permissions.values():
            try:
                mel_indicator = Mel_Indicators.objects.get(mel_indicator_id=id)

                if request.method == 'POST':
                    form = MelResultCreateForm(request.POST)
                    # noinspection PyArgumentList
                    if form.is_valid():
                        model = Mel_Results()
                        model.mel_indicators_mel_indicator_code = mel_indicator.mel_indicator_code
                        model.mel_result_details = form.cleaned_data['mel_result_details']
                        model.mel_indicator_ids = ''

                        model.mel_result_created_at = Utils.get_current_datetime_utc()
                        model.mel_result_created_id = operator.operator_id
                        model.mel_result_created_by = operator.operator_name
                        model.mel_result_created_department = operator.operator_department
                        model.mel_result_created_role = operator.operator_role

                        model.mel_result_updated_at = Utils.get_current_datetime_utc()
                        model.mel_result_updated_id = operator.operator_id
                        model.mel_result_updated_by = operator.operator_name
                        model.mel_result_updated_department = operator.operator_department
                        model.mel_result_updated_role = operator.operator_role

                        # noinspection PyCallByClass,PyTypeChecker
                        model.save('Created')

                        messages.success(request, 'Added successfully.')
                        return redirect(reverse("mel_results_index", kwargs={'id': mel_indicator.mel_indicator_id}))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("mel_results_index", kwargs={'id': mel_indicator.mel_indicator_id}))

                else:
                    form = MelResultCreateForm(
                        initial={
                            'mel_indicator_id': mel_indicator.mel_indicator_id,
                        },
                    )
                    INDICATORS = ()
                    indicators = Mel_Indicators.objects.all()
                    indicators = indicators.filter(mel_indicator_code=mel_indicator.mel_indicator_code).order_by(
                        'mel_indicator_number')
                    for indicator in indicators:
                        INDICATORS = INDICATORS + ((indicator.mel_indicator_id,
                                                    str(
                                                        indicator.mel_indicator_number) + '. ' + indicator.mel_indicator_details),)
                    form.fields['mel_indicator_ids'].choices = INDICATORS

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_MEL_DEPARTMENT_RESULTS,
                        'title': Mel_Results.TITLE,
                        'name': Mel_Results.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'index_url': reverse("mel_results_index", kwargs={'id': mel_indicator.mel_indicator_id}),
                    }
                )

            except Mel_Indicators.DoesNotExist:
                return HttpResponseNotFound('Not Found', content_type='text/plain')

        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update(request, pk):
    template_url = 'mel-results/update.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_RESULTS_UPDATE in auth_permissions.values():
            try:
                model = Mel_Results.objects.get(mel_result_id=pk)
                mel_indicator = Mel_Indicators.objects.get(mel_indicator_code=model.mel_indicators_mel_indicator_code,
                                                           mel_indicator_number=1)

                if request.method == 'POST':
                    form = MelResultUpdateForm(request.POST)
                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.mel_result_details = form.cleaned_data['mel_result_details']
                        print(form.cleaned_data['mel_indicator_ids'])
                        model.mel_indicator_ids = form.cleaned_data['mel_indicator_ids']

                        model.mel_result_updated_at = Utils.get_current_datetime_utc()
                        model.mel_result_updated_id = operator.operator_id
                        model.mel_result_updated_by = operator.operator_name
                        model.mel_result_updated_department = operator.operator_department
                        model.mel_result_updated_role = operator.operator_role

                        # noinspection PyCallByClass,PyTypeChecker
                        model.save()

                        messages.success(request, 'Added successfully.')
                        return redirect(reverse("mel_results_index", kwargs={'id': mel_indicator.mel_indicator_id}))
                    else:
                        error_string = ' '.join([' '.join(x for x in l) for l in list(form.errors.values())])
                        messages.error(request, '' + error_string)
                        return redirect(reverse("mel_results_index", kwargs={'id': mel_indicator.mel_indicator_id}))

                else:
                    form = MelResultUpdateForm(
                        initial={
                            'mel_indicator_id': mel_indicator.mel_indicator_id,
                            'mel_result_details': model.mel_result_details,
                            'mel_indicator_ids': [item for item in ','.join(model.mel_indicator_ids)],
                        }
                    )
                    INDICATORS = ()
                    indicators = Mel_Indicators.objects.all()
                    indicators = indicators.filter(mel_indicator_code=mel_indicator.mel_indicator_code).order_by(
                        'mel_indicator_number')
                    for indicator in indicators:
                        INDICATORS = INDICATORS + ((indicator.mel_indicator_id,
                                                    str(
                                                        indicator.mel_indicator_number) + '. ' + indicator.mel_indicator_details),)
                    form.fields['mel_indicator_ids'].choices = INDICATORS

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_MEL_DEPARTMENT_RESULTS,
                        'title': Mel_Results.TITLE,
                        'name': Mel_Results.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'model': model,
                        'index_url': reverse("mel_results_index", kwargs={'id': mel_indicator.mel_indicator_id}),
                        'view_url': reverse("mel_results_view", kwargs={'pk': model.mel_result_id}),
                    }
                )

            except (Mel_Results.DoesNotExist, Mel_Indicators.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')

        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def view(request, pk):
    template_url = 'mel-results/view.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_RESULTS_VIEW in auth_permissions.values():
            try:
                model = Mel_Results.objects.get(mel_result_id=pk)
                mel_indicator = Mel_Indicators.objects.get(mel_indicator_code=model.mel_indicators_mel_indicator_code,
                                                           mel_indicator_number=1)

                li_mel_indicator_ids = model.mel_indicator_ids
                li_mel_indicator_ids = li_mel_indicator_ids.replace('[', '')
                li_mel_indicator_ids = li_mel_indicator_ids.replace(']', '')
                li_mel_indicator_ids = li_mel_indicator_ids.replace('\'', '')
                li_mel_indicator_ids = li_mel_indicator_ids.replace(',', '')
                li_mel_indicator_ids = li_mel_indicator_ids.split()
                model.indicators = '<ul class="li_mel_indicators">'
                for li_mel_indicator_id in li_mel_indicator_ids:
                    try:
                        li_mel_indicator = Mel_Indicators.objects.get(mel_indicator_id=li_mel_indicator_id)
                        model.indicators = model.indicators + '<li>' + str(
                            li_mel_indicator.mel_indicator_number) + '. ' + li_mel_indicator.mel_indicator_details + '</li>'
                    except Mel_Indicators.DoesNotExist:
                        continue
                model.indicators = model.indicators + '</ul>'

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_MEL_DEPARTMENT_RESULTS,
                        'title': Mel_Results.TITLE,
                        'name': Mel_Results.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'model': model,
                        'mel_indicator': mel_indicator,
                        'index_url': reverse("mel_results_index", kwargs={'id': mel_indicator.mel_indicator_id}),
                    }
                )

            except (Mel_Results.DoesNotExist, Mel_Indicators.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')

        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')
