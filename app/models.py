import os
from decimal import Decimal

from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator
from django.core.validators import ValidationError
from django.db import models
from django.db.models import Q
from django.middleware.csrf import rotate_token
from django.utils.crypto import get_random_string, salted_hmac, constant_time_compare
from tinymce.models import HTMLField

from app import settings
from app.data import ARRAY_GENDER
from app.utils import Utils


def upload_image_validator(upload_file_obj):
    print('validating image')
    print(os.path.splitext(upload_file_obj.name)[0])
    ext = os.path.splitext(upload_file_obj.name)[1]  # [0] = returns path+filename
    print(ext)
    valid_extension = settings.VALID_IMAGE_EXTENSIONS
    if ext not in valid_extension:
        raise ValidationError(u'Unsupported file extension - (.png, .jpg, .jpeg only)')


# Create your models here.
# noinspection PyUnresolvedReferences
class Operators(models.Model):
    TITLE = settings.MODEL_OPERATORS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_OPERATORS_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    SESSION_KEY = '_' + TITLE.lower() + '_id'
    BACKEND_SESSION_KEY = '_' + TITLE.lower() + '_backend'
    HASH_SESSION_KEY = '_' + TITLE.lower() + '_hash'
    REDIRECT_FIELD_NAME = 'next'

    TYPE_SUPER_ADMIN = 'super-admin'
    TYPE_ADMIN = 'admin'
    TYPE_MANAGER = 'manager'
    TYPE_OTHER = 'other'
    ARRAY_OPERATOR_TYPES = [
        (TYPE_SUPER_ADMIN.title()).replace('-', ' '),
        (TYPE_ADMIN.title()).replace('-', ' '),
        (TYPE_MANAGER.title()).replace('-', ' '),
        (TYPE_OTHER.title()).replace('-', ' '),
    ]
    OPERATOR_TYPES = (
        ('', '--select--'),
        # (TYPE_SUPER_ADMIN, (TYPE_SUPER_ADMIN.title()).replace('-', ' ')),
        (TYPE_ADMIN, (TYPE_ADMIN.title()).replace('-', ' ')),
        (TYPE_MANAGER, (TYPE_MANAGER.title()).replace('-', ' ')),
        (TYPE_OTHER, (TYPE_OTHER.title()).replace('-', ' ')),
    )
    SUPER_OPERATOR_TYPES = (
        ('', '--select--'),
        (TYPE_SUPER_ADMIN, (TYPE_SUPER_ADMIN.title()).replace('-', ' ')),
        (TYPE_ADMIN, (TYPE_ADMIN.title()).replace('-', ' ')),
        (TYPE_MANAGER, (TYPE_MANAGER.title()).replace('-', ' ')),
        (TYPE_OTHER, (TYPE_OTHER.title()).replace('-', ' ')),
    )

    DEPARTMENT_NONE = 'NONE'  # None
    DEPARTMENT_DCOP = 'DCOP'  # Deputy Chief of Procurement
    DEPARTMENT_BFM = 'BFM'  # Business, Finance and Marketing
    DEPARTMENT_NUTRITION = 'NUTRITION'  # Nutrition
    DEPARTMENT_DAF = 'DAF'  # Department of Administrative and Finance
    DEPARTMENT_MAV = 'MAE'  # Monitoring and Evaluation
    DEPARTMENT_GRANT_MANAGER = 'GRANT-MANAGER'  # Grant Managers
    ARRAY_OPERATOR_DEPARTMENTS = [
        DEPARTMENT_NONE,
        'Deputy COP',
        'Business, Finance & Marketing',
        'Nutrition',
        'Administrative and Finance',
        'Monitoring and Evaluation',
        'Grant Manager',
    ]
    OPERATOR_DEPARTMENTS = (
        ('', '--select--'),
        (DEPARTMENT_NONE, 'NONE'),
        (DEPARTMENT_DCOP, 'Deputy COP'),
        (DEPARTMENT_BFM, 'Business, Finance & Marketing'),
        (DEPARTMENT_NUTRITION, 'Nutrition'),
        (DEPARTMENT_DAF, 'Administrative and Finance'),
        (DEPARTMENT_MAV, 'Monitoring and Evaluation'),
        (DEPARTMENT_GRANT_MANAGER, 'Grant Manager'),
    )

    ROLE_NONE = 'NONE'  # None
    ROLE_COP = 'COP'  # COP
    ROLE_OPM = 'OPM'  # OPM
    ROLE_DIRECTOR = 'Director'  # Director
    # for all departments
    ROLE_ADVISER = 'Adviser'  # Adviser
    # only for DCOP(C1/Agriculture) Department
    ROLE_REGIONAL_MANAGER = 'Regional Manager'  # Regional Manager
    ROLE_DISTRICT_MANAGER = 'District Manager'  # District Manager
    ROLE_FIELD_OFFICER = 'Field Officer'  # Field Officer
    # only for DAF Department
    ROLE_PROCUREMENT_OFFICER = 'Procurement Officer'  # Procurement Officer
    ROLE_HR_MANAGER = 'HR Manager'  # HR Manager
    ROLE_RECEPTIONIST = 'Receptionist'  # Receptionist
    ROLE_STOCK_ADMIN = 'Stock Admin'  # Stock Admin
    ROLE_ACCOUNTANT_MANAGER = 'Accountant Manager'  # Accountant Head
    ROLE_ACCOUNTANT_OFFICER = 'Accountant Officer'  # Accountant Officer

    ARRAY_OPERATOR_ROLES = [
        ROLE_NONE,
        ROLE_COP,
        ROLE_OPM,
        ROLE_DIRECTOR,
        ROLE_ADVISER,
        ROLE_REGIONAL_MANAGER,
        ROLE_DISTRICT_MANAGER,
        ROLE_FIELD_OFFICER,
        ROLE_PROCUREMENT_OFFICER,
        ROLE_HR_MANAGER,
        ROLE_RECEPTIONIST,
        ROLE_STOCK_ADMIN,
        ROLE_ACCOUNTANT_MANAGER,
        ROLE_ACCOUNTANT_OFFICER,
    ]
    OPERATOR_ROLES = (
        ('', '--select--'),
        (ROLE_NONE, ROLE_NONE),
        (ROLE_COP, ROLE_COP),
        (ROLE_OPM, ROLE_OPM),
        (ROLE_DIRECTOR, ROLE_DIRECTOR),
        (ROLE_ADVISER, ROLE_ADVISER),
        (ROLE_REGIONAL_MANAGER, ROLE_REGIONAL_MANAGER),
        (ROLE_DISTRICT_MANAGER, ROLE_DISTRICT_MANAGER),
        (ROLE_FIELD_OFFICER, ROLE_FIELD_OFFICER),
        (ROLE_PROCUREMENT_OFFICER, ROLE_PROCUREMENT_OFFICER),
        (ROLE_HR_MANAGER, ROLE_HR_MANAGER),
        (ROLE_RECEPTIONIST, ROLE_RECEPTIONIST),
        (ROLE_STOCK_ADMIN, ROLE_STOCK_ADMIN),
        (ROLE_ACCOUNTANT_MANAGER, ROLE_ACCOUNTANT_MANAGER),
        (ROLE_ACCOUNTANT_OFFICER, ROLE_ACCOUNTANT_OFFICER),
    )

    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUS_UNVERIFIED = 'unverified'
    STATUS_UNAPPROVED = 'unapproved'
    STATUS_BLOCKED = 'blocked'
    ARRAY_OPERATOR_STATUSES = [
        (STATUS_ACTIVE.title()).replace('-', ' '),
        (STATUS_INACTIVE.title()).replace('-', ' '),
        (STATUS_UNVERIFIED.title()).replace('-', ' '),
        (STATUS_UNAPPROVED.title()).replace('-', ' '),
        (STATUS_BLOCKED.title()).replace('-', ' '),
    ]
    OPERATOR_STATUSES = (
        ('', '--select--'),
        (STATUS_ACTIVE, (STATUS_ACTIVE.title()).replace('-', ' ')),
        (STATUS_INACTIVE, (STATUS_INACTIVE.title()).replace('-', ' ')),
        (STATUS_BLOCKED, (STATUS_UNVERIFIED.title()).replace('-', ' ')),
        (STATUS_UNVERIFIED, (STATUS_UNAPPROVED.title()).replace('-', ' ')),
        (STATUS_UNAPPROVED, (STATUS_BLOCKED.title()).replace('-', ' ')),
    )

    HTML_TAG_STATUS_ACTIVE_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_ACTIVE_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Active <b></div>'
    HTML_TAG_STATUS_INACTIVE_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_INACTIVE_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Inactive <b></div>'
    HTML_TAG_STATUS_BLOCKED_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_BLOCKED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Blocked <b></div>'
    HTML_TAG_STATUS_UNVERIFIED_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_UNVERIFIED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Unverified <b></div>'
    HTML_TAG_STATUS_UNAPPROVED_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_UNAPPROVED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Unapproved <b></div>'

    operator_notifications_count = 0
    operator_notifications_json = None

    operator_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    operator_type = models.CharField('Type', max_length=20, blank=False, choices=SUPER_OPERATOR_TYPES,
                                     default=TYPE_OTHER)
    operator_department = models.CharField('Department', max_length=255, blank=False, choices=OPERATOR_DEPARTMENTS,
                                           default=DEPARTMENT_NONE)
    operator_role = models.CharField('Role', max_length=255, blank=False, choices=OPERATOR_ROLES,
                                     default=ROLE_NONE)
    operator_parent_id = models.IntegerField('Parent Id',
                                             default='0')  # parent id is needed to maintain hierarchy of the operator
    operator_username = models.CharField('Username', max_length=100, blank=False, unique=True)
    operator_auth_key = models.CharField('Auth key', max_length=255, blank=False)
    operator_password_hash = models.CharField('Password', max_length=255, blank=False)
    operator_password_reset_token = models.CharField('Password reset token', max_length=255, blank=True)
    operator_name = models.CharField('Name', max_length=100, blank=False)
    operator_gender = models.CharField('Gender', max_length=6, choices=ARRAY_GENDER, default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,17}$',
                                 message="Phone number must be entered in the format: '1-(555)-555-5555'. Up to 17 digits allowed.")
    operator_contact_phone_number = models.CharField('Phone Number',
                                                     validators=[phone_regex, MinLengthValidator(9),
                                                                 MaxLengthValidator(17)],
                                                     max_length=17, blank=True)
    operator_contact_email_id = models.EmailField('Email id', max_length=100, blank=True)
    operator_profile_photo_file_path = models.CharField('Profile photo file path', max_length=255, blank=True)
    operator_created_at = models.DateTimeField('Created by', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    operator_created_by = models.EmailField('Created by', max_length=255, blank=True)
    operator_updated_at = models.DateTimeField('Updated at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    operator_updated_by = models.EmailField('Updated by', max_length=255, blank=True)
    operator_status = models.CharField('Status', max_length=20, blank=False, choices=OPERATOR_STATUSES,
                                       default=STATUS_UNVERIFIED)

    def __unicode__(self):
        return self.operator_id

    def get_session_auth_hash(self):
        key_salt = "qtacms.models.auth.Operators.get_session_auth_hash"
        return salted_hmac(key_salt, self.operator_password_hash).hexdigest()

    @classmethod
    def set_redirect_field_name(cls, request, url):
        request.session[Operators.REDIRECT_FIELD_NAME] = url

    @classmethod
    def get_redirect_field_name(cls, request):
        return request.session.get(Operators.REDIRECT_FIELD_NAME, None)

    @classmethod
    def get_session_key(cls, request):
        return str(request.session[Operators.SESSION_KEY])

    @classmethod
    def login(cls, request, operator):
        session_auth_hash = ''
        if hasattr(operator, 'get_session_auth_hash'):
            session_auth_hash = operator.get_session_auth_hash()

        if Operators.SESSION_KEY in request.session:
            if cls.get_session_key(request) != operator.pk or (
                    session_auth_hash and
                    not constant_time_compare(request.session.get(Operators.HASH_SESSION_KEY, ''),
                                              session_auth_hash)):
                request.session.flush()
        else:
            request.session.cycle_key()

        request.session[Operators.SESSION_KEY] = str(operator.pk)
        request.session[Operators.BACKEND_SESSION_KEY] = None
        request.session[Operators.HASH_SESSION_KEY] = session_auth_hash
        # one hour session timeout
        request.session.set_expiry(3600)

        # reset csrf token
        rotate_token(request)

        return True

    @classmethod
    def logout(cls, request):
        request.session.flush()
        return True

    @classmethod
    def login_required(cls, request):
        if Operators.SESSION_KEY in request.session:
            operator_id = request.session.get(Operators.SESSION_KEY, '0')
            try:
                operator = Operators.objects.get(operator_id=operator_id)
                notifications = Notifications.objects.filter(
                    Q(notification_to_id=operator.operator_id) &
                    Q(notification_status=Notifications.STATUS_UNREAD)
                ).order_by('-notification_created_at')

                if notifications.count() > 5:
                    count = "5+"
                else:
                    if notifications.count == 0:
                        count = 0
                    else:
                        count = notifications.count()
                notifications = notifications[: 5]
                operator.operator_notifications_count = count
                operator.operator_notifications_json = notifications

            except(TypeError, ValueError, OverflowError, Operators.DoesNotExist):
                operator = None
            return operator
        else:
            return None

    @classmethod
    def generate_unique_token(cls, operators, attribute):
        token = ''
        unique_token_found = False
        while not unique_token_found:
            token = get_random_string(32)
            if operators.objects.filter(**{attribute: token}).count() is 0:
                unique_token_found = True
        return token

    @classmethod
    def get_auth_permissions(cls, operator):
        operator_auth_permissions = Operator_Access_Permissions.objects.filter(
            operators_operator_id_id=operator.operator_id)
        auth_permissions = {}
        counter = 0
        for operator_auth_permission in operator_auth_permissions:
            auth_permissions[counter] = operator_auth_permission.access_permissions_access_permission_name_id
            counter = counter + 1
        return auth_permissions

    @classmethod
    def update_operator_access_permissions(cls, request, model, operator):

        Operator_Access_Permissions.objects.filter(operators_operator_id_id=model.operator_id).delete()

        if model.operator_type == Operators.TYPE_SUPER_ADMIN or model.operator_type == Operators.TYPE_ADMIN:
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_SETTINGS_VIEW, model,
                                                                       operator)
            Operator_Access_Permissions.add_operator_access_permission(request, settings.ACCESS_PERMISSION_LOG_DELETE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request, settings.ACCESS_PERMISSION_LOG_VIEW,
                                                                       model, operator)

        if model.operator_type == Operators.TYPE_SUPER_ADMIN or model.operator_type == Operators.TYPE_ADMIN or model.operator_type == Operators.TYPE_MANAGER:
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_DASHBOARD_VIEW, model,
                                                                       operator)
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_OPERATOR_CREATE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_OPERATOR_UPDATE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_OPERATOR_DELETE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_OPERATOR_VIEW, model,
                                                                       operator)

        if model.operator_type == Operators.TYPE_SUPER_ADMIN or model.operator_type == Operators.TYPE_ADMIN or model.operator_type == Operators.TYPE_MANAGER or model.operator_type == Operators.TYPE_OTHER:
            Operator_Access_Permissions.add_operator_access_permission(request, settings.ACCESS_PERMISSION_ORDER_CREATE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request, settings.ACCESS_PERMISSION_ORDER_UPDATE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request, settings.ACCESS_PERMISSION_ORDER_DELETE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request, settings.ACCESS_PERMISSION_ORDER_VIEW,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_PRODUCT_VIEW, model,
                                                                       operator)

        if model.operator_type == Operators.TYPE_SUPER_ADMIN or model.operator_type == Operators.TYPE_ADMIN or model.operator_type == Operators.TYPE_MANAGER or model.operator_role == Operators.ROLE_STOCK_ADMIN:
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_PRODUCT_CREATE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_PRODUCT_UPDATE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_PRODUCT_DELETE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_INVENTORY_CREATE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_INVENTORY_UPDATE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_INVENTORY_DELETE,
                                                                       model, operator)
            Operator_Access_Permissions.add_operator_access_permission(request,
                                                                       settings.ACCESS_PERMISSION_INVENTORY_VIEW, model,
                                                                       operator)

        Operator_Logs.add(
            model.operator_id,
            model.operator_username,
            model.operator_name,
            'Updated ' + Operators.SINGULAR_TITLE + ' Access Permissions',
            Utils.get_browser_details_from_request(request),
            Utils.get_ip_address(request),
            operator.operator_username,
        )

        model.save()
        return True

    @classmethod
    def get_child_operators(cls, operator):
        # noinspection PyShadowingNames
        def get_child_operators_inner(counter, child_operators, operator):
            operator_id = operator.operator_id
            operators = Operators.objects.filter(operator_parent_id=operator_id)

            for model in operators:
                child_operators[counter] = model.operator_id
                counter = counter + 1

            for model in operators:
                operators = Operators.objects.filter(operator_parent_id=model.operator_id)
                if operators.count() > 0:
                    child_operators = get_child_operators_inner(counter, child_operators, model)

            return child_operators

        child_operators = {0: operator.operator_id}
        child_operators = get_child_operators_inner(1, child_operators, operator)

        child_operators_array = []
        for key, value in child_operators.items():
            child_operators_array.append(value)

        return child_operators_array

    @classmethod
    def delete_operator(cls, request, model, operator):

        Operator_Access_Permissions.objects.filter(operators_operator_id_id=model.operator_id).delete()

        Operator_Logs.add(
            model.operator_id,
            model.operator_username,
            model.operator_name,
            'Deleted ' + Operators.SINGULAR_TITLE + ' Access Permissions',
            Utils.get_browser_details_from_request(request),
            Utils.get_ip_address(request),
            operator.operator_username,
        )

        if model.operator_profile_photo_file_path:
            Utils.delete_file(model.operator_profile_photo_file_path.path)

        Operator_Logs.add(
            model.operator_id,
            model.operator_username,
            model.operator_name,
            'Deleted ' + Operators.SINGULAR_TITLE,
            Utils.get_browser_details_from_request(request),
            Utils.get_ip_address(request),
            operator.operator_username,
        )

        model.delete()
        return True


