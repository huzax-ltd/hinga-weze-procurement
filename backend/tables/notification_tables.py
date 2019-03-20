from __future__ import unicode_literals

import itertools

import django_tables2 as tables
from django.utils.safestring import mark_safe

from app.models import Operators, Notifications, Utils


class NotificationsTable(tables.Table):
    auth_permissions = {}

    row_number = tables.Column(
        verbose_name='No.',
        attrs={
            'search_filter': '',
            'th_style': 'width:30px;',
        },
        orderable=False,
        empty_values=(),
    )
    notification_message = tables.Column(
        verbose_name='Message',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:500px;',
        }
    )
    notification_from_id = tables.Column(
        verbose_name='From',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:120px;',
        }
    )
    notification_url = tables.Column(
        verbose_name='View',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        },
        orderable=False,
        empty_values=(),
    )
    notification_created_at = tables.Column(
        verbose_name='Time',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    notification_status = tables.Column(
        verbose_name='Status',
        attrs={
            'search_filter': 'input-select',
            'search_data': Notifications.ARRAY_STATUSES,
            'search_type': 'status',
            'th_style': 'width:100px;',
        }
    )

    def __init__(self, *args, **kwargs):
        self.counter = itertools.count(1)
        super(NotificationsTable, self).__init__(*args, **kwargs)

    def set_auth_permissions(self, auth_permissions):
        self.auth_permissions = auth_permissions

    @staticmethod
    def render_row_check(record):
        return ''

    def render_row_number(self, record):
        return next(self.counter)

    @staticmethod
    def render_actions(record):
        action_data = ""
        return action_data

    @staticmethod
    def render_notification_message(record):
        return mark_safe(
            '<p>' + str(record.notification_message) + '</p>')

    @staticmethod
    def render_notification_from_id(record):
        operator = Operators.objects.get(operator_id=record.notification_from_id)
        if operator is None:
            return '-'
        else:
            return mark_safe(
                '<a href=\'/backend/operators/view/profile/' + str(
                    record.notification_from_id) + '\' style=\'text-decoration:underline; color:#1B82DC;\' >' + str(
                    operator.operator_name) + '</a></p>')

    @staticmethod
    def render_notification_url(record):
        return mark_safe(
            '<a href=\'' + str(
                record.notification_url) + '\' style=\'text-decoration:underline; color:#1B82DC;\' >More Details</a></p>')

    @staticmethod
    def render_notification_created_at(record):
        return Utils.timesince(record.notification_created_at)

    @staticmethod
    def render_notification_status(record):
        if record.notification_status == Notifications.STATUS_UNREAD:
            value = Notifications.HTML_TAG_STATUS_UNREAD_COLOR
        elif record.notification_status == Notifications.STATUS_READ:
            value = Notifications.HTML_TAG_STATUS_READ_COLOR
        elif record.notification_status == Notifications.STATUS_FIXED:
            value = Notifications.HTML_TAG_STATUS_FIXED_COLOR
        else:
            value = Operators.HTML_TAG_STATUS_INACTIVE_COLOR
        return value

    class Meta:
        model = Notifications
        attrs = {
            'id': 'table-' + Notifications.NAME,
            'name': Notifications.NAME,
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_number',
            'notification_message',
            'notification_from_id',
            'notification_url',
            'notification_created_at',
            'notification_status',
        )
        fields = (
            'notification_message',
            'notification_from_id',
            'notification_url',
            'notification_created_at',
            'notification_status',
        )
        template_name = '_include/bootstrap-datatable-no-checkbox-action.html'
