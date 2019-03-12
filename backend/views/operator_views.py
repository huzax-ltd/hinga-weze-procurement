import requests
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from app import settings
from app.models import Operators, Operator_Logs, Failed_Login, Access_Permissions, Operator_Access_Permissions
from app.utils import Utils
from backend.forms.operator_forms import OperatorSignUpForm, OperatorSignInForm, OperatorForgotPasswordForm, \
    OperatorResetPasswordForm, OperatorSearchIndexForm, OperatorCreateForm, OperatorUpdateForm, \
    OperatorChangePasswordForm
from backend.tables.operator_tables import OperatorsTable


def signup(request):
    return HttpResponseForbidden('Forbidden', content_type='text/plain')
    template_url = 'operators/signup.html'
    if request.method == 'POST':

        form = OperatorSignUpForm(request.POST)

        # validating recaptcha
        request.recaptcha_is_valid = None
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if not result['success']:
            request.recaptcha_is_valid = False
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return render(request, template_url, {'form': form})

        # noinspection PyArgumentList
        if form.is_valid():
            model = Operators()
            model.operator_type = Operators.TYPE_OTHER
            model.operator_username = form.cleaned_data['email']

            # generate operator auth token which
            model.operator_auth_key = Operators.generate_unique_token(Operators, 'operator_auth_key')

            model.operator_password_hash = make_password(form.cleaned_data['password'])
            model.operator_password_reset_token = ''
            model.operator_name = form.cleaned_data['name']
            model.operator_gender = ''
            model.operator_contact_phone_number = ''
            model.operator_contact_email_id = form.cleaned_data['email']
            model.operator_profile_photo_file_path = ''
            model.operator_created_at = Utils.get_current_datetime_utc()
            model.operator_created_by = form.cleaned_data['email']
            model.operator_updated_at = Utils.get_current_datetime_utc()
            model.operator_updated_by = form.cleaned_data['email']
            model.operator_status = Operators.STATUS_UNVERIFIED
            # noinspection PyCallByClass,PyTypeChecker
            model.save('Created')

            Operator_Logs.add(
                model.operator_id,
                model.operator_username,
                model.operator_name,
                'Created ' + Operators.SINGULAR_TITLE,
                Utils.get_browser_details_from_request(request),
                Utils.get_ip_address(request),
                model.operator_username,
            )

            # sending email confirmation mail
            if settings.IS_LOCAL:
                domain = settings.BACKEND_DOMAIN_LOCAL
            else:
                domain = settings.BACKEND_DOMAIN_PROD
            contact_url = '{domain}/{path}'.format(domain=domain, path=settings.CONTACT_URL)
            confirm_url = '{domain}/{path}'.format(
                domain=domain,
                path='operators/signup/confirm/' + model.operator_auth_key
            )
            html_content = render_to_string(
                'email/email-confirmation.html',
                {
                    'name': model.operator_name,
                    'contact_url': contact_url,
                    'confirm_url': confirm_url,
                }
            )
            send_mail(
                settings.EMAIL_VERIFICATION_SUBJECT,
                settings.EMAIL_VERIFICATION_MESSAGE,
                settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                [model.operator_username],
                fail_silently=False,
                html_message=html_content,
            )

            messages.info(request, 'An email has been sent for verification to your registered email address.')
            form = OperatorSignUpForm()
            return render(request, template_url, {'form': form})
        else:
            return render(request, template_url, {'form': form})
    else:
        form = OperatorSignUpForm()

    return render(request, template_url, {'form': form})


# noinspection PyUnusedLocal
def confirm(request, token):
    try:
        operator = Operators.objects.get(operator_auth_key=token)
    except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
        operator = None
    if operator is not None:

        model = operator

        model.operator_updated_at = Utils.get_current_datetime_utc()
        model.operator_updated_by = operator.operator_username
        model.operator_status = Operators.STATUS_UNAPPROVED
        model.save()

        messages.info(request, 'Thank you for your email confirmation. Now you can login to your account.')
        return redirect(reverse("operators_signin"))
    else:
        messages.info(request, 'Invalid token.')
        return redirect(reverse("operators_signin"))


