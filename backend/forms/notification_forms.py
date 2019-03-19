from django import forms

from app.models import Notifications


class NotificationSearchIndexForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(NotificationSearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Notifications
        fields = (
        )
