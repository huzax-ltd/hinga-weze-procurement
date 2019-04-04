from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from app import settings
from app.models import Operators, Mel_Results
from backend.forms.mel_result_forms import MelResultSearchIndexForm
from backend.tables.mel_result_tables import MelResultsTable


# noinspection PyUnusedLocal
def index(request):
    template_url = 'mel-results/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_MEL_RESULTS_VIEW in auth_permissions.values():
            search_form = MelResultSearchIndexForm(request.POST or None)
            objects = None

            objects = Mel_Results.objects.all()

            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                table = MelResultsTable(objects)
            else:
                display_search = False
                table = MelResultsTable(objects)

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
                    'search_form': search_form,
                    'display_search': display_search,
                    'index_url': reverse("mel_results_index"),
                    'select_multiple_url': reverse("mel_results_index"),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')
