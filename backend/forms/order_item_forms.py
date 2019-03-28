from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

from app.models import Operators, Order_Items


class OrderItemSearchIndexForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(OperatorSearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Order_Items
        fields = (

        )


class OrderItemCreateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    order_id = forms.CharField(
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
    type = forms.ChoiceField(
        choices=Order_Items.DROPDOWN_TYPES,
        initial='',
        label='Type',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-type',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    title = forms.CharField(
        label='Item Details',
        min_length=1,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    duration = forms.DecimalField(
        label='Time in Days',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    unit_price = forms.DecimalField(
        label='Unit Price',
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
    currency = forms.ChoiceField(
        choices=Order_Items.DROPDOWN_CURRENCIES,
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
    quantity_ordered = forms.DecimalField(
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
    quantity_unit = forms.CharField(
        label='Unit',
        min_length=1,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    def clean_order_id(self):
        data = self.cleaned_data['order_id']
        return data

    def clean_type(self):
        data = self.cleaned_data['type']
        return data

    def clean_title(self):
        data = self.cleaned_data['title']
        return data

    def clean_duration(self):
        data = self.cleaned_data['duration']
        return data

    def clean_unit_price(self):
        data = self.cleaned_data['unit_price']
        return data

    def clean_currency(self):
        data = self.cleaned_data['currency']
        return data

    def clean_quantity_ordered(self):
        data = self.cleaned_data['quantity_ordered']
        return data

    def clean_quantity_unit(self):
        data = self.cleaned_data['quantity_unit']
        return data

    def clean(self):
        cleaned_data = super(OrderItemCreateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Operators
        fields = (
            'order_id',
            'type',
            'title',
            'duration',
            'unit_price',
            'currency',
            'quantity_ordered',
            'quantity_unit'
        )


class OrderItemUpdateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    order_id = forms.CharField(
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
    type = forms.ChoiceField(
        choices=Order_Items.DROPDOWN_TYPES,
        initial='',
        label='Type',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-type',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    title = forms.CharField(
        label='Item Details',
        min_length=1,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    duration = forms.DecimalField(
        label='Time in Days',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    unit_price = forms.DecimalField(
        label='Unit Price',
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
    currency = forms.ChoiceField(
        choices=Order_Items.DROPDOWN_CURRENCIES,
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
    quantity_ordered = forms.DecimalField(
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
    quantity_unit = forms.CharField(
        label='Unit',
        min_length=1,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    def clean_order_id(self):
        data = self.cleaned_data['order_id']
        return data

    def clean_type(self):
        data = self.cleaned_data['type']
        return data

    def clean_title(self):
        data = self.cleaned_data['title']
        return data

    def clean_duration(self):
        data = self.cleaned_data['duration']
        return data

    def clean_unit_price(self):
        data = self.cleaned_data['unit_price']
        return data

    def clean_currency(self):
        data = self.cleaned_data['currency']
        return data

    def clean_quantity_ordered(self):
        data = self.cleaned_data['quantity_ordered']
        return data

    def clean_quantity_unit(self):
        data = self.cleaned_data['quantity_unit']
        return data

    def clean(self):
        cleaned_data = super(OrderItemUpdateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Operators
        fields = (
            'order_id',
            'type',
            'title',
            'duration',
            'unit_price',
            'currency',
            'quantity_ordered',
            'quantity_unit'
        )
