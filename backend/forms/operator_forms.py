# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from django.contrib.auth.hashers import check_password
from django.core.validators import ValidationError, MinLengthValidator, MaxLengthValidator, EmailValidator
from django.core.validators import validate_email, validate_integer

from app.data import ARRAY_GENDER
from app.models import Operators
from app.validators import IsPhoneNumberValidator


class OperatorSignUpForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        min_length=1,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(1), MaxLengthValidator(100)],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    email = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    password = forms.CharField(
        label='Password',
        min_length=8,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    repeat_password = forms.CharField(
        label='Repeat password',
        min_length=8,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    # captcha = ReCaptchaField(
    #     required=True,
    #     widget=ReCaptchaV2Checkbox(
    #         attrs={
    #             'data-theme': 'clean',
    #             'data-size': 'compact',
    #         }
    #     ))

    def clean_name(self):
        data = self.cleaned_data['name']
        # try:
        # except ValidationError:
        #     raise forms.ValidationError('Enter a valid name')
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            validate_email(data)
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address')
        try:
            operator = Operators.objects.get(operator_username=data)
        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
            operator = None
        if operator is not None:
            raise forms.ValidationError(u'Email Id: "%s" is already in use.' % data)
        else:
            return data

    def clean_password(self):
        password = self.cleaned_data['password']
        # check for min length
        min_length = 8
        if len(password) < min_length:
            msg = 'Password must be at least %s characters long.' % (str(min_length))
            self.add_error('password', msg)
        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password', msg)
        # check for uppercase letter
        if not any(c.isupper() for c in password):
            msg = 'Password must contain at least 1 uppercase letter.'
            self.add_error('password', msg)
        # check for lowercase letter
        if not any(c.islower() for c in password):
            msg = 'Password must contain at least 1 lowercase letter.'
            self.add_error('password', msg)
        return password

    def clean(self):
        cleaned_data = super(OperatorSignUpForm, self).clean()

        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        if password and repeat_password:
            if password != repeat_password:
                msg = 'Password doesn\'t match.'
                self.add_error('repeat_password', msg)
        return cleaned_data

    class Meta:
        model = Operators
        fields = (
            'name',
            'email',
            'password',
            'repeat_password',
        )


class OperatorSignInForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    password = forms.CharField(
        label='Password',
        min_length=8,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    # captcha = ReCaptchaField(
    #     required=False,
    #     widget=ReCaptchaV2Checkbox(
    #         attrs={
    #             'data-theme': 'clean',
    #             'data-size': 'compact',
    #         }
    #     ))

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            validate_email(data)
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address')
        try:
            operator = Operators.objects.get(operator_username=data)
        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
            operator = None
        if operator is None:
            raise forms.ValidationError(u'Email Id: "%s" is not yet registered.' % data)
        else:
            return data

    def clean_password(self):
        password = self.cleaned_data['password']
        # check for min length
        min_length = 8
        if len(password) < min_length:
            msg = 'Password must be at least %s characters long.' % (str(min_length))
            self.add_error('password', msg)
        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password', msg)
        # check for uppercase letter
        if not any(c.isupper() for c in password):
            msg = 'Password must contain at least 1 uppercase letter.'
            self.add_error('password', msg)
        # check for lowercase letter
        if not any(c.islower() for c in password):
            msg = 'Password must contain at least 1 lowercase letter.'
            self.add_error('password', msg)
        return password

    class Meta:
        model = Operators
        fields = (
            'email',
            'password',
        )


class OperatorForgotPasswordForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    # captcha = ReCaptchaField(
    #     required=False,
    #     widget=ReCaptchaV2Checkbox(
    #         attrs={
    #             'data-theme': 'clean',
    #             'data-size': 'compact',
    #         }
    #     ))

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            validate_email(data)
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address')
        try:
            operator = Operators.objects.get(operator_username=data)
        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
            operator = None
        if operator is None:
            raise forms.ValidationError(u'Email Id: "%s" is not yet registered.' % data)
        else:
            return data

    class Meta:
        model = Operators
        fields = (
            'email',
        )


class OperatorResetPasswordForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        disabled=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    password = forms.CharField(
        label='Password',
        min_length=8,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    repeat_password = forms.CharField(
        label='Repeat password',
        min_length=8,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            validate_email(data)
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address')
        return data

    def clean_password(self):
        password = self.cleaned_data['password']
        # check for min length
        min_length = 8
        if len(password) < min_length:
            msg = 'Password must be at least %s characters long.' % (str(min_length))
            self.add_error('password', msg)
        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password', msg)
        # check for uppercase letter
        if not any(c.isupper() for c in password):
            msg = 'Password must contain at least 1 uppercase letter.'
            self.add_error('password', msg)
        # check for lowercase letter
        if not any(c.islower() for c in password):
            msg = 'Password must contain at least 1 lowercase letter.'
            self.add_error('password', msg)
        return password

    def clean(self):
        cleaned_data = super(OperatorResetPasswordForm, self).clean()

        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        if password and repeat_password:
            if password != repeat_password:
                msg = 'Password doesn\'t match.'
                self.add_error('repeat_password', msg)
        return cleaned_data

    class Meta:
        model = Operators
        fields = (
            'email',
            'password',
            'repeat_password',
        )


class OperatorSearchIndexForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=ARRAY_GENDER,
        initial='',
        label='Gender',
        required=False,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-gender',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))

    def clean_gender(self):
        data = self.cleaned_data['gender']
        return data

    def clean(self):
        cleaned_data = super(OperatorSearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Operators
        fields = (
            'gender',
        )


class OperatorCreateForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
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
    type = forms.ChoiceField(
        choices=Operators.OPERATOR_TYPES,
        initial='',
        label='Type',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-type',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    department = forms.ChoiceField(
        choices=Operators.OPERATOR_DEPARTMENTS,
        initial='',
        label='Department',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-department',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
                'onchange': 'onDepartmentSelected();',
            }
        ))
    role = forms.ChoiceField(
        choices=Operators.OPERATOR_ROLES,
        initial='',
        label='Role',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-role',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
                'onchange': 'onRoleSelected();',
            }
        ))
    parent_id = forms.ChoiceField(
        choices=(('', '--select--'), ('0', 'NONE'),),
        initial='',
        label='Head Staff',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-parent-id',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    email = forms.EmailField(
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
    password = forms.CharField(
        label='Password',
        min_length=8,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    repeat_password = forms.CharField(
        label='Repeat password',
        min_length=8,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    def clean_name(self):
        data = self.cleaned_data['name']
        # try:
        # except ValidationError:
        #     raise forms.ValidationError('Enter a valid name')
        return data

    def clean_type(self):
        data = self.cleaned_data['type']
        return data

    def clean_department(self):
        data = self.cleaned_data['department']
        return data

    def clean_role(self):
        data = self.cleaned_data['role']
        return data

    def clean_parent_id(self):
        data = self.cleaned_data['parent_id']
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            validate_email(data)
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address')
        try:
            operator = Operators.objects.get(operator_username=data)
        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
            operator = None
        if operator is not None:
            raise forms.ValidationError(u'Email Id: "%s" is already in use.' % data)
        else:
            return data

    def clean_password(self):
        password = self.cleaned_data['password']
        # check for min length
        min_length = 8
        if len(password) < min_length:
            msg = 'Password must be at least %s characters long.' % (str(min_length))
            self.add_error('password', msg)
        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password', msg)
        # check for uppercase letter
        if not any(c.isupper() for c in password):
            msg = 'Password must contain at least 1 uppercase letter.'
            self.add_error('password', msg)
        # check for lowercase letter
        if not any(c.islower() for c in password):
            msg = 'Password must contain at least 1 lowercase letter.'
            self.add_error('password', msg)
        return password

    def clean(self):
        cleaned_data = super(OperatorCreateForm, self).clean()

        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        if password and repeat_password:
            if password != repeat_password:
                msg = 'Password doesn\'t match.'
                self.add_error('repeat_password', msg)
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(OperatorCreateForm, self).__init__(*args, **kwargs)

        OPERATORS = (('', '--select--'), ('0', 'NONE'),)
        operators = Operators.objects.all()
        for operator in operators:
            OPERATORS = OPERATORS + ((operator.operator_id, operator.operator_name),)

        self.fields['parent_id'] = forms.ChoiceField(
            choices=OPERATORS,
            initial='',
            label='Head Staff',
            required=True,
            validators=[],
            widget=forms.Select(
                attrs={
                    'id': 'search-input-select-parent-id',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                }
            ))

    class Meta:
        model = Operators
        fields = (
            'name',
            'type',
            'department',
            'role',
            'email',
            'password',
            'repeat_password'
        )


class OperatorUpdateForm(forms.ModelForm):
    email = forms.EmailField(
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
            }
        ))
    name = forms.CharField(
        label='Name',
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
    type = forms.ChoiceField(
        choices=Operators.OPERATOR_TYPES,
        initial='',
        label='Type',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-type',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    department = forms.ChoiceField(
        choices=Operators.OPERATOR_DEPARTMENTS,
        initial='',
        label='Department',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-department',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
                'onchange': 'onDepartmentSelected();',
            }
        ))
    role = forms.ChoiceField(
        choices=Operators.OPERATOR_ROLES,
        initial='',
        label='Role',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-role',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
                'onchange': 'onRoleSelected();',
            }
        ))
    parent_id = forms.ChoiceField(
        choices=(('', '--select--'), ('0', 'NONE'),),
        initial='',
        label='Head Staff',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-parent-id',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    gender = forms.ChoiceField(
        choices=ARRAY_GENDER,
        initial='',
        label='Gender',
        required=False,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-gender',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    phone_number = forms.CharField(
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

    def clean_name(self):
        data = self.cleaned_data['name']
        # try:
        # except ValidationError:
        #     raise forms.ValidationError('Enter a valid name')
        return data

    def clean_type(self):
        data = self.cleaned_data['type']
        return data

    def clean_department(self):
        data = self.cleaned_data['department']
        return data

    def clean_role(self):
        data = self.cleaned_data['role']
        return data

    def clean_parent_id(self):
        data = self.cleaned_data['parent_id']
        return data

    def clean_gender(self):
        data = self.cleaned_data['gender']
        return data

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        if data != '':
            try:
                validate_integer(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid phone number')
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            validate_email(data)
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address')
        try:
            operator = Operators.objects.get(operator_username=data)
        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
            operator = None
        if operator is None:
            raise forms.ValidationError(u'Email Id: "%s" does not exist.' % data)
        else:
            return data

    def clean(self):
        cleaned_data = super(OperatorUpdateForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(OperatorUpdateForm, self).__init__(*args, **kwargs)

        OPERATORS = (('', '--select--'), ('0', 'NONE'),)
        operators = Operators.objects.all()
        for operator in operators:
            OPERATORS = OPERATORS + ((operator.operator_id, operator.operator_name),)

        self.fields['parent_id'] = forms.ChoiceField(
            choices=OPERATORS,
            initial='',
            label='Head Staff',
            required=True,
            validators=[],
            widget=forms.Select(
                attrs={
                    'id': 'search-input-select-parent-id',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                }
            ))

    class Meta:
        model = Operators
        fields = (
            'email',
            'name',
            'department',
            'role',
            'parent_id',
            'gender',
            'phone_number',
        )


class SuperOperatorUpdateForm(forms.ModelForm):
    email = forms.EmailField(
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
            }
        ))
    name = forms.CharField(
        label='Name',
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
    type = forms.ChoiceField(
        choices=Operators.SUPER_OPERATOR_TYPES,
        initial='',
        label='Type',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-type',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    department = forms.ChoiceField(
        choices=Operators.OPERATOR_DEPARTMENTS,
        initial='',
        label='Department',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-department',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
                'onchange': 'onDepartmentSelected();',
            }
        ))
    role = forms.ChoiceField(
        choices=Operators.OPERATOR_ROLES,
        initial='',
        label='Role',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-role',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
                'onchange': 'onRoleSelected();',
            }
        ))
    parent_id = forms.ChoiceField(
        choices=(('', '--select--'), ('0', 'NONE'),),
        initial='',
        label='Head Staff',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-parent-id',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    gender = forms.ChoiceField(
        choices=ARRAY_GENDER,
        initial='',
        label='Gender',
        required=False,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-gender',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    phone_number = forms.CharField(
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

    def clean_name(self):
        data = self.cleaned_data['name']
        # try:
        # except ValidationError:
        #     raise forms.ValidationError('Enter a valid name')
        return data

    def clean_type(self):
        data = self.cleaned_data['type']
        return data

    def clean_department(self):
        data = self.cleaned_data['department']
        return data

    def clean_role(self):
        data = self.cleaned_data['role']
        return data

    def clean_parent_id(self):
        data = self.cleaned_data['parent_id']
        return data

    def clean_gender(self):
        data = self.cleaned_data['gender']
        return data

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        if data != '':
            try:
                validate_integer(data)
            except ValidationError:
                raise forms.ValidationError('Enter a valid phone number')
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            validate_email(data)
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address')
        try:
            operator = Operators.objects.get(operator_username=data)
        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
            operator = None
        if operator is None:
            raise forms.ValidationError(u'Email Id: "%s" does not exist.' % data)
        else:
            return data

    def clean(self):
        cleaned_data = super(SuperOperatorUpdateForm, self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(SuperOperatorUpdateForm, self).__init__(*args, **kwargs)

        OPERATORS = (('', '--select--'), ('0', 'NONE'),)
        operators = Operators.objects.all()
        for operator in operators:
            OPERATORS = OPERATORS + ((operator.operator_id, operator.operator_name),)

        self.fields['parent_id'] = forms.ChoiceField(
            choices=OPERATORS,
            initial='',
            label='Head Staff',
            required=True,
            validators=[],
            widget=forms.Select(
                attrs={
                    'id': 'search-input-select-parent-id',
                    'class': 'form-control',
                    'style': 'width:100%;',
                    'placeholder': '--select--',
                    'aria-label': 'form-label',
                }
            ))

    class Meta:
        model = Operators
        fields = (
            'email',
            'name',
            'department',
            'role',
            'parent_id',
            'gender',
            'phone_number',
        )


class OperatorUpdateProfileForm(forms.ModelForm):
    email = forms.EmailField(
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
            }
        ))
    name = forms.CharField(
        label='Name',
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
    department = forms.ChoiceField(
        choices=Operators.OPERATOR_DEPARTMENTS,
        initial='',
        label='Department',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-department',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
                'readonly': True,
            }
        ))
    role = forms.ChoiceField(
        choices=Operators.OPERATOR_ROLES,
        initial='',
        label='Role',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-role',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
                'readonly': True,
            }
        ))
    gender = forms.ChoiceField(
        choices=ARRAY_GENDER,
        initial='',
        label='Gender',
        required=True,
        validators=[],
        widget=forms.Select(
            attrs={
                'id': 'search-input-select-gender',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': '--select--',
                'aria-label': 'form-label',
            }
        ))
    phone_number = forms.CharField(
        label='Phone Number',
        min_length=9,
        max_length=17,
        validators=[MinLengthValidator(9), MaxLengthValidator(17), IsPhoneNumberValidator],
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'tel',
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    def clean_name(self):
        data = self.cleaned_data['name']
        # try:
        # except ValidationError:
        #     raise forms.ValidationError('Enter a valid name')
        return data

    def clean_department(self):
        data = self.cleaned_data['department']
        return data

    def clean_role(self):
        data = self.cleaned_data['role']
        return data

    def clean_gender(self):
        data = self.cleaned_data['gender']
        return data

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            validate_email(data)
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address')
        try:
            operator = Operators.objects.get(operator_username=data)
        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
            operator = None
        if operator is None:
            raise forms.ValidationError(u'Email Id: "%s" does not exist.' % data)
        else:
            return data

    def clean(self):
        cleaned_data = super(OperatorUpdateProfileForm, self).clean()
        return cleaned_data

    class Meta:
        model = Operators
        fields = (
            'email',
            'name',
            'department',
            'role',
            'gender',
            'phone_number',
        )


class OperatorChangePasswordForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email Id',
        min_length=5,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(5), MaxLengthValidator(100), EmailValidator],
        disabled=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    password = forms.CharField(
        label='Current Password',
        min_length=8,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    new_password = forms.CharField(
        label='New Password',
        min_length=8,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))
    repeat_password = forms.CharField(
        label='Repeat password',
        min_length=8,
        max_length=100,
        required=True,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'font-weight:bold',
                'placeholder': '',
                'autocomplete': 'off',
                'aria-label': 'form-label',
            }
        ))

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            validate_email(data)
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address')
        return data

    def clean_password(self):
        password = self.cleaned_data['password']
        # check for min length
        min_length = 8
        if len(password) < min_length:
            msg = 'Password must be at least %s characters long.' % (str(min_length))
            self.add_error('password', msg)
        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password', msg)
        # check for uppercase letter
        if not any(c.isupper() for c in password):
            msg = 'Password must contain at least 1 uppercase letter.'
            self.add_error('password', msg)
        # check for lowercase letter
        if not any(c.islower() for c in password):
            msg = 'Password must contain at least 1 lowercase letter.'
            self.add_error('password', msg)

        email = self.cleaned_data['email']
        try:
            operator = Operators.objects.get(operator_username=email)
        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
            operator = None
        if operator is None:
            raise forms.ValidationError('Incorrect current password')
        else:
            if not check_password(password, operator.operator_password_hash):
                raise forms.ValidationError('Incorrect current password')
            else:
                return password

    def clean_new_password(self):
        new_password = self.cleaned_data['new_password']
        # check for min length
        min_length = 8
        if len(new_password) < min_length:
            msg = 'Password must be at least %s characters long.' % (str(min_length))
            self.add_error('new_password', msg)
        # check for digit
        if sum(c.isdigit() for c in new_password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('new_password', msg)
        # check for uppercase letter
        if not any(c.isupper() for c in new_password):
            msg = 'Password must contain at least 1 uppercase letter.'
            self.add_error('new_password', msg)
        # check for lowercase letter
        if not any(c.islower() for c in new_password):
            msg = 'Password must contain at least 1 lowercase letter.'
            self.add_error('new_password', msg)
        return new_password

    def clean(self):
        cleaned_data = super(OperatorChangePasswordForm, self).clean()

        new_password = cleaned_data.get('new_password')
        repeat_password = cleaned_data.get('repeat_password')
        if new_password and repeat_password:
            if new_password != repeat_password:
                msg = 'Password doesn\'t match.'
                self.add_error('repeat_password', msg)
        return cleaned_data

    class Meta:
        model = Operators
        fields = (
            'email',
            'password',
            'new_password',
            'repeat_password',
        )
