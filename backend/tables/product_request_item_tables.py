from __future__ import unicode_literals

import itertools

import django_tables2 as tables

from app.models import Product_Request_Items


class ProductRequestItemsTable(tables.Table):
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
    products_product_id = tables.Column(
        verbose_name='Id',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_request_item_product_type = tables.Column(
        verbose_name='Type',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_request_item_product_tag = tables.Column(
        verbose_name='CNFA Tag',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_request_item_product_category = tables.Column(
        verbose_name='Category',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_request_item_product_title = tables.Column(
        verbose_name='Name',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:60px;',
        }
    )
    product_request_item_product_quantity_ordered = tables.Column(
        verbose_name='Quantity',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:60px;',
        }
    )
    product_request_item_status = tables.Column(
        verbose_name='Status',
        attrs={
            'search_filter': 'input-select',
            'search_data': Product_Request_Items.ARRAY_STATUSES,
            'search_type': 'status',
            'th_style': 'width:100px;',
        }
    )

    def __init__(self, *args, **kwargs):
        self.counter = itertools.count(1)
        super(ProductRequestItemsTable, self).__init__(*args, **kwargs)

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
    def render_product_request_item_quantity_ordered(record):
        return str(record.product_request_item_product_quantity_ordered) + " " + str(
            record.product_request_item_product_quantity_unit)

    @staticmethod
    def render_product_request_item_status(record):
        return Product_Request_Items.get_status_html_tag(record)

    class Meta:
        model = Product_Request_Items
        attrs = {
            'id': 'table-' + Product_Request_Items.NAME,
            'name': Product_Request_Items.NAME,
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_check',
            'row_number',
            'row_id',
            'products_product_id',
            'product_request_item_product_type',
            'product_request_item_product_tag',
            'product_request_item_product_category',
            'product_request_item_product_title',
            'product_request_item_product_quantity_ordered',
            'product_request_item_status',
        )
        fields = (
            'products_product_id',
            'product_request_item_product_type',
            'product_request_item_product_tag',
            'product_request_item_product_category',
            'product_request_item_product_title',
            'product_request_item_product_quantity_ordered',
            'product_request_item_status',
        )
        template_name = '_include/bootstrap-datatable-no-action.html'
