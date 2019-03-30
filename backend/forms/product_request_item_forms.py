from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

from app.models import Product_Request_Items, Products


class ProductRequestItemSearchIndexForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(ProductRequestItemSearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Product_Request_Items
        fields = (

        )


class ProductRequestItemCreateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    product_request_id = forms.CharField(
        label='Request Id',
        min_length=8,
        max_length=8,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
            }
        ))
    products_product_id = forms.ChoiceField(
        choices=(('', '--select--'),),
        initial='',
        label='Currency',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-currency',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    product_request_item_product_quantity_ordered = forms.DecimalField(
        label='Quantity',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    def clean_product_request_id(self):
        data = self.cleaned_data['product_request_id']
        return data

    def clean_products_product_id(self):
        data = self.cleaned_data['products_product_id']
        return data

    def clean_product_request_item_product_quantity_ordered(self):
        data = self.cleaned_data['product_request_item_product_quantity_ordered']
        return data

    def clean(self):
        cleaned_data = super(ProductRequestItemCreateForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(ProductRequestItemCreateForm, self).__init__(*args, **kwargs)

        PRODUCTS = (('', '--select--'),)
        products = Products.objects.all()
        for product in products:
            PRODUCTS = PRODUCTS + ((product.product_id, product.product_title),)

        self.fields['products_product_id'] = forms.ChoiceField(
            choices=PRODUCTS,
            initial='',
            label='Product',
            required=True,
            validators=[],
            widget=forms.Select(
                attrs={
                    'id': 'search-input-select-product-id',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                }
            ))

    class Meta:
        model = Product_Request_Items
        fields = (
            'product_request_id',
            'products_product_id',
            'product_request_item_product_quantity_ordered',
        )


class ProductRequestItemUpdateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    product_request_id = forms.CharField(
        label='Request Id',
        min_length=8,
        max_length=8,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
            }
        ))
    products_product_id = forms.ChoiceField(
        choices=(('', '--select--'),),
        initial='',
        label='Product',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-product-id',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    product_request_item_product_quantity_ordered = forms.DecimalField(
        label='Quantity',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    def clean_product_request_id(self):
        data = self.cleaned_data['product_request_id']
        return data

    def clean_products_product_id(self):
        data = self.cleaned_data['products_product_id']
        return data

    def clean_product_request_item_product_quantity_ordered(self):
        data = self.cleaned_data['product_request_item_product_quantity_ordered']
        return data

    def clean(self):
        cleaned_data = super(ProductRequestItemUpdateForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(ProductRequestItemUpdateForm, self).__init__(*args, **kwargs)

        PRODUCTS = (('', '--select--'),)
        products = Products.objects.all()
        for product in products:
            PRODUCTS = PRODUCTS + ((product.product_id, product.product_title),)

        self.fields['products_product_id'] = forms.ChoiceField(
            choices=PRODUCTS,
            initial='',
            label='Product',
            required=True,
            validators=[],
            widget=forms.Select(
                attrs={
                    'id': 'search-input-select-product-id',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                }
            ))

    class Meta:
        model = Product_Request_Items
        fields = (
            'product_request_id',
            'products_product_id',
            'product_request_item_product_quantity_ordered',
        )