def signin(request):
    template_url = 'operators/signin.html'

    failed_count = Failed_Login.objects.filter(failed_login_from=Failed_Login.FAILED_LOGIN_FROM_BACKEND,
                                               failed_login_ip_address=Utils.get_ip_address(request),
                                               failed_login_status=False).count()

    display_captcha = False
    if failed_count >= settings.MAX_LOGIN_ATTEMPTS_CAPTCHA:
        display_captcha = True

    if request.method == 'POST':
        form = OperatorSignInForm(request.POST)

        if display_captcha:
            request.recaptcha_is_valid = None
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            if not result['success']:
                request.recaptcha_is_valid = False
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return render(request, template_url,
                              {'form': form, 'display_captcha': display_captcha})

        if form.is_valid():
            try:
                operator = Operators.objects.get(operator_username=form.cleaned_data['email'])
            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                operator = None
            if operator is None:
                Failed_Login.add(form.cleaned_data['email'], form.cleaned_data['password'],
                                 Failed_Login.FAILED_LOGIN_FROM_BACKEND,
                                 Utils.get_ip_address(request),
                                 False)
                messages.error(request, 'Incorrect email address or password3.')
                return render(request, template_url,
                              {'form': form, 'display_captcha': display_captcha})
            else:

                model = operator

                if model.operator_status == Operators.STATUS_UNVERIFIED:
                    # sending email confirmation mail
                    if settings.IS_LOCAL:
                        domain = settings.BACKEND_DOMAIN_LOCAL
                    else:
                        domain = settings.BACKEND_DOMAIN_PROD
                    contact_url = '{domain}/{path}'.format(domain=domain, path=settings.CONTACT_URL)
                    confirm_url = '{domain}/{path}'.format(
                        domain=domain,
                        path='operators/signup/confirm/' + model.operator_auth_key
                    )
                    html_content = render_to_string(
                        'email/email-confirmation.html',
                        {
                            'name': model.operator_name,
                            'contact_url': contact_url,
                            'confirm_url': confirm_url,
                        }
                    )
                    send_mail(
                        settings.EMAIL_VERIFICATION_SUBJECT,
                        settings.EMAIL_VERIFICATION_MESSAGE,
                        settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                        [model.operator_username],
                        fail_silently=False,
                        html_message=html_content,
                    )
                    messages.error(request,
                                   'Your email address is not yet verified. Please check your mail to confirm.')
                    return render(request, template_url,
                                  {'form': form, 'display_captcha': display_captcha})
                elif model.operator_status == Operators.STATUS_UNAPPROVED:
                    messages.error(request, 'Your account is not yet approved. Please contact admin for support.')
                    return render(request, template_url,
                                  {'form': form, 'display_captcha': display_captcha})
                elif model.operator_status == Operators.STATUS_BLOCKED:
                    messages.error(request, 'Your account is blocked. Please contact admin for support.')
                    return render(request, template_url,
                                  {'form': form, 'display_captcha': display_captcha})
                elif check_password(form.cleaned_data['password'], model.operator_password_hash):

                    model.operator_updated_at = Utils.get_current_datetime_utc()
                    model.operator_updated_by = operator.operator_username
                    model.operator_status = Operators.STATUS_ACTIVE
                    model.save()

                    Operators.login(request, model)

                    Operator_Logs.add(
                        model.operator_id,
                        model.operator_username,
                        model.operator_name,
                        Operators.SINGULAR_TITLE + ' Login',
                        Utils.get_browser_details_from_request(request),
                        Utils.get_ip_address(request),
                        operator.operator_username,
                    )

                    Failed_Login.objects.filter(failed_login_from=Failed_Login.FAILED_LOGIN_FROM_BACKEND,
                                                failed_login_ip_address=Utils.get_ip_address(request),
                                                failed_login_status=False).update(failed_login_status=True)

                    redirect_field_name = Operators.get_redirect_field_name(request)
                    if redirect_field_name is None:
                        return redirect(reverse("operators_dashboard"))
                    else:
                        return redirect(redirect_field_name)

                else:
                    Failed_Login.add(form.cleaned_data['email'], form.cleaned_data['password'],
                                     Failed_Login.FAILED_LOGIN_FROM_BACKEND,
                                     Utils.get_ip_address(request),
                                     False)
                    messages.error(request, 'Incorrect email address or password.')
                    return render(request, template_url,
                                  {'form': form, 'display_captcha': display_captcha})
        else:
            return render(request, template_url, {'form': form, 'display_captcha': display_captcha})
    else:
        form = OperatorSignInForm()
        for key, value in request.session.items():
            print('{} => {}'.format(key, value))

    return render(request, template_url, {'form': form, 'display_captcha': display_captcha})


