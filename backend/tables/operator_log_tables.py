from __future__ import unicode_literals

import itertools

import django_tables2 as tables
from django.urls import reverse
from django.utils.safestring import mark_safe

from app import settings
from app.models import Operator_Logs
from app.utils import Utils


class OperatorLogsTable(tables.Table):
    auth_permissions = {}

    row_number = tables.Column(
        verbose_name='Id',
        attrs={
            'search_filter': '',
            'th_style': 'width:60px;',
        },
        orderable=False,
        empty_values=(),
        accessor='pk',
    )
    operator_log_id = tables.Column(
        verbose_name='Id',
        attrs={
            'search_filter': '',
        }
    )
    operators_operator_username = tables.Column(
        verbose_name='Email Id',
        attrs={
            'search_filter': 'input-text'
        }
    )
    operator_log_message = tables.Column(
        verbose_name='Message',
        attrs={
            'search_filter': 'input-text'
        }
    )
    operator_log_updated_at = tables.DateTimeColumn(
        verbose_name='Updated At',
        attrs={
            'search_filter': 'input-date',
            'th_style': 'width:180px;',
        }
    )
    actions = tables.Column(
        verbose_name='Actions',
        attrs={
            'search_filter': '',
            'th_style': 'width:60px;',
        },
        orderable=False,
        empty_values=(),
    )

    def __init__(self, *args, **kwargs):
        self.counter = itertools.count(1)
        super(OperatorLogsTable, self).__init__(*args, **kwargs)

    def set_auth_permissions(self, auth_permissions):
        self.auth_permissions = auth_permissions

    def render_row_number(self, record):
        value = '<a href=' + str(record.pk) + '>' + '%d' % next(self.counter) + '</a>'
        return value

    def render_actions(self, record):
        action_data = ""
        if settings.ACCESS_PERMISSION_LOG_VIEW in self.auth_permissions.values():
            url = reverse("operator_logs_view", args=[record.pk])
            action_data = action_data + "<a class=\"btn btn-default btn-block\" href=\"" + url + "\">View</a>"
        if settings.ACCESS_PERMISSION_LOG_DELETE in self.auth_permissions.values():
            url = reverse("operator_logs_single_select")
            action_data = action_data + "<a class=\"btn btn-default btn-block\" href=\"#\" onclick=\"javascript: singleSelect(\'" + url + "\', \'delete\', \'" + str(
                record.operator_log_id) + "\');\">Delete</a>"
        return action_data

    @staticmethod
    def render_operator_log_id(record):
        return mark_safe(
            '<a href=' + reverse("operator_logs_view",
                                 args=[record.pk]) + ' style=\'text-decoration:underline; color:#1B82DC;\' >' +
            str(record.operator_log_id) + '</a>')

    @staticmethod
    def render_operators_operator_username(record):
        return mark_safe(
            '<a href=' + reverse("operators_view",
                                 args=[
                                     record.operators_operator_id]) + ' style=\'text-decoration:underline; color:#1B82DC;\' >' +
            str(record.operators_operator_username) + '</a>')

    @staticmethod
    def render_operator_log_updated_at(value):
        return Utils.get_convert_datetime(value, settings.TIME_ZONE,
                                          settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO

    class Meta:
        model = Operator_Logs
        attrs = {
            'id': 'table-' + Operator_Logs.NAME,
            'name': Operator_Logs.NAME,
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_number',
            'operator_log_id',
            'operators_operator_username',
            'operator_log_message',
            'operator_log_updated_at',
            'actions'
        )
        fields = (
            'operator_log_id',
            'operators_operator_username',
            'operator_log_message',
            'operator_log_updated_at'
        )
        template_name = '_include/bootstrap-datatable.html'
