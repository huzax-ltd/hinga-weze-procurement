from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from app import settings
from app.models import Operators, Notifications, NotificationsTimeline
from app.models import Product_Requests, Product_Request_Items
from app.utils import Utils
from backend.forms.product_request_forms import ProductRequestSearchIndexForm, ProductRequestCreateForm, \
    ProductRequestUpdateForm
from backend.forms.product_request_item_forms import ProductRequestItemSearchIndexForm
from backend.tables.product_request_item_tables import ProductRequestItemsTable
from backend.tables.product_request_tables import ProductRequestsTable


# noinspection PyUnusedLocal
def index(request):
    template_url = 'product-requests/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            search_form = ProductRequestSearchIndexForm(request.POST or None)
            objects = None

            objects = Product_Requests.get_filtered_product_requests(operator)

            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                table = ProductRequestsTable(objects)
            else:
                display_search = False
                table = ProductRequestsTable(objects)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_STOCK_ALL_REQUESTS,
                    'title': Product_Requests.TITLE,
                    'name': Product_Requests.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'search_form': search_form,
                    'display_search': display_search,
                    'index_url': reverse("product_requests_index"),
                    'select_multiple_url': reverse("product_requests_select_multiple"),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal
def index_operator(request):
    template_url = 'product-requests/index-operator.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            search_form = ProductRequestSearchIndexForm(request.POST or None)
            objects = None

            objects = Product_Requests.objects.filter(product_request_created_id=operator.operator_id)

            if request.method == 'POST' and search_form.is_valid():
                display_search = True
                table = ProductRequestsTable(objects)
            else:
                display_search = False
                table = ProductRequestsTable(objects)

            table.set_auth_permissions(auth_permissions)
            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_STOCK_MY_REQUESTS,
                    'title': Product_Requests.TITLE,
                    'name': Product_Requests.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'table': table,
                    'search_form': search_form,
                    'display_search': display_search,
                    'index_url': reverse("product_requests_index"),
                    'select_multiple_url': reverse("product_requests_select_multiple"),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


