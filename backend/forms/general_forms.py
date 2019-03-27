from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from tinymce.widgets import TinyMCE

from app.models import Emails


class SendEmailForm(forms.ModelForm):
    email_to = forms.CharField(
        label='To',
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
    email_cc = forms.CharField(
        label='Cc',
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
    email_subject = forms.CharField(
        label='Subject',
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
                'readonly': True,
                'disabled': True,
            }
        ))

    email_message = forms.CharField(
        label='Message',
        required=False,
        widget=TinyMCE(
            attrs={
                'cols': 30,
                'rows': 10,
                'readonly': True,
                'disabled': True,
            }
        )
    )

    def clean_email_to(self):
        data = self.cleaned_data['email_to']
        return data

    def clean_email_cc(self):
        data = self.cleaned_data['email_cc']
        return data

    def clean_email_subject(self):
        data = self.cleaned_data['email_subject']
        return data

    def clean_email_message(self):
        data = self.cleaned_data['email_message']
        return data

    def clean(self):
        cleaned_data = super(SendEmailForm, self).clean()
        return cleaned_data

    class Meta:
        model = Emails
        fields = (
            'email_to',
            'email_cc',
            'email_subject',
            'email_message',
        )
