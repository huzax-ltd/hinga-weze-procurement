from django import forms
from django.core.validators import ValidationError, MinLengthValidator, MaxLengthValidator, EmailValidator
from django.core.validators import validate_email, validate_integer
from tinymce.widgets import TinyMCE

from app.models import Order_Proposals
from app.validators import IsPhoneNumberValidator


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class OrderProposalSearchIndexForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(OrderProposalSearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Order_Proposals
        fields = (

        )


class OrderProposalCreateForm(forms.ModelForm):
    company_type = forms.ChoiceField(
        choices=Order_Proposals.DROPDOWN_SUPPLIER_TYPES,
        initial='',
        label='Type',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-company-type',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))

    title = forms.CharField(
        label='Name',
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

    details = forms.CharField(
        label='Description',
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

    rf_number = forms.CharField(
        label='RFQ/RFP/RFA Number',
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

    proposal_title = forms.CharField(
        label='Tender Description title',
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

    legal_representatives = forms.CharField(
        label='Legal Representatives',
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

    address_plot_no = forms.CharField(
        label='Plot No.',
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

    address_street = forms.CharField(
        label='Street',
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

    address_av_no = forms.CharField(
        label='AV No.',
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

    address_sector = forms.CharField(
        label='Sector',
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

    address_district = forms.CharField(
        label='District',
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

    address_country = forms.CharField(
        label='Country',
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

    contact_phone_number = forms.CharField(
        label='Phone Number',
        min_length=9,
        max_length=13,
        validators=[MinLengthValidator(9), MaxLengthValidator(13), IsPhoneNumberValidator],
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    contact_email_id = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    tin_number = forms.CharField(
        label='TIN or VAT Number',
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

    bank_account_details = forms.CharField(
        label='Bank Account Details',
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

    previous_reference1_name = forms.CharField(
        label='Name',
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

    previous_reference1_contact_person = forms.CharField(
        label='Contact Person',
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

    previous_reference1_contact_number = forms.CharField(
        label='Phone Number',
        min_length=9,
        max_length=13,
        validators=[MinLengthValidator(9), MaxLengthValidator(13), IsPhoneNumberValidator],
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    previous_reference1_contact_email_id = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    previous_reference2_name = forms.CharField(
        label='Name',
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

    previous_reference2_contact_person = forms.CharField(
        label='Contact Person',
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

    previous_reference2_contact_number = forms.CharField(
        label='Phone Number',
        min_length=9,
        max_length=13,
        validators=[MinLengthValidator(9), MaxLengthValidator(13), IsPhoneNumberValidator],
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    previous_reference2_contact_email_id = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    previous_reference3_name = forms.CharField(
        label='Name',
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

    previous_reference3_contact_person = forms.CharField(
        label='Contact Person',
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

    previous_reference3_contact_number = forms.CharField(
        label='Phone Number',
        min_length=9,
        max_length=13,
        validators=[MinLengthValidator(9), MaxLengthValidator(13), IsPhoneNumberValidator],
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    previous_reference3_contact_email_id = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    def clean_company_type(self):
        data = self.cleaned_data['company_type']
        return data

    def clean_title(self):
        data = self.cleaned_data['title']
        return data

    def clean_details(self):
        data = self.cleaned_data['details']
        return data

    def clean_rf_number(self):
        data = self.cleaned_data['rf_number']
        return data

    def clean_proposal_title(self):
        data = self.cleaned_data['proposal_title']
        return data

    def clean_legal_representatives(self):
        data = self.cleaned_data['legal_representatives']
        return data

    def clean_address_plot_no(self):
        data = self.cleaned_data['address_plot_no']
        return data

    def clean_address_street(self):
        data = self.cleaned_data['address_street']
        return data

    def clean_address_av_no(self):
        data = self.cleaned_data['address_av_no']
        return data

    def clean_address_sector(self):
        data = self.cleaned_data['address_sector']
        return data

    def clean_address_district(self):
        data = self.cleaned_data['address_district']
        return data

    def clean_address_country(self):
        data = self.cleaned_data['address_country']
        return data

    def clean_contact_phone_number(self):
        data = self.cleaned_data['contact_phone_number']
        if data != '':
            try:
                validate_integer(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid phone number')
        return data

    def clean_contact_email_id(self):
        data = self.cleaned_data['contact_email_id']
        try:
            validate_email(data)
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address')
        return data

    def clean_tin_number(self):
        data = self.cleaned_data['tin_number']
        return data

    def clean_bank_account_details(self):
        data = self.cleaned_data['bank_account_details']
        return data

    def clean_previous_reference1_name(self):
        data = self.cleaned_data['previous_reference1_name']
        return data

    def clean_previous_reference1_contact_person(self):
        data = self.cleaned_data['previous_reference1_contact_person']
        return data

    def clean_previous_reference1_contact_number(self):
        data = self.cleaned_data['previous_reference1_contact_number']
        if data != '':
            try:
                validate_integer(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid phone number')
        return data

    def clean_previous_reference1_contact_email_id(self):
        data = self.cleaned_data['previous_reference1_contact_email_id']
        if data != '':
            try:
                validate_email(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid email address')
        return data

    def clean_previous_reference2_name(self):
        data = self.cleaned_data['previous_reference2_name']
        return data

    def clean_previous_reference2_contact_person(self):
        data = self.cleaned_data['previous_reference2_contact_person']
        return data

    def clean_previous_reference2_contact_number(self):
        data = self.cleaned_data['previous_reference2_contact_number']
        if data != '':
            try:
                validate_integer(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid phone number')
        return data

    def clean_previous_reference2_contact_email_id(self):
        data = self.cleaned_data['previous_reference2_contact_email_id']
        if data != '':
            try:
                validate_email(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid email address')
        return data

    def clean_previous_reference3_name(self):
        data = self.cleaned_data['previous_reference3_name']
        return data

    def clean_previous_reference3_contact_person(self):
        data = self.cleaned_data['previous_reference3_contact_person']
        return data

    def clean_previous_reference3_contact_number(self):
        data = self.cleaned_data['previous_reference3_contact_number']
        if data != '':
            try:
                validate_integer(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid phone number')
        return data

    def clean_previous_reference3_contact_email_id(self):
        data = self.cleaned_data['previous_reference3_contact_email_id']
        if data != '':
            try:
                validate_email(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid email address')
        return data

    def clean(self):
        cleaned_data = super(OrderProposalCreateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Order_Proposals
        fields = (
            'company_type',
            'title',
            'details',
            'rf_number',
            'proposal_title',
            'legal_representatives',
            'address_plot_no',
            'address_street',
            'address_av_no',
            'address_sector',
            'address_district',
            'address_country',
            'contact_phone_number',
            'contact_email_id',
            'tin_number',
            'bank_account_details',
            'previous_reference1_name',
            'previous_reference1_contact_person',
            'previous_reference1_contact_number',
            'previous_reference1_contact_email_id',
            'previous_reference2_name',
            'previous_reference2_contact_person',
            'previous_reference2_contact_number',
            'previous_reference2_contact_email_id',
            'previous_reference3_name',
            'previous_reference3_contact_person',
            'previous_reference3_contact_number',
            'previous_reference3_contact_email_id',
        )


class OrderProposalViewForm(forms.ModelForm):
    company_type = forms.ChoiceField(
        choices=Order_Proposals.DROPDOWN_SUPPLIER_TYPES,
        initial='',
        label='Type',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-company-type',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
                'readonly': True,
                'disabled': True,
            }
        ))

    title = forms.CharField(
        label='Name',
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
                'readonly': True,
                'disabled': True,
            }
        ))

    details = forms.CharField(
        label='Description',
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

    rf_number = forms.CharField(
        label='RFQ/RFP/RFA Number',
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
                'readonly': True,
                'disabled': True,
            }
        ))

    proposal_title = forms.CharField(
        label='Tender Description title',
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
                'readonly': True,
                'disabled': True,
            }
        ))

    legal_representatives = forms.CharField(
        label='Legal Representatives',
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
                'readonly': True,
                'disabled': True,
            }
        ))

    address_plot_no = forms.CharField(
        label='Plot No.',
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
                'readonly': True,
                'disabled': True,
            }
        ))

    address_street = forms.CharField(
        label='Street',
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
                'readonly': True,
                'disabled': True,
            }
        ))

    address_av_no = forms.CharField(
        label='AV No.',
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
                'readonly': True,
                'disabled': True,
            }
        ))

    address_sector = forms.CharField(
        label='Sector',
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
                'readonly': True,
                'disabled': True,
            }
        ))

    address_district = forms.CharField(
        label='District',
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
                'readonly': True,
                'disabled': True,
            }
        ))

    address_country = forms.CharField(
        label='Country',
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
                'readonly': True,
                'disabled': True,
            }
        ))

    contact_phone_number = forms.CharField(
        label='Phone Number',
        min_length=9,
        max_length=13,
        validators=[MinLengthValidator(9), MaxLengthValidator(13), IsPhoneNumberValidator],
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
                'disabled': True,
            }
        ))
    contact_email_id = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
                'disabled': True,
            }
        ))

    tin_number = forms.CharField(
        label='TIN or VAT Number',
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

    bank_account_details = forms.CharField(
        label='Bank Account Details',
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

    previous_reference1_name = forms.CharField(
        label='Name',
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

    previous_reference1_contact_person = forms.CharField(
        label='Contact Person',
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

    previous_reference1_contact_number = forms.CharField(
        label='Phone Number',
        min_length=9,
        max_length=13,
        validators=[MinLengthValidator(9), MaxLengthValidator(13), IsPhoneNumberValidator],
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
                'disabled': True,
            }
        ))
    previous_reference1_contact_email_id = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
                'disabled': True,
            }
        ))

    previous_reference2_name = forms.CharField(
        label='Name',
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

    previous_reference2_contact_person = forms.CharField(
        label='Contact Person',
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

    previous_reference2_contact_number = forms.CharField(
        label='Phone Number',
        min_length=9,
        max_length=13,
        validators=[MinLengthValidator(9), MaxLengthValidator(13), IsPhoneNumberValidator],
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
                'disabled': True,
            }
        ))
    previous_reference2_contact_email_id = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
                'disabled': True,
            }
        ))

    previous_reference3_name = forms.CharField(
        label='Name',
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

    previous_reference3_contact_person = forms.CharField(
        label='Contact Person',
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

    previous_reference3_contact_number = forms.CharField(
        label='Phone Number',
        min_length=9,
        max_length=13,
        validators=[MinLengthValidator(9), MaxLengthValidator(13), IsPhoneNumberValidator],
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
                'disabled': True,
            }
        ))
    previous_reference3_contact_email_id = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
                'disabled': True,
            }
        ))

    def clean_company_type(self):
        data = self.cleaned_data['company_type']
        return data

    def clean_title(self):
        data = self.cleaned_data['title']
        return data

    def clean_details(self):
        data = self.cleaned_data['details']
        return data

    def clean_rf_number(self):
        data = self.cleaned_data['rf_number']
        return data

    def clean_proposal_title(self):
        data = self.cleaned_data['proposal_title']
        return data

    def clean_legal_representatives(self):
        data = self.cleaned_data['legal_representatives']
        return data

    def clean_address_plot_no(self):
        data = self.cleaned_data['address_plot_no']
        return data

    def clean_address_street(self):
        data = self.cleaned_data['address_street']
        return data

    def clean_address_av_no(self):
        data = self.cleaned_data['address_av_no']
        return data

    def clean_address_sector(self):
        data = self.cleaned_data['address_sector']
        return data

    def clean_address_district(self):
        data = self.cleaned_data['address_district']
        return data

    def clean_address_country(self):
        data = self.cleaned_data['address_country']
        return data

    def clean_contact_phone_number(self):
        data = self.cleaned_data['contact_phone_number']
        if data != '':
            try:
                validate_integer(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid phone number')
        return data

    def clean_contact_email_id(self):
        data = self.cleaned_data['contact_email_id']
        try:
            validate_email(data)
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address')
        return data

    def clean_tin_number(self):
        data = self.cleaned_data['tin_number']
        return data

    def clean_bank_account_details(self):
        data = self.cleaned_data['bank_account_details']
        return data

    def clean_previous_reference1_name(self):
        data = self.cleaned_data['previous_reference1_name']
        return data

    def clean_previous_reference1_contact_person(self):
        data = self.cleaned_data['previous_reference1_contact_person']
        return data

    def clean_previous_reference1_contact_number(self):
        data = self.cleaned_data['previous_reference1_contact_number']
        if data != '':
            try:
                validate_integer(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid phone number')
        return data

    def clean_previous_reference1_contact_email_id(self):
        data = self.cleaned_data['previous_reference1_contact_email_id']
        if data != '':
            try:
                validate_email(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid email address')
        return data

    def clean_previous_reference2_name(self):
        data = self.cleaned_data['previous_reference2_name']
        return data

    def clean_previous_reference2_contact_person(self):
        data = self.cleaned_data['previous_reference2_contact_person']
        return data

    def clean_previous_reference2_contact_number(self):
        data = self.cleaned_data['previous_reference2_contact_number']
        if data != '':
            try:
                validate_integer(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid phone number')
        return data

    def clean_previous_reference2_contact_email_id(self):
        data = self.cleaned_data['previous_reference2_contact_email_id']
        if data != '':
            try:
                validate_email(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid email address')
        return data

    def clean_previous_reference3_name(self):
        data = self.cleaned_data['previous_reference3_name']
        return data

    def clean_previous_reference3_contact_person(self):
        data = self.cleaned_data['previous_reference3_contact_person']
        return data

    def clean_previous_reference3_contact_number(self):
        data = self.cleaned_data['previous_reference3_contact_number']
        if data != '':
            try:
                validate_integer(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid phone number')
        return data

    def clean_previous_reference3_contact_email_id(self):
        data = self.cleaned_data['previous_reference3_contact_email_id']
        if data != '':
            try:
                validate_email(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid email address')
        return data

    def clean(self):
        cleaned_data = super(OrderProposalViewForm, self).clean()
        return cleaned_data

    class Meta:
        model = Order_Proposals
        fields = (
            'company_type',
            'title',
            'details',
            'rf_number',
            'proposal_title',
            'legal_representatives',
            'address_plot_no',
            'address_street',
            'address_av_no',
            'address_sector',
            'address_district',
            'address_country',
            'contact_phone_number',
            'contact_email_id',
            'tin_number',
            'bank_account_details',
            'previous_reference1_name',
            'previous_reference1_contact_person',
            'previous_reference1_contact_number',
            'previous_reference1_contact_email_id',
            'previous_reference2_name',
            'previous_reference2_contact_person',
            'previous_reference2_contact_number',
            'previous_reference2_contact_email_id',
            'previous_reference3_name',
            'previous_reference3_contact_person',
            'previous_reference3_contact_number',
            'previous_reference3_contact_email_id',
        )