def forgot_password(request):
    template_url = 'operators/forgot-password.html'
    if request.method == 'POST':
        form = OperatorForgotPasswordForm(request.POST)

        request.recaptcha_is_valid = None
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if not result['success']:
            request.recaptcha_is_valid = False
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return render(request, template_url,
                          {'form': form})

        if form.is_valid():
            try:
                operator = Operators.objects.get(operator_username=form.cleaned_data['email'])
            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                operator = None
            if operator is None:
                messages.error(request, 'Email Id: "%s" is not yet registered.' % form.cleaned_data['email'])
                return render(request, template_url,
                              {'form': form})
            else:
                model = operator

                if model.operator_status == Operators.STATUS_UNVERIFIED:
                    # sending email confirmation mail
                    if settings.IS_LOCAL:
                        domain = settings.BACKEND_DOMAIN_LOCAL
                    else:
                        domain = settings.BACKEND_DOMAIN_PROD
                    contact_url = '{domain}/{path}'.format(domain=domain, path=settings.CONTACT_URL)
                    confirm_url = '{domain}/{path}'.format(
                        domain=domain,
                        path='operators/signup/confirm/' + model.operator_auth_key
                    )
                    html_content = render_to_string(
                        'email/email-confirmation.html',
                        {
                            'name': model.operator_name,
                            'contact_url': contact_url,
                            'confirm_url': confirm_url,
                        }
                    )
                    send_mail(
                        settings.EMAIL_VERIFICATION_SUBJECT,
                        settings.EMAIL_VERIFICATION_MESSAGE,
                        settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                        [model.operator_username],
                        fail_silently=False,
                        html_message=html_content,
                    )
                    messages.error(request,
                                   'Your email address is not yet verified. Please check your mail to confirm.')
                    return render(request, template_url,
                                  {'form': form})
                elif model.operator_status == Operators.STATUS_UNAPPROVED:
                    messages.error(request, 'Your email address is not yet approved. Please contact admin for support.')
                    return render(request, template_url,
                                  {'form': form})
                elif model.operator_status == Operators.STATUS_BLOCKED:
                    messages.error(request, 'Your account is blocked. Please contact admin for support.')
                    return render(request, template_url,
                                  {'form': form})
                else:
                    model.operator_password_reset_token = Operators.generate_unique_token(Operators,
                                                                                          'operator_password_reset_token')
                    model.save()

                    Operator_Logs.add(
                        model.operator_id,
                        model.operator_username,
                        model.operator_name,
                        Operators.SINGULAR_TITLE + ' Forgot Password',
                        Utils.get_browser_details_from_request(request),
                        Utils.get_ip_address(request),
                        operator.operator_username,
                    )

                    # sending password reset token mail
                    if settings.IS_LOCAL:
                        domain = settings.BACKEND_DOMAIN_LOCAL
                    else:
                        domain = settings.BACKEND_DOMAIN_PROD
                    contact_url = '{domain}/{path}'.format(domain=domain, path=settings.CONTACT_URL)
                    reset_url = '{domain}/{path}'.format(
                        domain=domain,
                        path='operators/reset-password/' + model.operator_password_reset_token
                    )
                    html_content = render_to_string(
                        'email/email-reset-password.html',
                        {
                            'name': model.operator_name,
                            'contact_url': contact_url,
                            'reset_url': reset_url,
                        }
                    )
                    send_mail(
                        settings.EMAIL_PASSWORD_RESET_SUBJECT,
                        settings.EMAIL_PASSWORD_RESET_MESSAGE,
                        settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                        [model.operator_username],
                        fail_silently=False,
                        html_message=html_content,
                    )

                    messages.info(request, 'An email has been sent to reset your password.')
                    form = OperatorForgotPasswordForm()
                    return render(request, template_url, {'form': form})

    else:
        form = OperatorForgotPasswordForm()
        return render(request, template_url, {'form': form})


def reset_password(request, token):
    template_url = 'operators/reset-password.html'
    try:
        operator = Operators.objects.get(operator_password_reset_token=token)
    except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
        operator = None
    if operator is not None:
        model = operator

        if request.method == 'POST':
            form = OperatorResetPasswordForm(request.POST)
            form.fields["email"].initial = model.operator_username

            # noinspection PyArgumentList
            if form.is_valid():

                model.operator_password_hash = make_password(form.cleaned_data['password'])
                model.operator_password_reset_token = ''

                model.operator_updated_at = Utils.get_current_datetime_utc()
                model.operator_updated_by = operator.operator_username
                model.save()

                Operator_Logs.add(
                    model.operator_id,
                    model.operator_username,
                    model.operator_name,
                    Operators.SINGULAR_TITLE + ' Reset Password',
                    Utils.get_browser_details_from_request(request),
                    Utils.get_ip_address(request),
                    operator.operator_username,
                )

                # sending password reset message mail
                if settings.IS_LOCAL:
                    domain = settings.BACKEND_DOMAIN_LOCAL
                else:
                    domain = settings.BACKEND_DOMAIN_PROD
                contact_url = '{domain}/{path}'.format(domain=domain, path=settings.CONTACT_URL)
                html_content = render_to_string(
                    'email/email-info.html',
                    {
                        'name': model.operator_name,
                        'message': 'Your password has been reset successfully.',
                        'contact_url': contact_url,
                    }
                )
                send_mail(
                    settings.EMAIL_NOTIFICATION_SUBJECT,
                    settings.EMAIL_NOTIFICATION_MESSAGE,
                    settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                    [model.operator_username],
                    fail_silently=False,
                    html_message=html_content,
                )

                messages.info(request, 'Your password has been reset successfully.')
                return redirect(reverse("operators_signin"))
            else:
                form.fields["email"].initial = model.operator_username
                return render(request, template_url, {'form': form})
        else:
            form = OperatorResetPasswordForm()
            form.fields["email"].initial = model.operator_username

        return render(request, template_url, {'form': form})
    else:
        messages.info(request, 'Invalid token.')
        return redirect(reverse("operators_signin"))


# noinspection PyUnusedLocal
def signout(request):
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        model = operator

        # update logout status
        model.operator_updated_at = Utils.get_current_datetime_utc()
        model.operator_updated_by = operator.operator_username
        model.operator_status = Operators.STATUS_INACTIVE
        model.save()

        # logout
        Operators.logout(request)

        # update log
        Operator_Logs.add(
            model.operator_id,
            model.operator_username,
            model.operator_name,
            Operators.SINGULAR_TITLE + ' Logout',
            Utils.get_browser_details_from_request(request),
            Utils.get_ip_address(request),
            operator.operator_username,
        )

        return redirect(reverse("operators_signin"))


