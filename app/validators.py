from django.core.validators import RegexValidator

'''
This regex assumes that you have a clean string,
you should clean the string for spaces and other characters
'''

IsAlphaNumericWithSpaceValidator = \
    RegexValidator(
        '^[A-Za-z0-9 ]+$',
        message='Alphanumeric and space characters only.',
        code='Invalid value'
    )

IsAlphaWithSpaceValidator = \
    RegexValidator(
        '^[A-Za-z ]+$',
        message='Alphabets and space characters only.',
        code='Invalid value'
    )

IsAlphaNumericValidator = \
    RegexValidator(
        '^[A-Za-z0-9]+$',
        message='Alphanumeric characters only.',
        code='Invalid value'
    )

IsAlphaNumericWithHyphenDotValidator = \
    RegexValidator(
        '^[A-Za-z0-9.-]+$',
        message='Alphanumeric, dot and hyphen characters only.',
        code='Invalid value'
    )

IsNumericValidator = \
    RegexValidator(
        '^[A-Za-z0-9]+$',
        message='Alphanumeric characters only.',
        code='Invalid value'
    )

IsPhoneNumberValidator = \
    RegexValidator(
        '^[0-9+]+$',
        message='Numeric characters only.',
        code='Invalid value'
    )

IsNameValidator = \
    RegexValidator(
        '^[A-Za-z0-9 ,.\'-]+$',
        message='Alphanumeric characters only.',
        code='Invalid value'
    )

IsDataValidator = \
    RegexValidator(
        '^[A-Za-z0-9-!$%^&*()_+|~={}[:;<>?,.@#\\\'\" ]+$',
        message='Alphanumeric characters only.',
        code='Invalid value'
    )
