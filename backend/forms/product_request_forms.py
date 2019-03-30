from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from tinymce.widgets import TinyMCE

from app.models import Product_Requests


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class ProductRequestSearchIndexForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(ProductRequestSearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Product_Requests
        fields = (

        )


class ProductRequestCreateForm(forms.ModelForm):
    product_request_project = forms.CharField(
        label='Project Name',
        min_length=1,
        max_length=255,
        required=True,
        validators=[MinLengthValidator(1), MaxLengthValidator(255)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    product_request_details = forms.CharField(
        label='Details',
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

    def clean_product_request_project(self):
        data = self.cleaned_data['product_request_project']
        return data

    def clean_product_request_details(self):
        data = self.cleaned_data['product_request_details']
        return data

    def clean(self):
        cleaned_data = super(ProductRequestCreateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Product_Requests
        fields = (
            'product_request_project',
            'product_request_details',
        )


class ProductRequestUpdateForm(forms.ModelForm):
    product_request_project = forms.CharField(
        label='Project Name',
        min_length=1,
        max_length=255,
        required=True,
        validators=[MinLengthValidator(1), MaxLengthValidator(255)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    product_request_details = forms.CharField(
        label='Details',
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

    def clean_product_request_project(self):
        data = self.cleaned_data['product_request_project']
        return data

    def clean_product_request_details(self):
        data = self.cleaned_data['product_request_details']
        return data

    def clean(self):
        cleaned_data = super(ProductRequestUpdateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Product_Requests
        fields = (
            'product_request_project',
            'product_request_details',
        )
