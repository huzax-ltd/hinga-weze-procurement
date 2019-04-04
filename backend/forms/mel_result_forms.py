from django import forms
from tinymce.widgets import TinyMCE

from app.models import Mel_Results


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class MelResultSearchIndexForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(MelResultSearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Mel_Results
        fields = (

        )
