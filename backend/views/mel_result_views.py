from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from app import settings
from app.models import Operators, Mel_Indicators, Mel_Results
from backend.forms.mel_result_forms import MelResultSearchIndexForm
from backend.tables.mel_result_tables import MelResultsTable


# noinspection PyUnusedLocal
def index(request, id):
    template_url = 'mel-results/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_INDICATORS_VIEW in auth_permissions.values():
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
                item.no_of_sub_results = 0
                item.no_of_indicators = 0
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
                    'indicators': results,
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