# noinspection PyPep8Naming
class Operator_Logs(models.Model):
    TITLE = Operators.SINGULAR_TITLE + ' Logs'
    NAME = "-".join((TITLE.lower()).split())
    operator_log_id = models.AutoField('Log Id', primary_key=True)
    operators_operator_id = models.IntegerField(Operators.SINGULAR_TITLE + ' Id', default=0)
    operators_operator_username = models.CharField('Username', max_length=100, blank=False)
    operators_operator_name = models.CharField('Name', max_length=100, blank=False)
    operator_log_message = models.CharField('Message', max_length=255, blank=True)
    operator_log_browser = models.TextField('Browser', blank=True)
    operator_log_ip_address = models.CharField('Ip address', max_length=30, blank=True)
    operator_log_updated_at = models.DateTimeField('Updated at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    operator_log_updated_by = models.EmailField('Updated by', max_length=255, blank=True)

    @classmethod
    def add(cls, operator_id, operator_username, operator_name, message, browser, ip_address, updated_by):
        log = Operator_Logs()
        log.operators_operator_id = operator_id
        log.operators_operator_username = operator_username
        log.operators_operator_name = operator_name
        log.operator_log_message = message
        log.operator_log_browser = browser
        log.operator_log_ip_address = ip_address
        log.operator_log_updated_at = Utils.get_current_datetime_utc()
        log.operator_log_updated_by = updated_by
        return log.save('Added ' + Operators.SINGULAR_TITLE + ' Log')


# Create your models here.
# noinspection PyUnresolvedReferences
class Orders(models.Model):
    TITLE = settings.MODEL_ORDERS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_ORDERS_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    CURRENCY_USD = 'USD'
    CURRENCY_RWF = 'RWF'

    ARRAY_CURRENCIES = [
        CURRENCY_USD,
        CURRENCY_RWF,
    ]
    DROPDOWN_CURRENCIES = (
        ('', '--select--'),
        (CURRENCY_USD, CURRENCY_USD),
        (CURRENCY_RWF, CURRENCY_RWF),
    )

    PROCUREMENT_METHOD_SINGLE_SOURCING = 'Single Sourcing'
    PROCUREMENT_METHOD_OPEN_TENDER = 'Open Tender'

    ARRAY_PROCUREMENT_METHODS = [
        PROCUREMENT_METHOD_SINGLE_SOURCING,
        PROCUREMENT_METHOD_OPEN_TENDER,
    ]
    DROPDOWN_PROCUREMENT_METHODS = (
        ('', '--select--'),
        (PROCUREMENT_METHOD_SINGLE_SOURCING, PROCUREMENT_METHOD_SINGLE_SOURCING),
        (PROCUREMENT_METHOD_OPEN_TENDER, PROCUREMENT_METHOD_OPEN_TENDER),
    )

    SUPPLIER_CATEGORY_1 = 'Category 1'
    SUPPLIER_CATEGORY_2 = 'Category 2'

    ARRAY_SUPPLIER_CATEGORIES = [
        SUPPLIER_CATEGORY_1,
        SUPPLIER_CATEGORY_2,
    ]
    DROPDOWN_SUPPLIER_CATEGORIES = (
        ('', '--select--'),
        (SUPPLIER_CATEGORY_1, SUPPLIER_CATEGORY_1),
        (SUPPLIER_CATEGORY_2, SUPPLIER_CATEGORY_2),
    )

    STATUS_PENDING = 'pending'
    STATUS_REQUESTED = 'requested'
    STATUS_LEVEL0_APPROVED = 'level0-approved'
    STATUS_LEVEL1_APPROVED = 'level1-approved'
    STATUS_LEVEL2_APPROVED = 'level2-approved'
    STATUS_LEVEL3_APPROVED = 'level3-approved'
    STATUS_LEVEL4_APPROVED = 'level4-approved'
    STATUS_LEVEL5_APPROVED = 'level5-approved'
    STATUS_LEVEL6_APPROVED = 'level6-approved'
    STATUS_LEVEL1_REJECTED = 'level1-rejected'
    STATUS_LEVEL2_REJECTED = 'level2-rejected'
    STATUS_LEVEL3_REJECTED = 'level3-rejected'
    STATUS_LEVEL4_REJECTED = 'level4-rejected'
    STATUS_LEVEL5_REJECTED = 'level5-rejected'
    STATUS_LEVEL6_REJECTED = 'level6-rejected'
    STATUS_REVIEWED = 'reviewed'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_ASSIGNED = 'assigned'
    STATUS_SUPPLIER_UPDATED = 'supplier-updated'
    STATUS_PROPOSAL_GENERATED = 'proposal-generated'
    STATUS_PROPOSAL_REQUESTED = 'proposal-requested'
    STATUS_PROPOSAL_SELECTED = 'proposal-selected'
    STATUS_PURCHASE_GENERATED = 'purchase-generated'
    STATUS_ACKNOWLEDGED = 'acknowledged'
    STATUS_RECEIVED = 'received'
    STATUS_INVOICE_UPLOADED = 'invoice-uploaded'
    STATUS_INVOICE_REVIEWED = 'invoice-reviewed'
    STATUS_INVOICE_PAYMENT_VOUCHER_GENERATED = 'invoice-payment-voucher-generated'
    STATUS_INVOICE_APPROVED = 'invoice-approved'
    STATUS_INVOICE_REJECTED = 'invoice-rejected'
    STATUS_INVOICE_DAF_APPROVED = 'invoice-daf-approved'
    STATUS_INVOICE_DAF_REJECTED = 'invoice-daf-rejected'
    STATUS_INVOICE_COP_APPROVED = 'invoice-cop-approved'
    STATUS_INVOICE_COP_REJECTED = 'invoice-cop-rejected'
    STATUS_PAID = 'paid'
    STATUS_CLOSED = 'closed'
    STATUS_CANCELLED = 'cancelled'
    STATUS_IN_PROGRESS = 'in-progress'
    STATUS_COMPLETED = 'completed'

    ARRAY_ORDER_STATUSES = [
        (STATUS_PENDING.title()).replace('-', ' '),
        (STATUS_REQUESTED.title()).replace('-', ' '),
        (STATUS_LEVEL0_APPROVED.title()).replace('-', ' '),
        (STATUS_LEVEL1_APPROVED.title()).replace('-', ' '),
        (STATUS_LEVEL2_APPROVED.title()).replace('-', ' '),
        (STATUS_LEVEL3_APPROVED.title()).replace('-', ' '),
        (STATUS_LEVEL4_APPROVED.title()).replace('-', ' '),
        (STATUS_LEVEL5_APPROVED.title()).replace('-', ' '),
        (STATUS_LEVEL6_APPROVED.title()).replace('-', ' '),
        (STATUS_LEVEL1_REJECTED.title()).replace('-', ' '),
        (STATUS_LEVEL2_REJECTED.title()).replace('-', ' '),
        (STATUS_LEVEL3_REJECTED.title()).replace('-', ' '),
        (STATUS_LEVEL4_REJECTED.title()).replace('-', ' '),
        (STATUS_LEVEL5_REJECTED.title()).replace('-', ' '),
        (STATUS_LEVEL6_REJECTED.title()).replace('-', ' '),
        (STATUS_REVIEWED.title()).replace('-', ' '),
        (STATUS_APPROVED.title()).replace('-', ' '),
        (STATUS_REJECTED.title()).replace('-', ' '),
        (STATUS_ASSIGNED.title()).replace('-', ' '),
        (STATUS_SUPPLIER_UPDATED.title()).replace('-', ' '),
        (STATUS_PROPOSAL_GENERATED.title()).replace('-', ' '),
        (STATUS_PROPOSAL_REQUESTED.title()).replace('-', ' '),
        (STATUS_PROPOSAL_SELECTED.title()).replace('-', ' '),
        (STATUS_PURCHASE_GENERATED.title()).replace('-', ' '),
        (STATUS_ACKNOWLEDGED.title()).replace('-', ' '),
        (STATUS_RECEIVED.title()).replace('-', ' '),
        (STATUS_INVOICE_UPLOADED.title()).replace('-', ' '),
        (STATUS_INVOICE_REVIEWED.title()).replace('-', ' '),
        (STATUS_INVOICE_PAYMENT_VOUCHER_GENERATED.title()).replace('-', ' '),
        (STATUS_INVOICE_APPROVED.title()).replace('-', ' '),
        (STATUS_INVOICE_REJECTED.title()).replace('-', ' '),
        (STATUS_INVOICE_DAF_APPROVED.title()).replace('-', ' '),
        (STATUS_INVOICE_DAF_REJECTED.title()).replace('-', ' '),
        (STATUS_INVOICE_COP_APPROVED.title()).replace('-', ' '),
        (STATUS_INVOICE_COP_REJECTED.title()).replace('-', ' '),
        (STATUS_PAID.title()).replace('-', ' '),
        (STATUS_CLOSED.title()).replace('-', ' '),
        (STATUS_CANCELLED.title()).replace('-', ' '),
    ]
    DISPLAY_ARRAY_ORDER_STATUSES = [
        (STATUS_PENDING.title()).replace('-', ' '),
        (STATUS_REQUESTED.title()).replace('-', ' '),
        (STATUS_REVIEWED.title()).replace('-', ' '),
        (STATUS_APPROVED.title()).replace('-', ' '),
        (STATUS_REJECTED.title()).replace('-', ' '),
        (STATUS_IN_PROGRESS.title()).replace('-', ' '),
        (STATUS_COMPLETED.title()).replace('-', ' '),
        (STATUS_CANCELLED.title()).replace('-', ' '),
    ]
    ORDER_STATUSES = (
        ('', '--select--'),
        (STATUS_PENDING, (STATUS_PENDING.title()).replace('-', ' ')),
        (STATUS_REQUESTED, (STATUS_REQUESTED.title()).replace('-', ' ')),
        (STATUS_LEVEL0_APPROVED, (STATUS_LEVEL0_APPROVED.title()).replace('-', ' ')),
        (STATUS_LEVEL1_APPROVED, (STATUS_LEVEL1_APPROVED.title()).replace('-', ' ')),
        (STATUS_LEVEL2_APPROVED, (STATUS_LEVEL2_APPROVED.title()).replace('-', ' ')),
        (STATUS_LEVEL3_APPROVED, (STATUS_LEVEL3_APPROVED.title()).replace('-', ' ')),
        (STATUS_LEVEL4_APPROVED, (STATUS_LEVEL4_APPROVED.title()).replace('-', ' ')),
        (STATUS_LEVEL5_APPROVED, (STATUS_LEVEL5_APPROVED.title()).replace('-', ' ')),
        (STATUS_LEVEL6_APPROVED, (STATUS_LEVEL6_APPROVED.title()).replace('-', ' ')),
        (STATUS_LEVEL1_REJECTED, (STATUS_LEVEL1_REJECTED.title()).replace('-', ' ')),
        (STATUS_LEVEL2_REJECTED, (STATUS_LEVEL2_REJECTED.title()).replace('-', ' ')),
        (STATUS_LEVEL3_REJECTED, (STATUS_LEVEL3_REJECTED.title()).replace('-', ' ')),
        (STATUS_LEVEL4_REJECTED, (STATUS_LEVEL4_REJECTED.title()).replace('-', ' ')),
        (STATUS_LEVEL5_REJECTED, (STATUS_LEVEL5_REJECTED.title()).replace('-', ' ')),
        (STATUS_LEVEL6_REJECTED, (STATUS_LEVEL6_REJECTED.title()).replace('-', ' ')),
        (STATUS_REVIEWED, (STATUS_REVIEWED.title()).replace('-', ' ')),
        (STATUS_APPROVED, (STATUS_APPROVED.title()).replace('-', ' ')),
        (STATUS_REJECTED, (STATUS_REJECTED.title()).replace('-', ' ')),
        (STATUS_ASSIGNED, (STATUS_ASSIGNED.title()).replace('-', ' ')),
        (STATUS_SUPPLIER_UPDATED, (STATUS_SUPPLIER_UPDATED.title()).replace('-', ' ')),
        (STATUS_PROPOSAL_GENERATED, (STATUS_PROPOSAL_GENERATED.title()).replace('-', ' ')),
        (STATUS_PROPOSAL_REQUESTED, (STATUS_PROPOSAL_REQUESTED.title()).replace('-', ' ')),
        (STATUS_PROPOSAL_SELECTED, (STATUS_PROPOSAL_SELECTED.title()).replace('-', ' ')),
        (STATUS_PURCHASE_GENERATED, (STATUS_PURCHASE_GENERATED.title()).replace('-', ' ')),
        (STATUS_ACKNOWLEDGED, (STATUS_ACKNOWLEDGED.title()).replace('-', ' ')),
        (STATUS_RECEIVED, (STATUS_RECEIVED.title()).replace('-', ' ')),
        (STATUS_INVOICE_UPLOADED, (STATUS_INVOICE_UPLOADED.title()).replace('-', ' ')),
        (STATUS_INVOICE_REVIEWED, (STATUS_INVOICE_REVIEWED.title()).replace('-', ' ')),
        (STATUS_INVOICE_PAYMENT_VOUCHER_GENERATED,
         (STATUS_INVOICE_PAYMENT_VOUCHER_GENERATED.title()).replace('-', ' ')),
        (STATUS_INVOICE_APPROVED, (STATUS_INVOICE_APPROVED.title()).replace('-', ' ')),
        (STATUS_INVOICE_REJECTED, (STATUS_INVOICE_REJECTED.title()).replace('-', ' ')),
        (STATUS_INVOICE_DAF_APPROVED, (STATUS_INVOICE_DAF_APPROVED.title()).replace('-', ' ')),
        (STATUS_INVOICE_DAF_REJECTED, (STATUS_INVOICE_DAF_REJECTED.title()).replace('-', ' ')),
        (STATUS_INVOICE_COP_APPROVED, (STATUS_INVOICE_COP_APPROVED.title()).replace('-', ' ')),
        (STATUS_INVOICE_COP_REJECTED, (STATUS_INVOICE_COP_REJECTED.title()).replace('-', ' ')),
        (STATUS_PAID, (STATUS_PAID.title()).replace('-', ' ')),
        (STATUS_CLOSED, (STATUS_CLOSED.title()).replace('-', ' ')),
        (STATUS_CANCELLED, (STATUS_CANCELLED.title()).replace('-', ' ')),
    )

    order_readable_status = ''

    order_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    order_code = models.CharField('Order Id', max_length=8, unique=True, blank=False, default=None)
    order_requester_name = models.CharField('Requester Name', max_length=100, blank=False)
    order_project_name = models.CharField('Project Name', max_length=100, blank=False)
    order_project_code = models.CharField('Project Code', max_length=100, blank=True)
    order_project_geo_code = models.CharField('Project GeoCode', max_length=100, blank=True)
    order_charge_code = models.CharField('Charge Code', max_length=100, blank=True)
    order_award_number = models.CharField('Award Number', max_length=100, blank=True)
    order_requisition_number = models.CharField('Requester Number', max_length=100, blank=True)
    order_donor = models.CharField('Donor', max_length=100, blank=True)
    order_description = models.CharField('Description', max_length=255, blank=True)
    order_anticipated_award_mechanism = models.CharField('Anticipated Award Mechanism', max_length=255, blank=True)
    order_anticipated_start_date = models.DateField('Anticipated Start Date',
                                                    default=settings.APP_CONSTANT_DEFAULT_DATE)
    order_anticipated_end_date = models.DateField('Anticipated End Date', default=settings.APP_CONSTANT_DEFAULT_DATE)
    order_special_considerations = models.CharField('Special Considerations', max_length=255, blank=True)
    order_procurement_method = models.CharField('Procurement Method', max_length=255, blank=False,
                                                choices=DROPDOWN_PROCUREMENT_METHODS, default='')
    order_procurement_method_updated_at = models.DateTimeField('Procurement Method Updated At',
                                                               default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_procurement_method_updated_id = models.CharField('Procurement Method Updated ID', max_length=100, blank=True)
    order_procurement_method_updated_by = models.CharField('Procurement Method Updated By', max_length=100, blank=True)
    order_procurement_method_updated_department = models.CharField('Procurement Method Updated Department',
                                                                   max_length=255, blank=True)
    order_procurement_method_updated_role = models.CharField('Procurement Method Updated Role', max_length=255,
                                                             blank=True)
    order_no_of_items = models.DecimalField('No. of Items', max_digits=10, decimal_places=0, default=Decimal(0))
    order_total_price = models.DecimalField('Total Amount', max_digits=10, decimal_places=0, default=Decimal(0))
    order_equipment_price = models.DecimalField('Equipment Cost', max_digits=10, decimal_places=0, default=Decimal(0))
    order_tax_price = models.DecimalField('Tax Amount', max_digits=10, decimal_places=0, default=Decimal(0))
    order_grand_total_price = models.DecimalField('Grand Total', max_digits=10, decimal_places=0, default=Decimal(0))
    order_currency = models.CharField('Currency', max_length=255, blank=False, choices=DROPDOWN_CURRENCIES,
                                      default=CURRENCY_RWF)
    order_supplier_category = models.CharField('Vendor Category', max_length=255, blank=False,
                                               choices=DROPDOWN_SUPPLIER_CATEGORIES, default='')
    order_supplier_updated_at = models.DateTimeField('Vendor Updated At',
                                                     default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_supplier_updated_id = models.CharField('Vendor Updated ID', max_length=100, blank=True)
    order_supplier_updated_by = models.CharField('Vendor Updated By', max_length=100, blank=True)
    order_supplier_updated_department = models.CharField('Vendor Updated Department', max_length=255, blank=True)
    order_supplier_updated_role = models.CharField('Vendor Updated Role', max_length=255, blank=True)

    order_email_to_supplier_subject = models.CharField('Email Subject', max_length=255, blank=True)
    # order_email_to_supplier_message = models.TextField('Email Message', blank=True)
    order_email_to_supplier_message = HTMLField('Email Message')
    order_email_to_supplier_proposal_submission_url = models.CharField('Proposal Submission URL', max_length=255,
                                                                       blank=True)
    order_email_to_supplier_updated_at = models.DateTimeField('Updated At',
                                                              default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_email_to_supplier_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    order_email_to_supplier_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    order_email_to_supplier_updated_department = models.CharField('Updated Department', max_length=255, blank=True)
    order_email_to_supplier_updated_role = models.CharField('Updated Role', max_length=255, blank=True)

    order_proposal_id = models.IntegerField('Proposal Id', blank=False, default=0)
    order_proposal_due_date = models.DateField('Proposal Due Date', default=settings.APP_CONSTANT_DEFAULT_DATE)
    order_purchase_no = models.CharField('Purchase Order No.', max_length=100, blank=True)
    order_invoice_no = models.CharField('Invoice No.', max_length=100, blank=True)
    order_payment_voucher_no = models.CharField('Voucher No.', max_length=100, blank=True)
    order_created_at = models.DateTimeField('Created At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_created_id = models.CharField('Created ID', max_length=100, blank=True)
    order_created_by = models.CharField('Created By', max_length=100, blank=True)
    order_created_department = models.CharField('Created Department', max_length=255, blank=True)
    order_created_role = models.CharField('Created Role', max_length=255, blank=True)
    order_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    order_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    order_updated_department = models.CharField('Updated Department', max_length=255, blank=True)
    order_updated_role = models.CharField('Updated Role', max_length=255, blank=True)
    order_requested_at = models.DateTimeField('Requested At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_requested_id = models.CharField('Requested ID', max_length=100, blank=True)
    order_requested_by = models.CharField('Requested By', max_length=100, blank=True)
    order_requested_department = models.CharField('Requested Department', max_length=255, blank=True)
    order_requested_role = models.CharField('Requested Role', max_length=255, blank=True)
    order_approval_no_of_levels = models.IntegerField('Approval Levels', blank=False, default=0)
    order_reviewed_at = models.DateTimeField('Reviewed At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_reviewed_id = models.CharField('Reviewed ID', max_length=100, blank=True)
    order_reviewed_by = models.CharField('Reviewed By', max_length=100, blank=True)
    order_reviewed_department = models.CharField('Reviewed Department', max_length=255, blank=True)
    order_reviewed_role = models.CharField('Reviewed Role', max_length=255, blank=True)
    order_approved_at = models.DateTimeField('Approved At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_approved_id = models.CharField('Approved ID', max_length=100, blank=True)
    order_approved_by = models.CharField('Approved By', max_length=100, blank=True)
    order_approved_department = models.CharField('Approved Department', max_length=255, blank=True)
    order_approved_role = models.CharField('Approved Role', max_length=255, blank=True)
    order_assigned_at = models.DateTimeField('Assigned At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_assigned_id = models.CharField('Assigned ID', max_length=100, blank=True)
    order_assigned_by = models.CharField('Assigned By', max_length=100, blank=True)
    order_assigned_department = models.CharField('Assigned Department', max_length=255, blank=True)
    order_assigned_role = models.CharField('Assigned Role', max_length=255, blank=True)
    order_assigned_to_at = models.DateTimeField('Assigned To At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_assigned_to_id = models.CharField('Assigned To ID', max_length=100, blank=True)
    order_assigned_to_by = models.CharField('Assigned To By', max_length=100, blank=True)
    order_assigned_to_department = models.CharField('Assigned To Department', max_length=255, blank=True)
    order_assigned_to_role = models.CharField('Assigned To Role', max_length=255, blank=True)
    order_proposal_generated_at = models.DateTimeField('Order Proposal Generated At',
                                                       default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_generated_id = models.CharField('Order Proposal Generated ID', max_length=100, blank=True)
    order_proposal_generated_by = models.CharField('Order Proposal Generated By', max_length=100, blank=True)
    order_proposal_generated_department = models.CharField('Order Proposal Generated Department', max_length=255,
                                                           blank=True)
    order_proposal_generated_role = models.CharField('Order Proposal Generated Role', max_length=255, blank=True)
    order_proposal_requested_at = models.DateTimeField('Order Proposal Requested At',
                                                       default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_requested_id = models.CharField('Order Proposal Requested ID', max_length=100, blank=True)
    order_proposal_requested_by = models.CharField('Order Proposal Requested By', max_length=100, blank=True)
    order_proposal_requested_department = models.CharField('Order Proposal Requested Department', max_length=255,
                                                           blank=True)
    order_proposal_requested_role = models.CharField('Order Proposal Requested Role', max_length=255, blank=True)
    order_proposal_selected_at = models.DateTimeField('Order Proposal Selected At',
                                                      default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_selected_id = models.CharField('Order Proposal Selected ID', max_length=100, blank=True)
    order_proposal_selected_by = models.CharField('Order Proposal Selected By', max_length=100, blank=True)
    order_proposal_selected_department = models.CharField('Order Proposal Selected Department', max_length=255,
                                                          blank=True)
    order_proposal_selected_role = models.CharField('Order Proposal Selected Role', max_length=255, blank=True)

    order_purchase_generated_at = models.DateTimeField('Purchase Order Generated At',
                                                       default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_purchase_generated_id = models.CharField('Purchase Order Generated ID', max_length=100, blank=True)
    order_purchase_generated_by = models.CharField('Purchase Order Generated By', max_length=100, blank=True)
    order_purchase_generated_department = models.CharField('Purchase Order Generated Department', max_length=255,
                                                           blank=True)
    order_purchase_generated_role = models.CharField('Purchase Order Generated Role', max_length=255, blank=True)
    order_acknowledged_at = models.DateTimeField('Order Acknowledged At',
                                                 default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_acknowledged_id = models.CharField('Order Acknowledged ID', max_length=100, blank=True)
    order_acknowledged_by = models.CharField('Order Acknowledged By', max_length=100, blank=True)
    order_acknowledged_department = models.CharField('Order Acknowledged Department', max_length=255,
                                                     blank=True)
    order_acknowledged_role = models.CharField('Order Acknowledged Role', max_length=255, blank=True)

    order_invoice_uploaded_at = models.DateTimeField('Uploaded At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_invoice_uploaded_id = models.CharField('Uploaded ID', max_length=100, blank=True)
    order_invoice_uploaded_by = models.CharField('Uploaded By', max_length=100, blank=True)
    order_invoice_uploaded_department = models.CharField('Uploaded Department', max_length=255, blank=True)
    order_invoice_uploaded_role = models.CharField('Uploaded Role', max_length=255, blank=True)

    order_invoice_reviewed_at = models.DateTimeField('Reviewed At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_invoice_reviewed_id = models.CharField('Reviewed ID', max_length=100, blank=True)
    order_invoice_reviewed_by = models.CharField('Reviewed By', max_length=100, blank=True)
    order_invoice_reviewed_department = models.CharField('Reviewed Department', max_length=255, blank=True)
    order_invoice_reviewed_role = models.CharField('Reviewed Role', max_length=255, blank=True)

    order_invoice_payment_voucher_uploaded_at = models.DateTimeField('Uploaded At',
                                                                     default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_invoice_payment_voucher_uploaded_id = models.CharField('Uploaded ID', max_length=100, blank=True)
    order_invoice_payment_voucher_uploaded_by = models.CharField('Uploaded By', max_length=100, blank=True)
    order_invoice_payment_voucher_uploaded_department = models.CharField('Uploaded Department', max_length=255,
                                                                         blank=True)
    order_invoice_payment_voucher_uploaded_role = models.CharField('Uploaded Role', max_length=255, blank=True)

    order_invoice_approval_updated_at = models.DateTimeField('Approved At',
                                                             default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_invoice_approval_updated_id = models.CharField('Approved ID', max_length=100, blank=True)
    order_invoice_approval_updated_by = models.CharField('Approved By', max_length=100, blank=True)
    order_invoice_approval_updated_department = models.CharField('Approved Department', max_length=255, blank=True)
    order_invoice_approval_updated_role = models.CharField('Approved Role', max_length=255, blank=True)

    order_invoice_daf_approval_updated_at = models.DateTimeField('Approved At',
                                                                 default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_invoice_daf_approval_updated_id = models.CharField('Approved ID', max_length=100, blank=True)
    order_invoice_daf_approval_updated_by = models.CharField('Approved By', max_length=100, blank=True)
    order_invoice_daf_approval_updated_department = models.CharField('Approved Department', max_length=255, blank=True)
    order_invoice_daf_approval_updated_role = models.CharField('Approved Role', max_length=255, blank=True)

    order_invoice_cop_approval_updated_at = models.DateTimeField('Approved At',
                                                                 default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_invoice_cop_approval_updated_id = models.CharField('Approved ID', max_length=100, blank=True)
    order_invoice_cop_approval_updated_by = models.CharField('Approved By', max_length=100, blank=True)
    order_invoice_cop_approval_updated_department = models.CharField('Approved Department', max_length=255, blank=True)
    order_invoice_cop_approval_updated_role = models.CharField('Approved Role', max_length=255, blank=True)

    order_paid_at = models.DateTimeField('Paid At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_paid_id = models.CharField('Paid ID', max_length=100, blank=True)
    order_paid_by = models.CharField('Paid By', max_length=100, blank=True)
    order_paid_department = models.CharField('Paid Department', max_length=255, blank=True)
    order_paid_role = models.CharField('Paid Role', max_length=255, blank=True)
    order_closed_at = models.DateTimeField('Closed At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_closed_id = models.CharField('Closed ID', max_length=100, blank=True)
    order_closed_by = models.CharField('Closed By', max_length=100, blank=True)
    order_closed_department = models.CharField('Closed Department', max_length=255, blank=True)
    order_closed_role = models.CharField('Closed Role', max_length=255, blank=True)
    order_cancelled_at = models.DateTimeField('Cancelled At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_cancelled_id = models.CharField('Cancelled ID', max_length=100, blank=True)
    order_cancelled_by = models.CharField('Cancelled By', max_length=100, blank=True)
    order_cancelled_department = models.CharField('Cancelled Department', max_length=255, blank=True)
    order_cancelled_role = models.CharField('Cancelled Role', max_length=255, blank=True)
    order_status = models.CharField('Status', max_length=255, blank=False, choices=ORDER_STATUSES,
                                    default=STATUS_PENDING)

    def __unicode__(self):
        return self.order_id

    @classmethod
    def generate_random_number(cls, attribute, length):
        token = ''
        unique_token_found = False
        while not unique_token_found:
            token = get_random_string(length, allowed_chars='0123456789')
            if (not token.startswith('0')) and Orders.objects.filter(**{attribute: token}).count() is 0:
                unique_token_found = True
        return token

    @classmethod
    def get_status_html_tag(cls, record):
        value = None
        if record.order_status == Orders.STATUS_PENDING:
            value = Utils.HTML_TAG_ORDER_STATUS_PENDING
        elif record.order_status == Orders.STATUS_REQUESTED:
            value = Utils.HTML_TAG_ORDER_STATUS_REQUESTED
        elif record.order_status == Orders.STATUS_LEVEL0_APPROVED:
            value = Utils.HTML_TAG_ORDER_STATUS_REQUESTED
        elif record.order_status == Orders.STATUS_LEVEL1_APPROVED:
            value = Utils.HTML_TAG_ORDER_STATUS_REQUESTED
        elif record.order_status == Orders.STATUS_LEVEL2_APPROVED:
            value = Utils.HTML_TAG_ORDER_STATUS_REQUESTED
        elif record.order_status == Orders.STATUS_LEVEL3_APPROVED:
            value = Utils.HTML_TAG_ORDER_STATUS_REQUESTED
        elif record.order_status == Orders.STATUS_LEVEL4_APPROVED:
            value = Utils.HTML_TAG_ORDER_STATUS_REQUESTED
        elif record.order_status == Orders.STATUS_LEVEL5_APPROVED:
            value = Utils.HTML_TAG_ORDER_STATUS_REQUESTED
        elif record.order_status == Orders.STATUS_LEVEL6_APPROVED:
            value = Utils.HTML_TAG_ORDER_STATUS_REQUESTED
        elif record.order_status == Orders.STATUS_LEVEL1_REJECTED:
            value = Utils.HTML_TAG_ORDER_STATUS_REJECTED
        elif record.order_status == Orders.STATUS_LEVEL2_REJECTED:
            value = Utils.HTML_TAG_ORDER_STATUS_REJECTED
        elif record.order_status == Orders.STATUS_LEVEL3_REJECTED:
            value = Utils.HTML_TAG_ORDER_STATUS_REJECTED
        elif record.order_status == Orders.STATUS_LEVEL4_REJECTED:
            value = Utils.HTML_TAG_ORDER_STATUS_REJECTED
        elif record.order_status == Orders.STATUS_LEVEL5_REJECTED:
            value = Utils.HTML_TAG_ORDER_STATUS_REJECTED
        elif record.order_status == Orders.STATUS_LEVEL6_REJECTED:
            value = Utils.HTML_TAG_ORDER_STATUS_REJECTED
        elif record.order_status == Orders.STATUS_REVIEWED:
            value = Utils.HTML_TAG_ORDER_STATUS_REVIEWED
        elif record.order_status == Orders.STATUS_APPROVED:
            value = Utils.HTML_TAG_ORDER_STATUS_APPROVED
        elif record.order_status == Orders.STATUS_REJECTED:
            value = Utils.HTML_TAG_ORDER_STATUS_REJECTED
        elif record.order_status == Orders.STATUS_ASSIGNED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_SUPPLIER_UPDATED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_PROPOSAL_GENERATED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_PROPOSAL_REQUESTED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_PROPOSAL_SELECTED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_PURCHASE_GENERATED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_ACKNOWLEDGED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_RECEIVED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_INVOICE_UPLOADED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_INVOICE_REVIEWED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_INVOICE_PAYMENT_VOUCHER_GENERATED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_INVOICE_APPROVED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_INVOICE_REJECTED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_INVOICE_DAF_APPROVED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_INVOICE_DAF_REJECTED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_INVOICE_COP_APPROVED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_INVOICE_COP_REJECTED:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_PAID:
            value = Utils.HTML_TAG_ORDER_STATUS_IN_PROGRESS
        elif record.order_status == Orders.STATUS_CLOSED:
            value = Utils.HTML_TAG_ORDER_STATUS_CLOSED
        elif record.order_status == Orders.STATUS_CANCELLED:
            value = Utils.HTML_TAG_ORDER_STATUS_CANCELLED
        return value

    @classmethod
    def get_filtered_orders(cls, operator):
        if operator.operator_type == Operators.TYPE_SUPER_ADMIN or operator.operator_type == Operators.TYPE_ADMIN or operator.operator_type == Operators.TYPE_MANAGER:
            objects = Orders.objects.all()
        else:
            objects = Orders.objects.all()
            if operator.operator_department == Operators.DEPARTMENT_NONE:
                objects = objects.filter(order_created_id=operator.operator_id)

            if operator.operator_department == Operators.DEPARTMENT_DCOP:
                if operator.operator_role == Operators.ROLE_NONE:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DCOP) &
                                             Q(order_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_DIRECTOR:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DCOP) &
                                             (Q(order_created_id__in=child_operators)))

                    child_operators = Operators.objects.filter(
                        Q(operator_department=Operators.DEPARTMENT_DCOP) &
                        Q(operator_role=Operators.ROLE_REGIONAL_MANAGER))

                    for child_operator in child_operators:
                        child_operators = Operators.get_child_operators(
                            Operators.objects.get(operator_id=child_operator.operator_id))
                        objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DCOP) &
                                                 (Q(order_created_id__in=child_operators)))

                if operator.operator_role == Operators.ROLE_ADVISER:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DCOP) &
                                             Q(order_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_REGIONAL_MANAGER:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DCOP) &
                                             (Q(order_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_DISTRICT_MANAGER:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DCOP) &
                                             (Q(order_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_FIELD_OFFICER:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DCOP) &
                                             Q(order_created_id=operator.operator_id))

            if operator.operator_department == Operators.DEPARTMENT_BFM:
                if operator.operator_role == Operators.ROLE_NONE:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_BFM) &
                                             Q(order_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_DIRECTOR:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_BFM) &
                                             (Q(order_created_id__in=child_operators)))
                if operator.operator_role == Operators.order_created_department:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_BFM) &
                                             Q(order_created_id=operator.operator_id))

            if operator.operator_department == Operators.DEPARTMENT_NUTRITION:
                if operator.operator_role == Operators.ROLE_NONE:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             Q(order_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_DIRECTOR:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             (Q(order_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_ADVISER:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             Q(order_created_id=operator.operator_id))

            if operator.operator_department == Operators.DEPARTMENT_DAF:
                if operator.operator_role == Operators.ROLE_NONE:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                             Q(order_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_DIRECTOR or operator.operator_role == Operators.ROLE_OPM:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                             (Q(order_created_id__in=child_operators)))

                    child_operators = Operators.objects.filter(
                        Q(operator_department=Operators.DEPARTMENT_DAF) &
                        Q(operator_role=Operators.ROLE_PROCUREMENT_OFFICER))

                    for child_operator in child_operators:
                        child_operators = Operators.get_child_operators(
                            Operators.objects.get(operator_id=child_operator.operator_id))
                        objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                                 (Q(order_created_id__in=child_operators)))

                    child_operators = Operators.objects.filter(
                        Q(operator_department=Operators.DEPARTMENT_DAF) &
                        Q(operator_role=Operators.ROLE_HR_MANAGER))

                    for child_operator in child_operators:
                        child_operators = Operators.get_child_operators(
                            Operators.objects.get(operator_id=child_operator.operator_id))
                        objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                                 (Q(order_created_id__in=child_operators)))

                    child_operators = Operators.objects.filter(
                        Q(operator_department=Operators.DEPARTMENT_DAF) &
                        Q(operator_role=Operators.ROLE_RECEPTIONIST))

                    for child_operator in child_operators:
                        child_operators = Operators.get_child_operators(
                            Operators.objects.get(operator_id=child_operator.operator_id))
                        objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                                 (Q(order_created_id__in=child_operators)))

                    child_operators = Operators.objects.filter(
                        Q(operator_department=Operators.DEPARTMENT_DAF) &
                        Q(operator_role=Operators.ROLE_STOCK_ADMIN))

                    for child_operator in child_operators:
                        child_operators = Operators.get_child_operators(
                            Operators.objects.get(operator_id=child_operator.operator_id))
                        objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                                 (Q(order_created_id__in=child_operators)))

                    child_operators = Operators.objects.filter(
                        Q(operator_department=Operators.DEPARTMENT_DAF) &
                        Q(operator_role=Operators.ROLE_ACCOUNTANT_MANAGER))

                    for child_operator in child_operators:
                        child_operators = Operators.get_child_operators(
                            Operators.objects.get(operator_id=child_operator.operator_id))
                        objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                                 (Q(order_created_id__in=child_operators)))

                if operator.operator_role == Operators.ROLE_ADVISER:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                             Q(order_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_PROCUREMENT_OFFICER:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                             (Q(order_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_HR_MANAGER:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                             (Q(order_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_RECEPTIONIST:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                             (Q(order_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_STOCK_ADMIN:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                             (Q(order_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_ACCOUNTANT_MANAGER:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                             (Q(order_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_ACCOUNTANT_OFFICER:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_DAF) &
                                             Q(order_created_id=operator.operator_id))

            if operator.operator_department == Operators.DEPARTMENT_MAV:
                if operator.operator_role == Operators.ROLE_NONE:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             Q(order_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_DIRECTOR:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             (Q(order_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_ADVISER:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             Q(order_created_id=operator.operator_id))

            if operator.operator_department == Operators.DEPARTMENT_GRANT_MANAGER:
                if operator.operator_role == Operators.ROLE_NONE:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             Q(order_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_DIRECTOR:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             (Q(order_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_ADVISER:
                    objects = objects.filter(Q(order_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             Q(order_created_id=operator.operator_id))

        return objects

    @classmethod
    def update_grand_total(cls, request, model, operator):

        order_items = Order_Items.objects.filter(orders_order_id=model.order_id).all()

        currency = Orders.CURRENCY_RWF
        order_total_price = 0
        for order_item in order_items:
            order_total_price += order_item.order_item_total_price
            currency = order_item.order_item_currency

        model.order_no_of_items = order_items.count()
        model.order_total_price = order_total_price
        model.order_grand_total_price = model.order_total_price + model.order_equipment_price + model.order_tax_price
        model.order_currency = currency

        model.save()
        return True

    @classmethod
    def add_order_approval(cls, request, type, model, operator, parent_operator, add_approval):

        if add_approval:
            if type == 'request':
                model.order_approval_no_of_levels = 1
                model.save()
            if type == 'approve':
                model.order_approval_no_of_levels = model.order_approval_no_of_levels + 1
                model.save()

            order_approval = Order_Approvals()
            order_approval.orders_order_id = model.order_id
            order_approval.order_approval_level = model.order_approval_no_of_levels
            order_approval.order_approval_created_at = Utils.get_current_datetime_utc()
            order_approval.order_approval_created_id = operator.operator_id
            order_approval.order_approval_created_by = operator.operator_name
            order_approval.order_approval_created_department = operator.operator_department
            order_approval.order_approval_created_role = operator.operator_role
            order_approval.order_approval_updated_at = Utils.get_current_datetime_utc()
            order_approval.order_approval_updated_id = parent_operator.operator_id
            order_approval.order_approval_updated_by = parent_operator.operator_name
            order_approval.order_approval_updated_department = parent_operator.operator_department
            order_approval.order_approval_updated_role = parent_operator.operator_role
            order_approval.order_approval_status = Order_Approvals.STATUS_PENDING
            order_approval.save()

        Notifications.add_notification(
            Notifications.TYPE_OPERATOR,
            operator.operator_id,
            Notifications.TYPE_OPERATOR,
            parent_operator.operator_id,
            Notifications.TYPE_ORDER,
            model.order_id,
            "Created a purchase request to review.",
            "/backend/orders/view/" + str(model.order_id) + "/"
        )

    @classmethod
    def request_or_level_approval_order(cls, request, type, model, operator):

        if type == 'request':
            model.order_requested_at = Utils.get_current_datetime_utc()
            model.order_requested_id = operator.operator_id
            model.order_requested_by = operator.operator_name
            model.order_requested_department = operator.operator_department
            model.order_requested_role = operator.operator_role
            model.order_status = Orders.STATUS_REQUESTED
            model.save()

        if type == 'approve' or type == 'reject':
            order_approvals = Order_Approvals.objects.filter(
                Q(orders_order_id=model.order_id) &
                Q(order_approval_updated_id=operator.operator_id) &
                Q(order_approval_status=Order_Approvals.STATUS_PENDING)
            )

            if order_approvals.count() == 1:
                for order_approval in order_approvals:
                    level = order_approval.order_approval_level
                    order_approval.order_approval_updated_at = Utils.get_current_datetime_utc()
                    if type == 'approve':
                        order_approval.order_approval_status = Order_Approvals.STATUS_APPROVED
                    if type == 'reject':
                        order_approval.order_approval_status = Order_Approvals.STATUS_REJECTED
                    order_approval.save()
                    if type == 'approve':
                        if level == 1:
                            model.order_status = Orders.STATUS_LEVEL1_APPROVED
                        if level == 2:
                            model.order_status = Orders.STATUS_LEVEL2_APPROVED
                        if level == 3:
                            model.order_status = Orders.STATUS_LEVEL3_APPROVED
                        if level == 4:
                            model.order_status = Orders.STATUS_LEVEL4_APPROVED
                        model.save()

                        level_order_approvals = Order_Approvals.objects.filter(
                            Q(orders_order_id=model.order_id)
                        )
                        # .exclude(Q(order_approval_status=Order_Approvals.STATUS_FIXED))
                        for level_order_approval in level_order_approvals:
                            Notifications.add_notification(
                                Notifications.TYPE_OPERATOR,
                                level_order_approval.order_approval_updated_id,
                                Notifications.TYPE_OPERATOR,
                                level_order_approval.order_approval_created_id,
                                Notifications.TYPE_ORDER,
                                model.order_id,
                                "Approved your purchase request at level " + str(level) + ".",
                                "/backend/orders/view/" + str(model.order_id) + "/"
                            )

                    if type == 'reject':
                        if level == 1:
                            model.order_status = Orders.STATUS_LEVEL1_REJECTED
                        if level == 2:
                            model.order_status = Orders.STATUS_LEVEL2_REJECTED
                        if level == 3:
                            model.order_status = Orders.STATUS_LEVEL3_REJECTED
                        if level == 4:
                            model.order_status = Orders.STATUS_LEVEL4_REJECTED
                        model.save()

                        level_order_approvals = Order_Approvals.objects.filter(
                            Q(orders_order_id=model.order_id)
                        )
                        # .exclude(Q(order_approval_status=Order_Approvals.STATUS_FIXED))
                        for level_order_approval in level_order_approvals:
                            Notifications.add_notification(
                                Notifications.TYPE_OPERATOR,
                                level_order_approval.order_approval_updated_id,
                                Notifications.TYPE_OPERATOR,
                                level_order_approval.order_approval_created_id,
                                Notifications.TYPE_ORDER,
                                model.order_id,
                                "Rejected your purchase request at level " + str(level) + ".",
                                "/backend/orders/view/" + str(model.order_id) + "/"
                            )

        parent_operator = None
        if operator.operator_parent_id != 0:
            parent_operator = Operators.objects.get(operator_id=operator.operator_parent_id)

        if parent_operator is not None and (type == 'request' or type == 'approve'):
            Orders.add_order_approval(request, type, model, operator, parent_operator, True)
        else:
            operators = None
            if operator.operator_type == Operators.TYPE_SUPER_ADMIN or operator.operator_type == Operators.TYPE_ADMIN:
                model.order_status = Orders.STATUS_LEVEL0_APPROVED
                model.save()
                operators = Operators.objects.all().filter(operator_role=Operators.ROLE_OPM)
            else:
                if operator.operator_department == Operators.DEPARTMENT_NONE:
                    model.order_status = Orders.STATUS_LEVEL0_APPROVED
                    model.save()
                    operators = Operators.objects.all().filter(operator_role=Operators.ROLE_OPM)

                if operator.operator_department == Operators.DEPARTMENT_DCOP:
                    if operator.operator_role == Operators.ROLE_NONE or operator.operator_role == Operators.ROLE_DIRECTOR or operator.operator_role == Operators.ROLE_ADVISER:
                        model.order_status = Orders.STATUS_LEVEL0_APPROVED
                        model.save()
                        operators = Operators.objects.all().filter(
                            operator_role=Operators.ROLE_OPM)
                    if operator.operator_role == Operators.ROLE_REGIONAL_MANAGER or operator.operator_role == Operators.ROLE_DISTRICT_MANAGER or operator.operator_role == Operators.ROLE_FIELD_OFFICER:
                        operators = Operators.objects.all().filter(
                            (Q(operator_department=Operators.DEPARTMENT_DCOP) &
                             Q(operator_role=ROLE_DIRECTOR)))

                if operator.operator_department == Operators.DEPARTMENT_BFM:
                    if operator.operator_role == Operators.ROLE_NONE or operator.operator_role == Operators.ROLE_DIRECTOR or operator.operator_role == Operators.ROLE_ADVISER:
                        model.order_status = Orders.STATUS_LEVEL0_APPROVED
                        model.save()
                        operators = Operators.objects.all().filter(
                            operator_role=Operators.ROLE_OPM)

                if operator.operator_department == Operators.DEPARTMENT_NUTRITION:
                    if operator.operator_role == Operators.ROLE_NONE or operator.operator_role == Operators.ROLE_DIRECTOR or operator.operator_role == Operators.ROLE_ADVISER:
                        model.order_status = Orders.STATUS_LEVEL0_APPROVED
                        model.save()
                        operators = Operators.objects.all().filter(
                            operator_role=Operators.ROLE_OPM)

                if operator.operator_department == Operators.DEPARTMENT_DAF:
                    if operator.operator_role == Operators.ROLE_NONE or operator.operator_role == Operators.ROLE_DIRECTOR or operator.operator_role == Operators.ROLE_ADVISER or operator.operator_role == Operators.ROLE_OPM:
                        model.order_status = Orders.STATUS_LEVEL0_APPROVED
                        model.save()
                        operators = Operators.objects.all().filter(
                            operator_role=Operators.ROLE_OPM)

                    if operator.operator_role == Operators.ROLE_PROCUREMENT_OFFICER or operator.operator_role == Operators.ROLE_HR_MANAGER or operator.operator_role == Operators.ROLE_RECEPTIONIST or operator.operator_role == Operators.ROLE_STOCK_ADMIN or operator.operator_role == Operators.ROLE_ACCOUNTANT_MANAGER or operator.operator_role == Operators.ROLE_ACCOUNTANT_OFFICER:
                        operators = Operators.objects.all().filter(
                            (Q(operator_department=Operators.DEPARTMENT_DAF) &
                             Q(operator_role=ROLE_DIRECTOR)))

                if operator.operator_department == Operators.DEPARTMENT_MAV:
                    if operator.operator_role == Operators.ROLE_NONE or operator.operator_role == Operators.ROLE_DIRECTOR or operator.operator_role == Operators.ROLE_ADVISER:
                        model.order_status = Orders.STATUS_LEVEL0_APPROVED
                        model.save()
                        operators = Operators.objects.all().filter(
                            operator_role=Operators.ROLE_OPM)

                if operator.operator_department == Operators.DEPARTMENT_GRANT_MANAGER:
                    if operator.operator_role == Operators.ROLE_NONE or operator.operator_role == Operators.ROLE_DIRECTOR or operator.operator_role == Operators.ROLE_ADVISER:
                        model.order_status = Orders.STATUS_LEVEL0_APPROVED
                        model.save()
                        operators = Operators.objects.all().filter(
                            operator_role=Operators.ROLE_OPM)

            if operators.count() == 0:
                model.order_status = Orders.STATUS_LEVEL0_APPROVED
                model.save()
                operators = Operators.objects.all().filter(operator_role=Operators.ROLE_OPM)

            if operators.count() == 0:
                model.order_status = Orders.STATUS_LEVEL0_APPROVED
                model.save()
                operators = Operators.objects.all().filter(operator_type=Operators.TYPE_ADMIN)

            for item in operators:
                add_approval = True
                if model.order_status != Orders.STATUS_LEVEL0_APPROVED:
                    add_approval = False
                Orders.add_order_approval(request, type, model, operator, item, add_approval)

        return True

    @classmethod
    def level_approval_order(cls, request, model, operator):

        model.order_requested_at = Utils.get_current_datetime_utc()
        model.order_requested_id = operator.operator_id
        model.order_requested_by = operator.operator_name
        model.order_requested_department = operator.operator_department
        model.order_requested_role = operator.operator_role
        model.order_status = Orders.STATUS_REQUESTED
        model.save()

    @classmethod
    def delete_order(cls, request, model, operator):
        # Order_Logs.add(
        #     model.order_id,
        #     'Deleted ' + Orders.SINGULAR_TITLE,
        #     Utils.get_browser_details_from_request(request),
        #     Utils.get_ip_address(request),
        #     operator.operator_username,
        # )
        #
        # model.delete()
        return True


# noinspection PyPep8Naming
class Order_Logs(models.Model):
    TITLE = Orders.SINGULAR_TITLE + ' Logs'
    NAME = "-".join((TITLE.lower()).split())
    order_log_id = models.AutoField('Log Id', primary_key=True)
    orders_order_id = models.IntegerField(Orders.SINGULAR_TITLE + ' Id', default=0)
    order_log_message = models.CharField('Message', max_length=255, blank=True)
    order_log_browser = models.TextField('Browser', blank=True)
    order_log_ip_address = models.CharField('Ip address', max_length=30, blank=True)
    order_log_updated_at = models.DateTimeField('Updated at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_log_updated_by = models.EmailField('Updated by', max_length=255, blank=True)

    @classmethod
    def add(cls, order_id, message, browser, ip_address, updated_by):
        log = Order_Logs()
        log.orders_order_id = order_id
        log.order_log_message = message
        log.order_log_browser = browser
        log.order_log_ip_address = ip_address
        log.order_log_updated_at = Utils.get_current_datetime_utc()
        log.order_log_updated_by = updated_by
        return log.save('Added ' + Orders.SINGULAR_TITLE + ' Log')


# Create your models here.
# noinspection PyUnresolvedReferences
class Order_Approvals(models.Model):
    TITLE = settings.MODEL_ORDER_APPROVALS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_ORDER_APPROVALS_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'

    ARRAY_STATUSES = [
        (STATUS_PENDING.title()).replace('-', ' '),
        (STATUS_APPROVED.title()).replace('-', ' '),
        (STATUS_REJECTED.title()).replace('-', ' '),
    ]
    DROPDOWN_STATUSES = (
        ('', '--select--'),
        (STATUS_PENDING, (STATUS_PENDING.title()).replace('-', ' ')),
        (STATUS_APPROVED, (STATUS_APPROVED.title()).replace('-', ' ')),
        (STATUS_REJECTED, (STATUS_REJECTED.title()).replace('-', ' ')),
    )

    order_approval_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    orders_order_id = models.IntegerField('Order Id', blank=False)
    order_approval_level = models.IntegerField('Approval Level', blank=False)
    order_approval_created_at = models.DateTimeField('Created At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_approval_created_id = models.CharField('Created ID', max_length=100, blank=True)
    order_approval_created_by = models.CharField('Created By', max_length=100, blank=True)
    order_approval_created_department = models.CharField('Created Department', max_length=255, blank=True)
    order_approval_created_role = models.CharField('Updated Role', max_length=255, blank=True)
    order_approval_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_approval_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    order_approval_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    order_approval_updated_department = models.CharField('Updated Department', max_length=255, blank=True)
    order_approval_updated_role = models.CharField('Updated Role', max_length=255, blank=True)
    order_approval_status = models.CharField('Status', max_length=255, blank=False, choices=DROPDOWN_STATUSES,
                                             default=STATUS_PENDING)

    def __unicode__(self):
        return self.order_id


# Create your models here.
# noinspection PyUnresolvedReferences
class Order_Payments(models.Model):
    TITLE = settings.MODEL_ORDER_PAYMENTS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_ORDER_PAYMENTS_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    order_payment_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    orders_order_id = models.IntegerField('Order Id', blank=False)
    order_payment_paid_at = models.DateTimeField('Paid At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_payment_paid_id = models.CharField('Paid ID', max_length=100, blank=True)
    order_payment_paid_by = models.CharField('Paid By', max_length=100, blank=True)
    order_payment_paid_department = models.CharField('Paid Department', max_length=255, blank=True)
    order_payment_paid_role = models.CharField('Paid Role', max_length=255, blank=True)
    order_payment_paid_amount = models.DecimalField('Paid Amount', max_digits=10, decimal_places=0, default=Decimal(0))
    order_payment_paid_pending = models.DecimalField('Pending Amount', max_digits=10, decimal_places=0,
                                                     default=Decimal(0))
    order_payment_paid_note = models.CharField('Paid Note', max_length=255, blank=True)

    def __unicode__(self):
        return self.order_payment_id


# Create your models here.
# noinspection PyUnresolvedReferences
class Order_Proposals(models.Model):
    TITLE = settings.MODEL_ORDER_PROPOSALS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_ORDER_PROPOSALS_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    CURRENCY_USD = 'USD'
    CURRENCY_RWF = 'RWF'

    ARRAY_CURRENCIES = [
        CURRENCY_USD,
        CURRENCY_RWF,
    ]
    DROPDOWN_CURRENCIES = (
        ('', '--select--'),
        (CURRENCY_USD, CURRENCY_USD),
        (CURRENCY_RWF, CURRENCY_RWF),
    )

    STATUS_PENDING = 'pending'
    STATUS_EVALUATED = 'evaluated'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_SELECTED = 'selected'
    STATUS_ACKNOWLEDGED = 'acknowledged'

    ARRAY_STATUSES = [
        (STATUS_PENDING.title()).replace('-', ' '),
        (STATUS_EVALUATED.title()).replace('-', ' '),
        (STATUS_APPROVED.title()).replace('-', ' '),
        (STATUS_REJECTED.title()).replace('-', ' '),
        (STATUS_SELECTED.title()).replace('-', ' '),
        (STATUS_ACKNOWLEDGED.title()).replace('-', ' '),
    ]
    DROPDOWN_STATUSES = (
        ('', '--select--'),
        (STATUS_PENDING, (STATUS_PENDING.title()).replace('-', ' ')),
        (STATUS_EVALUATED, (STATUS_EVALUATED.title()).replace('-', ' ')),
        (STATUS_APPROVED, (STATUS_APPROVED.title()).replace('-', ' ')),
        (STATUS_REJECTED, (STATUS_REJECTED.title()).replace('-', ' ')),
        (STATUS_SELECTED, (STATUS_SELECTED.title()).replace('-', ' ')),
        (STATUS_ACKNOWLEDGED, (STATUS_ACKNOWLEDGED.title()).replace('-', ' ')),
    )

    SUPPLIER_TYPE_COMPANY = 'company'
    SUPPLIER_TYPE_ASSOCIATION = 'association'
    SUPPLIER_TYPE_INDIVIDUAL = 'individual'

    ARRAY_SUPPLIER_TYPES = [
        (SUPPLIER_TYPE_COMPANY.title()).replace('-', ' '),
        (SUPPLIER_TYPE_ASSOCIATION.title()).replace('-', ' '),
        (SUPPLIER_TYPE_INDIVIDUAL.title()).replace('-', ' '),
    ]
    DROPDOWN_SUPPLIER_TYPES = (
        ('', '--select--'),
        (SUPPLIER_TYPE_COMPANY, (SUPPLIER_TYPE_COMPANY.title()).replace('-', ' ')),
        (SUPPLIER_TYPE_ASSOCIATION, (SUPPLIER_TYPE_ASSOCIATION.title()).replace('-', ' ')),
        (SUPPLIER_TYPE_INDIVIDUAL, (SUPPLIER_TYPE_INDIVIDUAL.title()).replace('-', ' ')),
    )

    order_proposal_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    order_proposal_code = models.CharField('Proposal Id', max_length=8, unique=True, blank=False, default=None)
    orders_order_id = models.IntegerField('Order Id', blank=False)
    order_proposal_supplier_category = models.CharField('Vendor Category', max_length=255, blank=False)
    order_proposal_supplier_company_type = models.CharField('Type', max_length=255, blank=True,
                                                            choices=DROPDOWN_SUPPLIER_TYPES, default='')
    order_proposal_supplier_title = models.CharField('Name', max_length=255, blank=True)
    order_proposal_supplier_details = models.CharField('Details', max_length=255, blank=True)
    order_proposal_supplier_rf_number = models.CharField('RFQ/RFP/RFA', max_length=255, blank=True)
    order_proposal_supplier_proposal_title = models.CharField('Tender Description Title', max_length=255, blank=True)
    order_proposal_supplier_legal_representatives = models.CharField('Names of Legal Representatives', max_length=255,
                                                                     blank=True)
    order_proposal_supplier_address_plot_no = models.CharField('Plot No.', max_length=255, blank=True)
    order_proposal_supplier_address_street = models.CharField('Street', max_length=255, blank=True)
    order_proposal_supplier_address_av_no = models.CharField('AV No.', max_length=255, blank=True)
    order_proposal_supplier_address_sector = models.CharField('Sector', max_length=255, blank=True)
    order_proposal_supplier_address_district = models.CharField('District', max_length=255, blank=True)
    order_proposal_supplier_address_country = models.CharField('Country', max_length=255, blank=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+250123456789'. Up to 13 digits allowed.")
    order_proposal_supplier_contact_phone_number = models.CharField('Phone Number',
                                                                    validators=[phone_regex, MinLengthValidator(10),
                                                                                MaxLengthValidator(13)], max_length=13,
                                                                    blank=True)
    order_proposal_supplier_contact_email_id = models.EmailField('Email id', max_length=100, blank=True)
    order_proposal_supplier_tin_number = models.CharField('TIN Number', max_length=255, blank=True)
    order_proposal_supplier_bank_account_details = models.CharField('Bank Account Details', max_length=255, blank=True)

    order_proposal_supplier_previous_reference1_name = models.CharField('Bank Account Details', max_length=255,
                                                                        blank=True)
    order_proposal_supplier_previous_reference1_contact_person = models.CharField('Bank Account Details',
                                                                                  max_length=255, blank=True)
    order_proposal_supplier_previous_reference1_contact_number = models.CharField('Phone Number',
                                                                                  validators=[phone_regex,
                                                                                              MinLengthValidator(10),
                                                                                              MaxLengthValidator(13)],
                                                                                  max_length=13,
                                                                                  blank=True)
    order_proposal_supplier_previous_reference1_contact_email_id = models.EmailField('Email id', max_length=100,
                                                                                     blank=True)
    order_proposal_supplier_previous_reference2_name = models.CharField('Bank Account Details', max_length=255,
                                                                        blank=True)
    order_proposal_supplier_previous_reference2_contact_person = models.CharField('Bank Account Details',
                                                                                  max_length=255, blank=True)
    order_proposal_supplier_previous_reference2_contact_number = models.CharField('Phone Number',
                                                                                  validators=[phone_regex,
                                                                                              MinLengthValidator(10),
                                                                                              MaxLengthValidator(13)],
                                                                                  max_length=13,
                                                                                  blank=True)
    order_proposal_supplier_previous_reference2_contact_email_id = models.EmailField('Email id', max_length=100,
                                                                                     blank=True)
    order_proposal_supplier_previous_reference3_name = models.CharField('Bank Account Details', max_length=255,
                                                                        blank=True)
    order_proposal_supplier_previous_reference3_contact_person = models.CharField('Bank Account Details',
                                                                                  max_length=255, blank=True)
    order_proposal_supplier_previous_reference3_contact_number = models.CharField('Phone Number',
                                                                                  validators=[phone_regex,
                                                                                              MinLengthValidator(10),
                                                                                              MaxLengthValidator(13)],
                                                                                  max_length=13,
                                                                                  blank=True)
    order_proposal_supplier_previous_reference3_contact_email_id = models.EmailField('Email id', max_length=100,
                                                                                     blank=True)

    order_proposal_cost = models.DecimalField('Proposal Cost', max_digits=10, decimal_places=0, default=Decimal(0))
    order_proposal_cost_currency = models.CharField('Currency', max_length=255, blank=False,
                                                    choices=DROPDOWN_CURRENCIES,
                                                    default=CURRENCY_RWF)
    order_proposal_evaluated_score = models.IntegerField('Score', blank=False, default=0)
    order_proposal_evaluation_details = models.CharField('Comments', max_length=255, blank=True)
    order_proposal_created_at = models.DateTimeField('Created At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_created_id = models.CharField('Created ID', max_length=100, blank=True)
    order_proposal_created_by = models.CharField('Created By', max_length=100, blank=True)
    order_proposal_created_department = models.CharField('Created Department', max_length=255, blank=True)
    order_proposal_created_role = models.CharField('Created Role', max_length=255, blank=True)
    order_proposal_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    order_proposal_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    order_proposal_updated_department = models.CharField('Updated Department', max_length=255, blank=True)
    order_proposal_updated_role = models.CharField('Updated Role', max_length=255, blank=True)
    order_proposal_evaluated_at = models.DateTimeField('Evaluated At',
                                                       default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_evaluated_id = models.CharField('Evaluated ID', max_length=100, blank=True)
    order_proposal_evaluated_by = models.CharField('Evaluated By', max_length=100, blank=True)
    order_proposal_evaluated_department = models.CharField('Evaluated Department', max_length=255, blank=True)
    order_proposal_evaluated_role = models.CharField('Evaluated Role', max_length=255, blank=True)
    order_proposal_approval_updated_at = models.DateTimeField('Approval Updated At',
                                                              default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_approval_updated_id = models.CharField('Approval Updated ID', max_length=100, blank=True)
    order_proposal_approval_updated_by = models.CharField('Approval Updated By', max_length=100, blank=True)
    order_proposal_approval_updated_department = models.CharField('Approval Updated Department', max_length=255,
                                                                  blank=True)
    order_proposal_approval_updated_role = models.CharField('Approval Updated Role', max_length=255, blank=True)
    order_proposal_selected_at = models.DateTimeField('Selected At',
                                                      default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_selected_id = models.CharField('Selected ID', max_length=100, blank=True)
    order_proposal_selected_by = models.CharField('Selected By', max_length=100, blank=True)
    order_proposal_selected_department = models.CharField('Selected Department', max_length=255, blank=True)
    order_proposal_selected_role = models.CharField('Selected Role', max_length=255, blank=True)
    order_proposal_acknowledged_at = models.DateTimeField('Acknowledged At',
                                                          default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_acknowledged_id = models.CharField('Acknowledged ID', max_length=100, blank=True)
    order_proposal_acknowledged_by = models.CharField('Acknowledged By', max_length=100, blank=True)
    order_proposal_acknowledged_department = models.CharField('Acknowledged Department', max_length=255, blank=True)
    order_proposal_acknowledged_role = models.CharField('Acknowledged Role', max_length=255, blank=True)
    order_proposal_status = models.CharField('Status', max_length=255, blank=False, choices=DROPDOWN_STATUSES,
                                             default=STATUS_PENDING)

    def __unicode__(self):
        return self.order_proposal_id

    @classmethod
    def generate_random_number(cls, attribute, length):
        token = ''
        unique_token_found = False
        while not unique_token_found:
            token = get_random_string(length, allowed_chars='0123456789')
            if (not token.startswith('0')) and Order_Proposals.objects.filter(**{attribute: token}).count() is 0:
                unique_token_found = True
        return token


# Create your models here.
# noinspection PyUnresolvedReferences
class Order_Items(models.Model):
    TITLE = settings.MODEL_ORDER_ITEMS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_ORDER_ITEM_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    TYPE_GOODS = 'goods'
    TYPE_ASSET = 'asset'
    TYPE_SERVICE = 'service'

    ARRAY_TYPES = [
        TYPE_GOODS,
        TYPE_ASSET,
        TYPE_SERVICE,
    ]
    DROPDOWN_TYPES = (
        ('', '--select--'),
        (TYPE_GOODS, TYPE_GOODS),
        (TYPE_ASSET, TYPE_ASSET),
        (TYPE_SERVICE, TYPE_SERVICE),
    )

    CURRENCY_USD = 'USD'
    CURRENCY_RWF = 'RWF'

    ARRAY_CURRENCIES = [
        CURRENCY_USD,
        CURRENCY_RWF,
    ]
    DROPDOWN_CURRENCIES = (
        ('', '--select--'),
        (CURRENCY_USD, CURRENCY_USD),
        (CURRENCY_RWF, CURRENCY_RWF),
    )

    STATUS_PENDING = 'pending'
    STATUS_RECEIVED = 'received'

    ARRAY_STATUSES = [
        (STATUS_PENDING.title()).replace('-', ' '),
        (STATUS_RECEIVED.title()).replace('-', ' '),
    ]
    DROPDOWN_STATUSES = (
        ('', '--select--'),
        (STATUS_PENDING, (STATUS_PENDING.title()).replace('-', ' ')),
        (STATUS_RECEIVED, (STATUS_RECEIVED.title()).replace('-', ' ')),
    )

    order_item_total_price = 0

    order_item_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    orders_order_id = models.IntegerField('Order Id', blank=False)
    order_item_type = models.CharField('Type', max_length=255, blank=False, choices=DROPDOWN_TYPES, default=TYPE_GOODS)
    order_item_type_id = models.IntegerField('Type Id', blank=False, default=0)
    order_item_title = models.CharField('Item Details', max_length=255, blank=False)
    order_item_sub_title = models.CharField('Item Details', max_length=255, blank=True)
    order_item_duration = models.IntegerField('Time in Days', blank=False, default=0)
    order_item_quantity_ordered = models.DecimalField('Quantity Ordered', max_digits=10, decimal_places=0,
                                                      default=Decimal(0))
    order_item_quantity_unit = models.CharField('Quantity Unit', max_length=255, blank=True)
    order_item_unit_price = models.DecimalField('Unit Price', max_digits=10, decimal_places=0, default=Decimal(0))
    order_item_total_price = models.DecimalField('Total Price', max_digits=10, decimal_places=0, default=Decimal(0))
    order_item_currency = models.CharField('Currency', max_length=255, blank=False, choices=DROPDOWN_CURRENCIES,
                                           default=CURRENCY_RWF)
    order_item_usaid_approval = models.BooleanField('USAID Approval', default=False)
    order_item_created_at = models.DateTimeField('Created At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_item_created_id = models.CharField('Created ID', max_length=100, blank=True)
    order_item_created_by = models.CharField('Created By', max_length=100, blank=True)
    order_item_created_department = models.CharField('Created Department', max_length=255, blank=True)
    order_item_created_role = models.CharField('Created Role', max_length=255, blank=True)
    order_item_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_item_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    order_item_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    order_item_updated_department = models.CharField('Updated Department', max_length=255, blank=True)
    order_item_updated_role = models.CharField('Updated Role', max_length=255, blank=True)
    order_item_received_at = models.DateTimeField('Received At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_item_received_id = models.CharField('Received ID', max_length=100, blank=True)
    order_item_received_by = models.CharField('Received By', max_length=100, blank=True)
    order_item_received_department = models.CharField('Received Department', max_length=255, blank=True)
    order_item_received_role = models.CharField('Received Role', max_length=255, blank=True)
    order_item_status = models.CharField('Status', max_length=255, blank=False, choices=DROPDOWN_STATUSES,
                                         default=STATUS_PENDING)

    def __unicode__(self):
        return self.order_item_id

    @classmethod
    def get_status_html_tag(cls, record):
        value = None
        if record.order_item_status == Order_Items.STATUS_PENDING:
            value = Utils.HTML_TAG_ORDER_ITEM_STATUS_PENDING
        elif record.order_item_status == Order_Items.STATUS_RECEIVED:
            value = Utils.HTML_TAG_ORDER_ITEM_STATUS_RECEIVED
        return value

    @classmethod
    def delete_order_item(cls, request, model, operator):
        model.delete()
        return True


# noinspection PyPep8Naming
class Access_Permissions(models.Model):
    access_permission_name = models.CharField('Access Permission Name', primary_key=True, max_length=100, blank=False,
                                              unique=True)
    access_permission_details = models.CharField('Details', max_length=255, blank=True)
    access_permission_created_at = models.DateTimeField('Created at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    access_permission_updated_at = models.DateTimeField('Updated at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)

    @classmethod
    def get_access_permissions(cls):
        access_permissions = Access_Permissions.objects.all()
        auth_permissions = {}
        counter = 0
        for access_permission in access_permissions:
            auth_permissions[counter] = access_permission.access_permission_name
            counter = counter + 1
        return auth_permissions


# noinspection PyPep8Naming
class Operator_Access_Permissions(models.Model):
    operator_access_permission_id = models.AutoField('Id', primary_key=True)
    operators_operator_id = models.ForeignKey(Operators, on_delete=models.CASCADE)
    access_permissions_access_permission_name = models.ForeignKey(Access_Permissions, on_delete=models.CASCADE)
    operator_access_permission_updated_at = models.DateTimeField('Updated at',
                                                                 default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    operator_access_permission_updated_by = models.EmailField('Updated by', max_length=255, blank=True)

    @classmethod
    def get_access_permissions(cls, id):
        access_permissions = Operator_Access_Permissions.objects.filter(operators_operator_id=id)
        auth_permissions = {}
        counter = 0
        for access_permission in access_permissions:
            auth_permissions[
                counter] = access_permission.access_permissions_access_permission_name.access_permission_name
            counter = counter + 1
        return auth_permissions

    @classmethod
    def add_operator_access_permission(cls, request, access_permission, model, operator):
        object_access_permission = Access_Permissions.objects.get(access_permission_name=access_permission)
        operator_access_permission = Operator_Access_Permissions()
        operator_access_permission.access_permissions_access_permission_name = object_access_permission
        operator_access_permission.operators_operator_id = model
        operator_access_permission.operator_access_permission_updated_at = Utils.get_current_datetime_utc()
        operator_access_permission.operator_access_permission_updated_by = operator.operator_username
        operator_access_permission.save()
        return True


# Create your models here.
# noinspection PyUnresolvedReferences
class Notifications(models.Model):
    TITLE = settings.MODEL_NOTIFICATIONS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_NOTIFICATIONS_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    TYPE_SYSTEM = 'system'
    TYPE_ORDER = 'order'
    TYPE_ORDER_PROPOSAL = 'order-proposal'
    TYPE_SUPPLIER = 'supplier'
    TYPE_PRODUCT_REQUEST = 'product-request'
    TYPE_OPERATOR = 'operator'
    ARRAY_TYPES = [
        (TYPE_SYSTEM.title()).replace('-', ' '),
        (TYPE_ORDER.title()).replace('-', ' '),
        (TYPE_ORDER_PROPOSAL.title()).replace('-', ' '),
        (TYPE_SUPPLIER.title()).replace('-', ' '),
        (TYPE_PRODUCT_REQUEST.title()).replace('-', ' '),
        (TYPE_OPERATOR.title()).replace('-', ' '),
    ]
    DROPDOWN_TYPES = (
        ('', '--select--'),
        (TYPE_SYSTEM, (TYPE_SYSTEM.title()).replace('-', ' ')),
        (TYPE_ORDER, (TYPE_ORDER.title()).replace('-', ' ')),
        (TYPE_ORDER_PROPOSAL, (TYPE_ORDER_PROPOSAL.title()).replace('-', ' ')),
        (TYPE_SUPPLIER, (TYPE_SUPPLIER.title()).replace('-', ' ')),
        (TYPE_PRODUCT_REQUEST, (TYPE_PRODUCT_REQUEST.title()).replace('-', ' ')),
        (TYPE_OPERATOR, (TYPE_OPERATOR.title()).replace('-', ' ')),
    )

    STATUS_UNREAD = 'unread'
    STATUS_READ = 'read'
    STATUS_FIXED = 'fixed'
    ARRAY_STATUSES = [
        (STATUS_UNREAD.title()).replace('-', ' '),
        (STATUS_READ.title()).replace('-', ' '),
        (STATUS_FIXED.title()).replace('-', ' '),
    ]
    DROPDOWN_STATUSES = (
        ('', '--select--'),
        (STATUS_UNREAD, (STATUS_UNREAD.title()).replace('-', ' ')),
        (STATUS_READ, (STATUS_READ.title()).replace('-', ' ')),
        (STATUS_FIXED, (STATUS_FIXED.title()).replace('-', ' ')),
    )

    HTML_TAG_STATUS_UNREAD_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_BLOCKED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Pending <b></div>'
    HTML_TAG_STATUS_READ_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_UNAPPROVED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Unresolved <b></div>'
    HTML_TAG_STATUS_FIXED_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_ACTIVE_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Fixed <b></div>'

    notification_from_by = ''

    notification_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    notification_from_type = models.CharField('Type', max_length=20, blank=False, choices=DROPDOWN_TYPES,
                                              default=TYPE_SYSTEM)
    notification_from_id = models.IntegerField('From Id', blank=False, default=0)
    notification_to_type = models.CharField('Type', max_length=20, blank=False, choices=DROPDOWN_TYPES,
                                            default=TYPE_SYSTEM)
    notification_to_id = models.IntegerField('To Id', blank=False, default=0)
    notification_model_type = models.CharField('Type', max_length=20, blank=False, choices=DROPDOWN_TYPES,
                                               default=TYPE_SYSTEM)
    notification_model_id = models.IntegerField('Model Id', blank=False, default=0)
    notification_message = models.CharField('Message', max_length=255, blank=False)
    notification_url = models.CharField('URL', max_length=255, blank=False)
    notification_created_at = models.DateTimeField('Created at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    notification_read_at = models.DateTimeField('Read at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    notification_fixed_at = models.DateTimeField('Fixed at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    notification_status = models.CharField('Status', max_length=20, blank=False, choices=DROPDOWN_STATUSES,
                                           default=STATUS_UNREAD)

    def __unicode__(self):
        return self.notification_id

    @classmethod
    def add_notification(cls, from_type, from_id, to_type, to_id, model_type, model_id, message, url):
        notification = Notifications()
        notification.notification_from_type = from_type
        notification.notification_from_id = from_id
        notification.notification_to_type = to_type
        notification.notification_to_id = to_id
        notification.notification_model_type = model_type
        notification.notification_model_id = model_id
        notification.notification_message = message
        notification.notification_url = url
        notification.notification_created_at = Utils.get_current_datetime_utc()
        notification.notification_read_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
        notification.notification_fixed_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
        notification.save()


# noinspection PyPep8Naming
class Failed_Login(models.Model):
    FAILED_LOGIN_FROM_BACKEND = 'backend'
    FAILED_LOGIN_FROM_FRONTEND = 'frontend'
    FAILED_LOGIN_FROM = (
        ('backend', 'backend'),
        ('frontend', 'frontend'),
    )
    failed_login_id = models.AutoField('Id', primary_key=True)
    failed_login_username = models.CharField('Username', max_length=255, blank=False)
    failed_login_password = models.CharField('Password', max_length=255, blank=False)
    failed_login_from = models.CharField('From', max_length=10, choices=FAILED_LOGIN_FROM,
                                         default=FAILED_LOGIN_FROM_FRONTEND)
    failed_login_ip_address = models.CharField('Ip Address', max_length=100, blank=False)
    failed_login_attempted_at = models.DateTimeField('Updated at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    failed_login_status = models.BooleanField('Status', default=False)

    @classmethod
    def add(cls, failed_login_username, failed_login_password, failed_login_from, failed_login_ip_address,
            failed_login_status):
        failed_login = Failed_Login()
        failed_login.failed_login_username = failed_login_username
        failed_login.failed_login_password = failed_login_password
        failed_login.failed_login_from = failed_login_from
        failed_login.failed_login_ip_address = failed_login_ip_address
        failed_login.failed_login_attempted_at = Utils.get_current_datetime_utc()
        failed_login.failed_login_status = failed_login_status
        return failed_login.save('Added Failed Login')


class Backups(models.Model):
    TITLE = settings.MODEL_BACKUPS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_BACKUPS_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    backup_file_name = models.CharField('Name', max_length=100, blank=False)
    backup_file_size = models.CharField('Size', max_length=100, blank=False)
    backup_file_created_at = models.DateTimeField('Created at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    backup_file_updated_at = models.DateTimeField('Updated at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)

    class Meta:
        managed = False  # disable migration for this mode


class NotificationsTimeline(models.Model):
    message = models.CharField('Message', max_length=255, blank=True)
    datetime = models.DateTimeField('Time', default=settings.APP_CONSTANT_DEFAULT_DATETIME)

    class Meta:
        managed = False  # disable migration for this mode


# Create your models here.
# noinspection PyUnresolvedReferences
class Emails(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_SENT = 'sent'
    STATUS_DELIVERED = 'delivered'

    ARRAY_STATUSES = [
        (STATUS_PENDING.title()).replace('-', ' '),
        (STATUS_SENT.title()).replace('-', ' '),
        (STATUS_DELIVERED.title()).replace('-', ' '),
    ]
    DROPDOWN_STATUSES = (
        ('', '--select--'),
        (STATUS_PENDING, (STATUS_PENDING.title()).replace('-', ' ')),
        (STATUS_SENT, (STATUS_SENT.title()).replace('-', ' ')),
        (STATUS_DELIVERED, (STATUS_DELIVERED.title()).replace('-', ' ')),
    )

    email_id = models.AutoField('Id', primary_key=True)
    email_from = models.CharField('From', max_length=255, blank=False)
    email_from_name = models.CharField('From Name', max_length=255, blank=False)
    email_to = models.CharField('To', max_length=255, blank=False)
    email_cc = models.CharField('Cc', max_length=255, blank=False)
    email_subject = models.CharField('Subject', max_length=255, blank=False)
    email_message = models.TextField('Message', blank=False)

    email_created_at = models.DateTimeField('Created At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    email_created_id = models.CharField('Created ID', max_length=100, blank=True)
    email_created_by = models.CharField('Created By', max_length=100, blank=True)
    email_created_department = models.CharField('Created Department', max_length=255, blank=True)
    email_created_role = models.CharField('Created Role', max_length=255, blank=True)
    email_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    email_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    email_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    email_updated_department = models.CharField('Updated Department', max_length=255, blank=True)
    email_updated_role = models.CharField('Updated Role', max_length=255, blank=True)
    email_sent_at = models.DateTimeField('Sent At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    email_delivered_at = models.DateTimeField('Delivered At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    email_status = models.CharField('Status', max_length=255, blank=False, choices=DROPDOWN_STATUSES,
                                    default=STATUS_PENDING)

    def __unicode__(self):
        return self.email_id


# Create your models here.
# noinspection PyUnresolvedReferences
class Attachments(models.Model):
    UPLOAD_PATH = 'unknown/'
    EMAILS_UPLOAD_PATH = 'emails/'
    ORDERS_UPLOAD_PATH = 'orders/'

    MODEL_NONE = 'none'
    MODEL_EMAILS = 'emails'
    MODEL_ORDERS = 'orders'

    ARRAY_MODELS = [
        (MODEL_NONE.title()).replace('-', ' '),
        (MODEL_EMAILS.title()).replace('-', ' '),
        (MODEL_ORDERS.title()).replace('-', ' '),
    ]
    MODELS = (
        ('', '--select--'),
        (MODEL_NONE, (MODEL_NONE.title()).replace('-', ' ')),
        (MODEL_EMAILS, (MODEL_EMAILS.title()).replace('-', ' ')),
        (MODEL_ORDERS, (MODEL_ORDERS.title()).replace('-', ' ')),
    )

    TYPE_NONE = 'none'
    TYPE_EMAIL = 'email'
    TYPE_ORDER = 'order'
    TYPE_ORDER_EMAIL = 'order-email'
    TYPE_ORDER_PROPOSAL_BUSINESS_LICENSE = 'order-proposal-business-license'
    TYPE_ORDER_PROPOSAL_OFFER_LETTER = 'order-proposal-offer-letter'
    TYPE_ORDER_PROPOSAL_QUOTATION = 'order-proposal-quotation'
    TYPE_ORDER_PROPOSAL_VAT_REGISTRATION = 'order-proposal-vat-registration'
    TYPE_ORDER_PROPOSAL_OTHER_DOCUMENT = 'order-proposal-other-document'
    TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT = 'order-proposal-reference-document'
    TYPE_ORDER_PURCHASE = 'order-purchase'
    TYPE_ORDER_INVOICE = 'order-invoice'
    TYPE_ORDER_PAYMENT_VOUCHER = 'order-payment-voucher'

    ARRAY_TYPES = [
        (TYPE_NONE.title()).replace('-', ' '),
        (TYPE_EMAIL.title()).replace('-', ' '),
        (TYPE_ORDER.title()).replace('-', ' '),
        (TYPE_ORDER_EMAIL.title()).replace('-', ' '),
        (TYPE_ORDER_PROPOSAL_BUSINESS_LICENSE.title()).replace('-', ' '),
        (TYPE_ORDER_PROPOSAL_OFFER_LETTER.title()).replace('-', ' '),
        (TYPE_ORDER_PROPOSAL_QUOTATION.title()).replace('-', ' '),
        (TYPE_ORDER_PROPOSAL_VAT_REGISTRATION.title()).replace('-', ' '),
        (TYPE_ORDER_PROPOSAL_OTHER_DOCUMENT.title()).replace('-', ' '),
        (TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT.title()).replace('-', ' '),
        (TYPE_ORDER_PURCHASE.title()).replace('-', ' '),
        (TYPE_ORDER_INVOICE.title()).replace('-', ' '),
        (TYPE_ORDER_PAYMENT_VOUCHER.title()).replace('-', ' '),
    ]
    TYPES = (
        ('', '--select--'),
        (TYPE_NONE, (TYPE_NONE.title()).replace('-', ' ')),
        (TYPE_EMAIL, (TYPE_EMAIL.title()).replace('-', ' ')),
        (TYPE_ORDER, (TYPE_ORDER.title()).replace('-', ' ')),
        (TYPE_ORDER_EMAIL, (TYPE_ORDER_EMAIL.title()).replace('-', ' ')),
        (TYPE_ORDER_PROPOSAL_BUSINESS_LICENSE, (TYPE_ORDER_PROPOSAL_BUSINESS_LICENSE.title()).replace('-', ' ')),
        (TYPE_ORDER_PROPOSAL_OFFER_LETTER, (TYPE_ORDER_PROPOSAL_OFFER_LETTER.title()).replace('-', ' ')),
        (TYPE_ORDER_PROPOSAL_QUOTATION, (TYPE_ORDER_PROPOSAL_QUOTATION.title()).replace('-', ' ')),
        (TYPE_ORDER_PROPOSAL_VAT_REGISTRATION, (TYPE_ORDER_PROPOSAL_VAT_REGISTRATION.title()).replace('-', ' ')),
        (TYPE_ORDER_PROPOSAL_OTHER_DOCUMENT, (TYPE_ORDER_PROPOSAL_OTHER_DOCUMENT.title()).replace('-', ' ')),
        (TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT, (TYPE_ORDER_PROPOSAL_REFERENCE_DOCUMENT.title()).replace('-', ' ')),
        (TYPE_ORDER_PURCHASE, (TYPE_ORDER_PURCHASE.title()).replace('-', ' ')),
        (TYPE_ORDER_INVOICE, (TYPE_ORDER_INVOICE.title()).replace('-', ' ')),
        (TYPE_ORDER_PAYMENT_VOUCHER, (TYPE_ORDER_PAYMENT_VOUCHER.title()).replace('-', ' ')),
    )

    attachment_id = models.AutoField('Id', primary_key=True)
    attachment_model = models.CharField('Model', max_length=255, blank=False, choices=MODELS, default=MODEL_NONE)
    attachment_model_id = models.IntegerField('Id', blank=False, default=0)
    attachment_type = models.CharField('Type', max_length=255, blank=False, choices=TYPES, default=TYPE_NONE)
    attachment_type_id = models.IntegerField('Id', blank=False, default=0)
    attachment_number = models.IntegerField('Number', blank=False, default=0)
    attachment_file_name = models.CharField('File Name', max_length=255, blank=True)
    attachment_file_path = models.FileField('File Path', upload_to=UPLOAD_PATH)
    attachment_file_size = models.CharField('File Size', max_length=255, blank=True)
    attachment_file_type = models.CharField('File Type', max_length=255, blank=True)
    attachment_file_uploaded_at = models.DateTimeField('Uploaded At',
                                                       default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    attachment_file_uploaded_id = models.CharField('Uploaded ID', max_length=100, blank=True)
    attachment_file_uploaded_by = models.CharField('Uploaded By', max_length=100, blank=True)
    attachment_file_uploaded_department = models.CharField('Uploaded Department', max_length=255, blank=True)
    attachment_file_uploaded_role = models.CharField('Uploaded Role', max_length=255, blank=True)

    def __unicode__(self):
        return self.attachment_id


# Create your models here.
# noinspection PyUnresolvedReferences
class Products(models.Model):
    TITLE = settings.MODEL_PRODUCTS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_PRODUCTS_ITEM_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    TYPE_GOODS = 'goods'
    TYPE_ASSET = 'asset'
    TYPE_SERVICE = 'service'

    ARRAY_TYPES = [
        TYPE_GOODS,
        TYPE_ASSET,
        TYPE_SERVICE,
    ]
    DROPDOWN_TYPES = (
        ('', '--select--'),
        (TYPE_GOODS, TYPE_GOODS),
        (TYPE_ASSET, TYPE_ASSET),
        (TYPE_SERVICE, TYPE_SERVICE),
    )

    product_inventory_search_start_date = ''
    product_inventory_search_end_date = ''
    product_quantity_initial = 0
    product_quantity_in = 0
    product_quantity_out = 0
    product_quantity_final = 0

    product_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    product_type = models.CharField('Type', max_length=255, blank=False, choices=DROPDOWN_TYPES, default=TYPE_GOODS)
    product_code = models.CharField('Code', max_length=8, unique=True, blank=False, default=None)
    product_tag = models.CharField('Tag', max_length=255, blank=True)
    product_category = models.CharField('Category', max_length=255, blank=True)
    product_title = models.CharField('Title', max_length=100, blank=False)
    product_sub_title = models.CharField('Sub title', max_length=255, blank=True)
    product_quantity_available = models.DecimalField('Quantity Available', max_digits=10, decimal_places=0,
                                                     default=Decimal(0))
    product_quantity_unit = models.CharField('Quantity Unit', max_length=255, blank=True)

    product_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    product_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    product_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    product_updated_department = models.CharField('Updated Department', max_length=255, blank=True)
    product_updated_role = models.CharField('Updated Role', max_length=255, blank=True)

    def __unicode__(self):
        return self.product_id

    @classmethod
    def generate_random_number(cls, attribute, length):
        token = ''
        unique_token_found = False
        while not unique_token_found:
            token = get_random_string(length, allowed_chars='0123456789')
            if (not token.startswith('0')) and Products.objects.filter(**{attribute: token}).count() is 0:
                unique_token_found = True
        return token


# Create your models here.
# noinspection PyUnresolvedReferences
class Inventory(models.Model):
    TITLE = settings.MODEL_INVENTORY_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_INVENTORY_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    inventory_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    inventory_order_purchase_no = models.CharField('Purchase Order No.', max_length=100, unique=True, blank=False)
    inventory_order_proposal_id = models.CharField('Proposal Id', max_length=255, blank=True)
    inventory_order_proposal_supplier_title = models.CharField('Supplier Name', max_length=255, blank=True)
    inventory_created_at = models.DateTimeField('Created At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    inventory_created_id = models.CharField('Created ID', max_length=100, blank=True)
    inventory_created_by = models.CharField('Created By', max_length=100, blank=True)
    inventory_created_department = models.CharField('Created Department', max_length=255, blank=True)
    inventory_created_role = models.CharField('Created Role', max_length=255, blank=True)

    inventory_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    inventory_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    inventory_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    inventory_updated_department = models.CharField('Updated Department', max_length=255, blank=True)
    inventory_updated_role = models.CharField('Updated Role', max_length=255, blank=True)

    def __unicode__(self):
        return self.inventory_id


# Create your models here.
# noinspection PyUnresolvedReferences
class Inventory_Items(models.Model):
    TITLE = settings.MODEL_INVENTORY_ITEMS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_INVENTORY_ITEMS_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    TYPE_GOODS = 'goods'
    TYPE_ASSET = 'asset'
    TYPE_SERVICE = 'service'

    ARRAY_TYPES = [
        TYPE_GOODS,
        TYPE_ASSET,
        TYPE_SERVICE,
    ]
    DROPDOWN_TYPES = (
        ('', '--select--'),
        (TYPE_GOODS, TYPE_GOODS),
        (TYPE_ASSET, TYPE_ASSET),
        (TYPE_SERVICE, TYPE_SERVICE),
    )

    CURRENCY_USD = 'USD'
    CURRENCY_RWF = 'RWF'

    ARRAY_CURRENCIES = [
        CURRENCY_USD,
        CURRENCY_RWF,
    ]
    DROPDOWN_CURRENCIES = (
        ('', '--select--'),
        (CURRENCY_USD, CURRENCY_USD),
        (CURRENCY_RWF, CURRENCY_RWF),
    )

    inventory_item_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    inventory_inventory_id = models.IntegerField('Inventory Id', blank=False)
    products_product_id = models.IntegerField('Product Id', blank=False)
    inventory_item_product_type = models.CharField('Type', max_length=255, blank=False, choices=DROPDOWN_TYPES,
                                                   default=TYPE_GOODS)
    inventory_item_product_code = models.CharField('Code', max_length=8, blank=False, default=None)
    inventory_item_product_tag = models.CharField('Tag', max_length=255, blank=True)
    inventory_item_product_category = models.CharField('Category', max_length=255, blank=True)
    inventory_item_product_title = models.CharField('Title', max_length=100, blank=False)
    inventory_item_product_sub_title = models.CharField('Sub title', max_length=255, blank=True)
    inventory_item_product_quantity_initial = models.DecimalField('Initial Quantity', max_digits=10, decimal_places=0,
                                                                  default=Decimal(0))
    inventory_item_product_quantity_ordered = models.DecimalField('Quantity Ordered', max_digits=10, decimal_places=0,
                                                                  default=Decimal(0))
    inventory_item_product_quantity_balance = models.DecimalField('Balance Quantity', max_digits=10, decimal_places=0,
                                                                  default=Decimal(0))
    inventory_item_product_quantity_unit = models.CharField('Quantity Unit', max_length=255, blank=True)

    inventory_item_product_currency = models.CharField('Currency', max_length=255, blank=False,
                                                       choices=DROPDOWN_CURRENCIES, default=CURRENCY_RWF)

    inventory_item_product_unit_price = models.DecimalField('Quantity Ordered', max_digits=10, decimal_places=0,
                                                            default=Decimal(0))
    inventory_item_product_rate_price = models.DecimalField('Quantity Ordered', max_digits=10, decimal_places=0,
                                                            default=Decimal(0))
    inventory_item_product_usd_price = models.DecimalField('Quantity Ordered', max_digits=10, decimal_places=0,
                                                           default=Decimal(0))

    inventory_item_product_usaid_equipment_price = models.DecimalField('Quantity Ordered', max_digits=10,
                                                                       decimal_places=0, default=Decimal(0))
    inventory_item_product_small_equipment_price = models.DecimalField('Quantity Ordered', max_digits=10,
                                                                       decimal_places=0, default=Decimal(0))

    inventory_item_project = models.CharField('Project', max_length=255, blank=True)
    inventory_item_voucher_reference = models.CharField('Voucher Reference', max_length=255, blank=True)
    inventory_item_location = models.CharField('Location', max_length=255, blank=True)
    inventory_item_equipment_holder_status = models.CharField('Equipment Holder Status', max_length=255, blank=True)
    inventory_item_staff_name = models.CharField('Staff Name', max_length=255, blank=True)
    inventory_item_room_number = models.CharField('Room Number', max_length=255, blank=True)
    inventory_item_present_condition = models.CharField('Present Condition', max_length=255, blank=True)

    inventory_item_disposal_date = models.DateField('Disposal Date',
                                                    default=settings.APP_CONSTANT_DEFAULT_DATE)
    inventory_item_verified_date = models.DateField('Physically Verified Date',
                                                    default=settings.APP_CONSTANT_DEFAULT_DATE)

    inventory_item_remark = models.CharField('Remark', max_length=255, blank=True)

    inventory_item_created_at = models.DateTimeField('Created At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    inventory_item_created_id = models.CharField('Created ID', max_length=100, blank=True)
    inventory_item_created_by = models.CharField('Created By', max_length=100, blank=True)
    inventory_item_created_department = models.CharField('Created Department', max_length=255, blank=True)
    inventory_item_created_role = models.CharField('Created Role', max_length=255, blank=True)

    inventory_item_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    inventory_item_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    inventory_item_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    inventory_item_updated_department = models.CharField('Updated Department', max_length=255, blank=True)
    inventory_item_updated_role = models.CharField('Updated Role', max_length=255, blank=True)

    def __unicode__(self):
        return self.inventory_id


# Create your models here.
# noinspection PyUnresolvedReferences
class Product_Requests(models.Model):
    TITLE = settings.MODEL_PRODUCT_REQUESTS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_PRODUCT_REQUEST_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    STATUS_PENDING = 'pending'
    STATUS_REQUESTED = 'requested'
    STATUS_REVIEWED = 'reviewed'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_CLOSED = 'closed'
    STATUS_CANCELLED = 'cancelled'

    ARRAY_STATUSES = [
        (STATUS_PENDING.title()).replace('-', ' '),
        (STATUS_REQUESTED.title()).replace('-', ' '),
        (STATUS_REVIEWED.title()).replace('-', ' '),
        (STATUS_APPROVED.title()).replace('-', ' '),
        (STATUS_REJECTED.title()).replace('-', ' '),
        (STATUS_CLOSED.title()).replace('-', ' '),
        (STATUS_CANCELLED.title()).replace('-', ' '),
    ]
    DROPDOWN_STATUSES = (
        ('', '--select--'),
        (STATUS_PENDING, (STATUS_PENDING.title()).replace('-', ' ')),
        (STATUS_REQUESTED, (STATUS_REQUESTED.title()).replace('-', ' ')),
        (STATUS_REVIEWED, (STATUS_REVIEWED.title()).replace('-', ' ')),
        (STATUS_APPROVED, (STATUS_APPROVED.title()).replace('-', ' ')),
        (STATUS_REJECTED, (STATUS_REJECTED.title()).replace('-', ' ')),
        (STATUS_CLOSED, (STATUS_CLOSED.title()).replace('-', ' ')),
        (STATUS_CANCELLED, (STATUS_CANCELLED.title()).replace('-', ' ')),
    )

    product_request_readable_status = ''

    product_request_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    product_request_code = models.CharField('Code', max_length=8, unique=True, blank=False, default=None)
    product_request_project = models.CharField('Project', max_length=255, blank=True)
    product_request_details = models.CharField('Project', max_length=255, blank=True)
    product_request_no_of_items = models.DecimalField('No. of Items', max_digits=10, decimal_places=0,
                                                      default=Decimal(0))

    product_request_created_at = models.DateTimeField('Created At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    product_request_created_id = models.CharField('Created ID', max_length=100, blank=True)
    product_request_created_by = models.CharField('Created By', max_length=100, blank=True)
    product_request_created_department = models.CharField('Created Department', max_length=255, blank=True)
    product_request_created_role = models.CharField('Created Role', max_length=255, blank=True)

    product_request_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    product_request_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    product_request_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    product_request_updated_department = models.CharField('Updated Department', max_length=255, blank=True)
    product_request_updated_role = models.CharField('Updated Role', max_length=255, blank=True)

    product_request_requested_at = models.DateTimeField('Requested At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    product_request_requested_id = models.CharField('Requested ID', max_length=100, blank=True)
    product_request_requested_by = models.CharField('Requested By', max_length=100, blank=True)
    product_request_requested_department = models.CharField('Requested Department', max_length=255, blank=True)
    product_request_requested_role = models.CharField('Requested Role', max_length=255, blank=True)

    product_request_reviewed_at = models.DateTimeField('Reviewed At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    product_request_reviewed_id = models.CharField('Reviewed ID', max_length=100, blank=True)
    product_request_reviewed_by = models.CharField('Reviewed By', max_length=100, blank=True)
    product_request_reviewed_department = models.CharField('Reviewed Department', max_length=255, blank=True)
    product_request_reviewed_role = models.CharField('Reviewed Role', max_length=255, blank=True)

    product_request_approved_updated_at = models.DateTimeField('Approved At',
                                                               default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    product_request_approved_updated_id = models.CharField('Approved ID', max_length=100, blank=True)
    product_request_approved_updated_by = models.CharField('Approved By', max_length=100, blank=True)
    product_request_approved_updated_department = models.CharField('Approved Department', max_length=255, blank=True)
    product_request_approved_updated_role = models.CharField('Approved Role', max_length=255, blank=True)

    product_request_closed_at = models.DateTimeField('Closed At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    product_request_closed_id = models.CharField('Closed ID', max_length=100, blank=True)
    product_request_closed_by = models.CharField('Closed By', max_length=100, blank=True)
    product_request_closed_department = models.CharField('Closed Department', max_length=255, blank=True)
    product_request_closed_role = models.CharField('Closed Role', max_length=255, blank=True)

    product_request_cancelled_at = models.DateTimeField('Cancelled At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    product_request_cancelled_id = models.CharField('Cancelled ID', max_length=100, blank=True)
    product_request_cancelled_by = models.CharField('Cancelled By', max_length=100, blank=True)
    product_request_cancelled_department = models.CharField('Cancelled Department', max_length=255, blank=True)
    product_request_cancelled_role = models.CharField('Cancelled Role', max_length=255, blank=True)

    product_request_status = models.CharField('Status', max_length=255, blank=False, choices=DROPDOWN_STATUSES,
                                              default=STATUS_PENDING)

    def __unicode__(self):
        return self.product_request_id

    @classmethod
    def generate_random_number(cls, attribute, length):
        token = ''
        unique_token_found = False
        while not unique_token_found:
            token = get_random_string(length, allowed_chars='0123456789')
            if (not token.startswith('0')) and Product_Requests.objects.filter(**{attribute: token}).count() is 0:
                unique_token_found = True
        return token

    @classmethod
    def update_grand_total(cls, request, model, operator):
        product_request_items = Product_Request_Items.objects.filter(
            product_requests_product_request_id=model.product_request_id).all()
        model.product_request_no_of_items = product_request_items.count()
        model.save()
        return True

    @classmethod
    def get_filtered_product_requests(cls, operator):
        if operator.operator_type == Operators.TYPE_SUPER_ADMIN or operator.operator_type == Operators.TYPE_ADMIN or operator.operator_type == Operators.TYPE_MANAGER or operator.operator_role == Operators.ROLE_STOCK_ADMIN:
            objects = Product_Requests.objects.all()
        else:
            objects = Product_Requests.objects.all()
            if operator.operator_department == Operators.DEPARTMENT_NONE:
                objects = objects.filter(product_request_item_created_id=operator.operator_id)

            if operator.operator_department == Operators.DEPARTMENT_DCOP:
                if operator.operator_role == Operators.ROLE_NONE:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DCOP) &
                                             Q(product_request_item_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_DIRECTOR:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DCOP) &
                                             (Q(product_request_item_created_id__in=child_operators)))

                    child_operators = Operators.objects.filter(
                        Q(operator_department=Operators.DEPARTMENT_DCOP) &
                        Q(operator_role=Operators.ROLE_REGIONAL_MANAGER))

                    for child_operator in child_operators:
                        child_operators = Operators.get_child_operators(
                            Operators.objects.get(operator_id=child_operator.operator_id))
                        objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DCOP) &
                                                 (Q(product_request_item_created_id__in=child_operators)))

                if operator.operator_role == Operators.ROLE_ADVISER:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DCOP) &
                                             Q(product_request_item_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_REGIONAL_MANAGER:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DCOP) &
                                             (Q(product_request_item_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_DISTRICT_MANAGER:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DCOP) &
                                             (Q(product_request_item_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_FIELD_OFFICER:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DCOP) &
                                             Q(product_request_item_created_id=operator.operator_id))

            if operator.operator_department == Operators.DEPARTMENT_BFM:
                if operator.operator_role == Operators.ROLE_NONE:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_BFM) &
                                             Q(product_request_item_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_DIRECTOR:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_BFM) &
                                             (Q(product_request_item_created_id__in=child_operators)))
                if operator.operator_role == Operators.order_created_department:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_BFM) &
                                             Q(product_request_item_created_id=operator.operator_id))

            if operator.operator_department == Operators.DEPARTMENT_NUTRITION:
                if operator.operator_role == Operators.ROLE_NONE:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             Q(product_request_item_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_DIRECTOR:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             (Q(product_request_item_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_ADVISER:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             Q(product_request_item_created_id=operator.operator_id))

            if operator.operator_department == Operators.DEPARTMENT_DAF:
                if operator.operator_role == Operators.ROLE_NONE:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                             Q(product_request_item_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_DIRECTOR or operator.operator_role == Operators.ROLE_OPM:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                             (Q(product_request_item_created_id__in=child_operators)))

                    child_operators = Operators.objects.filter(
                        Q(operator_department=Operators.DEPARTMENT_DAF) &
                        Q(operator_role=Operators.ROLE_PROCUREMENT_OFFICER))

                    for child_operator in child_operators:
                        child_operators = Operators.get_child_operators(
                            Operators.objects.get(operator_id=child_operator.operator_id))
                        objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                                 (Q(product_request_item_created_id__in=child_operators)))

                    child_operators = Operators.objects.filter(
                        Q(operator_department=Operators.DEPARTMENT_DAF) &
                        Q(operator_role=Operators.ROLE_HR_MANAGER))

                    for child_operator in child_operators:
                        child_operators = Operators.get_child_operators(
                            Operators.objects.get(operator_id=child_operator.operator_id))
                        objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                                 (Q(product_request_item_created_id__in=child_operators)))

                    child_operators = Operators.objects.filter(
                        Q(operator_department=Operators.DEPARTMENT_DAF) &
                        Q(operator_role=Operators.ROLE_RECEPTIONIST))

                    for child_operator in child_operators:
                        child_operators = Operators.get_child_operators(
                            Operators.objects.get(operator_id=child_operator.operator_id))
                        objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                                 (Q(product_request_item_created_id__in=child_operators)))

                    child_operators = Operators.objects.filter(
                        Q(operator_department=Operators.DEPARTMENT_DAF) &
                        Q(operator_role=Operators.ROLE_STOCK_ADMIN))

                    for child_operator in child_operators:
                        child_operators = Operators.get_child_operators(
                            Operators.objects.get(operator_id=child_operator.operator_id))
                        objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                                 (Q(product_request_item_created_id__in=child_operators)))

                    child_operators = Operators.objects.filter(
                        Q(operator_department=Operators.DEPARTMENT_DAF) &
                        Q(operator_role=Operators.ROLE_ACCOUNTANT_MANAGER))

                    for child_operator in child_operators:
                        child_operators = Operators.get_child_operators(
                            Operators.objects.get(operator_id=child_operator.operator_id))
                        objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                                 (Q(product_request_item_created_id__in=child_operators)))

                if operator.operator_role == Operators.ROLE_ADVISER:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                             Q(product_request_item_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_PROCUREMENT_OFFICER:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                             (Q(product_request_item_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_HR_MANAGER:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                             (Q(product_request_item_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_RECEPTIONIST:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                             (Q(product_request_item_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_STOCK_ADMIN:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                             (Q(product_request_item_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_ACCOUNTANT_MANAGER:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                             (Q(product_request_item_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_ACCOUNTANT_OFFICER:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_DAF) &
                                             Q(product_request_item_created_id=operator.operator_id))

            if operator.operator_department == Operators.DEPARTMENT_MAV:
                if operator.operator_role == Operators.ROLE_NONE:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             Q(product_request_item_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_DIRECTOR:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             (Q(product_request_item_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_ADVISER:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             Q(product_request_item_created_id=operator.operator_id))

            if operator.operator_department == Operators.DEPARTMENT_GRANT_MANAGER:
                if operator.operator_role == Operators.ROLE_NONE:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             Q(product_request_item_created_id=operator.operator_id))
                if operator.operator_role == Operators.ROLE_DIRECTOR:
                    child_operators = Operators.get_child_operators(
                        Operators.objects.get(operator_id=operator.operator_id))
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             (Q(product_request_item_created_id__in=child_operators)))
                if operator.operator_role == Operators.ROLE_ADVISER:
                    objects = objects.filter(Q(product_request_item_created_department=Operators.DEPARTMENT_NUTRITION) &
                                             Q(product_request_item_created_id=operator.operator_id))

        return objects

    @classmethod
    def get_status_html_tag(cls, record):
        value = None
        if record.product_request_status == Product_Requests.STATUS_PENDING:
            value = Utils.HTML_TAG_ORDER_STATUS_PENDING
        elif record.product_request_status == Product_Requests.STATUS_REQUESTED:
            value = Utils.HTML_TAG_ORDER_STATUS_REQUESTED
        elif record.product_request_status == Product_Requests.STATUS_REVIEWED:
            value = Utils.HTML_TAG_ORDER_STATUS_REVIEWED
        elif record.product_request_status == Product_Requests.STATUS_APPROVED:
            value = Utils.HTML_TAG_ORDER_STATUS_APPROVED
        elif record.product_request_status == Product_Requests.STATUS_REJECTED:
            value = Utils.HTML_TAG_ORDER_STATUS_REJECTED
        elif record.product_request_status == Product_Requests.STATUS_CLOSED:
            value = Utils.HTML_TAG_ORDER_STATUS_CLOSED
        elif record.product_request_status == Product_Requests.STATUS_CANCELLED:
            value = Utils.HTML_TAG_ORDER_STATUS_CANCELLED
        return value


# Create your models here.
# noinspection PyUnresolvedReferences
class Product_Request_Items(models.Model):
    TITLE = settings.MODEL_PRODUCT_REQUESTS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_PRODUCT_REQUEST_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    TYPE_GOODS = 'goods'
    TYPE_ASSET = 'asset'
    TYPE_SERVICE = 'service'

    ARRAY_TYPES = [
        TYPE_GOODS,
        TYPE_ASSET,
        TYPE_SERVICE,
    ]
    DROPDOWN_TYPES = (
        ('', '--select--'),
        (TYPE_GOODS, TYPE_GOODS),
        (TYPE_ASSET, TYPE_ASSET),
        (TYPE_SERVICE, TYPE_SERVICE),
    )

    STATUS_PENDING = 'pending'
    STATUS_RECEIVED = 'received'

    ARRAY_STATUSES = [
        (STATUS_PENDING.title()).replace('-', ' '),
        (STATUS_RECEIVED.title()).replace('-', ' '),
    ]
    DROPDOWN_STATUSES = (
        ('', '--select--'),
        (STATUS_PENDING, (STATUS_PENDING.title()).replace('-', ' ')),
        (STATUS_RECEIVED, (STATUS_RECEIVED.title()).replace('-', ' ')),
    )

    product_request_item_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    product_requests_product_request_id = models.IntegerField('Request Id', blank=False)
    products_product_id = models.IntegerField('Product Id', blank=False)
    product_request_item_product_type = models.CharField('Type', max_length=255, blank=False, choices=DROPDOWN_TYPES,
                                                         default=TYPE_GOODS)
    product_request_item_product_code = models.CharField('Code', max_length=8, blank=False, default=None)
    product_request_item_product_tag = models.CharField('Tag', max_length=255, blank=True)
    product_request_item_product_category = models.CharField('Category', max_length=255, blank=True)
    product_request_item_product_title = models.CharField('Title', max_length=100, blank=False)
    product_request_item_product_sub_title = models.CharField('Sub title', max_length=255, blank=True)
    product_request_item_product_quantity_initial = models.DecimalField('Initial Quantity', max_digits=10,
                                                                        decimal_places=0, default=Decimal(0))
    product_request_item_product_quantity_ordered = models.DecimalField('Quantity Ordered', max_digits=10,
                                                                        decimal_places=0, default=Decimal(0))
    product_request_item_product_quantity_balance = models.DecimalField('Balance Quantity', max_digits=10,
                                                                        decimal_places=0, default=Decimal(0))
    product_request_item_product_quantity_unit = models.CharField('Quantity Unit', max_length=255, blank=True)

    product_request_item_created_at = models.DateTimeField('Created At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    product_request_item_created_id = models.CharField('Created ID', max_length=100, blank=True)
    product_request_item_created_by = models.CharField('Created By', max_length=100, blank=True)
    product_request_item_created_department = models.CharField('Created Department', max_length=255, blank=True)
    product_request_item_created_role = models.CharField('Created Role', max_length=255, blank=True)

    product_request_item_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    product_request_item_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    product_request_item_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    product_request_item_updated_department = models.CharField('Updated Department', max_length=255, blank=True)
    product_request_item_updated_role = models.CharField('Updated Role', max_length=255, blank=True)

    product_request_item_received_at = models.DateTimeField('Received At',
                                                            default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    product_request_item_received_id = models.CharField('Received ID', max_length=100, blank=True)
    product_request_item_received_by = models.CharField('Received By', max_length=100, blank=True)
    product_request_item_received_department = models.CharField('Received Department', max_length=255, blank=True)
    product_request_item_received_role = models.CharField('Received Role', max_length=255, blank=True)

    product_request_item_status = models.CharField('Status', max_length=255, blank=False, choices=DROPDOWN_STATUSES,
                                                   default=STATUS_PENDING)

    def __unicode__(self):
        return self.product_request_item_id

    @classmethod
    def get_status_html_tag(cls, record):
        value = None
        if record.product_request_item_status == Product_Request_Items.STATUS_PENDING:
            value = Utils.HTML_TAG_ORDER_ITEM_STATUS_PENDING
        elif record.product_request_item_status == Product_Request_Items.STATUS_RECEIVED:
            value = Utils.HTML_TAG_ORDER_ITEM_STATUS_RECEIVED
        return value

    @classmethod
    def delete_product_request_item(cls, request, model, operator):
        model.delete()
        return True