@csrf_exempt
# noinspection PyUnusedLocal
def select_single(request):
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
                if action == 'order-request':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Product_Requests.objects.get(product_request_id=id)
                            if model.product_request_created_id == str(operator.operator_id):
                                model.product_request_requested_at = Utils.get_current_datetime_utc()
                                model.product_request_requested_id = operator.operator_id
                                model.product_request_requested_by = operator.operator_name
                                model.product_request_requested_department = operator.operator_department
                                model.product_request_requested_role = operator.operator_role
                                model.product_request_status = Product_Requests.STATUS_REQUESTED
                                model.save()

                                # sending notification to COP
                                operators = Operators.objects.filter(operator_role=Operators.ROLE_STOCK_ADMIN)
                                for item in operators:
                                    Notifications.add_notification(
                                        Notifications.TYPE_OPERATOR,
                                        operator.operator_id,
                                        Notifications.TYPE_OPERATOR,
                                        item.operator_id,
                                        Notifications.TYPE_PRODUCT_REQUEST,
                                        model.product_request_id,
                                        "A stock request has been sent for approval.",
                                        "/backend/product-requests/view/" + str(
                                            model.product_request_id) + "/"
                                    )

                                messages.success(request, 'Stock requested successfully.')
                            else:
                                messages.success(request, 'Forbidden')
                        except(TypeError, ValueError, OverflowError, Product_Requests.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-review':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Product_Requests.objects.get(product_request_id=id)
                            model.product_request_reviewed_at = Utils.get_current_datetime_utc()
                            model.product_request_reviewed_id = operator.operator_id
                            model.product_request_reviewed_by = operator.operator_name
                            model.product_request_reviewed_department = operator.operator_department
                            model.product_request_reviewed_role = operator.operator_role
                            model.product_request_status = Product_Requests.STATUS_REVIEWED
                            model.save()

                            # sending notification
                            operators = Operators.objects.filter(operator_id=model.product_request_requested_id)
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_PRODUCT_REQUEST,
                                    model.product_request_id,
                                    "Your stock request has been reviewed.",
                                    "/backend/product-requests/view/" + str(
                                        model.product_request_id) + "/"
                                )

                            messages.success(request, 'Stock reviewed successfully.')

                        except(TypeError, ValueError, OverflowError, Product_Requests.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-approve':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Product_Requests.objects.get(product_request_id=id)
                            model.product_request_approved_updated_at = Utils.get_current_datetime_utc()
                            model.product_request_approved_updated_id = operator.operator_id
                            model.product_request_approved_updated_by = operator.operator_name
                            model.product_request_approved_updated_department = operator.operator_department
                            model.product_request_approved_updated_role = operator.operator_role
                            model.product_request_status = Product_Requests.STATUS_APPROVED
                            model.save()

                            # sending notification
                            operators = Operators.objects.filter(operator_id=model.product_request_requested_id)
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_PRODUCT_REQUEST,
                                    model.product_request_id,
                                    "Your stock request has been approved.",
                                    "/backend/product-requests/view/" + str(
                                        model.product_request_id) + "/"
                                )

                            messages.success(request, 'Stock approved successfully.')

                        except(TypeError, ValueError, OverflowError, Product_Requests.DoesNotExist):
                            return HttpResponseBadRequest('Bad Request', content_type='text/plain')
                    else:
                        return HttpResponseForbidden('Forbidden', content_type='text/plain')
                if action == 'order-reject':
                    if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
                        try:
                            model = Product_Requests.objects.get(product_request_id=id)
                            model.product_request_approved_updated_at = Utils.get_current_datetime_utc()
                            model.product_request_approved_updated_id = operator.operator_id
                            model.product_request_approved_updated_by = operator.operator_name
                            model.product_request_approved_updated_department = operator.operator_department
                            model.product_request_approved_updated_role = operator.operator_role
                            model.product_request_status = Product_Requests.STATUS_REVIEWED
                            model.save()

                            # sending notification
                            operators = Operators.objects.filter(operator_id=model.product_request_requested_id)
                            for item in operators:
                                Notifications.add_notification(
                                    Notifications.TYPE_OPERATOR,
                                    operator.operator_id,
                                    Notifications.TYPE_OPERATOR,
                                    item.operator_id,
                                    Notifications.TYPE_PRODUCT_REQUEST,
                                    model.product_request_id,
                                    "Your stock request has been rejected.",
                                    "/backend/product-requests/view/" + str(
                                        model.product_request_id) + "/"
                                )

                            messages.success(request, 'Stock rejected successfully.')

                        except(TypeError, ValueError, OverflowError, Product_Requests.DoesNotExist):
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
def select_multiple(request):
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
                return HttpResponse('success', content_type='text/plain')
            else:
                return HttpResponseBadRequest('Bad Request', content_type='text/plain')
    else:
        return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def create(request):
    template_url = 'product-requests/create.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_CREATE in auth_permissions.values():
            if request.method == 'POST':

                form = ProductRequestCreateForm(request.POST)
                # noinspection PyArgumentList
                if form.is_valid():
                    model = Product_Requests()
                    model.product_request_code = Product_Requests.generate_random_number('product_request_code', 8)

                    model.product_request_project = form.cleaned_data['product_request_project']
                    model.product_request_details = form.cleaned_data['product_request_details']

                    model.product_request_no_of_items = 0

                    model.product_request_created_at = Utils.get_current_datetime_utc()
                    model.product_request_created_id = operator.operator_id
                    model.product_request_created_by = operator.operator_name
                    model.product_request_created_department = operator.operator_department
                    model.product_request_created_role = operator.operator_role

                    model.product_request_updated_at = Utils.get_current_datetime_utc()
                    model.product_request_updated_id = operator.operator_id
                    model.product_request_updated_by = operator.operator_name
                    model.product_request_updated_department = operator.operator_department
                    model.product_request_updated_role = operator.operator_role

                    model.product_request_requested_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.product_request_requested_id = ''
                    model.product_request_requested_by = ''
                    model.product_request_requested_department = ''
                    model.product_request_requested_role = ''

                    model.product_request_reviewed_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.product_request_reviewed_id = ''
                    model.product_request_reviewed_by = ''
                    model.product_request_reviewed_department = ''
                    model.product_request_reviewed_role = ''

                    model.product_request_approved_updated_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.product_request_approved_updated_id = ''
                    model.product_request_approved_updated_by = ''
                    model.product_request_approved_updated_department = ''
                    model.product_request_approved_updated_role = ''

                    model.product_request_closed_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.product_request_closed_id = ''
                    model.product_request_closed_by = ''
                    model.product_request_closed_department = ''
                    model.product_request_closed_role = ''

                    model.product_request_cancelled_at = settings.APP_CONSTANT_DEFAULT_DATETIME_VALUE
                    model.product_request_cancelled_id = ''
                    model.product_request_cancelled_by = ''
                    model.product_request_cancelled_department = ''
                    model.product_request_cancelled_role = ''

                    model.product_request_status = Product_Requests.STATUS_PENDING
                    # noinspection PyCallByClass,PyTypeChecker
                    model.save('Created')

                    messages.info(request,
                                  'Your stock request has been created successfully.')
                    return redirect(reverse("product_requests_view", args=[model.product_request_id]))
                else:
                    return render(
                        request, template_url,
                        {
                            'section': settings.BACKEND_SECTION_STOCK_ALL_REQUESTS,
                            'title': Product_Requests.TITLE,
                            'name': Product_Requests.NAME,
                            'operator': operator,
                            'auth_permissions': auth_permissions,
                            'form': form,
                            'index_url': reverse("product_requests_index"),
                        }
                    )
            else:
                form = ProductRequestCreateForm()

            return render(
                request, template_url,
                {
                    'section': settings.BACKEND_SECTION_STOCK_ALL_REQUESTS,
                    'title': Product_Requests.TITLE,
                    'name': Product_Requests.NAME,
                    'operator': operator,
                    'auth_permissions': auth_permissions,
                    'form': form,
                    'index_url': reverse("product_requests_index"),
                }
            )
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def update(request, pk):
    template_url = 'product-requests/update.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_UPDATE in auth_permissions.values():
            try:
                model = Product_Requests.objects.get(product_request_id=pk)
                if request.method == 'POST':

                    form = ProductRequestUpdateForm(request.POST)

                    # noinspection PyArgumentList
                    if form.is_valid():
                        model.product_request_project = form.cleaned_data['product_request_project']
                        model.product_request_details = form.cleaned_data['product_request_details']

                        model.product_request_updated_at = Utils.get_current_datetime_utc()
                        model.product_request_updated_id = operator.operator_id
                        model.product_request_updated_by = operator.operator_name
                        model.product_request_updated_department = operator.operator_department
                        model.product_request_updated_role = operator.operator_role
                        model.save()

                        messages.success(request, 'Updated successfully.')
                        return redirect(reverse("product_requests_view", args=[model.product_request_id]))
                    else:
                        return render(
                            request, template_url,
                            {
                                'section': settings.BACKEND_SECTION_STOCK_ALL_REQUESTS,
                                'title': Product_Requests.TITLE,
                                'name': Product_Requests.NAME,
                                'operator': operator,
                                'auth_permissions': auth_permissions,
                                'form': form,
                                'model': model,
                                'index_url': reverse("product_requests_index"),
                            }
                        )
                else:
                    form = ProductRequestUpdateForm(
                        initial={
                            'product_request_project': model.product_request_project,
                            'product_request_details': model.product_request_details,
                        }
                    )

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_STOCK_ALL_REQUESTS,
                        'title': Product_Requests.TITLE,
                        'name': Product_Requests.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'form': form,
                        'model': model,
                        'index_url': reverse("product_requests_index"),
                    }
                )
            except(TypeError, ValueError, OverflowError, Product_Requests.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def view(request, pk):
    template_url = 'product-requests/view.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            try:
                model = Product_Requests.objects.get(product_request_id=pk)
                product_request_items = Product_Request_Items.objects.filter(
                    product_requests_product_request_id=pk).all()

                if model.product_request_created_id == str(
                        operator.operator_id) and model.product_request_status == Product_Requests.STATUS_PENDING:
                    template_url = 'product-requests/view-edit.html'

                display_level_approval = False

                timeline_notifications = []
                counter = -1
                if model.product_request_requested_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Requested <small>by ' + model.product_request_requested_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.product_request_requested_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.product_request_reviewed_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Reviewed <small>by ' + model.product_request_reviewed_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(model.product_request_reviewed_at,
                                                                                settings.TIME_ZONE,
                                                                                settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.product_request_approved_updated_id != '':
                    notification_timeline = NotificationsTimeline()
                    notification_timeline.message = 'Approved <small>by ' + model.product_request_approved_updated_role + '</small>'
                    if model.product_request_status == Product_Requests.STATUS_REJECTED:
                        notification_timeline.message = 'Rejected <small>by ' + model.product_request_approved_updated_role + '</small>'
                    notification_timeline.datetime = Utils.get_convert_datetime(
                        model.product_request_approved_updated_at,
                        settings.TIME_ZONE,
                        settings.APP_CONSTANT_DISPLAY_TIME_ZONE) + ' ' + settings.APP_CONSTANT_DISPLAY_TIME_ZONE_INFO
                    timeline_notifications.append(notification_timeline)

                if model.product_request_status == Product_Requests.STATUS_REQUESTED:
                    notification_timeline = NotificationsTimeline()
                    model.product_request_readable_status = notification_timeline.message = "<b class='text-red'>Review pending from Stock Admin</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.product_request_status == Product_Requests.STATUS_REVIEWED:
                    notification_timeline = NotificationsTimeline()
                    model.product_request_readable_status = notification_timeline.message = "<b class='text-red'>Approval pending from Stock Admin</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.product_request_status == Product_Requests.STATUS_APPROVED:
                    notification_timeline = NotificationsTimeline()
                    model.product_request_readable_status = notification_timeline.message = "<b class='text-red'>Approved</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                if model.product_request_status == Product_Requests.STATUS_REJECTED:
                    notification_timeline = NotificationsTimeline()
                    model.product_request_readable_status = notification_timeline.message = "<b class='text-red'>Rejected</b>"
                    notification_timeline.datetime = ''
                    timeline_notifications.append(notification_timeline)

                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_STOCK_ALL_REQUESTS,
                        'title': Product_Requests.TITLE,
                        'name': Product_Requests.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'model': model,
                        'index_url': reverse("product_requests_index"),
                        'select_single_url': reverse("product_requests_select_single"),
                        'product_request_items': product_request_items,
                        'product_request_items_size': product_request_items,
                        'item_index_url': reverse("product_requests_view", kwargs={'pk': pk}),
                        'item_select_single_url': reverse("product_request_items_select_single"),
                        'status_html_tag': Product_Requests.get_status_html_tag(model),
                        'display_level_approval': display_level_approval,
                        'timeline_notifications': timeline_notifications,
                    }
                )
            except(TypeError, ValueError, OverflowError, Product_Requests.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')


# noinspection PyUnusedLocal, PyShadowingBuiltins
def view_product_request_items(request, pk):
    template_url = 'product-request-items/index.html'
    operator = Operators.login_required(request)
    if operator is None:
        Operators.set_redirect_field_name(request, request.path)
        return redirect(reverse("operators_signin"))
    else:
        auth_permissions = Operators.get_auth_permissions(operator)
        if settings.ACCESS_PERMISSION_ORDER_VIEW in auth_permissions.values():
            try:
                model = Product_Requests.objects.get(product_request_id=pk)

                search_form = ProductRequestItemSearchIndexForm(request.POST or None)
                objects = Product_Request_Items.objects.filter(
                    product_requests_product_request_id=model.product_request_id)

                if request.method == 'POST' and search_form.is_valid():
                    display_search = True
                    table = ProductRequestItemsTable(objects)
                else:
                    display_search = False
                    table = ProductRequestItemsTable(objects)

                table.set_auth_permissions(auth_permissions)
                return render(
                    request, template_url,
                    {
                        'section': settings.BACKEND_SECTION_STOCK_ALL_REQUESTS,
                        'title': Product_Requests.TITLE,
                        'name': Product_Requests.NAME,
                        'operator': operator,
                        'auth_permissions': auth_permissions,
                        'table': table,
                        'search_form': search_form,
                        'display_search': display_search,
                        'index_url': reverse("product_request_items_index", kwargs={'pk': pk}),
                        'select_multiple_url': reverse("product_request_items_select_multiple"),
                        'model': model,
                        'item_index_url': reverse("product_requests_view", kwargs={'pk': pk}),
                    }
                )

            except(TypeError, ValueError, OverflowError, Product_Requests.DoesNotExist):
                return HttpResponseNotFound('Not Found', content_type='text/plain')
        else:
            return HttpResponseForbidden('Forbidden', content_type='text/plain')
