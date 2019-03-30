from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

from app import settings
from app.models import Inventory_Items


class InventoryItemSearchIndexForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(InventoryItemSearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Inventory_Items
        fields = (

        )


class InventoryItemCreateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    inventory_order_purchase_no = forms.CharField(
        label='Purchase Order Number',
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
                'readonly': True,
            }
        ))
    inventory_order_project_name = forms.CharField(
        label='Project Name',
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
                'readonly': True,
            }
        ))

    inventory_item_voucher_reference = forms.CharField(
        label='Voucher Reference',
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

    inventory_item_location = forms.CharField(
        label='Location',
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

    inventory_item_equipment_holder_status = forms.CharField(
        label='Equipment Holder Status',
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

    inventory_item_staff_name = forms.CharField(
        label='Staff Name',
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

    inventory_item_room_number = forms.CharField(
        label='Room Number',
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

    inventory_item_disposal_date = forms.DateField(
        label='Disposal Date',
        required=False,
        validators=[],
        input_formats=['%Y-%m-%d', '%d %b %Y'],
        widget=forms.DateInput(
            format='%d %b %Y',
            attrs={
                'type': 'date',
                'id': 'search-input-date-disposal-date',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': 'Date of Birth',
                'aria-label': 'form-label',
            }
        ))

    inventory_item_verified_date = forms.DateField(
        label='Verified Date',
        required=False,
        validators=[],
        input_formats=['%Y-%m-%d', '%d %b %Y'],
        widget=forms.DateInput(
            format='%d %b %Y',
            attrs={
                'type': 'date',
                'id': 'search-input-date-verified-date',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': 'Date of Birth',
                'aria-label': 'form-label',
            }
        ))

    inventory_item_present_condition = forms.CharField(
        label='Present Condition',
        min_length=1,
        max_length=255,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(255)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    inventory_item_remark = forms.CharField(
        label='Remark',
        min_length=1,
        max_length=255,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(255)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    def clean_inventory_order_purchase_no(self):
        data = self.cleaned_data['inventory_order_purchase_no']
        return data

    def clean_inventory_order_project_name(self):
        data = self.cleaned_data['inventory_order_project_name']
        return data

    def clean_inventory_item_voucher_reference(self):
        data = self.cleaned_data['inventory_item_voucher_reference']
        return data

    def clean_inventory_item_location(self):
        data = self.cleaned_data['inventory_item_location']
        return data

    def clean_inventory_item_equipment_holder_status(self):
        data = self.cleaned_data['inventory_item_equipment_holder_status']
        return data

    def clean_inventory_item_staff_name(self):
        data = self.cleaned_data['inventory_item_staff_name']
        return data

    def clean_inventory_item_room_number(self):
        data = self.cleaned_data['inventory_item_room_number']
        return data

    def clean_inventory_item_disposal_date(self):
        data = self.cleaned_data['inventory_item_disposal_date']
        if not data:
            data = settings.APP_CONSTANT_DEFAULT_DATE_VALUE
        return data

    def clean_inventory_item_verified_date(self):
        data = self.cleaned_data['inventory_item_verified_date']
        if not data:
            data = settings.APP_CONSTANT_DEFAULT_DATE_VALUE
        return data

    def clean_inventory_item_present_condition(self):
        data = self.cleaned_data['inventory_item_present_condition']
        return data

    def clean_inventory_item_remark(self):
        data = self.cleaned_data['inventory_item_remark']
        return data

    def clean(self):
        cleaned_data = super(InventoryItemCreateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Inventory_Items
        fields = (
            'inventory_order_purchase_no',
            'inventory_order_project_name',
            'inventory_item_voucher_reference',
            'inventory_item_location',
            'inventory_item_equipment_holder_status',
            'inventory_item_staff_name',
            'inventory_item_room_number',
            'inventory_item_disposal_date',
            'inventory_item_verified_date',
            'inventory_item_present_condition',
            'inventory_item_remark',
        )
