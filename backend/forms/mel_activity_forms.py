from django import forms
from tinymce.widgets import TinyMCE

from app.models import Mel_Activities


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class MelActivitySearchIndexForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(MelActivitySearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Mel_Activities
        fields = (

        )
