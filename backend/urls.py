# noinspection PyProtectedMember
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from backend.views import operator_views, operator_log_views, site_views, setting_views

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
    url(r'^settings/backup_restore/single-select/$', setting_views.backup_restore_single_select,
        name='backup_restore_single_select'),
    url(r'^settings/backup_restore/multiple-select/$', setting_views.backup_restore_multiple_select,
        name='backup_restore_multiple_select'),

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

    # single or multiple select
    url(r'^operators/single-select/$', operator_views.single_select,
        name='operators_single_select'),
    url(r'^operators/multiple-select/$', operator_views.multiple_select,
        name='operators_multiple_select'),

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

    # update permissions
    url(r'^operators/update/permissions/(?P<pk>\d+)/$', operator_views.update_permissions_view,
        name='operators_update_permissions_view'),
    url(r'^operators/update/permissions/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    url(r'^operators/update/permissions/$', operator_views.update_permissions_action,
        name='operators_update_permissions_action'),

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

    # operator_logs
    path('', operator_log_views.index, name='index'),
    url(r'^operator-logs/json/$', operator_log_views.json_operator_logs, name='json_operator_logs'),
    url(r'^operator-logs/index/$', operator_log_views.index, name='operator_logs_index'),
    url(r'^operator-logs/index/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    url(r'^operator-logs/single-select/$', operator_log_views.single_select,
        name='operator_logs_single_select'),
    url(r'^operator-logs/multiple-select/$', operator_log_views.multiple_select,
        name='operator_logs_multiple_select'),
    url(r'^operator-logs/(?P<pk>\d+)/$', operator_log_views.view, name='operator_logs_view'),
    url(r'^operator-logs/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

]
