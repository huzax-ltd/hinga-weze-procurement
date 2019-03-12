from __future__ import unicode_literals

import itertools

import django_tables2 as tables
from django.urls import reverse
from django.utils.safestring import mark_safe

from app import settings
from app.models import Operators


class OperatorsTable(tables.Table):
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
    operator_username = tables.Column(
        verbose_name='Email Id',
        attrs={
            'search_filter': 'input-text',
        }
    )
    operator_name = tables.Column(
        verbose_name='Name',
        attrs={
            'search_filter': 'input-text',
        }
    )
    operator_type = tables.Column(
        verbose_name='Type',
        attrs={
            'search_filter': 'input-select',
            'search_data': Operators.ARRAY_OPERATOR_TYPES,
            'th_style': 'width:100px; text-align:center;',
            'td_style': 'text-align:center;',
        }
    )
    operator_status = tables.Column(
        verbose_name='Status',
        attrs={
            'search_filter': 'input-select',
            'search_data': Operators.ARRAY_OPERATOR_STATUSES,
            'search_type': 'status',
            'th_style': 'width:100px;',
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
        super(OperatorsTable, self).__init__(*args, **kwargs)

    def set_auth_permissions(self, auth_permissions):
        self.auth_permissions = auth_permissions

    def render_row_number(self, record):
        value = '<a href=' + str(record.pk) + '>' + '%d' % next(self.counter) + '</a>'
        return value

    def render_actions(self, record):
        action_data = ""
        if settings.ACCESS_PERMISSION_OPERATOR_VIEW in self.auth_permissions.values():
            url = reverse("operators_view", args=[record.pk])
            action_data = action_data + "<a class=\"btn btn-default btn-block\" href=\"" + url + "\">View</a>"
        if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in self.auth_permissions.values():
            url = reverse("operators_update", args=[record.pk])
            action_data = action_data + "<a class=\"btn btn-default btn-block\" href=\"" + url + "\">Update</a>"
        if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in self.auth_permissions.values() and record.operator_status == Operators.STATUS_UNVERIFIED:
            url = reverse("operators_single_select")
            action_data = action_data + "<a class=\"btn btn-default btn-block\" href=\"#\" onclick=\"javascript: singleSelect(\'" + url + "\', \'verify\', \'" + str(
                record.operator_id) + "\');\">Verify</a>"
        if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in self.auth_permissions.values() and record.operator_status == Operators.STATUS_UNAPPROVED:
            url = reverse("operators_single_select")
            action_data = action_data + "<a class=\"btn btn-default btn-block\" href=\"#\" onclick=\"javascript: singleSelect(\'" + url + "\', \'approve\', \'" + str(
                record.operator_id) + "\');\">Approve</a>"
        if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in self.auth_permissions.values() and (
                record.operator_status == Operators.STATUS_ACTIVE or record.operator_status == Operators.STATUS_INACTIVE):
            url = reverse("operators_single_select")
            action_data = action_data + "<a class=\"btn btn-default btn-block\" href=\"#\" onclick=\"javascript: singleSelect(\'" + url + "\', \'block\', \'" + str(
                record.operator_id) + "\');\">Block</a>"
        if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in self.auth_permissions.values() and record.operator_status == Operators.STATUS_BLOCKED:
            url = reverse("operators_single_select")
            action_data = action_data + "<a class=\"btn btn-default btn-block\" href=\"#\" onclick=\"javascript: singleSelect(\'" + url + "\', \'unblock\', \'" + str(
                record.operator_id) + "\');\">Unblock</a>"
        if settings.ACCESS_PERMISSION_OPERATOR_DELETE in self.auth_permissions.values():
            url = reverse("operators_single_select")
            action_data = action_data + "<a class=\"btn btn-default btn-block\" href=\"#\" onclick=\"javascript: singleSelect(\'" + url + "\', \'delete\', \'" + str(
                record.operator_id) + "\');\">Delete</a>"
        return action_data

    @staticmethod
    def render_operator_username(record):
        return mark_safe(
            '<a href=' + reverse("operators_view",
                                 args=[record.pk]) + ' style=\'text-decoration:underline; color:#1B82DC;\' >' +
            str(record.operator_username) + '</a>')

    @staticmethod
    def render_operator_status(record):
        if record.operator_status == Operators.STATUS_ACTIVE:
            value = Operators.HTML_TAG_STATUS_ACTIVE_COLOR
        elif record.operator_status == Operators.STATUS_BLOCKED:
            value = Operators.HTML_TAG_STATUS_BLOCKED_COLOR
        elif record.operator_status == Operators.STATUS_UNVERIFIED:
            value = Operators.HTML_TAG_STATUS_UNVERIFIED_COLOR
        elif record.operator_status == Operators.STATUS_UNAPPROVED:
            value = Operators.HTML_TAG_STATUS_UNAPPROVED_COLOR
        else:
            value = Operators.HTML_TAG_STATUS_INACTIVE_COLOR
        return value

    class Meta:
        model = Operators
        attrs = {
            'id': 'table-' + Operators.NAME,
            'name': Operators.NAME,
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_number',
            'operator_username',
            'operator_name',
            'operator_type',
            'operator_status',
            'actions'
        )
        fields = (
            'operator_username',
            'operator_name',
            'operator_type',
            'operator_status',
        )
        template_name = '_include/bootstrap-datatable.html'
