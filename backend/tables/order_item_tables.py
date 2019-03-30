from __future__ import unicode_literals

import itertools

import django_tables2 as tables

from app.models import Order_Items


class OrderItemsTable(tables.Table):
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
    order_item_title = tables.Column(
        verbose_name='Item details',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:100px;',
        }
    )
    order_item_usaid_approval = tables.Column(
        verbose_name='USAID Approval',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    order_item_duration = tables.Column(
        verbose_name='Time in days',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    order_item_unit_price = tables.Column(
        verbose_name='Unit Price',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    order_item_quantity_ordered = tables.Column(
        verbose_name='Quantity',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:60px;',
        }
    )
    order_item_total_price = tables.Column(
        verbose_name='Total Amount',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    order_item_status = tables.Column(
        verbose_name='Status',
        attrs={
            'search_filter': 'input-select',
            'search_data': Order_Items.ARRAY_STATUSES,
            'search_type': 'status',
            'th_style': 'width:100px;',
        }
    )

    def __init__(self, *args, **kwargs):
        self.counter = itertools.count(1)
        super(OrderItemsTable, self).__init__(*args, **kwargs)

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
    def render_order_item_title(record):
        return record.order_item_title

    @staticmethod
    def render_order_item_usaid_approval(record):
        value = 'No'
        if record.order_item_usaid_approval:
            value = 'Yes'
        return value

    @staticmethod
    def render_order_item_duration(record):
        return record.order_item_duration

    @staticmethod
    def render_order_item_unit_price(record):
        return str(record.order_item_currency) + " " + str(record.order_item_unit_price)

    @staticmethod
    def render_order_item_quantity_ordered(record):
        return str(record.order_item_quantity_ordered) + " " + str(record.order_item_quantity_unit)

    @staticmethod
    def render_order_item_total_price(record):
        total = float(record.order_item_unit_price) * float(record.order_item_quantity_ordered)
        return str(record.order_item_currency) + " " + str(total)

    @staticmethod
    def render_order_item_status(record):
        return Order_Items.get_status_html_tag(record)

    class Meta:
        model = Order_Items
        attrs = {
            'id': 'table-' + Order_Items.NAME,
            'name': Order_Items.NAME,
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_check',
            'row_number',
            'row_id',
            'order_item_title',
            'order_item_usaid_approval',
            'order_item_duration',
            'order_item_unit_price',
            'order_item_quantity_ordered',
            'order_item_total_price',
            'order_item_status',
        )
        fields = (
            'order_item_title',
            'order_item_usaid_approval',
            'order_item_duration',
            'order_item_unit_price',
            'order_item_quantity_ordered',
            'order_item_total_price',
            'order_item_status',
        )
        template_name = '_include/bootstrap-datatable-no-action.html'