# noinspection PyUnusedLocal
def dashboard(request):
    template_url = 'operators/dashboard.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        return render(
            request, template_url,
            {
                'section': settings.BACKEND_SECTION_DASHBOARD,
                'title': 'Dashboard',
                'name': 'dashboard',
                'operator': operator,
                'auth_permissions': auth_permissions,
                'operators': Operators.objects.all().count(),
            }
        )


# noinspection PyUnusedLocal
def json_operators(request):
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_OPERATOR_VIEW in auth_permissions.values():
            return HttpResponse(serializers.serialize("json", Operators.objects.all()),
                                content_type="application/json")
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal
def index(request):
    template_url = 'operators/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_OPERATOR_VIEW in auth_permissions.values():
            search_form = OperatorSearchIndexForm(request.POST or None)
            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                objects = Operators.objects.order_by('operator_name').all()
                gender = search_form.cleaned_data['gender']
                if gender != '':
                    objects = objects.filter(operator_gender=gender)

                table = OperatorsTable(objects)
            else:
                display_search = False
                table = OperatorsTable(Operators.objects.order_by('operator_name').all())

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_OPERATORS,
                    'title': Operators.TITLE,
                    'name': Operators.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'search_form': search_form,
                    'display_search': display_search,
                    'index_url': reverse("operators_index"),
                    'multiple_select_url': reverse("operators_multiple_select"),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


@csrf_exempt
# noinspection PyUnusedLocal
def single_select(request):
    if request.is_ajax():
        operator = Operators.login_required(request)
        if operator is None:
            # Operators.set_redirect_field_name(request, request.path)
            # return redirect(reverse("operators_signin"))
            return HttpResponse('signin', content_type='text/plain')
        else:
            auth_permissions = Operators.get_auth_permissions(operator)
            action = request.POST['action']
            id = request.POST['id']
            if action != '' and id is not None:
                if action == 'verify':
                    if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
                        try:
                            model = Operators.objects.get(operator_id=id)
                            if model.operator_status == Operators.STATUS_UNVERIFIED:
                                model.operator_status = Operators.STATUS_UNAPPROVED
                                model.operator_updated_at = Utils.get_current_datetime_utc()
                                model.operator_updated_by = operator.operator_username
                                model.save()
                                Operator_Logs.add(
                                    model.operator_id,
                                    model.operator_username,
                                    model.operator_name,
                                    'Verified ' + Operators.SINGULAR_TITLE,
                                    Utils.get_browser_details_from_request(request),
                                    Utils.get_ip_address(request),
                                    operator.operator_username,
                                )
                                messages.success(request, 'Verified successfully.')
                        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                if action == 'approve':
                    if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
                        try:
                            model = Operators.objects.get(operator_id=id)
                            if model.operator_status == Operators.STATUS_UNAPPROVED:
                                model.operator_status = Operators.STATUS_INACTIVE
                                model.operator_updated_at = Utils.get_current_datetime_utc()
                                model.operator_updated_by = operator.operator_username
                                model.save()
                                Operator_Logs.add(
                                    model.operator_id,
                                    model.operator_username,
                                    model.operator_name,
                                    'Approved ' + Operators.SINGULAR_TITLE,
                                    Utils.get_browser_details_from_request(request),
                                    Utils.get_ip_address(request),
                                    operator.operator_username,
                                )
                                messages.success(request, 'Approved successfully.')
                        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                if action == 'block':
                    if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
                        try:
                            model = Operators.objects.get(operator_id=id)
                            if model.operator_status == Operators.STATUS_ACTIVE or model.operator_status == Operators.STATUS_INACTIVE:
                                model.operator_status = Operators.STATUS_BLOCKED
                                model.operator_updated_at = Utils.get_current_datetime_utc()
                                model.operator_updated_by = operator.operator_username
                                model.save()
                                Operator_Logs.add(
                                    model.operator_id,
                                    model.operator_username,
                                    model.operator_name,
                                    'Blocked ' + Operators.SINGULAR_TITLE,
                                    Utils.get_browser_details_from_request(request),
                                    Utils.get_ip_address(request),
                                    operator.operator_username,
                                )
                                messages.success(request, 'Blocked successfully.')
                        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                if action == 'unblock':
                    if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
                        try:
                            model = Operators.objects.get(operator_id=id)
                            if model.operator_status == Operators.STATUS_BLOCKED:
                                model.operator_status = Operators.STATUS_INACTIVE
                                model.operator_updated_at = Utils.get_current_datetime_utc()
                                model.operator_updated_by = operator.operator_username
                                model.save()
                                Operator_Logs.add(
                                    model.operator_id,
                                    model.operator_username,
                                    model.operator_name,
                                    'Unblocked ' + Operators.SINGULAR_TITLE,
                                    Utils.get_browser_details_from_request(request),
                                    Utils.get_ip_address(request),
                                    operator.operator_username,
                                )
                                messages.success(request, 'Unblocked successfully.')
                        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                if action == 'delete':
                    if settings.ACCESS_PERMISSION_OPERATOR_DELETE in auth_permissions.values():
                        try:
                            model = Operators.objects.get(operator_id=id)
                            Operators.delete_operator(request, model, operator)
                            messages.success(request, 'Deleted successfully.')
                        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                return HttpResponse('success', content_type='text/plain')
            else:
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')
    else:
        return HttpResponseForbidden('Forbidden', content_type='text/plain')


