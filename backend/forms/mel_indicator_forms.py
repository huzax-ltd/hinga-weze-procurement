from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from tinymce.widgets import TinyMCE

from app.models import Mel_Indicators


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class MelIndicatorSearchIndexForm(forms.ModelForm):
    mel_indicator_id = forms.ChoiceField(
        choices=(('', '--select--'),),
        initial='',
        label='Project',
        required=False,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-id',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))

    def clean_mel_indicator_id(self):
        data = self.cleaned_data['mel_indicator_id']
        return data

    def clean(self):
        cleaned_data = super(MelIndicatorSearchIndexForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(MelIndicatorSearchIndexForm, self).__init__(*args, **kwargs)

        INDICATORS = (('', '--select--'),)
        indicators = Mel_Indicators.objects.filter(mel_indicator_number=1).all()
        for indicator in indicators:
            INDICATORS = INDICATORS + ((indicator.mel_indicator_id, indicator.mel_indicator_name),)

        self.fields['mel_indicator_id'] = forms.ChoiceField(
            choices=INDICATORS,
            initial='',
            label='Project',
            required=False,
            validators=[],
            widget=forms.Select(
                attrs={
                    'id': 'search-input-select-id',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                }
            ))

    class Meta:
        model = Mel_Indicators
        fields = (
            'mel_indicator_id',
        )


class MelIndicatorCreateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    mel_indicator_name = forms.CharField(
        label='Project Name',
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

    def clean_mel_indicator_name(self):
        data = self.cleaned_data['mel_indicator_name']
        return data

    def clean(self):
        cleaned_data = super(MelIndicatorCreateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Mel_Indicators
        fields = (
            'mel_indicator_name',
        )


class MelIndicatorUpdateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    mel_indicator_name = forms.CharField(
        label='Project Name',
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

    def clean_mel_indicator_name(self):
        data = self.cleaned_data['mel_indicator_name']
        return data

    def clean(self):
        cleaned_data = super(MelIndicatorUpdateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Mel_Indicators
        fields = (
            'mel_indicator_name',
        )


class MelIndicatorItemUpdateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    mel_indicator_id = forms.ChoiceField(
        choices=(('', '--select--'),),
        initial='',
        label='Project',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-item-id',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
                'readonly': True,
            }
        ))

    mel_indicator_number = forms.CharField(
        label='Number',
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

    mel_indicator_details = forms.CharField(
        label='Indicator Details',
        min_length=1,
        max_length=255,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(255)],
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'rows': 5,
            }
        ))

    def clean_mel_indicator_id(self):
        data = self.cleaned_data['mel_indicator_id']
        return data

    def clean_mel_indicator_number(self):
        data = self.cleaned_data['mel_indicator_number']
        return data

    def clean_mel_indicator_details(self):
        data = self.cleaned_data['mel_indicator_details']
        return data

    def clean(self):
        cleaned_data = super(MelIndicatorItemUpdateForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(MelIndicatorItemUpdateForm, self).__init__(*args, **kwargs)

        INDICATORS = (('', '--select--'),)
        indicators = Mel_Indicators.objects.filter(mel_indicator_number=1).all()
        for indicator in indicators:
            INDICATORS = INDICATORS + ((indicator.mel_indicator_id, indicator.mel_indicator_name),)

        self.fields['mel_indicator_id'] = forms.ChoiceField(
            choices=INDICATORS,
            initial='',
            label='Project',
            required=True,
            validators=[],
            widget=forms.Select(
                attrs={
                    'id': 'search-input-select-item-id',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                    'readonly': True,
                }
            ))

    class Meta:
        model = Mel_Indicators
        fields = (
            'mel_indicator_id',
            'mel_indicator_number',
            'mel_indicator_details',
        )
