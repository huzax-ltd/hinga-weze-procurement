from __future__ import unicode_literals

import itertools

import django_tables2 as tables
from django.urls import reverse
from django.utils.safestring import mark_safe

from app.models import Product_Requests


class ProductRequestsTable(tables.Table):
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
    product_request_code = tables.Column(
        verbose_name='Request Id',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:80px;',
        }
    )
    product_request_project = tables.Column(
        verbose_name='Project Name',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:500px;',
        }
    )
    product_request_no_of_items = tables.Column(
        verbose_name='No. of Items',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:80px;',
        }
    )
    product_request_requested_by = tables.Column(
        verbose_name='Requested By',
        attrs={
            'search_filter': 'input-text',
        }
    )
    product_request_status = tables.Column(
        verbose_name='Status',
        attrs={
            'search_filter': 'input-select',
            'search_data': Product_Requests.ARRAY_STATUSES,
            'search_type': 'status',
            'th_style': 'width:100px;',
        }
    )

    def __init__(self, *args, **kwargs):
        self.counter = itertools.count(1)
        super(ProductRequestsTable, self).__init__(*args, **kwargs)

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
    def render_product_request_code(record):
        return mark_safe(
            '<a href=' + reverse("product_requests_view",
                                 args=[record.pk]) + ' style=\'text-decoration:underline; color:#1B82DC;\' >' +
            str(record.product_request_code) + '</a>')

    @staticmethod
    def render_product_request_status(record):
        return Product_Requests.get_status_html_tag(record)

    class Meta:
        model = Product_Requests
        attrs = {
            'id': 'table-' + Product_Requests.NAME,
            'name': Product_Requests.NAME,
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_check',
            'row_number',
            'row_id',
            'product_request_code',
            'product_request_project',
            'product_request_no_of_items',
            'product_request_requested_by',
            'product_request_status',
        )
        fields = (
            'product_request_code',
            'product_request_project',
            'product_request_no_of_items',
            'product_request_requested_by',
            'product_request_status',
        )
        template_name = '_include/bootstrap-datatable-no-action.html'
