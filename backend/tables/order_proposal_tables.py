from __future__ import unicode_literals

import itertools

import django_tables2 as tables
from django.urls import reverse
from django.utils.safestring import mark_safe

from app.models import Orders, Order_Proposals


class Order_ProposalsTable(tables.Table):
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

    order_proposal_code = tables.Column(
        verbose_name='Proposal Code',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    order_proposal_supplier_rf_number = tables.Column(
        verbose_name='RFQ/RFP/RFA',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    order_proposal_supplier_proposal_title = tables.Column(
        verbose_name='Proposal Title',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:200px;',
        }
    )
    order_proposal_supplier_title = tables.Column(
        verbose_name='Supplier Name',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:200px;',
        }
    )
    order_proposal_cost = tables.Column(
        verbose_name='Cost',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:80px;',
        }
    )
    order_proposal_evaluated_score = tables.Column(
        verbose_name='Score',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:80px;',
        }
    )
    order_proposal_status = tables.Column(
        verbose_name='Status',
        attrs={
            'search_filter': 'input-select',
            'search_data': Order_Proposals.ARRAY_STATUSES,
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
        super(Order_ProposalsTable, self).__init__(*args, **kwargs)

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
    def render_order_proposal_code(record):
        return mark_safe(
            '<a href=' + reverse("order_proposals_view_internal",
                                 args=[record.pk]) + ' style=\'text-decoration:underline; color:#1B82DC;\' >' +
            str(record.order_proposal_code) + '</a>')

    def render_actions(self, record):
        action_data = ""
        return action_data

    @staticmethod
    def render_order_status(record):
        return Orders.get_status_html_tag(record)

    class Meta:
        model = Order_Proposals
        attrs = {
            'id': 'table-' + Order_Proposals.NAME,
            'name': Order_Proposals.NAME,
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_check',
            'row_number',
            'row_id',
            'order_proposal_code',
            'order_proposal_supplier_rf_number',
            'order_proposal_supplier_proposal_title',
            'order_proposal_supplier_title',
            'order_proposal_cost',
            'order_proposal_evaluated_score',
            'order_proposal_status',
            'actions'
        )
        fields = (
            'order_proposal_code',
            'order_proposal_supplier_rf_number',
            'order_proposal_supplier_proposal_title',
            'order_proposal_supplier_title',
            'order_proposal_cost',
            'order_proposal_evaluated_score',
            'order_proposal_status',
        )
        template_name = '_include/bootstrap-datatable.html'
