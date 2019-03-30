from __future__ import unicode_literals

import itertools

import django_tables2 as tables

from app.models import Products


class ProductGoodsTable(tables.Table):
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
    product_code = tables.Column(
        verbose_name='Product Id',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_tag = tables.Column(
        verbose_name='CNFA Tag',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_title = tables.Column(
        verbose_name='Name',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:500px;',
        }
    )
    product_category = tables.Column(
        verbose_name='Category',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_quantity_available = tables.Column(
        verbose_name='Quantity',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
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
        super(ProductGoodsTable, self).__init__(*args, **kwargs)

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
    #     return action_data

    class Meta:
        model = Products
        attrs = {
            'id': 'table-goods',
            'name': 'Goods',
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_check',
            'row_number',
            'row_id',
            'product_code',
            'product_tag',
            'product_title',
            'product_category',
            'product_quantity_available',
            # 'actions'
        )
        fields = (
            'product_code',
            'product_tag',
            'product_title',
            'product_category',
            'product_quantity_available',
        )
        template_name = '_include/bootstrap-datatable-no-action.html'


class ProductAssetsTable(tables.Table):
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
    product_code = tables.Column(
        verbose_name='Product Id',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_tag = tables.Column(
        verbose_name='CNFA Tag',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_title = tables.Column(
        verbose_name='Name',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:500px;',
        }
    )
    product_category = tables.Column(
        verbose_name='Category',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_quantity_available = tables.Column(
        verbose_name='Quantity',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
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
        super(ProductAssetsTable, self).__init__(*args, **kwargs)

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
    #     return action_data

    class Meta:
        model = Products
        attrs = {
            'id': 'table-assets',
            'name': 'Assets',
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_check',
            'row_number',
            'row_id',
            'product_code',
            'product_tag',
            'product_title',
            'product_category',
            'product_quantity_available',
            # 'actions'
        )
        fields = (
            'product_code',
            'product_tag',
            'product_title',
            'product_category',
            'product_quantity_available',
        )
        template_name = '_include/bootstrap-datatable-no-action.html'


class ProductGoodsInventoryTable(tables.Table):
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
    product_code = tables.Column(
        verbose_name='Product Id',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_tag = tables.Column(
        verbose_name='CNFA Tag',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_title = tables.Column(
        verbose_name='Name',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:500px;',
        }
    )
    product_quantity_initial = tables.Column(
        verbose_name='Stock Initial',
        orderable=False,
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_quantity_in = tables.Column(
        verbose_name='Stock In',
        orderable=False,
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_quantity_out = tables.Column(
        verbose_name='Stock Out',
        orderable=False,
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_quantity_final = tables.Column(
        verbose_name='Stock Final',
        orderable=False,
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )

    def __init__(self, *args, **kwargs):
        self.counter = itertools.count(1)
        super(ProductGoodsInventoryTable, self).__init__(*args, **kwargs)

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
    #     return action_data

    class Meta:
        model = Products
        attrs = {
            'id': 'table-goods',
            'name': 'Inventory of Goods',
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_check',
            'row_number',
            'row_id',
            'product_code',
            'product_tag',
            'product_title',
            'product_quantity_initial',
            'product_quantity_in',
            'product_quantity_out',
            'product_quantity_final',
            # 'actions'
        )
        fields = (
            'product_code',
            'product_tag',
            'product_title',
            'product_quantity_initial',
            'product_quantity_in',
            'product_quantity_out',
            'product_quantity_final',
        )
        template_name = '_include/bootstrap-datatable-no-action.html'


class ProductAssetsInventoryTable(tables.Table):
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
    product_code = tables.Column(
        verbose_name='Product Id',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_tag = tables.Column(
        verbose_name='CNFA Tag',
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_title = tables.Column(
        verbose_name='Name',
        attrs={
            'search_filter': 'input-text',
            # 'th_style': 'width:500px;',
        }
    )
    product_quantity_initial = tables.Column(
        verbose_name='Stock Initial',
        orderable=False,
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_quantity_in = tables.Column(
        verbose_name='Stock In',
        orderable=False,
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_quantity_out = tables.Column(
        verbose_name='Stock Out',
        orderable=False,
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )
    product_quantity_final = tables.Column(
        verbose_name='Stock Final',
        orderable=False,
        attrs={
            'search_filter': 'input-text',
            'th_style': 'width:100px;',
        }
    )

    def __init__(self, *args, **kwargs):
        self.counter = itertools.count(1)
        super(ProductAssetsInventoryTable, self).__init__(*args, **kwargs)

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
    #     return action_data

    class Meta:
        model = Products
        attrs = {
            'id': 'table-assets',
            'name': 'Inventory of Assets',
            'class': 'table table-bordered table-hover thead-dark',
            'cellspacing': '0',
            'width': '100%',
        }
        sequence = (
            'row_check',
            'row_number',
            'row_id',
            'product_code',
            'product_tag',
            'product_title',
            'product_quantity_initial',
            'product_quantity_in',
            'product_quantity_out',
            'product_quantity_final',
            # 'actions'
        )
        fields = (
            'product_code',
            'product_tag',
            'product_title',
            'product_quantity_initial',
            'product_quantity_in',
            'product_quantity_out',
            'product_quantity_final',
        )
        template_name = '_include/bootstrap-datatable-no-action.html'
