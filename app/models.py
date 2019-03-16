import os
from decimal import Decimal

from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator
from django.core.validators import ValidationError
from django.db import models
from django.middleware.csrf import rotate_token
from django.utils.crypto import get_random_string, salted_hmac, constant_time_compare

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
        'Deputy COP (Agriculture)',
        'Business, Finance & Marketing',
        'Nutrition',
        'Administrative and Finance',
        'Monitoring and Evaluation',
        'Grant Manager',
    ]
    OPERATOR_DEPARTMENTS = (
        ('', '--select--'),
        (DEPARTMENT_NONE, 'NONE'),
        (DEPARTMENT_DCOP, 'Deputy COP (Agriculture)'),
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

    STATUS_PENDING = 'pending'
    STATUS_REQUESTED = 'requested'
    STATUS_LEVEL1_APPROVED = 'level1-approved'
    STATUS_LEVEL2_APPROVED = 'level2-approved'
    STATUS_LEVEL3_APPROVED = 'level3-approved'
    STATUS_LEVEL4_APPROVED = 'level4-approved'
    STATUS_LEVEL1_REJECTED = 'level1-rejected'
    STATUS_LEVEL2_REJECTED = 'level2-rejected'
    STATUS_LEVEL3_REJECTED = 'level3-rejected'
    STATUS_LEVEL4_REJECTED = 'level4-rejected'
    STATUS_REVIEWED = 'reviewed'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_ASSIGNED = 'assigned'
    STATUS_PROPOSAL_GENERATED = 'proposal-generated'
    STATUS_PROPOSAL_REQUESTED = 'proposal-requested'
    STATUS_PROPOSAL_EVALUATED = 'proposal-evaluated'
    STATUS_PROPOSAL_APPROVED = 'proposal-approved'
    STATUS_PROPOSAL_REJECTED = 'proposal-rejected'
    STATUS_PURCHASE_GENERATED = 'purchase-generated'
    STATUS_PROPOSAL_ACKNOWLEDGED = 'proposal-acknowledged'
    STATUS_RECEIVED = 'received'
    STATUS_PARTIALLY_PAID = 'partially-paid'
    STATUS_PAID = 'paid'
    STATUS_CLOSED = 'closed'

    ARRAY_ORDER_STATUSES = [
        (STATUS_PENDING.title()).replace('-', ' '),
        (STATUS_REQUESTED.title()).replace('-', ' '),
        (STATUS_LEVEL1_APPROVED.title()).replace('-', ' '),
        (STATUS_LEVEL2_APPROVED.title()).replace('-', ' '),
        (STATUS_LEVEL3_APPROVED.title()).replace('-', ' '),
        (STATUS_LEVEL4_APPROVED.title()).replace('-', ' '),
        (STATUS_LEVEL1_REJECTED.title()).replace('-', ' '),
        (STATUS_LEVEL2_REJECTED.title()).replace('-', ' '),
        (STATUS_LEVEL3_REJECTED.title()).replace('-', ' '),
        (STATUS_LEVEL4_REJECTED.title()).replace('-', ' '),
        (STATUS_REVIEWED.title()).replace('-', ' '),
        (STATUS_APPROVED.title()).replace('-', ' '),
        (STATUS_REJECTED.title()).replace('-', ' '),
        (STATUS_ASSIGNED.title()).replace('-', ' '),
        (STATUS_PROPOSAL_GENERATED.title()).replace('-', ' '),
        (STATUS_PROPOSAL_REQUESTED.title()).replace('-', ' '),
        (STATUS_PROPOSAL_EVALUATED.title()).replace('-', ' '),
        (STATUS_PROPOSAL_APPROVED.title()).replace('-', ' '),
        (STATUS_PROPOSAL_REJECTED.title()).replace('-', ' '),
        (STATUS_PURCHASE_GENERATED.title()).replace('-', ' '),
        (STATUS_PROPOSAL_ACKNOWLEDGED.title()).replace('-', ' '),
        (STATUS_RECEIVED.title()).replace('-', ' '),
        (STATUS_PARTIALLY_PAID.title()).replace('-', ' '),
        (STATUS_PAID.title()).replace('-', ' '),
        (STATUS_CLOSED.title()).replace('-', ' '),
    ]
    ORDER_STATUSES = (
        ('', '--select--'),
        (STATUS_PENDING, (STATUS_PENDING.title()).replace('-', ' ')),
        (STATUS_REQUESTED, (STATUS_REQUESTED.title()).replace('-', ' ')),
        (STATUS_LEVEL1_APPROVED, (STATUS_LEVEL1_APPROVED.title()).replace('-', ' ')),
        (STATUS_LEVEL2_APPROVED, (STATUS_LEVEL2_APPROVED.title()).replace('-', ' ')),
        (STATUS_LEVEL3_APPROVED, (STATUS_LEVEL3_APPROVED.title()).replace('-', ' ')),
        (STATUS_LEVEL4_APPROVED, (STATUS_LEVEL4_APPROVED.title()).replace('-', ' ')),
        (STATUS_LEVEL1_REJECTED, (STATUS_LEVEL1_REJECTED.title()).replace('-', ' ')),
        (STATUS_LEVEL2_REJECTED, (STATUS_LEVEL2_REJECTED.title()).replace('-', ' ')),
        (STATUS_LEVEL3_REJECTED, (STATUS_LEVEL3_REJECTED.title()).replace('-', ' ')),
        (STATUS_LEVEL4_REJECTED, (STATUS_LEVEL4_REJECTED.title()).replace('-', ' ')),
        (STATUS_REVIEWED, (STATUS_REVIEWED.title()).replace('-', ' ')),
        (STATUS_APPROVED, (STATUS_APPROVED.title()).replace('-', ' ')),
        (STATUS_REJECTED, (STATUS_REJECTED.title()).replace('-', ' ')),
        (STATUS_ASSIGNED, (STATUS_ASSIGNED.title()).replace('-', ' ')),
        (STATUS_PROPOSAL_GENERATED, (STATUS_PROPOSAL_GENERATED.title()).replace('-', ' ')),
        (STATUS_PROPOSAL_REQUESTED, (STATUS_PROPOSAL_REQUESTED.title()).replace('-', ' ')),
        (STATUS_PROPOSAL_EVALUATED, (STATUS_PROPOSAL_EVALUATED.title()).replace('-', ' ')),
        (STATUS_PROPOSAL_APPROVED, (STATUS_PROPOSAL_APPROVED.title()).replace('-', ' ')),
        (STATUS_PROPOSAL_REJECTED, (STATUS_PROPOSAL_REJECTED.title()).replace('-', ' ')),
        (STATUS_PURCHASE_GENERATED, (STATUS_PURCHASE_GENERATED.title()).replace('-', ' ')),
        (STATUS_PROPOSAL_ACKNOWLEDGED, (STATUS_PROPOSAL_ACKNOWLEDGED.title()).replace('-', ' ')),
        (STATUS_RECEIVED, (STATUS_RECEIVED.title()).replace('-', ' ')),
        (STATUS_PARTIALLY_PAID, (STATUS_PARTIALLY_PAID.title()).replace('-', ' ')),
        (STATUS_PAID, (STATUS_PAID.title()).replace('-', ' ')),
        (STATUS_CLOSED, (STATUS_CLOSED.title()).replace('-', ' ')),
    )

    order_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    order_requester_name = models.CharField('Requester Name', max_length=100, blank=False)
    order_project_name = models.CharField('Project Name', max_length=100, blank=False)
    order_project_code = models.CharField('Project Code', max_length=100, blank=True)
    order_project_geo_code = models.CharField('Project GeoCode', max_length=100, blank=True)
    order_charge_code = models.CharField('Charge Code', max_length=100, blank=True)
    order_award_number = models.CharField('Award Number', max_length=100, blank=True)
    order_requisition_number = models.CharField('Requisition Number', max_length=100, blank=True)
    order_description = models.CharField('Description', max_length=255, blank=True)
    order_anticipated_award_mechanism = models.CharField('Anticipated Award Mechanism', max_length=255, blank=True)
    order_anticipated_start_date = models.DateField('Anticipated Start Date',
                                                    default=settings.APP_CONSTANT_DEFAULT_DATE)
    order_anticipated_end_date = models.DateField('Anticipated End Date', default=settings.APP_CONSTANT_DEFAULT_DATE)
    order_special_considerations = models.CharField('Special Considerations', max_length=255, blank=True)
    order_procurement_method = models.CharField('Procurement Method', max_length=100, blank=True)
    order_procurement_method_updated_at = models.DateTimeField('Procurement Method Updated At',
                                                               default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_procurement_method_updated_id = models.CharField('Procurement Method Updated ID', max_length=100, blank=True)
    order_procurement_method_updated_by = models.CharField('Procurement Method Updated By', max_length=100, blank=True)
    order_procurement_method_updated_role = models.CharField('Procurement Method Updated Title', max_length=100,
                                                             blank=True)
    order_no_of_items = models.DecimalField('No. of Items', max_digits=10, decimal_places=0, default=Decimal(0))
    order_total_price = models.DecimalField('Total Amount', max_digits=10, decimal_places=0, default=Decimal(0))
    order_equipment_price = models.DecimalField('Equipment Cost', max_digits=10, decimal_places=0, default=Decimal(0))
    order_tax_price = models.DecimalField('Tax Amount', max_digits=10, decimal_places=0, default=Decimal(0))
    order_grand_total_price = models.DecimalField('Grand Total', max_digits=10, decimal_places=0, default=Decimal(0))
    order_supplier_category = models.CharField('Vendor Category', max_length=255, blank=True)
    order_proposal_id = models.IntegerField('Proposal Id', blank=False, default=0)
    order_proposal_due_date = models.DateField('Proposal Due Date', default=settings.APP_CONSTANT_DEFAULT_DATE)
    order_purchase_no = models.CharField('Purchase Order No.', max_length=100, blank=True)
    order_invoice_no = models.CharField('Invoice No.', max_length=100, blank=True)
    order_created_at = models.DateTimeField('Created At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_created_id = models.CharField('Created ID', max_length=100, blank=True)
    order_created_by = models.CharField('Created By', max_length=100, blank=True)
    order_created_role = models.CharField('Created Title', max_length=100, blank=True)
    order_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    order_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    order_updated_role = models.CharField('Updated Title', max_length=100, blank=True)
    order_approval_no_of_levels = models.IntegerField('Approval Levels', blank=False, default=0)
    order_reviewed_at = models.DateTimeField('Reviewed At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_reviewed_id = models.CharField('Reviewed ID', max_length=100, blank=True)
    order_reviewed_by = models.CharField('Reviewed By', max_length=100, blank=True)
    order_reviewed_role = models.CharField('Reviewed Title', max_length=100, blank=True)
    order_approved_at = models.DateTimeField('Approved At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_approved_id = models.CharField('Approved ID', max_length=100, blank=True)
    order_approved_by = models.CharField('Approved By', max_length=100, blank=True)
    order_approved_role = models.CharField('Approved Title', max_length=100, blank=True)
    order_assigned_at = models.DateTimeField('Assigned At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_assigned_id = models.CharField('Assigned ID', max_length=100, blank=True)
    order_assigned_by = models.CharField('Assigned By', max_length=100, blank=True)
    order_assigned_role = models.CharField('Assigned Title', max_length=100, blank=True)
    order_assigned_to_at = models.DateTimeField('Assigned To At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_assigned_to_role = models.CharField('Assigned To Title', max_length=100, blank=True)
    order_proposal_generated_at = models.DateTimeField('Order Proposal Generated At',
                                                       default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_generated_id = models.CharField('Order Proposal Generated ID', max_length=100, blank=True)
    order_proposal_generated_by = models.CharField('Order Proposal Generated By', max_length=100, blank=True)
    order_proposal_generated_role = models.CharField('Order Proposal Generated Title', max_length=100, blank=True)
    order_proposal_requested_at = models.DateTimeField('Order Proposal Requested At',
                                                       default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_requested_id = models.CharField('Order Proposal Requested ID', max_length=100, blank=True)
    order_proposal_requested_by = models.CharField('Order Proposal Requested By', max_length=100, blank=True)
    order_proposal_requested_role = models.CharField('Order Proposal Requested Title', max_length=100, blank=True)
    order_purchase_generated_at = models.DateTimeField('Purchase Order Generated At',
                                                       default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_purchase_generated_id = models.CharField('Purchase Order Generated ID', max_length=100, blank=True)
    order_purchase_generated_by = models.CharField('Purchase Order Generated By', max_length=100, blank=True)
    order_purchase_generated_role = models.CharField('Purchase Order Generated Title', max_length=100, blank=True)
    order_paid_at = models.DateTimeField('Paid At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_paid_id = models.CharField('Paid ID', max_length=100, blank=True)
    order_paid_by = models.CharField('Paid By', max_length=100, blank=True)
    order_paid_role = models.CharField('Paid Title', max_length=100, blank=True)
    order_closed_at = models.DateTimeField('Closed At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_closed_id = models.CharField('Closed ID', max_length=100, blank=True)
    order_closed_by = models.CharField('Closed By', max_length=100, blank=True)
    order_closed_role = models.CharField('Closed Title', max_length=100, blank=True)
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
            if (not token.startswith('0')) and Offices.objects.filter(**{attribute: token}).count() is 0:
                unique_token_found = True
        return token

    @classmethod
    def delete_order(cls, request, model, operator):

        Order_Logs.add(
            model.order_id,
            'Deleted ' + Orders.SINGULAR_TITLE,
            Utils.get_browser_details_from_request(request),
            Utils.get_ip_address(request),
            operator.operator_username,
        )

        model.delete()
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

    STATUS_NONE = 'none'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'

    ARRAY_STATUSES = [
        (STATUS_NONE.title()).replace('-', ' '),
        (STATUS_APPROVED.title()).replace('-', ' '),
        (STATUS_REJECTED.title()).replace('-', ' '),
    ]
    DROPDOWN_STATUSES = (
        ('', '--select--'),
        (STATUS_APPROVED, (STATUS_APPROVED.title()).replace('-', ' ')),
        (STATUS_REJECTED, (STATUS_REJECTED.title()).replace('-', ' ')),
    )

    order_approval_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    orders_order_id = models.IntegerField('Order Id', blank=False)
    order_approval_level = models.IntegerField('Approval Level', blank=False)
    order_approval_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_approval_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    order_approval_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    order_approval_updated_role = models.CharField('Updated Title', max_length=100, blank=True)
    order_approval_status = models.CharField('Status', max_length=255, blank=False, choices=DROPDOWN_STATUSES,
                                             default=STATUS_NONE)

    def __unicode__(self):
        return self.order_id


# Create your models here.
# noinspection PyUnresolvedReferences
class Order_Attachments(models.Model):
    TITLE = settings.MODEL_ORDER_APPROVALS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_ORDER_APPROVALS_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

    TYPE_NONE = 'none'
    TYPE_ORDER_REQUEST = 'order-request'
    TYPE_ORDER_PROPOSAL = 'order-proposal'
    TYPE_ORDER_PURCHASE = 'order-purchase'
    TYPE_ORDER_INVOICE = 'order-invoice'

    ARRAY_TYPES = [
        (TYPE_NONE.title()).replace('-', ' '),
        (TYPE_ORDER_REQUEST.title()).replace('-', ' '),
        (TYPE_ORDER_PROPOSAL.title()).replace('-', ' '),
        (TYPE_ORDER_PURCHASE.title()).replace('-', ' '),
        (TYPE_ORDER_INVOICE.title()).replace('-', ' '),
    ]
    TYPES = (
        ('', '--select--'),
        (TYPE_ORDER_REQUEST, (TYPE_ORDER_REQUEST.title()).replace('-', ' ')),
        (TYPE_ORDER_PROPOSAL, (TYPE_ORDER_PROPOSAL.title()).replace('-', ' ')),
        (TYPE_ORDER_PURCHASE, (TYPE_ORDER_PURCHASE.title()).replace('-', ' ')),
        (TYPE_ORDER_INVOICE, (TYPE_ORDER_INVOICE.title()).replace('-', ' ')),
    )

    order_attachment_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    orders_order_id = models.IntegerField('Order Id', blank=False)
    order_attachment_type = models.CharField('Type', max_length=255, blank=False, choices=TYPES, default=TYPE_NONE)
    order_attachment_type_id = models.IntegerField('Proposal Id', blank=False, default=0)
    order_attachment_file_name = models.CharField('File Name', max_length=255, blank=True)
    order_attachment_file_path = models.CharField('File Path', max_length=255, blank=True)
    order_attachment_file_uploaded_at = models.DateTimeField('Uploaded At',
                                                             default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_attachment_file_uploaded_id = models.CharField('Uploaded ID', max_length=100, blank=True)
    order_attachment_file_uploaded_by = models.CharField('Uploaded By', max_length=100, blank=True)
    order_attachment_file_uploaded_role = models.CharField('Uploaded Title', max_length=100, blank=True)

    def __unicode__(self):
        return self.order_attachment_id


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
    order_payment_paid_role = models.CharField('Paid Title', max_length=100, blank=True)
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

    STATUS_PENDING = 'pending'
    STATUS_EVALUATED = 'evaluated'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_ACKNOWLEDGED = 'acknowledged'

    ARRAY_STATUSES = [
        (STATUS_PENDING.title()).replace('-', ' '),
        (STATUS_EVALUATED.title()).replace('-', ' '),
        (STATUS_APPROVED.title()).replace('-', ' '),
        (STATUS_REJECTED.title()).replace('-', ' '),
        (STATUS_ACKNOWLEDGED.title()).replace('-', ' '),
    ]
    DROPDOWN_STATUSES = (
        ('', '--select--'),
        (STATUS_PENDING, (STATUS_PENDING.title()).replace('-', ' ')),
        (STATUS_EVALUATED, (STATUS_EVALUATED.title()).replace('-', ' ')),
        (STATUS_APPROVED, (STATUS_APPROVED.title()).replace('-', ' ')),
        (STATUS_REJECTED, (STATUS_REJECTED.title()).replace('-', ' ')),
        (STATUS_ACKNOWLEDGED, (STATUS_ACKNOWLEDGED.title()).replace('-', ' ')),
    )

    order_proposal_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    orders_order_id = models.IntegerField('Order Id', blank=False)
    order_proposal_supplier_category = models.CharField('Supplier Category', max_length=255, blank=False)
    order_proposal_supplier_title = models.CharField('Supplier Name', max_length=255, blank=False)
    order_proposal_supplier_details = models.CharField('Supplier Details', max_length=255, blank=True)
    order_proposal_supplier_address = models.CharField('Supplier Address', max_length=255, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+250123456789'. Up to 13 digits allowed.")
    order_proposal_supplier_contact_phone_number = models.CharField('Phone Number',
                                                                    validators=[phone_regex, MinLengthValidator(10),
                                                                                MaxLengthValidator(13)], max_length=13,
                                                                    blank=True)
    order_proposal_supplier_contact_email_id = models.EmailField('Email id', max_length=100, blank=True)
    order_proposal_cost = models.DecimalField('Proposal Cost', max_digits=10, decimal_places=0, default=Decimal(0))
    order_proposal_evaluated_score = models.IntegerField('Score', blank=False, default=0)
    order_proposal_evaluation_details = models.CharField('Evaluation Details', max_length=255, blank=True)
    order_proposal_created_at = models.DateTimeField('Created At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_created_id = models.CharField('Created ID', max_length=100, blank=True)
    order_proposal_created_by = models.CharField('Created By', max_length=100, blank=True)
    order_proposal_created_role = models.CharField('Created Title', max_length=100, blank=True)
    order_proposal_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    order_proposal_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    order_proposal_updated_role = models.CharField('Updated Title', max_length=100, blank=True)
    order_proposal_evaluated_at = models.DateTimeField('Evaluated At',
                                                       default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_evaluated_id = models.CharField('Evaluated ID', max_length=100, blank=True)
    order_proposal_evaluated_by = models.CharField('Evaluated By', max_length=100, blank=True)
    order_proposal_evaluated_role = models.CharField('Evaluated Title', max_length=100, blank=True)
    order_proposal_approval_updated_at = models.DateTimeField('Approval Updated At',
                                                              default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_approval_updated_id = models.CharField('Approval Updated ID', max_length=100, blank=True)
    order_proposal_approval_updated_by = models.CharField('Approval Updated By', max_length=100, blank=True)
    order_proposal_approval_updated_role = models.CharField('Approval Updated Title', max_length=100, blank=True)
    order_proposal_acknowledged_at = models.DateTimeField('Acknowledged At',
                                                          default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_proposal_acknowledged_id = models.CharField('Acknowledged ID', max_length=100, blank=True)
    order_proposal_acknowledged_by = models.CharField('Acknowledged By', max_length=100, blank=True)
    order_proposal_acknowledged_role = models.CharField('Acknowledged Title', max_length=100, blank=True)
    order_proposal_status = models.CharField('Status', max_length=255, blank=False, choices=DROPDOWN_STATUSES,
                                             default=STATUS_PENDING)

    def __unicode__(self):
        return self.order_proposal_id


# Create your models here.
# noinspection PyUnresolvedReferences
class Order_Items(models.Model):
    TITLE = settings.MODEL_ORDER_ITEMS_PLURAL_TITLE
    SINGULAR_TITLE = settings.MODEL_ORDER_ITEM_SINGULAR_TITLE
    NAME = "-".join((TITLE.lower()).split())

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

    order_item_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    orders_order_id = models.IntegerField('Order Id', blank=False)
    order_item_title = models.CharField('Item Details', max_length=255, blank=False)
    order_item_sub_title = models.CharField('Item Details', max_length=255, blank=True)
    order_item_quantity_ordered = models.DecimalField('Quantity Ordered', max_digits=10, decimal_places=0,
                                                      default=Decimal(0))
    order_item_quantity_unit = models.CharField('Quantity Unit', max_length=255, blank=True)
    order_item_unit_price = models.DecimalField('Unit Price', max_digits=10, decimal_places=0, default=Decimal(0))
    order_item_total_price = models.DecimalField('Total Price', max_digits=10, decimal_places=0, default=Decimal(0))
    order_item_usaid_approval = models.BooleanField('USAID Approval', default=False)
    order_item_created_at = models.DateTimeField('Created At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_item_created_id = models.CharField('Created ID', max_length=100, blank=True)
    order_item_created_by = models.CharField('Created By', max_length=100, blank=True)
    order_item_created_role = models.CharField('Created Title', max_length=100, blank=True)
    order_item_updated_at = models.DateTimeField('Updated At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_item_updated_id = models.CharField('Updated ID', max_length=100, blank=True)
    order_item_updated_by = models.CharField('Updated By', max_length=100, blank=True)
    order_item_updated_role = models.CharField('Updated Title', max_length=100, blank=True)
    order_item_received_at = models.DateTimeField('Received At', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    order_item_received_id = models.CharField('Received ID', max_length=100, blank=True)
    order_item_received_by = models.CharField('Received By', max_length=100, blank=True)
    order_item_received_role = models.CharField('Received Title', max_length=100, blank=True)
    order_item_status = models.CharField('Status', max_length=255, blank=False, choices=DROPDOWN_STATUSES,
                                         default=STATUS_PENDING)

    def __unicode__(self):
        return self.order_item_id


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
    TYPE_OPERATOR = 'operator'
    ARRAY_TYPES = [
        (TYPE_SYSTEM.title()).replace('-', ' '),
        (TYPE_ORDER.title()).replace('-', ' '),
        (TYPE_OPERATOR.title()).replace('-', ' '),
    ]
    DROPDOWN_TYPES = (
        ('', '--select--'),
        (TYPE_SYSTEM, (TYPE_SYSTEM.title()).replace('-', ' ')),
        (TYPE_ORDER, (TYPE_ORDER.title()).replace('-', ' ')),
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

    HTML_TAG_STATUS_ACTIVE_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_ACTIVE_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Active <b></div>'
    HTML_TAG_STATUS_INACTIVE_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_INACTIVE_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Inactive <b></div>'
    HTML_TAG_STATUS_BLOCKED_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_BLOCKED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Blocked <b></div>'
    HTML_TAG_STATUS_UNVERIFIED_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_UNVERIFIED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Unverified <b></div>'
    HTML_TAG_STATUS_UNAPPROVED_COLOR = '<div class=\'center-block\' style=\'background-color:' + settings.STATUS_UNAPPROVED_COLOR + ';color:#FFFFFF;width:100px;text-align: center;\'><b> Unapproved <b></div>'

    notification_id = models.AutoField(SINGULAR_TITLE + ' Id', primary_key=True)
    notification_from_type = models.CharField('Type', max_length=20, blank=False, choices=DROPDOWN_TYPES,
                                              default=TYPE_SYSTEM)
    notification_from_id = models.IntegerField('From Id', max_length=100, blank=False, default=0)
    notification_to_type = models.CharField('Type', max_length=20, blank=False, choices=DROPDOWN_TYPES,
                                            default=TYPE_SYSTEM)
    notification_to_id = models.IntegerField('To Id', max_length=100, blank=False, default=0)
    notification_message = models.CharField('Message', max_length=255, blank=False)
    notification_url = models.CharField('URL', max_length=255, blank=False)
    notification_created_at = models.DateTimeField('Created at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    notification_read_at = models.DateTimeField('Read at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    notification_fixed_at = models.DateTimeField('Fixed at', default=settings.APP_CONSTANT_DEFAULT_DATETIME)
    notification_status = models.CharField('Status', max_length=20, blank=False, choices=DROPDOWN_STATUSES,
                                           default=STATUS_UNREAD)

    def __unicode__(self):
        return self.notification_id


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
