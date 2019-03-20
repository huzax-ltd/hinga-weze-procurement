from __future__ import unicode_literals

import itertools

import django_tables2 as tables
from django.urls import reverse
from django.utils.safestring import mark_safe

from app import settings
from app.models import Orders


class OrdersTable(tables.Table):
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
    order_requester_name = tables.Column(
        verbose_name='Requester Name',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:100px;',
        }
    )
    order_project_name = tables.Column(
        verbose_name='Project Name',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:500px;',
        }
    )
    order_requisition_number = tables.Column(
        verbose_name='Requester Number',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:500px;',
        }
    )
    order_award_number = tables.Column(
        verbose_name='Award Number',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:500px;',
        }
    )
    order_project_code = tables.Column(
        verbose_name='Project Code',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:500px;',
        }
    )
    order_status = tables.Column(
        verbose_name='Status',
        attrs={
            'search_filter': 'input-select',
            'search_data': Orders.ARRAY_ORDER_STATUSES,
            'search_type': 'status',
            'th_style': 'width:100px;',
        }
    )
    actions = tables.Column(
        verbose_name='',
        attrs={
            'search_filter': '',
            'th_style': 'width:60px;',
        },
        orderable=False,
        empty_values=(),
    )

    def __init__(self, *args, **kwargs):
        self.counter = itertools.count(1)
        super(OrdersTable, self).__init__(*args, **kwargs)

    def set_auth_permissions(self, auth_permissions):
        self.auth_permissions = auth_permissions

    @staticmethod
    def render_row_check(record):
        return ''

    def render_row_number(self, record):
        return next(self.counter)

    def render_row_id(self, record):
        return str(record.pk)

    @staticmethod
    def render_order_code(record):
        return mark_safe(
            '<a href=' + reverse("orders_view",
                                 args=[record.pk]) + ' style=\'text-decoration:underline; color:#1B82DC;\' >' +
            str(record.order_code) + '</a>')

    def render_actions(self, record):
        action_data = ""
        if settings.ACCESS_PERMISSION_ORDER_VIEW in self.auth_permissions.values():
            url = reverse("operators_view", args=[record.pk])
            action_data = action_data + "<a class=\"dropdown-item\" href=\"" + url + "\">View</a>"
        if settings.ACCESS_PERMISSION_ORDER_DELETE in self.auth_permissions.values():
            url = reverse("operators_select_single")
            action_data = action_data + "<a class=\"dropdown-item\" href=\"#\" onclick=\"javascript: singleSelect(\'" + url + "\', \'delete\', \'" + str(
                record.order_id) + "\');\">Delete</a>"
        return action_data

    @staticmethod
    def render_order_status(record):
        return Orders.get_status_html_tag(record)

    class Meta:
        model = Orders
        attrs = {
            'id': 'table-' + Orders.NAME,
            'name': Orders.NAME,
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_check',
            'row_number',
            'row_id',
            'order_code',
            'order_requester_name',
            'order_project_name',
            'order_requisition_number',
            'order_award_number',
            'order_project_code',
            'order_status',
            'actions'
        )
        fields = (
            'order_code',
            'order_requester_name',
            'order_project_name',
            'order_requisition_number',
            'order_award_number',
            'order_project_code',
            'order_status',
        )
        template_name = '_include/bootstrap-datatable.html'
