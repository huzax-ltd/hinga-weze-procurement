from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from app import settings
from app.models import Operators, Notifications
from backend.forms.notification_forms import NotificationSearchIndexForm
from backend.tables.notification_tables import NotificationsTable


# noinspection PyUnusedLocal
def json_notifications(request):
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        objects = Notifications.objects.filter(notification_to_id=operator.operator_id)
        return HttpResponse(serializers.serialize("json", objects),
                            content_type="application/json")


# noinspection PyUnusedLocal
def index(request):
    template_url = 'notifications/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        search_form = NotificationSearchIndexForm(request.POST or None)
        if request.method == 'POST' and search_form.is_valid():
            display_search = True
            objects = Notifications.objects.filter(notification_to_id=operator.operator_id)
            objects = Operators.objects.order_by('operator_name').all()

            table = NotificationsTable(objects)
        else:
            display_search = False
            objects = Notifications.objects.filter(notification_to_id=operator.operator_id)
            table = NotificationsTable(objects)

        table.set_auth_permissions(auth_permissions)
        return render(
            request, template_url,
            {
                'section': settings.BACKEND_SECTION_NOTIFICATIONS,
                'title': Notifications.TITLE,
                'name': Notifications.NAME,
                'operator': operator,
                'auth_permissions': auth_permissions,
                'table': table,
                'search_form': search_form,
                'display_search': display_search,
                'index_url': reverse("notifications_index"),
            }
        )