@csrf_exempt
# noinspection PyUnusedLocal
def multiple_select(request):
    if request.is_ajax():
        operator = Operators.login_required(request)
        if operator is None:
            # Operators.set_redirect_field_name(request, request.path)
            # return redirect(reverse("operators_signin"))
            return HttpResponse('signin', content_type='text/plain')
        else:
            auth_permissions = Operators.get_auth_permissions(operator)
            action = request.POST['action']
            ids = request.POST['ids']
            try:
                ids = ids.split(",")
            except(TypeError, ValueError, OverflowError):
                ids = None
            if action != '' and ids is not None:
                if action == 'verify':
                    if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
                        for id in ids:
                            try:
                                model = Operators.objects.get(operator_id=id)
                                if model.operator_status == Operators.STATUS_UNVERIFIED:
                                    model.operator_status = Operators.STATUS_UNAPPROVED
                                    model.operator_updated_at = Utils.get_current_datetime_utc()
                                    model.operator_updated_by = operator.operator_username
                                    model.save()
                                    Operator_Logs.add(
                                        model.operator_id,
                                        model.operator_username,
                                        model.operator_name,
                                        'Verified ' + Operators.SINGULAR_TITLE,
                                        Utils.get_browser_details_from_request(request),
                                        Utils.get_ip_address(request),
                                        operator.operator_username,
                                    )
                            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                                continue
                        messages.success(request, 'Verified successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                if action == 'approve':
                    if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
                        for id in ids:
                            try:
                                model = Operators.objects.get(operator_id=id)
                                if model.operator_status == Operators.STATUS_UNAPPROVED:
                                    model.operator_status = Operators.STATUS_INACTIVE
                                    model.operator_updated_at = Utils.get_current_datetime_utc()
                                    model.operator_updated_by = operator.operator_username
                                    model.save()
                                    Operator_Logs.add(
                                        model.operator_id,
                                        model.operator_username,
                                        model.operator_name,
                                        'Approved ' + Operators.SINGULAR_TITLE,
                                        Utils.get_browser_details_from_request(request),
                                        Utils.get_ip_address(request),
                                        operator.operator_username,
                                    )
                            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                                continue
                        messages.success(request, 'Approved successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                if action == 'block':
                    if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
                        for id in ids:
                            try:
                                model = Operators.objects.get(operator_id=id)
                                if model.operator_status == Operators.STATUS_ACTIVE or model.operator_status == Operators.STATUS_INACTIVE:
                                    model.operator_status = Operators.STATUS_BLOCKED
                                    model.operator_updated_at = Utils.get_current_datetime_utc()
                                    model.operator_updated_by = operator.operator_username
                                    model.save()
                                    Operator_Logs.add(
                                        model.operator_id,
                                        model.operator_username,
                                        model.operator_name,
                                        'Blocked ' + Operators.SINGULAR_TITLE,
                                        Utils.get_browser_details_from_request(request),
                                        Utils.get_ip_address(request),
                                        operator.operator_username,
                                    )
                            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                                continue
                        messages.success(request, 'Blocked successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                if action == 'unblock':
                    if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
                        for id in ids:
                            try:
                                model = Operators.objects.get(operator_id=id)
                                if model.operator_status == Operators.STATUS_BLOCKED:
                                    model.operator_status = Operators.STATUS_INACTIVE
                                    model.operator_updated_at = Utils.get_current_datetime_utc()
                                    model.operator_updated_by = operator.operator_username
                                    model.save()
                                    Operator_Logs.add(
                                        model.operator_id,
                                        model.operator_username,
                                        model.operator_name,
                                        'Unblocked ' + Operators.SINGULAR_TITLE,
                                        Utils.get_browser_details_from_request(request),
                                        Utils.get_ip_address(request),
                                        operator.operator_username,
                                    )
                            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                                continue
                        messages.success(request, 'Unblocked successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                if action == 'delete':
                    if settings.ACCESS_PERMISSION_OPERATOR_DELETE in auth_permissions.values():
                        for id in ids:
                            try:
                                model = Operators.objects.get(operator_id=id)
                                Operators.delete_operator(request, model, operator)
                            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                                continue
                        messages.success(request, 'Deleted successfully.')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')

                return HttpResponse('success', content_type='text/plain')
            else:
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')
    else:
        return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def create(request):
    template_url = 'operators/create.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_OPERATOR_CREATE in auth_permissions.values():
            if request.method == 'POST':

                form = OperatorCreateForm(request.POST)

                # noinspection PyArgumentList
                if form.is_valid():
                    model = Operators()
                    model.operator_type = form.cleaned_data['type']
                    model.operator_username = form.cleaned_data['email']

                    model.operator_auth_key = Operators.generate_unique_token(Operators, 'operator_auth_key')

                    model.operator_password_hash = make_password(form.cleaned_data['password'])
                    model.operator_password_reset_token = ''
                    model.operator_name = form.cleaned_data['name']
                    model.operator_gender = form.cleaned_data['gender']
                    model.operator_contact_phone_number = form.cleaned_data['phone_number']
                    model.operator_contact_email_id = form.cleaned_data['email']
                    model.operator_profile_photo_file_path = ''
                    model.operator_created_at = Utils.get_current_datetime_utc()
                    model.operator_created_by = operator.operator_username
                    model.operator_updated_at = Utils.get_current_datetime_utc()
                    model.operator_updated_by = operator.operator_username
                    model.operator_status = Operators.STATUS_UNVERIFIED
                    # noinspection PyCallByClass,PyTypeChecker
                    model.save('Created')

                    Operator_Logs.add(
                        model.operator_id,
                        model.operator_username,
                        model.operator_name,
                        'Created ' + Operators.SINGULAR_TITLE,
                        Utils.get_browser_details_from_request(request),
                        Utils.get_ip_address(request),
                        operator.operator_username,
                    )

                    # sending email confirmation mail
                    if settings.IS_LOCAL:
                        domain = settings.BACKEND_DOMAIN_LOCAL
                    else:
                        domain = settings.BACKEND_DOMAIN_PROD
                    contact_url = '{domain}/{path}'.format(domain=domain, path=settings.CONTACT_URL)
                    confirm_url = '{domain}/{path}'.format(
                        domain=domain,
                        path='operators/signup/confirm/' + model.operator_auth_key
                    )
                    html_content = render_to_string(
                        'email/email-confirmation.html',
                        {
                            'name': model.operator_name,
                            'contact_url': contact_url,
                            'confirm_url': confirm_url,
                        }
                    )
                    send_mail(
                        settings.EMAIL_VERIFICATION_SUBJECT,
                        settings.EMAIL_VERIFICATION_MESSAGE,
                        settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                        [model.operator_username],
                        fail_silently=False,
                        html_message=html_content,
                    )

                    messages.info(request,
                                  'An email has been sent for verification to your registered email address.')
                    return redirect(reverse("operators_view", args=[model.operator_id]))
                else:
                    return render(
                        request, template_url,
                        {
                            'section': settings.BACKEND_SECTION_OPERATORS,
                            'title': Operators.TITLE,
                            'name': Operators.NAME,
                            'operator': operator,
                            'auth_permissions': auth_permissions,
                            'form': form,
                        }
                    )
            else:
                form = OperatorCreateForm()

            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_OPERATORS,
                    'title': Operators.TITLE,
                    'name': Operators.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'form': form,
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update(request, pk):
    template_url = 'operators/update.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
            try:
                model = Operators.objects.get(operator_id=pk)
                if request.method == 'POST':

                    form = OperatorUpdateForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.operator_username = form.cleaned_data['email']
                        model.operator_name = form.cleaned_data['name']
                        model.operator_type = form.cleaned_data['type']
                        model.operator_gender = form.cleaned_data['gender']
                        model.operator_contact_phone_number = form.cleaned_data['phone_number']

                        model.operator_updated_at = Utils.get_current_datetime_utc()
                        model.operator_updated_by = operator.operator_username
                        model.save()

                        Operator_Logs.add(
                            model.operator_id,
                            model.operator_username,
                            model.operator_name,
                            'Updated ' + Operators.SINGULAR_TITLE,
                            Utils.get_browser_details_from_request(request),
                            Utils.get_ip_address(request),
                            operator.operator_username,
                        )

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("operators_view", args=[model.operator_id]))
                    else:
                        return render(
                            request, template_url,
                            {
                                'section': settings.BACKEND_SECTION_OPERATORS,
                                'title': Operators.TITLE,
                                'name': Operators.NAME,
                                'operator': operator,
                                'auth_permissions': auth_permissions,
                                'form': form,
                                'model': model,
                            }
                        )
                else:
                    form = OperatorUpdateForm(
                        initial={
                            'email': model.operator_username,
                            'name': model.operator_name,
                            'type': model.operator_type,
                            'gender': model.operator_gender,
                            'phone_number': model.operator_contact_phone_number,
                        }
                    )

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_OPERATORS,
                        'title': Operators.TITLE,
                        'name': Operators.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'model': model,
                    }
                )
            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update_permissions_view(request, pk):
    template_url = 'operators/update-permissions.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
            try:
                model = Operators.objects.get(operator_id=pk)
                if request.method == 'POST':

                    form = OperatorUpdateForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():

                        model.save()

                        Operator_Logs.add(
                            model.operator_id,
                            model.operator_username,
                            model.operator_name,
                            'Updated ' + Operators.SINGULAR_TITLE,
                            Utils.get_browser_details_from_request(request),
                            Utils.get_ip_address(request),
                            operator.operator_username,
                        )

                        messages.success(request, 'Updated permissions successfully.')
                        return redirect(reverse("operators_view", args=[model.operator_id]))
                    else:
                        return render(
                            request, template_url,
                            {
                                'section': settings.BACKEND_SECTION_OPERATORS,
                                'title': Operators.TITLE,
                                'name': Operators.NAME,
                                'operator': operator,
                                'auth_permissions': auth_permissions,
                                'form': form,
                                'model': model,
                            }
                        )
                else:
                    form = OperatorUpdateForm(
                        initial={
                            'email': model.operator_username,
                            'name': model.operator_name,
                            'type': model.operator_type,
                            'gender': model.operator_gender,
                            'phone_number': model.operator_contact_phone_number,
                        }
                    )
                    form.fields['name'].widget.attrs['readonly'] = 'true'
                    form.fields['name'].widget.attrs['disabled'] = 'true'

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_OPERATORS,
                        'title': Operators.TITLE,
                        'name': Operators.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'model': model,
                        'all_auth_permissions': Access_Permissions.get_access_permissions(),
                        'operator_auth_permissions': Operator_Access_Permissions.get_access_permissions(
                            model.operator_id),
                    }
                )
            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal
