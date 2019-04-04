from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from app import settings
from app.models import Operators, Mel_Indicators
from backend.forms.mel_indicator_forms import MelIndicatorSearchIndexForm
from backend.tables.mel_indicator_tables import MelIndicatorsTable


# noinspection PyUnusedLocal
def index(request):
    template_url = 'mel-indicators/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_INDICATORS_VIEW in auth_permissions.values():
            search_form = MelIndicatorSearchIndexForm(request.POST or None)
            objects = None

            objects = Mel_Indicators.objects.all()

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
                    'search_form': search_form,
                    'display_search': display_search,
                    'index_url': reverse("mel_indicators_index"),
                    'select_multiple_url': reverse("mel_indicators_index"),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')
