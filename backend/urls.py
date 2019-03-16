# noinspection PyProtectedMember
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from backend.views import operator_views, operator_log_views, order_views, site_views, setting_views

urlpatterns = [

    # site
    url(r'^site/contact/$', site_views.contact, name='site_contact'),

    # settings
    url(r'^settings/$', setting_views.index, name='settings_index'),
    url(r'^settings/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    # file upload
    url(r'^settings/upload/$', setting_views.temp_upload, name='temp_upload'),
    # qr code
    url(r'^settings/qrcode/(?P<size>\d+)/(?P<text>.+)/$', setting_views.get_qr_code_image, name='get_qr_code_image'),

    # backup_restore
    url(r'^settings/backup-restore/$', setting_views.backup_restore, name='backup_restore'),
    url(r'^settings/backup-restore/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    url(r'^settings/backup_restore/select-single/$', setting_views.backup_restore_select_single,
        name='backup_restore_select_single'),
    url(r'^settings/backup_restore/select-multiple/$', setting_views.backup_restore_select_multiple,
        name='backup_restore_select_multiple'),

    # operators (removed - {'template_name': 'operators/signup.html'})
    path('', operator_views.index, name='index'),

    # signup and confirmation
    url(r'^operators/signup/$', operator_views.signup, name='operators_signup'),
    url(r'^operators/signup/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    url(r'^operators/signup/confirm/(?P<token>.+)/$',
        operator_views.confirm, name='operators_signup_confirm'),

    # signin
    url(r'^operators/signin/$', operator_views.signin, name='operators_signin'),
    url(r'^operators/signin/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # forgot password
    url(r'^operators/forgot-password/$', operator_views.forgot_password, name='operators_forgot_password'),
    url(r'^operators/forgot-password/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # reset password
    url(r'^operators/reset-password/(?P<token>.+)/$', operator_views.reset_password, name='operators_reset_password'),
    url(r'^operators/reset-password/(?P<token>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # signout
    url(r'^operators/signout/$', operator_views.signout, name='operators_signout'),

    # dashboard
    url(r'^operators/dashboard/$', operator_views.dashboard, name='operators_dashboard'),
    url(r'^operators/dashboard/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # index
    url(r'^operators/json/$', operator_views.json_operators, name='json_operators'),
    url(r'^operators/index/$', operator_views.index, name='operators_index'),
    url(r'^operators/index/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    # other
    url(r'^operators/api/dropdown/roles/(?P<department>.+)/$', operator_views.api_dropdown_roles,
        name='api_dropdown_roles'),
    url(r'^operators/api/dropdown/parent-operators/(?P<role>.+)/$', operator_views.api_dropdown_parent_operators,
        name='api_dropdown_parent_operators'),

    # single or multiple select
    url(r'^operators/select-single/$', operator_views.select_single,
        name='operators_select_single'),
    url(r'^operators/select-multiple/$', operator_views.select_multiple,
        name='operators_select_multiple'),

    # create
    url(r'^operators/create/$', operator_views.create, name='operators_create'),
    url(r'^operators/create/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # update
    url(r'^operators/update/(?P<pk>\d+)/$', operator_views.update, name='operators_update'),
    url(r'^operators/update/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # view
    url(r'^operators/view/(?P<pk>\d+)/$', operator_views.view, name='operators_view'),
    url(r'^operators/view/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # profile-view
    url(r'^operators/profile/view/$', operator_views.profile_view, name='operators_profile_view'),
    url(r'^operators/profile/view/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # profile-update
    url(r'^operators/profile/update/$', operator_views.profile_update, name='operators_profile_update'),
    url(r'^operators/profile/update/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # profile-change-password
    url(r'^operators/profile/change-password/$', operator_views.profile_change_password,
        name='operators_profile_change_password'),
    url(r'^operators/profile/change-password/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # update-reset-password
    url(r'^operators/update/reset-password/(?P<pk>\d+)/$', operator_views.update_reset_password,
        name='operators_update_reset_password'),
    url(r'^operators/update/reset-password/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # orders
    path('', order_views.index, name='index'),

    # index
    url(r'^orders/json/$', order_views.json_orders, name='json_orders'),
    url(r'^orders/index/$', order_views.index, name='orders_index'),
    url(r'^orders/index/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # single or multiple select
    url(r'^orders/select-single/$', order_views.select_single,
        name='orders_select_single'),
    url(r'^orders/select-multiple/$', order_views.select_multiple,
        name='orders_select_multiple'),

    # create
    url(r'^orders/create/$', order_views.create, name='orders_create'),
    url(r'^orders/create/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # update
    url(r'^orders/update/(?P<pk>\d+)/$', order_views.update, name='orders_update'),
    url(r'^orders/update/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # view
    url(r'^orders/view/(?P<pk>\d+)/$', order_views.view, name='orders_view'),
    url(r'^orders/view/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # operator_logs
    path('', operator_log_views.index, name='index'),
    url(r'^operator-logs/json/$', operator_log_views.json_operator_logs, name='json_operator_logs'),
    url(r'^operator-logs/index/$', operator_log_views.index, name='operator_logs_index'),
    url(r'^operator-logs/index/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    url(r'^operator-logs/select-single/$', operator_log_views.select_single,
        name='operator_logs_select_single'),
    url(r'^operator-logs/select-multiple/$', operator_log_views.select_multiple,
        name='operator_logs_select_multiple'),
    url(r'^operator-logs/(?P<pk>\d+)/$', operator_log_views.view, name='operator_logs_view'),
    url(r'^operator-logs/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

]
