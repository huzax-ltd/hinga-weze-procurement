from __future__ import unicode_literals

import itertools

import django_tables2 as tables

from app.models import Mel_Results


class MelResultsTable(tables.Table):
    auth_permissions = {}

    row_check = tables.Column(
        verbose_name='',
        attrs={
            'search_filter': '',
            'th_style': 'width:30px;',
        },
        orderable=False,
        empty_values=(),
    )
    row_number = tables.Column(
        verbose_name='No.',
        attrs={
            'search_filter': '',
            'th_style': 'width:30px;',
        },
        orderable=False,
        empty_values=(),
    )
    row_id = tables.Column(
        verbose_name='Id',
        attrs={
            'search_filter': '',
            'th_style': 'width:0px;',
        },
        orderable=False,
        empty_values=(),
        visible=True,
    )
    mel_result_details = tables.Column(
        verbose_name='Details',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:80px;',
        }
    )
    mel_indicator_ids = tables.Column(
        verbose_name='Indicators',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:500px;',
        }
    )

    # actions = tables.Column(
    #     verbose_name='',
    #     attrs={
    #         'search_filter': '',
    #         'th_style': 'width:60px;',
    #     },
    #     orderable=False,
    #     empty_values=(),
    # )

    def __init__(self, *args, **kwargs):
        self.counter = itertools.count(1)
        super(MelResultsTable, self).__init__(*args, **kwargs)

    def set_auth_permissions(self, auth_permissions):
        self.auth_permissions = auth_permissions

    @staticmethod
    def render_row_check(record):
        return ''

    def render_row_number(self, record):
        return next(self.counter)

    def render_row_id(self, record):
        return str(record.pk)

    # def render_actions(self, record):
    #     action_data = ""
    #     if settings.ACCESS_PERMISSION_ORDER_VIEW in self.auth_permissions.values():
    #         url = reverse("operators_view", args=[record.pk])
    #         action_data = action_data + "<a class=\"dropdown-item\" href=\"" + url + "\">View</a>"
    #     if settings.ACCESS_PERMISSION_ORDER_DELETE in self.auth_permissions.values():
    #         url = reverse("operators_select_single")
    #         action_data = action_data + "<a class=\"dropdown-item\" href=\"#\" onclick=\"javascript: singleSelect(\'" + url + "\', \'delete\', \'" + str(
    #             record.order_id) + "\');\">Delete</a>"
    #     return action_data

    class Meta:
        model = Mel_Results
        attrs = {
            'id': 'table-' + Mel_Results.NAME,
            'name': Mel_Results.NAME,
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_check',
            'row_number',
            'row_id',
            'mel_result_details',
            'mel_indicator_ids',
            # 'actions'
        )
        fields = (
            'mel_result_details',
            'mel_indicator_ids',
        )
        template_name = '_include/bootstrap-datatable-no-action.html'
