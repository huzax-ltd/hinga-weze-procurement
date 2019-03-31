# noinspection PyProtectedMember
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from backend.views import operator_views, operator_log_views, order_views, order_item_views, order_proposal_views, \
    product_views, inventory_item_views, product_request_views, product_request_item_views, site_views, setting_views, \
    notification_views

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
    url(r'^operators/api/dropdown/role/operators/(?P<role>.+)/$', operator_views.api_dropdown_role_operators,
        name='api_dropdown_role_operators'),

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

    # view-profile
    url(r'^operators/view/profile/(?P<pk>\d+)/$', operator_views.view_profile, name='operators_view_profile'),
    url(r'^operators/view/profile/(?P<pk>\d+)/service-worker.js',
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
    url(r'^orders/index/stock/$', order_views.index_stock, name='orders_index_stock'),
    url(r'^orders/index/stock/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # single or multiple select
    url(r'^orders/select-single/$', order_views.select_single,
        name='orders_select_single'),
    url(r'^orders/select-multiple/$', order_views.select_multiple,
        name='orders_select_multiple'),
    url(r'^orders/select-single/external/$', order_views.select_single_external,
        name='orders_select_single_external'),

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

    # update order assignment
    url(r'^orders/update/assignment/(?P<pk>.+)/$', order_views.update_order_assignment,
        name='orders_update_assignment'),
    url(r'^orders/update/assignment/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # view order items
    url(r'^orders/view/order-items/(?P<pk>\d+)/$', order_views.view_order_items, name='order_items_index'),
    url(r'^orders/view/order-items/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # update procurement method
    url(r'^orders/update/procurement-method/(?P<pk>.+)/$', order_views.update_procurement_method,
        name='orders_update_procurement_method'),
    url(r'^orders/update/procurement-method/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # update supplier category
    url(r'^orders/update/supplier/(?P<pk>.+)/$', order_views.update_supplier,
        name='orders_update_supplier'),
    url(r'^orders/update/supplier/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # update email to supplier draft
    url(r'^orders/update/supplier-email/(?P<pk>.+)/$', order_views.update_email_to_supplier,
        name='orders_update_email_to_supplier'),
    url(r'^orders/update/supplier-email/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    # send email to supplier
    url(r'^orders/supplier-email/send/(?P<pk>.+)/$', order_views.send_email_to_supplier,
        name='orders_send_email_to_supplier'),
    url(r'^orders/supplier-email/send/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # upload attachments
    url(r'^orders/upload/attachments/$', order_views.upload_attachments,
        name='orders_upload_attachments'),
    url(r'^orders/upload/attachments/external/$', order_views.upload_attachments_external,
        name='orders_upload_attachments_external'),

    # update purchase
    url(r'^orders/update/purchase/(?P<pk>.+)/$', order_views.update_purchase_order,
        name='orders_update_purchase'),
    url(r'^orders/update/purchase/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # send purchase
    url(r'^orders/update/purchase-send/(?P<pk>.+)/$', order_views.send_purchase_order,
        name='orders_send_purchase'),
    url(r'^orders/update/purchase-send/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # acknowledge
    url(r'^orders/update/acknowledge/(?P<pk>.+)/$', order_views.acknowledge_proposal_external,
        name='orders_acknowledge'),
    url(r'^orders/update/acknowledge/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # update invoice
    url(r'^orders/update/invoice/(?P<pk>.+)/$', order_views.update_invoice_order,
        name='orders_update_invoice'),
    url(r'^orders/update/invoice/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # update payment voucher
    url(r'^orders/update/payment-voucher/(?P<pk>.+)/$', order_views.update_payment_voucher_order,
        name='orders_update_payment_voucher'),
    url(r'^orders/update/payment-voucher/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # order items
    # create
    url(r'^order-items/create/(?P<order_id>.+)/$', order_item_views.create, name='order_items_create'),
    url(r'^order-items/create/(?P<order_id>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # update
    url(r'^order-items/update/(?P<pk>.+)/$', order_item_views.update, name='order_items_update'),
    url(r'^order-items/update/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # single or multiple select
    url(r'^order-items/select-single/$', order_item_views.select_single, name='order_items_select_single'),
    url(r'^order-items/select-multiple/$', order_item_views.select_multiple, name='order_items_select_multiple'),

    # order proposals
    path('', order_proposal_views.index, name='index'),

    # index
    url(r'^order-proposals/index/(?P<pk>\d+)/$', order_proposal_views.index, name='order_proposals_index'),
    url(r'^order-proposals/index/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # single or multiple select
    url(r'^order-proposals/select-single/$', order_proposal_views.select_single,
        name='order_proposals_select_single'),
    url(r'^order-proposals/select-multiple/$', order_proposal_views.select_multiple,
        name='order_proposals_select_multiple'),
    # create
    url(r'^order-proposals/create/(?P<pk>.+)/(?P<code>.+)/$', order_proposal_views.create,
        name='order_proposals_create'),
    url(r'^order-proposals/create/(?P<pk>.+)/(?P<code>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    # view
    url(r'^order-proposals/view/internal/(?P<pk>.+)/$', order_proposal_views.view_internal,
        name='order_proposals_view_internal'),
    url(r'^order-proposals/view/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    # update evaluate
    url(r'^order-proposals/update/evaluate/(?P<pk>.+)/$', order_proposal_views.evaluate_proposal,
        name='order_proposals_update_evaluate'),
    url(r'^order-proposals/update/evaluate/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    # select proposal
    url(r'^order-proposals/update/select/(?P<pk>.+)/$', order_proposal_views.select_proposal,
        name='order_proposals_update_select'),
    url(r'^order-proposals/update/select/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    # other
    url(r'^order-proposals/api/dropdown/proposals/approved/(?P<code>.+)/$',
        order_proposal_views.api_dropdown_approved_proposals,
        name='api_dropdown_approved_proposals'),
    # acknowledge
    url(r'^order-proposals/update/acknowledge/(?P<pk>.+)/$', order_proposal_views.acknowledge_proposal_external,
        name='order_proposals_acknowledge'),
    url(r'^order-proposals/update/acknowledge/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # notifications
    path('', notification_views.index, name='index'),

    # index
    url(r'^notifications/json/$', notification_views.json_notifications, name='json_notifications'),
    url(r'^notifications/index/$', notification_views.index, name='notifications_index'),
    url(r'^notifications/index/service-worker.js',
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

    # products
    # path('', order_proposal_views.index, name='index'),

    # import
    url(r'^products/import-excel/$', product_views.import_excel, name='products_import_excel'),
    url(r'^products/import-excel/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    # index
    url(r'^products/goods/$', product_views.index_goods, name='products_index_goods'),
    url(r'^products/goods/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    url(r'^products/assets/$', product_views.index_assets, name='products_index_assets'),
    url(r'^products/assets/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # index inventory
    url(r'^products/goods/inventory/$', product_views.index_inventory_goods, name='products_index_inventory_goods'),
    url(r'^products/goods/inventory/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),
    url(r'^products/assets/inventory/$', product_views.index_inventory_assets, name='products_index_inventory_assets'),
    url(r'^products/assets/inventory/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # inventory items
    # create
    url(r'^inventory-items/create/(?P<pk>.+)/(?P<action>.+)/(?P<ids>.+)/$', inventory_item_views.create,
        name='inventory_item_views_create'),
    url(r'^inventory-items/create/(?P<pk>.+)/(?P<action>.+)/(?P<ids>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # product requests
    path('', product_request_views.index, name='index'),

    # index
    url(r'^product-requests/index/$', product_request_views.index, name='product_requests_index'),
    url(r'^product-requests/index/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # single or multiple select
    url(r'^product-requests/select-single/$', product_request_views.select_single,
        name='product_requests_select_single'),
    url(r'^product-requests/select-multiple/$', product_request_views.select_multiple,
        name='product_requests_select_multiple'),

    # create
    url(r'^product-requests/create/$', product_request_views.create, name='product_requests_create'),
    url(r'^product-requests/create/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # update
    url(r'^product-requests/update/(?P<pk>\d+)/$', product_request_views.update, name='product_requests_update'),
    url(r'^product-requests/update/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # view
    url(r'^product-requests/view/(?P<pk>\d+)/$', product_request_views.view, name='product_requests_view'),
    url(r'^product-requests/view/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # view product requests items
    url(r'^product-requests/view/items/(?P<pk>\d+)/$', product_request_views.view_product_request_items,
        name='product_request_items_index'),
    url(r'^product-requests/view/items/(?P<pk>\d+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # product requests items
    # create
    url(r'^product-request-items/create/(?P<id>.+)/$', product_request_item_views.create,
        name='product_request_items_create'),
    url(r'^product-request-items/create/(?P<id>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # update
    url(r'^product-request-items/update/(?P<pk>.+)/$', product_request_item_views.update,
        name='product_request_items_update'),
    url(r'^product-request-items/update/(?P<pk>.+)/service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # single or multiple select
    url(r'^product-request-items/select-single/$', product_request_item_views.select_single,
        name='product_request_items_select_single'),
    url(r'^product-request-items/select-multiple/$', product_request_item_views.select_multiple,
        name='product_request_items_select_multiple'),

]
