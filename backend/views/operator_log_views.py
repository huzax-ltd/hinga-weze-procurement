from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from app import settings
from app.models import Operators, Operator_Logs
from app.utils import Utils
from backend.tables.operator_log_tables import OperatorLogsTable


# noinspection PyUnusedLocal
def index(request):
    template_url = 'operator_logs/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_LOG_VIEW in auth_permissions.values():
            table = OperatorLogsTable(Operator_Logs.objects.all().order_by('-operator_log_id')[:100],
                                      Operators.get_auth_permissions(operator))
            # [:1000]
            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_OPERATOR_LOGS,
                    'title': Operator_Logs.TITLE,
                    'name': Operator_Logs.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'index_url': reverse("operator_logs_index"),
                    'select_multiple_url': reverse("operator_logs_select_multiple"),
                }
            )
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
            row_id = request.POST['id']
            if action != '' and row_id is not None:
                if action == 'delete':
                    if settings.ACCESS_PERMISSION_LOG_DELETE in auth_permissions.values():
                        try:
                            model = Operator_Logs.objects.get(operator_log_id=row_id)
                            model.delete()
                            messages.success(request, 'Deleted successfully.')
                        except(TypeError, ValueError, OverflowError, Operator_Logs.DoesNotExist):
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

                if action == 'delete':
                    if settings.ACCESS_PERMISSION_LOG_DELETE in auth_permissions.values():
                        for id in ids:
                            try:
                                model = Operator_Logs.objects.get(operator_log_id=id)
                                model.delete()
                            except(TypeError, ValueError, OverflowError, Operator_Logs.DoesNotExist):
                                continue
                        messages.success(request, 'Deleted successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                if action == 'delete-all':
                    if settings.ACCESS_PERMISSION_LOG_DELETE in auth_permissions.values():
                        Operator_Logs.objects.all().delete()
                        messages.success(request, 'Deleted successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                return HttpResponse('success', content_type='text/plain')
            else:
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')
    else:
        return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def view(request, pk):
    template_url = 'operator_logs/view.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_LOG_VIEW in auth_permissions.values():
            try:
                model = Operator_Logs.objects.get(operator_log_id=pk)
                model.operator_log_updated_at = Utils.get_convert_datetime(model.operator_log_updated_at,
                                                                           settings.TIME_ZONE,
                                                                           settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_OPERATOR_LOGS,
                        'title': Operator_Logs.TITLE,
                        'name': Operator_Logs.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'model': model,
                        'index_url': reverse("operator_logs_index"),
                        'select_single_url': reverse("operator_logs_select_single"),
                    }
                )
            except(TypeError, ValueError, OverflowError, Operator_Logs.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')
