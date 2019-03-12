from __future__ import unicode_literals

import itertools
from datetime import datetime

import django_tables2 as tables
from django.urls import reverse

from app import settings
from app.models import Backups
from app.utils import Utils


class BackupsTable(tables.Table):
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
    backup_file_name = tables.Column(
        verbose_name='Name',
        attrs={
            'search_filter': '',
        }
    )
    backup_file_size = tables.Column(
        verbose_name='Size',
        attrs={
            'search_filter': '',
        }
    )
    backup_file_created_at = tables.DateTimeColumn(
        verbose_name='Created At',
        attrs={
            'search_filter': 'input-date',
            'th_style': 'width:180px;',
        }
    )
    backup_file_updated_at = tables.DateTimeColumn(
        verbose_name='Updated At',
        attrs={
            'search_filter': '',
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
        super(BackupsTable, self).__init__(*args, **kwargs)

    def set_auth_permissions(self, auth_permissions):
        self.auth_permissions = auth_permissions

    def render_row_number(self, record):
        value = '<a href=' + str(record.pk) + '>' + '%d' % next(self.counter) + '</a>'
        return value

    def render_actions(self, record):
        action_data = ""
        # if settings.ACCESS_PERMISSION_DASHBOARD_VIEW in self.auth_permissions.values():
        #     url = reverse("backup_restore_single_select")
        #     action_data = action_data + "<a class=\"btn btn-default btn-block\" href=\"#\" onclick=\"javascript: singleSelect(\'" + url + "\', \'restore\', \'" + str(
        #         record.backup_file_name) + "\');\">Restore</a>"
        if settings.ACCESS_PERMISSION_SETTINGS_VIEW in self.auth_permissions.values():
            url = reverse("backup_restore_single_select")
            action_data = action_data + "<a class=\"btn btn-default btn-block\" href=\"#\" onclick=\"javascript: singleSelect(\'" + url + "\', \'download\', \'" + str(
                record.backup_file_name) + "\');\">Download</a>"
        if settings.ACCESS_PERMISSION_SETTINGS_VIEW in self.auth_permissions.values():
            url = reverse("backup_restore_single_select")
            action_data = action_data + "<a class=\"btn btn-default btn-block\" href=\"#\" onclick=\"javascript: singleSelect(\'" + url + "\', \'delete\', \'" + str(
                record.backup_file_name) + "\');\">Delete</a>"
        return action_data

    @staticmethod
    def render_backup_file_created_at(value):
        ts = datetime.fromtimestamp(value)
        return Utils.get_convert_datetime(ts, settings.TIME_ZONE,
                                          settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO

    @staticmethod
    def render_backup_file_updated_at(value):
        ts = datetime.fromtimestamp(value)
        return Utils.pretty_date(ts)

    class Meta:
        model = Backups
        attrs = {
            'id': 'table-' + Backups.NAME,
            'name': Backups.NAME,
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_number',
            'backup_file_name',
            'backup_file_size',
            'backup_file_created_at',
            'backup_file_updated_at',
            'actions'
        )
        fields = (
            'backup_file_name',
            'backup_file_size',
            'backup_file_created_at',
            'backup_file_updated_at',
        )
        template_name = '_include/bootstrap-datatable.html'
