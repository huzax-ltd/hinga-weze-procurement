from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from app import settings
from app.models import Operators, Mel_Indicators, Mel_Activities
from backend.forms.mel_activity_forms import MelActivitySearchIndexForm
from backend.tables.mel_activity_tables import MelActivitiesTable


# noinspection PyUnusedLocal
def index(request, id, result_id):
    template_url = 'mel-activities/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_ACTIVITIES_VIEW in auth_permissions.values():
            search_form = MelActivitySearchIndexForm(request.POST or None)
            try:
                mel_indicator = Mel_Indicators.objects.get(mel_indicator_id=id)
                search_form.fields['mel_indicator_id'].initial = id
                search_form.fields['mel_result_id'].initial = result_id
            except Mel_Indicators.DoesNotExist:
                mel_indicator = Mel_Indicators()
                mel_indicator.mel_indicator_id = 0
                mel_indicator.mel_indicator_code = 0
                result_id = 0
                search_form.fields['mel_indicator_id'].initial = ''
                search_form.fields['mel_result_id'].initial = ''

            objects = None

            objects = Mel_Activities.objects.all()

            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                table = MelActivitiesTable(objects)
            else:
                display_search = False
                table = MelActivitiesTable(objects)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_MEL_DEPARTMENT_ACTIVITIES,
                    'title': Mel_Activities.TITLE,
                    'name': Mel_Activities.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'objects': objects,
                    'search_form': search_form,
                    'display_search': display_search,
                    'model': mel_indicator,
                    'result_id': result_id,
                    'index_url': reverse("mel_activities_index",
                                         kwargs={'id': mel_indicator.mel_indicator_code, 'result_id': result_id}),
                    'select_multiple_url': reverse("mel_activities_index",
                                                   kwargs={'id': mel_indicator.mel_indicator_code,
                                                           'result_id': result_id}),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')
