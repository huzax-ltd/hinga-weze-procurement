from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from tinymce.widgets import TinyMCE

from app.models import Mel_Indicators, Mel_Results, Mel_Sub_Results


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class MelResultSearchIndexForm(forms.ModelForm):
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
        cleaned_data = super(MelResultSearchIndexForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(MelResultSearchIndexForm, self).__init__(*args, **kwargs)

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
        model = Mel_Results
        fields = (
            'mel_indicator_id',
        )


class MelResultCreateForm(forms.ModelForm):
    mel_indicator_id = forms.ChoiceField(
        choices=(('', '--select--'),),
        initial='',
        label='Project',
        required=True,
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

    mel_result_details = forms.CharField(
        label='Result Details',
        min_length=1,
        max_length=255,
        required=True,
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

    mel_indicator_ids = forms.MultipleChoiceField(
        choices=(),
        initial='',
        label='Indicators',
        required=False,
        validators=[],
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'id': 'search-input-select-indicators',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))

    def clean_mel_indicator_id(self):
        data = self.cleaned_data['mel_indicator_id']
        return data

    def clean_mel_result_details(self):
        data = self.cleaned_data['mel_result_details']
        return data

    def clean_mel_indicator_ids(self):
        data = self.cleaned_data['mel_indicator_ids']
        return data

    def clean(self):
        cleaned_data = super(MelResultCreateForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(MelResultCreateForm, self).__init__(*args, **kwargs)

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
                    'id': 'search-input-select-id',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                }
            ))

        INDICATORS = ()
        indicators = Mel_Indicators.objects.all()
        for indicator in indicators:
            INDICATORS = INDICATORS + ((indicator.mel_indicator_id, indicator.mel_indicator_details),)

        self.fields['mel_indicator_ids'] = forms.MultipleChoiceField(
            choices=INDICATORS,
            initial='',
            label='Indicators',
            required=False,
            validators=[],
            widget=forms.CheckboxSelectMultiple(
                attrs={
                    'id': 'search-input-select-indicators',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                }
            ))

    class Meta:
        model = Mel_Results
        fields = (
            'mel_indicator_id',
            'mel_result_details',
            'mel_indicator_ids',
        )


class MelResultUpdateForm(forms.ModelForm):
    mel_indicator_id = forms.ChoiceField(
        choices=(('', '--select--'),),
        initial='',
        label='Project',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-id',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
                'readonly': True,
            }
        ))

    mel_result_details = forms.CharField(
        label='Result Details',
        min_length=1,
        max_length=255,
        required=True,
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
    mel_indicator_ids = forms.MultipleChoiceField(
        choices=(),
        initial='',
        label='Indicators',
        required=False,
        validators=[],
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'id': 'search-input-select-indicators',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))

    def clean_mel_indicator_id(self):
        data = self.cleaned_data['mel_indicator_id']
        return data

    def clean_mel_result_details(self):
        data = self.cleaned_data['mel_result_details']
        return data

    def clean_mel_indicator_ids(self):
        data = self.cleaned_data['mel_indicator_ids']
        return data

    def clean(self):
        cleaned_data = super(MelResultUpdateForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(MelResultUpdateForm, self).__init__(*args, **kwargs)

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
                    'id': 'search-input-select-id',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                }
            ))

        INDICATORS = ()
        indicators = Mel_Indicators.objects.all()
        for indicator in indicators:
            INDICATORS = INDICATORS + ((indicator.mel_indicator_id, indicator.mel_indicator_details),)

        self.fields['mel_indicator_ids'] = forms.MultipleChoiceField(
            choices=INDICATORS,
            initial='',
            label='Indicators',
            required=False,
            validators=[],
            widget=forms.CheckboxSelectMultiple(
                attrs={
                    'id': 'search-input-select-indicators',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                }
            ))

    class Meta:
        model = Mel_Results
        fields = (
            'mel_indicator_id',
            'mel_result_details',
            'mel_indicator_ids',
        )


class MelSubResultCreateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    mel_sub_result_details = forms.CharField(
        label='Sub Result Details',
        min_length=1,
        max_length=255,
        required=True,
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

    def clean_mel_sub_result_details(self):
        data = self.cleaned_data['mel_sub_result_details']
        return data

    def clean(self):
        cleaned_data = super(MelSubResultCreateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Mel_Sub_Results
        fields = (
            'mel_sub_result_details',
        )


class MelSubResultUpdateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    mel_sub_result_details = forms.CharField(
        label='Sub Result Details',
        min_length=1,
        max_length=255,
        required=True,
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

    def clean_mel_sub_result_details(self):
        data = self.cleaned_data['mel_sub_result_details']
        return data

    def clean(self):
        cleaned_data = super(MelSubResultUpdateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Mel_Sub_Results
        fields = (
            'mel_sub_result_details',
        )