def update_permissions_action(request):
    if request.is_ajax():
        operator = Operators.login_required(request)
        if operator is None:
            Operators.set_redirect_field_name(request, request.path)
            return redirect(reverse("operators_signin"))
        else:
            auth_permissions = Operators.get_auth_permissions(operator)
            id = request.POST['id']
            permissions = request.POST['permissions']
            print(permissions)
            permissions_list = None
            if permissions != '' and permissions != 'null':
                permissions_list = permissions.split(",")
                print(len(permissions_list))
            print(permissions_list)

            if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
                try:
                    model = Operators.objects.get(operator_id=id)
                    # delete existing permissions
                    Operator_Access_Permissions.objects.filter(operators_operator_id=id).delete()
                    if permissions_list is not None:
                        # add permission one by one
                        i = 0
                        while i < len(permissions_list):
                            if permissions_list[i]:
                                access_permission = Access_Permissions.objects.get(
                                    access_permission_name=permissions_list[i])
                                operator_access_permission = Operator_Access_Permissions()
                                operator_access_permission.access_permissions_access_permission_name = access_permission
                                operator_access_permission.operators_operator_id = model
                                operator_access_permission.operator_access_permission_updated_at = Utils.get_current_datetime_utc()
                                operator_access_permission.operator_access_permission_updated_by = operator.operator_username
                                operator_access_permission.save()
                            i += 1

                    messages.success(request, 'Updated successfully.')
                    return HttpResponse('success', content_type='text/plain')
                except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                    return HttpResponseBadRequest('Bad Request', content_type='text/plain')
            else:
                return HttpResponseForbidden('Forbidden', content_type='text/plain')
    else:
        return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update_reset_password(request, pk):
    template_url = 'operators/update-reset-password.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
            try:
                model = Operators.objects.get(operator_id=pk)
                if request.method == 'POST':
                    form = OperatorResetPasswordForm(request.POST)
                    form.fields["email"].initial = model.operator_username

                    # noinspection PyArgumentList
                    if form.is_valid():

                        model.operator_password_hash = make_password(form.cleaned_data['password'])
                        model.operator_password_reset_token = ''

                        model.operator_updated_at = Utils.get_current_datetime_utc()
                        model.operator_updated_by = operator.operator_username
                        model.save()

                        Operator_Logs.add(
                            model.operator_id,
                            model.operator_username,
                            model.operator_name,
                            Operators.SINGULAR_TITLE + ' Reset Password',
                            Utils.get_browser_details_from_request(request),
                            Utils.get_ip_address(request),
                            operator.operator_username,
                        )

                        # sending password reset message mail
                        if settings.IS_LOCAL:
                            domain = settings.BACKEND_DOMAIN_LOCAL
                        else:
                            domain = settings.BACKEND_DOMAIN_PROD
                        contact_url = '{domain}/{path}'.format(domain=domain, path=settings.CONTACT_URL)
                        html_content = render_to_string(
                            'email/email-info.html',
                            {
                                'name': model.operator_name,
                                'message': 'Your password has been reset successfully by admin.',
                                'contact_url': contact_url,
                            }
                        )
                        send_mail(
                            settings.EMAIL_NOTIFICATION_SUBJECT,
                            settings.EMAIL_NOTIFICATION_MESSAGE,
                            settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                            [model.operator_username],
                            fail_silently=False,
                            html_message=html_content,
                        )

                        messages.info(request, 'Password has been reset successfully.')
                        return redirect(reverse("operators_view", args=[model.operator_id]))

                    else:
                        return render(
                            request, template_url,
                            {
                                'section': settings.BACKEND_SECTION_PROFILE,
                                'title': Operators.TITLE,
                                'name': Operators.NAME,
                                'operator': operator,
                                'auth_permissions': auth_permissions,
                                'form': form,
                                'model': model,
                            }
                        )
                else:
                    form = OperatorResetPasswordForm()
                    form.fields["email"].initial = model.operator_username

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_PROFILE,
                        'title': Operators.TITLE,
                        'name': Operators.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'model': model,
                    }
                )
            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def view(request, pk):
    template_url = 'operators/view.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_OPERATOR_VIEW in auth_permissions.values():
            try:
                model = Operators.objects.get(operator_id=pk)
                model.operator_created_at = Utils.get_convert_datetime(model.operator_created_at,
                                                                       settings.TIME_ZONE,
                                                                       settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                model.operator_updated_at = Utils.get_convert_datetime(model.operator_updated_at,
                                                                       settings.TIME_ZONE,
                                                                       settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_OPERATORS,
                        'title': Operators.TITLE,
                        'name': Operators.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'model': model,
                        'index_url': reverse("operators_index"),
                        'single_select_url': reverse("operators_single_select"),
                    }
                )
            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def profile_view(request):
    template_url = 'operators/profile-view.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        try:
            model = operator
            model.operator_created_at = Utils.get_convert_datetime(model.operator_created_at,
                                                                   settings.TIME_ZONE,
                                                                   settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
            model.operator_updated_at = Utils.get_convert_datetime(model.operator_updated_at,
                                                                   settings.TIME_ZONE,
                                                                   settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO

            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_PROFILE,
                    'title': Operators.TITLE,
                    'name': Operators.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'model': model,
                }
            )
        except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
            return HttpResponseNotFound('Not Found', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def profile_update(request):
    template_url = 'operators/profile-update.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
            try:
                model = operator
                if request.method == 'POST':

                    form = OperatorUpdateForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.operator_username = form.cleaned_data['email']
                        model.operator_name = form.cleaned_data['name']
                        model.operator_type = form.cleaned_data['type']
                        model.operator_gender = form.cleaned_data['gender']
                        model.operator_contact_phone_number = form.cleaned_data['phone_number']

                        model.operator_updated_at = Utils.get_current_datetime_utc()
                        model.operator_updated_by = operator.operator_username
                        model.save()

                        Operator_Logs.add(
                            model.operator_id,
                            model.operator_username,
                            model.operator_name,
                            'Updated ' + Operators.SINGULAR_TITLE,
                            Utils.get_browser_details_from_request(request),
                            Utils.get_ip_address(request),
                            operator.operator_username,
                        )

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("operators_profile_view"))
                    else:
                        return render(
                            request, template_url,
                            {
                                'section': settings.BACKEND_SECTION_PROFILE,
                                'title': Operators.TITLE,
                                'name': Operators.NAME,
                                'operator': operator,
                                'auth_permissions': auth_permissions,
                                'form': form,
                            }
                        )
                else:
                    form = OperatorUpdateForm(
                        initial={
                            'email': model.operator_username,
                            'name': model.operator_name,
                            'type': model.operator_type,
                            'gender': model.operator_gender,
                            'phone_number': model.operator_contact_phone_number,
                        }
                    )

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_PROFILE,
                        'title': Operators.TITLE,
                        'name': Operators.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                    }
                )
            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def profile_change_password(request):
    template_url = 'operators/profile-change-password.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_OPERATOR_UPDATE in auth_permissions.values():
            try:
                model = operator

                if request.method == 'POST':
                    form = OperatorChangePasswordForm(request.POST)
                    form.fields["email"].initial = model.operator_username

                    # noinspection PyArgumentList
                    if form.is_valid():

                        model.operator_password_hash = make_password(form.cleaned_data['new_password'])
                        model.operator_password_reset_token = ''

                        model.operator_updated_at = Utils.get_current_datetime_utc()
                        model.operator_updated_by = operator.operator_username
                        model.save()

                        Operator_Logs.add(
                            model.operator_id,
                            model.operator_username,
                            model.operator_name,
                            Operators.SINGULAR_TITLE + ' Changed Password',
                            Utils.get_browser_details_from_request(request),
                            Utils.get_ip_address(request),
                            operator.operator_username,
                        )

                        # sending password reset message mail
                        if settings.IS_LOCAL:
                            domain = settings.BACKEND_DOMAIN_LOCAL
                        else:
                            domain = settings.BACKEND_DOMAIN_PROD
                        contact_url = '{domain}/{path}'.format(domain=domain, path=settings.CONTACT_URL)
                        html_content = render_to_string(
                            'email/email-info.html',
                            {
                                'name': model.operator_name,
                                'message': 'Your password has been changed successfully.',
                                'contact_url': contact_url,
                            }
                        )
                        send_mail(
                            settings.EMAIL_NOTIFICATION_SUBJECT,
                            settings.EMAIL_NOTIFICATION_MESSAGE,
                            settings.APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID,
                            [model.operator_username],
                            fail_silently=False,
                            html_message=html_content,
                        )

                        messages.info(request, 'Your password has been changed successfully.')
                        return redirect(reverse("operators_profile_view"))

                    else:
                        return render(
                            request, template_url,
                            {
                                'section': settings.BACKEND_SECTION_PROFILE,
                                'title': Operators.TITLE,
                                'name': Operators.NAME,
                                'operator': operator,
                                'auth_permissions': auth_permissions,
                                'form': form,
                            }
                        )
                else:
                    form = OperatorChangePasswordForm()
                    form.fields["email"].initial = model.operator_username

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_PROFILE,
                        'title': Operators.TITLE,
                        'name': Operators.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                    }
                )

            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')
