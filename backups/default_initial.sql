-- Access Permissions
INSERT INTO `app_access_permissions` (`access_permission_name`, `access_permission_details`, `access_permission_created_at`, `access_permission_updated_at`) VALUES
('dashboard-view', 'dashboard-view', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('log-delete', 'log-delete', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('log-view', 'log-view', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('office-create', 'office-create', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('office-delete', 'office-delete', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('office-update', 'office-update', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('office-view', 'office-view', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('operator-create', 'operator-create', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('operator-delete', 'operator-delete', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('operator-update', 'operator-update', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('operator-view', 'operator-view', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('settings-view', 'settings-view', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('template-create', 'template-create', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('template-delete', 'template-delete', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('template-update', 'template-update', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('template-view', 'template-view', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('user-create', 'user-create', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('user-delete', 'user-delete', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('user-update', 'user-update', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('user-view', 'user-view', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('visitor-create', 'visitor-create', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('visitor-delete', 'visitor-delete', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('visitor-scan', 'visitor-scan', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('visitor-update', 'visitor-update', '2018-01-01 00:00:00', '2018-01-01 00:00:00'),
('visitor-view', 'visitor-view', '2018-01-01 00:00:00', '2018-01-01 00:00:00');


-- Operators
INSERT INTO `app_operators` (`operator_id`, `operator_type`, `operator_username`, `operator_auth_key`, `operator_password_hash`, `operator_password_reset_token`, `operator_name`, `operator_gender`, `operator_contact_phone_number`, `operator_contact_email_id`, `operator_profile_photo_file_path`, `operator_created_at`, `operator_created_by`, `operator_updated_at`, `operator_updated_by`, `operator_status`) VALUES
(1, 'super-admin', 'support@qtsoftwareltd.com', 'xc48ITBOTVBu87185KUSK2TlKxKiLJiw', 'pbkdf2_sha256$100000$7rCV1tEjZeRC$N6Cv6fpo1S/Nnii7F7csUjwmEEgCu2n833ccxgQHTDY=', '', 'QT Support', '', '', 'support@qtsoftwareltd.com', '', '2018-01-01 00:00:00', 'support@qtsoftwareltd.com', '2018-01-01 00:00:00', 'support@qtsoftwareltd.com', 'active');


-- Operator Access Permissions
INSERT INTO `app_operator_access_permissions` (`operator_access_permission_id`, `operator_access_permission_updated_at`, `operator_access_permission_updated_by`, `access_permissions_access_permission_name_id`, `operators_operator_id_id`) VALUES ('1', '2018-01-01 00:00:00', 'support@qtsoftwareltd.com', 'operator-create', '1');
INSERT INTO `app_operator_access_permissions` (`operator_access_permission_id`, `operator_access_permission_updated_at`, `operator_access_permission_updated_by`, `access_permissions_access_permission_name_id`, `operators_operator_id_id`) VALUES ('2', '2018-01-01 00:00:00', 'support@qtsoftwareltd.com', 'operator-delete', '1');
INSERT INTO `app_operator_access_permissions` (`operator_access_permission_id`, `operator_access_permission_updated_at`, `operator_access_permission_updated_by`, `access_permissions_access_permission_name_id`, `operators_operator_id_id`) VALUES ('3', '2018-01-01 00:00:00', 'support@qtsoftwareltd.com', 'operator-update', '1');
INSERT INTO `app_operator_access_permissions` (`operator_access_permission_id`, `operator_access_permission_updated_at`, `operator_access_permission_updated_by`, `access_permissions_access_permission_name_id`, `operators_operator_id_id`) VALUES ('4', '2018-01-01 00:00:00', 'support@qtsoftwareltd.com', 'operator-view', '1');