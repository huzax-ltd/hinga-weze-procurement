from django import forms
from tinymce.widgets import TinyMCE

from app.models import Mel_Indicators


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class MelIndicatorSearchIndexForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(MelIndicatorSearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Mel_Indicators
        fields = (

        )
