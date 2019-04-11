from django import forms
from tinymce.widgets import TinyMCE

from app.models import Mel_Indicators, Mel_Results, Mel_Activities


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class MelActivitySearchIndexForm(forms.ModelForm):
    mel_indicator_id = forms.ChoiceField(
        choices=(('', '--select--'),),
        initial='',
        label='Project',
        required=False,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-indicator-id',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))

    mel_result_id = forms.ChoiceField(
        choices=(('', '--select--'),),
        initial='',
        label='Project',
        required=False,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-result-id',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))

    def clean_mel_indicator_id(self):
        data = self.cleaned_data['mel_indicator_id']
        return data

    def clean_mel_result_id(self):
        data = self.cleaned_data['mel_result_id']
        return data

    def clean(self):
        cleaned_data = super(MelActivitySearchIndexForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(MelActivitySearchIndexForm, self).__init__(*args, **kwargs)

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
                    'id': 'search-input-select-indicator-id',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select project--',
                    'aria-label': 'form-label',
                }
            ))

        RESULTS = (('', '--select--'),)
        results = Mel_Results.objects.all()
        for result in results:
            RESULTS = RESULTS + ((result.mel_result_id, result.mel_result_details),)

        self.fields['mel_result_id'] = forms.ChoiceField(
            choices=RESULTS,
            initial='',
            label='Result',
            required=False,
            validators=[],
            widget=forms.Select(
                attrs={
                    'id': 'search-input-select-result-id',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select result--',
                    'aria-label': 'form-label',
                }
            ))

    class Meta:
        model = Mel_Activities
        fields = (
            'mel_indicator_id',
            'mel_result_id',
        )
