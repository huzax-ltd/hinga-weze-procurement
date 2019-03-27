from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MinLengthValidator, MaxLengthValidator
from tinymce.widgets import TinyMCE

from app.models import Orders, Order_Attachments, Operators


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class OrderSearchIndexForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(OperatorSearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Orders
        fields = (

        )


class OrderCreateForm(forms.ModelForm):
    requester_name = forms.CharField(
        label='Requester Name',
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
    project_name = forms.CharField(
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
    project_code = forms.CharField(
        label='Project Code',
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
    project_geo_code = forms.CharField(
        label='Project GeoCode',
        min_length=1,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    charge_code = forms.CharField(
        label='Charge Code',
        min_length=1,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    award_number = forms.CharField(
        label='Award Number',
        min_length=1,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    requisition_number = forms.CharField(
        label='Requisition Number',
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
    donor = forms.CharField(
        label='Donor',
        min_length=1,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    description = forms.CharField(
        label='Description',
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
    anticipated_award_mechanism = forms.CharField(
        label='Anticipated Award Mechanism',
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
    anticipated_start_date = forms.DateField(
        label='Anticipated Start Date',
        required=True,
        validators=[],
        input_formats=['%Y-%m-%d', '%d %b %Y'],
        widget=forms.DateInput(
            format='%d %b %Y',
            attrs={
                'type': 'date',
                'id': 'search-input-date-anticipated-start-date',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': 'Date of Birth',
                'aria-label': 'form-label',
            }
        ))
    anticipated_end_date = forms.DateField(
        label='Anticipated End Date',
        required=True,
        validators=[],
        input_formats=['%Y-%m-%d', '%d %b %Y'],
        widget=forms.DateInput(
            format='%d %b %Y',
            attrs={
                'type': 'date',
                'id': 'search-input-date-anticipated-end-date',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': 'Date of Birth',
                'aria-label': 'form-label',
            }
        ))
    special_considerations = forms.CharField(
        label='Special Considerations',
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

    def clean_requester_name(self):
        data = self.cleaned_data['requester_name']
        return data

    def clean_project_name(self):
        data = self.cleaned_data['project_name']
        return data

    def clean_project_code(self):
        data = self.cleaned_data['project_code']
        return data

    def clean_project_geo_code(self):
        data = self.cleaned_data['project_geo_code']
        return data

    def clean_charge_code(self):
        data = self.cleaned_data['charge_code']
        return data

    def clean_award_number(self):
        data = self.cleaned_data['award_number']
        return data

    def clean_requisition_number(self):
        data = self.cleaned_data['requisition_number']
        return data

    def clean_donor(self):
        data = self.cleaned_data['donor']
        return data

    def clean_description(self):
        data = self.cleaned_data['description']
        return data

    def clean_anticipated_award_mechanism(self):
        data = self.cleaned_data['anticipated_award_mechanism']
        return data

    def clean_anticipated_start_date(self):
        data = self.cleaned_data['anticipated_start_date']
        return data

    def clean_anticipated_end_date(self):
        data = self.cleaned_data['anticipated_end_date']
        return data

    def clean_special_considerations(self):
        data = self.cleaned_data['special_considerations']
        return data

    def clean(self):
        cleaned_data = super(OrderCreateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Orders
        fields = (
            'requester_name',
            'project_name',
            'project_code',
            'project_geo_code',
            'charge_code',
            'award_number',
            'requisition_number',
            'donor',
            'description',
            'anticipated_award_mechanism',
            'anticipated_start_date',
            'anticipated_end_date',
            'special_considerations'
        )


class OrderUpdateForm(forms.ModelForm):
    requester_name = forms.CharField(
        label='Requester Name',
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
    project_name = forms.CharField(
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
    project_code = forms.CharField(
        label='Project Code',
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
    project_geo_code = forms.CharField(
        label='Project GeoCode',
        min_length=1,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    charge_code = forms.CharField(
        label='Charge Code',
        min_length=1,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    award_number = forms.CharField(
        label='Award Number',
        min_length=1,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    requisition_number = forms.CharField(
        label='Requisition Number',
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
    donor = forms.CharField(
        label='Donor',
        min_length=1,
        max_length=100,
        required=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    description = forms.CharField(
        label='Description',
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
    anticipated_award_mechanism = forms.CharField(
        label='Anticipated Award Mechanism',
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
    anticipated_start_date = forms.DateField(
        label='Anticipated Start Date (MM/DD/YYYY)',
        required=True,
        validators=[],
        input_formats=['%Y-%m-%d', '%d %b %Y'],
        widget=forms.DateInput(
            format='%d %b %Y',
            attrs={
                'type': 'date',
                'id': 'search-input-date-anticipated-start-date',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': 'Date of Birth',
                'aria-label': 'form-label',
            }
        ))
    anticipated_end_date = forms.DateField(
        label='Anticipated End Date (MM/DD/YYYY)',
        required=True,
        validators=[],
        input_formats=['%Y-%m-%d', '%d %b %Y'],
        widget=forms.DateInput(
            format='%d %b %Y',
            attrs={
                'type': 'date',
                'id': 'search-input-date-anticipated-end-date',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': 'Date of Birth',
                'aria-label': 'form-label',
            }
        ))
    special_considerations = forms.CharField(
        label='Special Considerations',
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

    def clean_requester_name(self):
        data = self.cleaned_data['requester_name']
        return data

    def clean_project_name(self):
        data = self.cleaned_data['project_name']
        return data

    def clean_project_code(self):
        data = self.cleaned_data['project_code']
        return data

    def clean_project_geo_code(self):
        data = self.cleaned_data['project_geo_code']
        return data

    def clean_charge_code(self):
        data = self.cleaned_data['charge_code']
        return data

    def clean_award_number(self):
        data = self.cleaned_data['award_number']
        return data

    def clean_requisition_number(self):
        data = self.cleaned_data['requisition_number']
        return data

    def clean_donor(self):
        data = self.cleaned_data['donor']
        return data

    def clean_description(self):
        data = self.cleaned_data['description']
        return data

    def clean_anticipated_award_mechanism(self):
        data = self.cleaned_data['anticipated_award_mechanism']
        return data

    def clean_anticipated_start_date(self):
        data = self.cleaned_data['anticipated_start_date']
        return data

    def clean_anticipated_end_date(self):
        data = self.cleaned_data['anticipated_end_date']
        return data

    def clean_special_considerations(self):
        data = self.cleaned_data['special_considerations']
        return data

    def clean(self):
        cleaned_data = super(OrderUpdateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Orders
        fields = (
            'requester_name',
            'project_name',
            'project_code',
            'project_geo_code',
            'charge_code',
            'award_number',
            'requisition_number',
            'donor',
            'description',
            'anticipated_award_mechanism',
            'anticipated_start_date',
            'anticipated_end_date',
            'special_considerations'
        )


class OrderProcurementForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    order_id = forms.CharField(
        label='Request Id',
        min_length=8,
        max_length=8,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
            }
        ))
    procurement_method = forms.ChoiceField(
        choices=Orders.DROPDOWN_PROCUREMENT_METHODS,
        initial='',
        label='Procurement Method',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-procurement-method',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))

    def clean_procurement_method(self):
        data = self.cleaned_data['procurement_method']
        return data

    def clean(self):
        cleaned_data = super(OrderProcurementForm, self).clean()
        return cleaned_data

    class Meta:
        model = Orders
        fields = (
            'order_id',
            'procurement_method',
        )


class OrderAssignmentForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    order_id = forms.CharField(
        label='Request Id',
        min_length=8,
        max_length=8,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
            }
        ))
    order_assigned_role = forms.ChoiceField(
        choices=(('', '--select--'),),
        initial='',
        label='Role',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-order-assign-role',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
                'onchange': 'onRoleSelected();',
            }
        ))
    order_assigned_id = forms.ChoiceField(
        choices=(('', '--select--'), ('0', 'NONE'),),
        initial='',
        label='Operator',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-order-assigned-id',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))

    def clean_order_assigned_role(self):
        data = self.cleaned_data['order_assigned_role']
        return data

    def clean_order_assigned_id(self):
        data = self.cleaned_data['order_assigned_id']
        return data

    def clean(self):
        cleaned_data = super(OrderAssignmentForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(OrderAssignmentForm, self).__init__(*args, **kwargs)

        OPERATOR_ROLES = (
            ('', '--select--'),
            (Operators.ROLE_PROCUREMENT_OFFICER, Operators.ROLE_PROCUREMENT_OFFICER),
            (Operators.ROLE_HR_MANAGER, Operators.ROLE_HR_MANAGER),
            (Operators.ROLE_STOCK_ADMIN, Operators.ROLE_STOCK_ADMIN),
            (Operators.ROLE_ACCOUNTANT_MANAGER, Operators.ROLE_ACCOUNTANT_MANAGER),
            (Operators.ROLE_ACCOUNTANT_OFFICER, Operators.ROLE_ACCOUNTANT_OFFICER),
        )

        self.fields['order_assigned_role'] = forms.ChoiceField(
            choices=OPERATOR_ROLES,
            initial='',
            label='Role',
            required=True,
            validators=[],
            widget=forms.Select(
                attrs={
                    'id': 'search-input-select-order-assign-role',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                    'onchange': 'onRoleSelected();',
                }
            ))

        OPERATORS = (('', '--select--'), ('0', 'NONE'),)
        operators = Operators.objects.all()
        for operator in operators:
            OPERATORS = OPERATORS + ((operator.operator_id, operator.operator_name),)

        self.fields['order_assigned_id'] = forms.ChoiceField(
            choices=OPERATORS,
            initial='',
            label='Operator',
            required=True,
            validators=[],
            widget=forms.Select(
                attrs={
                    'id': 'search-input-select-order-assigned-id',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                }
            ))

    class Meta:
        model = Orders
        fields = (
            'order_id',
            'order_assigned_role',
            'order_assigned_id',
        )


class OrderSupplierForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    order_id = forms.CharField(
        label='Request Id',
        min_length=8,
        max_length=8,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
            }
        ))
    order_supplier_category = forms.ChoiceField(
        choices=Orders.DROPDOWN_SUPPLIER_CATEGORIES,
        initial='',
        label='Vendor Category',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-supplier-category',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))

    def clean_order_supplier_category(self):
        data = self.cleaned_data['order_supplier_category']
        return data

    def clean(self):
        cleaned_data = super(OrderSupplierForm, self).clean()
        return cleaned_data

    class Meta:
        model = Orders
        fields = (
            'order_id',
            'order_supplier_category',
        )


class OrderEmailToSupplierForm(forms.ModelForm):
    order_email_to_supplier_subject = forms.CharField(
        label='Subject',
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

    order_email_to_supplier_message = forms.CharField(
        label='Message',
        required=True,
        widget=TinyMCE(
            attrs={
                'cols': 30,
                'rows': 10
            }
        )
    )

    def clean_order_email_to_supplier_subject(self):
        data = self.cleaned_data['order_email_to_supplier_subject']
        return data

    def clean_order_email_to_supplier_message(self):
        data = self.cleaned_data['order_email_to_supplier_message']
        return data

    def clean(self):
        cleaned_data = super(OrderEmailToSupplierForm, self).clean()
        return cleaned_data

    class Meta:
        model = Orders
        fields = (
            'order_email_to_supplier_subject',
            'order_email_to_supplier_message',
        )


class OrderUploadAttachmentForm(forms.ModelForm):
    order_attachment_file_path = forms.FileField(
        label='File',
        required=True,
        validators=[],
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'aria-label': 'form-label',
                'accept': '*/*',
                'style': "display: none;",
            }
        ))

    def clean_order_attachment_file_path(self):
        file = self.cleaned_data['order_attachment_file_path']

        if not file:
            raise forms.ValidationError('File type - none')

        try:
            assert isinstance(file,
                              InMemoryUploadedFile), "File rewrite has been only tested on in-memory upload backend"

            # Make sure the image is not too big, so that PIL trashes the server
            if file:
                if file.size > settings.MAX_FILE_UPLOAD_SIZE:
                    raise forms.ValidationError("File too large - the limit is 10 megabytes")

            filename = file.name
            temp_file_path = settings.MEDIA_ROOT + '/temp/' + filename
            default_storage.save(temp_file_path, ContentFile(file.read()))

            return filename

        except Exception as e:
            print('Exception: ' + str(e))
            raise forms.ValidationError('Exception: ' + str(e))

    def clean(self):
        cleaned_data = super(OrderUploadAttachmentForm, self).clean()
        return cleaned_data

    class Meta:
        model = Order_Attachments
        fields = (
            'order_attachment_file_path',
        )


class OrderPurchaseUpdateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    order_id = forms.CharField(
        label='Request Id',
        min_length=8,
        max_length=8,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
            }
        ))
    order_purchase_no = forms.CharField(
        label='Purchase Order No.',
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
    order_attachment_file_path = forms.FileField(
        label='File',
        required=True,
        validators=[],
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'aria-label': 'form-label',
                'accept': '*/*',
            }
        ))

    def clean_order_purchase_no(self):
        data = self.cleaned_data['order_purchase_no']
        return data

    def clean_order_attachment_file_path(self):
        file = self.cleaned_data['order_attachment_file_path']

        if not file:
            raise forms.ValidationError('File type - none')

        try:
            assert isinstance(file,
                              InMemoryUploadedFile), "File rewrite has been only tested on in-memory upload backend"

            # Make sure the image is not too big, so that PIL trashes the server
            if file:
                if file.size > settings.MAX_FILE_UPLOAD_SIZE:
                    raise forms.ValidationError("File too large - the limit is 10 megabytes")

            filename = file.name
            temp_file_path = settings.MEDIA_ROOT + '/temp/' + filename
            default_storage.save(temp_file_path, ContentFile(file.read()))

            return filename

        except Exception as e:
            print('Exception: ' + str(e))
            raise forms.ValidationError('Exception: ' + str(e))

    def clean(self):
        cleaned_data = super(OrderPurchaseUpdateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Orders
        fields = (
            'order_id',
            'order_purchase_no',
            'order_attachment_file_path',
        )


class OrderInvoiceUpdateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    order_id = forms.CharField(
        label='Request Id',
        min_length=8,
        max_length=8,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
                'readonly': True,
            }
        ))
    order_invoice_no = forms.CharField(
        label='Invoice No.',
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
    order_attachment_file_path = forms.FileField(
        label='File',
        required=True,
        validators=[],
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'aria-label': 'form-label',
                'accept': '*/*',
            }
        ))

    def clean_order_purchase_no(self):
        data = self.cleaned_data['order_purchase_no']
        return data

    def clean_order_attachment_file_path(self):
        file = self.cleaned_data['order_attachment_file_path']

        if not file:
            raise forms.ValidationError('File type - none')

        try:
            assert isinstance(file,
                              InMemoryUploadedFile), "File rewrite has been only tested on in-memory upload backend"

            # Make sure the image is not too big, so that PIL trashes the server
            if file:
                if file.size > settings.MAX_FILE_UPLOAD_SIZE:
                    raise forms.ValidationError("File too large - the limit is 10 megabytes")

            filename = file.name
            temp_file_path = settings.MEDIA_ROOT + '/temp/' + filename
            default_storage.save(temp_file_path, ContentFile(file.read()))

            return filename

        except Exception as e:
            print('Exception: ' + str(e))
            raise forms.ValidationError('Exception: ' + str(e))

    def clean(self):
        cleaned_data = super(OrderInvoiceUpdateForm, self).clean()
        return cleaned_data

    class Meta:
        model = Orders
        fields = (
            'order_id',
            'order_invoice_no',
            'order_attachment_file_path',
        )
