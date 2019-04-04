from django import forms
from tinymce.widgets import TinyMCE

from app.models import Mel_Indicators, Mel_Results


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
