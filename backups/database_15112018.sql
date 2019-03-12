-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Nov 15, 2018 at 09:44 AM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `qt_vms_main_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_access_permissions`
--

CREATE TABLE `app_access_permissions` (
  `access_permission_name` varchar(100) NOT NULL,
  `access_permission_details` varchar(255) NOT NULL,
  `access_permission_created_at` datetime NOT NULL,
  `access_permission_updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_access_permissions`
--

INSERT INTO `app_access_permissions` (`access_permission_name`, `access_permission_details`, `access_permission_created_at`, `access_permission_updated_at`) VALUES
(''dashboard-view'', ''dashboard-view'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''door-create'', ''door-create'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''door-delete'', ''door-delete'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''door-update'', ''door-update'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''door-view'', ''door-view'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''log-delete'', ''log-delete'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''log-view'', ''log-view'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''office-create'', ''office-create'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''office-delete'', ''office-delete'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''office-update'', ''office-update'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''office-view'', ''office-view'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''operator-create'', ''operator-create'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''operator-delete'', ''operator-delete'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''operator-update'', ''operator-update'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''operator-view'', ''operator-view'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''settings-view'', ''settings-view'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''template-create'', ''template-create'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''template-delete'', ''template-delete'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''template-update'', ''template-update'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''template-view'', ''template-view'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''user-create'', ''user-create'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''user-delete'', ''user-delete'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''user-update'', ''user-update'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''user-view'', ''user-view'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''visitor-create'', ''visitor-create'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''visitor-delete'', ''visitor-delete'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''visitor-scan'', ''visitor-scan'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''visitor-update'', ''visitor-update'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00''),
(''visitor-view'', ''visitor-view'', ''2018-01-01 00:00:00'', ''2018-01-01 00:00:00'');

-- --------------------------------------------------------

--
-- Table structure for table `app_doors`
--

CREATE TABLE `app_doors` (
  `door_id` varchar(6) NOT NULL,
  `door_type` varchar(10) NOT NULL,
  `offices_office_id` int(11) NOT NULL,
  `door_parent_id` int(11) NOT NULL,
  `door_code` varchar(10) NOT NULL,
  `door_title` varchar(100) NOT NULL,
  `door_details` longtext NOT NULL,
  `door_created_at` datetime NOT NULL,
  `door_created_by` varchar(255) NOT NULL,
  `door_updated_at` datetime NOT NULL,
  `door_updated_by` varchar(255) NOT NULL,
  `door_status` varchar(255) NOT NULL,
  `door_location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_doors`
--

INSERT INTO `app_doors` (`door_id`, `door_type`, `offices_office_id`, `door_parent_id`, `door_code`, `door_title`, `door_details`, `door_created_at`, `door_created_by`, `door_updated_at`, `door_updated_by`, `door_status`, `door_location`) VALUES
(''296234'', ''internal'', 0, 0, ''519865'', ''Corridor'', '''', ''2018-08-08 10:43:09'', ''support@qtsoftwareltd.com'', ''2018-08-08 10:43:09'', ''support@qtsoftwareltd.com'', ''closed'', ''''),
(''550791'', ''main'', 474063, 0, ''550791'', ''Main Gate'', '''', ''2018-08-08 09:55:01'', ''support@qtsoftwareltd.com'', ''2018-08-08 10:29:51'', ''support@qtsoftwareltd.com'', ''closed'', '''');

-- --------------------------------------------------------

--
-- Table structure for table `app_door_logs`
--

CREATE TABLE `app_door_logs` (
  `door_log_id` int(11) NOT NULL,
  `doors_door_id` int(11) NOT NULL,
  `doors_door_type` varchar(100) NOT NULL,
  `doors_door_title` varchar(100) NOT NULL,
  `door_log_message` varchar(255) NOT NULL,
  `door_log_browser` longtext NOT NULL,
  `door_log_ip_address` varchar(30) NOT NULL,
  `door_log_updated_at` datetime NOT NULL,
  `door_log_updated_by` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_door_logs`
--

INSERT INTO `app_door_logs` (`door_log_id`, `doors_door_id`, `doors_door_type`, `doors_door_title`, `door_log_message`, `door_log_browser`, `door_log_ip_address`, `door_log_updated_at`, `door_log_updated_by`) VALUES
(1, 874250, ''main'', ''Main Gate'', ''Created Door'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 09:53:51'', ''support@qtsoftwareltd.com''),
(2, 874250, ''main'', ''Main Gate'', ''Opened Door'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 09:54:37'', ''support@qtsoftwareltd.com''),
(3, 874250, ''main'', ''Main Gate'', ''Restricted Door'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 09:54:45'', ''support@qtsoftwareltd.com''),
(4, 874250, ''main'', ''Main Gate'', ''Deleted Door'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 09:54:51'', ''support@qtsoftwareltd.com''),
(5, 550791, ''main'', ''Main Gate'', ''Created Door'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 09:55:01'', ''support@qtsoftwareltd.com''),
(6, 550791, ''main'', ''Main Gate'', ''Updated Door'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 10:15:41'', ''support@qtsoftwareltd.com''),
(7, 550791, ''main'', ''Main Gate'', ''Updated Door'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 10:29:51'', ''support@qtsoftwareltd.com''),
(8, 296234, ''internal'', ''519865 (Corridor)'', ''Created Door'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 10:43:09'', ''support@qtsoftwareltd.com'');

-- --------------------------------------------------------

--
-- Table structure for table `app_failed_login`
--

CREATE TABLE `app_failed_login` (
  `failed_login_id` int(11) NOT NULL,
  `failed_login_username` varchar(255) NOT NULL,
  `failed_login_password` varchar(255) NOT NULL,
  `failed_login_from` varchar(10) NOT NULL,
  `failed_login_ip_address` varchar(100) NOT NULL,
  `failed_login_attempted_at` datetime NOT NULL,
  `failed_login_status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `app_fixed_badges`
--

CREATE TABLE `app_fixed_badges` (
  `badge_id` varchar(4) NOT NULL,
  `badge_code` varchar(255) NOT NULL,
  `badge_code_file_path` varchar(100) NOT NULL,
  `badge_name` varchar(255) NOT NULL,
  `badge_image_file_path` varchar(100) NOT NULL,
  `badge_created_at` datetime NOT NULL,
  `badge_created_by` varchar(255) NOT NULL,
  `badge_updated_at` datetime NOT NULL,
  `badge_updated_by` varchar(255) NOT NULL,
  `templates_template_id` int(11) NOT NULL,
  `badge_log_id` int(11) NOT NULL,
  `badge_status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_fixed_badges`
--

INSERT INTO `app_fixed_badges` (`badge_id`, `badge_code`, `badge_code_file_path`, `badge_name`, `badge_image_file_path`, `badge_created_at`, `badge_created_by`, `badge_updated_at`, `badge_updated_by`, `templates_template_id`, `badge_log_id`, `badge_status`) VALUES
(''6544'', ''GDK8CtvlaShq2cQNHoywwSCg9CcI5l3w'', '''', ''Badge 2'', ''fixed-badges/1533637057284.png'', ''2018-08-07 10:17:37'', ''support@qtsoftwareltd.com'', ''2018-08-07 10:17:37'', ''support@qtsoftwareltd.com'', 4647, 0, ''inactive''),
(''6637'', ''aDSLsiOrBFfyo9KkFEnqEB651qfXvrIn'', '''', ''Badge 1'', ''fixed-badges/1533636751438.png'', ''2018-08-07 10:12:31'', ''support@qtsoftwareltd.com'', ''2018-08-08 15:53:10'', ''support@qtsoftwareltd.com'', 4647, 1, ''active'');

-- --------------------------------------------------------

--
-- Table structure for table `app_fixed_badge_logs`
--

CREATE TABLE `app_fixed_badge_logs` (
  `badge_log_id` int(11) NOT NULL,
  `badges_badge_id` varchar(4) NOT NULL,
  `badge_issued_at` datetime NOT NULL,
  `badge_issued_by` varchar(255) NOT NULL,
  `badge_issued_to` varchar(255) NOT NULL,
  `badge_collected_at` datetime NOT NULL,
  `badge_collected_by` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_fixed_badge_logs`
--

INSERT INTO `app_fixed_badge_logs` (`badge_log_id`, `badges_badge_id`, `badge_issued_at`, `badge_issued_by`, `badge_issued_to`, `badge_collected_at`, `badge_collected_by`) VALUES
(1, ''6637'', ''2018-08-08 15:53:10'', ''support@qtsoftwareltd.com'', ''27378413'', ''0001-01-01 00:00:00'', '''');

-- --------------------------------------------------------

--
-- Table structure for table `app_offices`
--

CREATE TABLE `app_offices` (
  `office_id` varchar(6) NOT NULL,
  `office_type` varchar(10) NOT NULL,
  `office_code` varchar(10) NOT NULL,
  `office_title` varchar(100) NOT NULL,
  `office_sub_title` varchar(100) NOT NULL,
  `office_details` longtext NOT NULL,
  `office_location` varchar(255) NOT NULL,
  `office_start_time` time NOT NULL,
  `office_end_time` time NOT NULL,
  `office_off_days` varchar(7) NOT NULL,
  `operators_operator_id` int(11) NOT NULL,
  `office_contact_phone_number` varchar(13) NOT NULL,
  `office_contact_email_id` varchar(100) NOT NULL,
  `office_logo_file_path` varchar(100) NOT NULL,
  `templates_template_id` int(11) NOT NULL,
  `office_created_at` datetime NOT NULL,
  `office_created_by` varchar(255) NOT NULL,
  `office_updated_at` datetime NOT NULL,
  `office_updated_by` varchar(255) NOT NULL,
  `office_status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_offices`
--

INSERT INTO `app_offices` (`office_id`, `office_type`, `office_code`, `office_title`, `office_sub_title`, `office_details`, `office_location`, `office_start_time`, `office_end_time`, `office_off_days`, `operators_operator_id`, `office_contact_phone_number`, `office_contact_email_id`, `office_logo_file_path`, `templates_template_id`, `office_created_at`, `office_created_by`, `office_updated_at`, `office_updated_by`, `office_status`) VALUES
(''474063'', ''office'', ''474063'', ''QT Software Ltd.'', '''', '''', '''', ''00:00:00'', ''00:00:00'', ''1000001'', 1, '''', '''', '''', 4305, ''2018-08-07 09:15:48'', ''support@qtsoftwareltd.com'', ''2018-08-08 10:13:33'', ''support@qtsoftwareltd.com'', ''closed'');

-- --------------------------------------------------------

--
-- Table structure for table `app_office_logs`
--

CREATE TABLE `app_office_logs` (
  `office_log_id` int(11) NOT NULL,
  `offices_office_id` int(11) NOT NULL,
  `offices_office_owner` varchar(100) NOT NULL,
  `offices_office_title` varchar(100) NOT NULL,
  `office_log_message` varchar(255) NOT NULL,
  `office_log_browser` longtext NOT NULL,
  `office_log_ip_address` varchar(30) NOT NULL,
  `office_log_updated_at` datetime NOT NULL,
  `office_log_updated_by` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_office_logs`
--

INSERT INTO `app_office_logs` (`office_log_id`, `offices_office_id`, `offices_office_owner`, `offices_office_title`, `office_log_message`, `office_log_browser`, `office_log_ip_address`, `office_log_updated_at`, `office_log_updated_by`) VALUES
(1, 466847, ''1'', ''QT Software Ltd.'', ''Created Office'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 07:55:53'', ''support@qtsoftwareltd.com''),
(2, 466847, ''1'', ''QT Software Ltd.'', ''Deleted Office'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 09:15:27'', ''support@qtsoftwareltd.com''),
(3, 474063, ''1'', ''QT Software Ltd.'', ''Created Office'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 09:15:48'', ''support@qtsoftwareltd.com''),
(4, 474063, ''1'', ''QT Software Ltd.'', ''Updated Office'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 10:08:00'', ''support@qtsoftwareltd.com''),
(5, 474063, ''1'', ''QT Software Ltd.'', ''Updated Office'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 10:08:26'', ''support@qtsoftwareltd.com''),
(6, 474063, ''1'', ''QT Software Ltd.'', ''Updated Office'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 10:09:41'', ''support@qtsoftwareltd.com''),
(7, 474063, ''1'', ''QT Software Ltd.'', ''Updated Office'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 10:13:33'', ''support@qtsoftwareltd.com'');

-- --------------------------------------------------------

--
-- Table structure for table `app_operators`
--

CREATE TABLE `app_operators` (
  `operator_id` int(11) NOT NULL,
  `operator_type` varchar(20) NOT NULL,
  `operator_username` varchar(100) NOT NULL,
  `operator_auth_key` varchar(255) NOT NULL,
  `operator_password_hash` varchar(255) NOT NULL,
  `operator_password_reset_token` varchar(255) NOT NULL,
  `operator_name` varchar(100) NOT NULL,
  `operator_gender` varchar(6) NOT NULL,
  `operator_contact_phone_number` varchar(13) NOT NULL,
  `operator_contact_email_id` varchar(100) NOT NULL,
  `operator_profile_photo_file_path` varchar(255) NOT NULL,
  `operator_created_at` datetime NOT NULL,
  `operator_created_by` varchar(255) NOT NULL,
  `operator_updated_at` datetime NOT NULL,
  `operator_updated_by` varchar(255) NOT NULL,
  `operator_status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_operators`
--

INSERT INTO `app_operators` (`operator_id`, `operator_type`, `operator_username`, `operator_auth_key`, `operator_password_hash`, `operator_password_reset_token`, `operator_name`, `operator_gender`, `operator_contact_phone_number`, `operator_contact_email_id`, `operator_profile_photo_file_path`, `operator_created_at`, `operator_created_by`, `operator_updated_at`, `operator_updated_by`, `operator_status`) VALUES
(1, ''super-admin'', ''support@qtsoftwareltd.com'', ''xc48ITBOTVBu87185KUSK2TlKxKiLJiw'', ''pbkdf2_sha256$100000$7rCV1tEjZeRC$N6Cv6fpo1S/Nnii7F7csUjwmEEgCu2n833ccxgQHTDY='', '''', ''QT Support'', '''', '''', ''support@qtsoftwareltd.com'', '''', ''2018-01-01 00:00:00'', ''support@qtsoftwareltd.com'', ''2018-08-22 15:09:20'', ''support@qtsoftwareltd.com'', ''inactive''),
(2, ''office-owner'', ''nnavin@qtsoftwareltd.com'', ''OnK5cibo5KL8VEaLLEo7iadmPiWg4WYp'', ''pbkdf2_sha256$100000$rGV3xNythuDQ$3rnU59iDFuV9hmdFBkLu96UGvzMZ3J6zuMpJCme4XJg='', '''', ''Navin Nyalapelli'', ''male'', ''250726875122'', ''nnavin@qtsoftwareltd.com'', '''', ''2018-08-06 14:33:44'', ''support@qtsoftwareltd.com'', ''2018-08-06 14:33:58'', ''support@qtsoftwareltd.com'', ''inactive'');

-- --------------------------------------------------------

--
-- Table structure for table `app_operator_access_permissions`
--

CREATE TABLE `app_operator_access_permissions` (
  `operator_access_permission_id` int(11) NOT NULL,
  `operator_access_permission_updated_at` datetime NOT NULL,
  `operator_access_permission_updated_by` varchar(255) NOT NULL,
  `access_permissions_access_permission_name_id` varchar(100) NOT NULL,
  `operators_operator_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_operator_access_permissions`
--

INSERT INTO `app_operator_access_permissions` (`operator_access_permission_id`, `operator_access_permission_updated_at`, `operator_access_permission_updated_by`, `access_permissions_access_permission_name_id`, `operators_operator_id_id`) VALUES
(30, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''dashboard-view'', 1),
(31, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''door-create'', 1),
(32, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''door-delete'', 1),
(33, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''door-update'', 1),
(34, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''door-view'', 1),
(35, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''log-delete'', 1),
(36, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''log-view'', 1),
(37, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''office-create'', 1),
(38, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''office-delete'', 1),
(39, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''office-update'', 1),
(40, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''office-view'', 1),
(41, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''operator-create'', 1),
(42, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''operator-delete'', 1),
(43, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''operator-update'', 1),
(44, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''operator-view'', 1),
(45, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''settings-view'', 1),
(46, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''template-create'', 1),
(47, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''template-delete'', 1),
(48, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''template-update'', 1),
(49, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''template-view'', 1),
(50, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''user-create'', 1),
(51, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''user-delete'', 1),
(52, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''user-update'', 1),
(53, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''user-view'', 1),
(54, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''visitor-create'', 1),
(55, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''visitor-delete'', 1),
(56, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''visitor-scan'', 1),
(57, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''visitor-update'', 1),
(58, ''2018-08-08 09:31:51'', ''support@qtsoftwareltd.com'', ''visitor-view'', 1);

-- --------------------------------------------------------

--
-- Table structure for table `app_operator_logs`
--

CREATE TABLE `app_operator_logs` (
  `operator_log_id` int(11) NOT NULL,
  `operators_operator_id` int(11) NOT NULL,
  `operators_operator_username` varchar(100) NOT NULL,
  `operators_operator_name` varchar(100) NOT NULL,
  `operator_log_message` varchar(255) NOT NULL,
  `operator_log_browser` longtext NOT NULL,
  `operator_log_ip_address` varchar(30) NOT NULL,
  `operator_log_updated_at` datetime NOT NULL,
  `operator_log_updated_by` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_operator_logs`
--

INSERT INTO `app_operator_logs` (`operator_log_id`, `operators_operator_id`, `operators_operator_username`, `operators_operator_name`, `operator_log_message`, `operator_log_browser`, `operator_log_ip_address`, `operator_log_updated_at`, `operator_log_updated_by`) VALUES
(1, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-06 14:08:06'', ''support@qtsoftwareltd.com''),
(2, 2, ''nnavin@qtsoftwareltd.com'', ''Navin Nyalapelli'', ''Created Operator'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-06 14:33:44'', ''support@qtsoftwareltd.com''),
(3, 2, ''nnavin@qtsoftwareltd.com'', ''Navin Nyalapelli'', ''Verified Operator'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-06 14:33:55'', ''support@qtsoftwareltd.com''),
(4, 2, ''nnavin@qtsoftwareltd.com'', ''Navin Nyalapelli'', ''Approved Operator'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-06 14:33:58'', ''support@qtsoftwareltd.com''),
(5, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-06 15:32:01'', ''support@qtsoftwareltd.com''),
(6, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-06 17:47:26'', ''support@qtsoftwareltd.com''),
(7, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 06:55:20'', ''support@qtsoftwareltd.com''),
(8, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 07:55:41'', ''support@qtsoftwareltd.com''),
(9, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 08:59:44'', ''support@qtsoftwareltd.com''),
(10, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 10:03:20'', ''support@qtsoftwareltd.com''),
(11, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 10:22:49'', ''support@qtsoftwareltd.com''),
(12, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 10:23:02'', ''support@qtsoftwareltd.com''),
(13, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 12:21:33'', ''support@qtsoftwareltd.com''),
(14, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 14:10:22'', ''support@qtsoftwareltd.com''),
(15, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 07:45:16'', ''support@qtsoftwareltd.com''),
(16, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 09:30:38'', ''support@qtsoftwareltd.com''),
(17, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 10:30:46'', ''support@qtsoftwareltd.com''),
(18, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 12:25:33'', ''support@qtsoftwareltd.com''),
(19, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 12:27:56'', ''support@qtsoftwareltd.com''),
(20, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 12:28:25'', ''support@qtsoftwareltd.com''),
(21, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 12:38:27'', ''support@qtsoftwareltd.com''),
(22, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 12:39:07'', ''support@qtsoftwareltd.com''),
(23, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 12:47:42'', ''support@qtsoftwareltd.com''),
(24, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:02:42'', ''support@qtsoftwareltd.com''),
(25, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:10:48'', ''support@qtsoftwareltd.com''),
(26, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:11:12'', ''support@qtsoftwareltd.com''),
(27, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:11:28'', ''support@qtsoftwareltd.com''),
(28, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:11:54'', ''support@qtsoftwareltd.com''),
(29, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:14:18'', ''support@qtsoftwareltd.com''),
(30, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:14:53'', ''support@qtsoftwareltd.com''),
(31, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:20:28'', ''support@qtsoftwareltd.com''),
(32, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:22:14'', ''support@qtsoftwareltd.com''),
(33, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:36:29'', ''support@qtsoftwareltd.com''),
(34, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:45:41'', ''support@qtsoftwareltd.com''),
(35, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:47:28'', ''support@qtsoftwareltd.com''),
(36, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:47:28'', ''support@qtsoftwareltd.com''),
(37, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:47:32'', ''support@qtsoftwareltd.com''),
(38, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:50:37'', ''support@qtsoftwareltd.com''),
(39, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:52:33'', ''support@qtsoftwareltd.com''),
(40, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:55:22'', ''support@qtsoftwareltd.com''),
(41, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 13:56:52'', ''support@qtsoftwareltd.com''),
(42, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:00:57'', ''support@qtsoftwareltd.com''),
(43, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:03:46'', ''support@qtsoftwareltd.com''),
(44, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:03:49'', ''support@qtsoftwareltd.com''),
(45, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:05:04'', ''support@qtsoftwareltd.com''),
(46, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:05:04'', ''support@qtsoftwareltd.com''),
(47, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:05:07'', ''support@qtsoftwareltd.com''),
(48, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:18:53'', ''support@qtsoftwareltd.com''),
(49, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:19:03'', ''support@qtsoftwareltd.com''),
(50, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:20:04'', ''support@qtsoftwareltd.com''),
(51, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:26:43'', ''support@qtsoftwareltd.com''),
(52, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:32:11'', ''support@qtsoftwareltd.com''),
(53, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:40:52'', ''support@qtsoftwareltd.com''),
(54, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:40:55'', ''support@qtsoftwareltd.com''),
(55, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:43:44'', ''support@qtsoftwareltd.com''),
(56, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:44:07'', ''support@qtsoftwareltd.com''),
(57, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:44:22'', ''support@qtsoftwareltd.com''),
(58, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:52:27'', ''support@qtsoftwareltd.com''),
(59, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:57:29'', ''support@qtsoftwareltd.com''),
(60, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:58:27'', ''support@qtsoftwareltd.com''),
(61, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 15:39:43'', ''support@qtsoftwareltd.com''),
(62, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 15:56:57'', ''support@qtsoftwareltd.com''),
(63, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Safari 11.1.1 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-20 14:07:02'', ''support@qtsoftwareltd.com''),
(64, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-22 15:03:04'', ''support@qtsoftwareltd.com''),
(65, 1, ''support@qtsoftwareltd.com'', ''QT Support'', ''Operator Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-22 15:09:20'', ''support@qtsoftwareltd.com'');

-- --------------------------------------------------------

--
-- Table structure for table `app_templates`
--

CREATE TABLE `app_templates` (
  `template_id` varchar(4) NOT NULL,
  `template_type` varchar(10) NOT NULL,
  `template_display_card_background_image` tinyint(1) NOT NULL,
  `template_card_background_image` varchar(100) NOT NULL,
  `template_card_background_color` varchar(30) NOT NULL,
  `template_display_header_background_image` tinyint(1) NOT NULL,
  `template_header_background_image` varchar(100) NOT NULL,
  `template_header_background_color` varchar(30) NOT NULL,
  `template_display_header_title` tinyint(1) NOT NULL,
  `template_header_title` varchar(30) NOT NULL,
  `template_header_title_font_color` varchar(30) NOT NULL,
  `template_display_center_photo` tinyint(1) NOT NULL,
  `template_center_photo` varchar(100) NOT NULL,
  `template_display_center_name` tinyint(1) NOT NULL,
  `template_center_name` varchar(30) NOT NULL,
  `template_center_name_font_color` varchar(30) NOT NULL,
  `template_display_center_company` tinyint(1) NOT NULL,
  `template_center_company` varchar(30) NOT NULL,
  `template_center_company_font_color` varchar(30) NOT NULL,
  `template_display_center_armed` tinyint(1) NOT NULL,
  `template_display_center_code` tinyint(1) NOT NULL,
  `template_display_category` tinyint(1) NOT NULL,
  `template_category_background_color` varchar(30) NOT NULL,
  `template_category_title` varchar(30) NOT NULL,
  `template_category_title_font_color` varchar(30) NOT NULL,
  `template_display_footer` tinyint(1) NOT NULL,
  `template_footer_background_color` varchar(30) NOT NULL,
  `template_footer_title` varchar(30) NOT NULL,
  `template_footer_title_font_color` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_templates`
--

INSERT INTO `app_templates` (`template_id`, `template_type`, `template_display_card_background_image`, `template_card_background_image`, `template_card_background_color`, `template_display_header_background_image`, `template_header_background_image`, `template_header_background_color`, `template_display_header_title`, `template_header_title`, `template_header_title_font_color`, `template_display_center_photo`, `template_center_photo`, `template_display_center_name`, `template_center_name`, `template_center_name_font_color`, `template_display_center_company`, `template_center_company`, `template_center_company_font_color`, `template_display_center_armed`, `template_display_center_code`, `template_display_category`, `template_category_background_color`, `template_category_title`, `template_category_title_font_color`, `template_display_footer`, `template_footer_background_color`, `template_footer_title`, `template_footer_title_font_color`) VALUES
(''4305'', ''dynamic'', 1, ''templates/1533633535420.png'', ''rgb(255, 255, 255)'', 0, '''', ''rgb(255, 245, 0)'', 1, ''Telecom House.'', ''rgb(0, 0, 0)'', 1, '''', 1, ''Employee Name'', ''rgb(255, 255, 255)'', 1, ''QT Software Ltd.'', ''rgb(250, 255, 0)'', 0, 1, 1, ''rgb(255, 230, 0)'', ''Employee'', ''rgb(0, 0, 0)'', 1, ''rgba(179, 33, 33, 0)'', ''Contact +250726875122'', ''rgb(255, 255, 255)''),
(''4647'', ''static'', 1, ''templates/1533636363329.png'', ''rgb(255, 255, 255)'', 0, '''', ''rgba(158, 0, 255, 0.39)'', 1, ''Telecom House.'', ''rgb(255, 255, 255)'', 1, '''', 1, ''Badge Name'', ''rgb(255, 255, 255)'', 0, '''', ''rgba(0, 0, 0, 1)'', 0, 1, 1, ''rgb(196, 52, 219)'', ''Visitor'', ''rgb(255, 255, 255)'', 1, ''rgba(255, 255, 255, 0)'', '''', ''rgb(0, 0, 0)'');

-- --------------------------------------------------------

--
-- Table structure for table `app_users`
--

CREATE TABLE `app_users` (
  `user_id` varchar(6) NOT NULL,
  `user_type` varchar(10) NOT NULL,
  `user_username` varchar(100) NOT NULL,
  `user_access_id` varchar(100) NOT NULL,
  `user_auth_key` varchar(255) NOT NULL,
  `user_auth_key_pin` varchar(255) NOT NULL,
  `user_auth_key_finger` varchar(255) NOT NULL,
  `user_auth_key_face` varchar(255) NOT NULL,
  `user_auth_key_eyes` varchar(255) NOT NULL,
  `user_password_hash` varchar(255) NOT NULL,
  `user_password_reset_token` varchar(255) NOT NULL,
  `user_title` varchar(3) NOT NULL,
  `user_firstname` varchar(100) NOT NULL,
  `user_middlename` varchar(100) NOT NULL,
  `user_lastname` varchar(100) NOT NULL,
  `user_gender` varchar(6) NOT NULL,
  `user_date_of_birth` date NOT NULL,
  `user_profession` varchar(255) NOT NULL,
  `user_company` varchar(255) NOT NULL,
  `user_position` varchar(255) NOT NULL,
  `user_address` varchar(255) NOT NULL,
  `user_area` varchar(255) NOT NULL,
  `user_landmark` varchar(255) NOT NULL,
  `user_city` varchar(255) NOT NULL,
  `user_state` varchar(255) NOT NULL,
  `user_country` varchar(255) NOT NULL,
  `user_zipcode` varchar(255) NOT NULL,
  `user_location_latitude` decimal(30,6) NOT NULL,
  `user_location_longitude` decimal(30,6) NOT NULL,
  `user_contact_phone_number` varchar(13) NOT NULL,
  `user_contact_email_id` varchar(100) NOT NULL,
  `user_profile_photo_file_path` varchar(100) NOT NULL,
  `user_identity_type` varchar(255) NOT NULL,
  `user_identity_number` varchar(255) NOT NULL,
  `user_identity_file_path` varchar(100) NOT NULL,
  `user_armed` varchar(3) NOT NULL,
  `offices_office_id` int(11) NOT NULL,
  `user_created_at` datetime NOT NULL,
  `user_created_by` varchar(255) NOT NULL,
  `user_updated_at` datetime NOT NULL,
  `user_updated_by` varchar(255) NOT NULL,
  `user_approved_at` datetime NOT NULL,
  `user_approved_by` varchar(255) NOT NULL,
  `user_badge_code` varchar(255) NOT NULL,
  `user_badge_code_file_path` varchar(100) NOT NULL,
  `user_badge_category` varchar(255) NOT NULL,
  `user_badge_expires_at` date NOT NULL,
  `user_badge_issued_at` datetime NOT NULL,
  `user_badge_issued_by` varchar(255) NOT NULL,
  `user_badge_collected_at` datetime NOT NULL,
  `user_badge_collected_by` varchar(255) NOT NULL,
  `user_status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_users`
--

INSERT INTO `app_users` (`user_id`, `user_type`, `user_username`, `user_access_id`, `user_auth_key`, `user_auth_key_pin`, `user_auth_key_finger`, `user_auth_key_face`, `user_auth_key_eyes`, `user_password_hash`, `user_password_reset_token`, `user_title`, `user_firstname`, `user_middlename`, `user_lastname`, `user_gender`, `user_date_of_birth`, `user_profession`, `user_company`, `user_position`, `user_address`, `user_area`, `user_landmark`, `user_city`, `user_state`, `user_country`, `user_zipcode`, `user_location_latitude`, `user_location_longitude`, `user_contact_phone_number`, `user_contact_email_id`, `user_profile_photo_file_path`, `user_identity_type`, `user_identity_number`, `user_identity_file_path`, `user_armed`, `offices_office_id`, `user_created_at`, `user_created_by`, `user_updated_at`, `user_updated_by`, `user_approved_at`, `user_approved_by`, `user_badge_code`, `user_badge_code_file_path`, `user_badge_category`, `user_badge_expires_at`, `user_badge_issued_at`, `user_badge_issued_by`, `user_badge_collected_at`, `user_badge_collected_by`, `user_status`) VALUES
(''655571'', ''employee'', ''nnavin@qtsoftwareltd.com'', '''', ''ch1jGddoOUEcaigf52vpxUg9zjsrcr3s'', '''', '''', '''', '''', ''pbkdf2_sha256$100000$AndqNIMSMLBM$8g5wVIGoBVje1SFITCjXQt5pIbqtR4goRZ6l+Jh1Hc8='', '''', '''', ''Navin'', '''', ''Nyalapelli'', ''male'', ''0001-01-01'', '''', '''', '''', '''', '''', '''', '''', '''', '''', '''', ''0.000000'', ''0.000000'', ''250726875122'', ''nnavin@qtsoftwareltd.com'', ''users/profile/1533644594662.png'', '''', '''', '''', ''no'', 474063, ''2018-08-07 10:50:13'', ''support@qtsoftwareltd.com'', ''2018-08-08 15:47:58'', ''support@qtsoftwareltd.com'', ''2018-08-08 14:52:35'', ''support@qtsoftwareltd.com'', ''5NAqTS3N3LurbJOqwOlRS2rfdIrhzjDT'', '''', ''Employee'', ''0001-01-01'', ''2018-08-07 14:47:15'', ''support@qtsoftwareltd.com'', ''0001-01-01 00:00:00'', '''', ''inactive'');

-- --------------------------------------------------------

--
-- Table structure for table `app_user_attendances`
--

CREATE TABLE `app_user_attendances` (
  `user_attendance_id` int(11) NOT NULL,
  `users_user_id` int(11) NOT NULL,
  `user_attendance_entered_at` datetime NOT NULL,
  `user_attendance_exited_at` datetime NOT NULL,
  `user_attendance_status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `app_user_logs`
--

CREATE TABLE `app_user_logs` (
  `user_log_id` int(11) NOT NULL,
  `users_user_id` int(11) NOT NULL,
  `users_user_username` varchar(100) NOT NULL,
  `users_user_name` varchar(100) NOT NULL,
  `user_log_message` varchar(255) NOT NULL,
  `user_log_browser` longtext NOT NULL,
  `user_log_ip_address` varchar(30) NOT NULL,
  `user_log_updated_at` datetime NOT NULL,
  `user_log_updated_by` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_user_logs`
--

INSERT INTO `app_user_logs` (`user_log_id`, `users_user_id`, `users_user_username`, `users_user_name`, `user_log_message`, `user_log_browser`, `user_log_ip_address`, `user_log_updated_at`, `user_log_updated_by`) VALUES
(1, 655571, ''nnavin@qtsoftwareltd.com'', ''Navin Nyalapelli'', ''Created Employee'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 10:50:13'', ''support@qtsoftwareltd.com''),
(2, 655571, ''nnavin@qtsoftwareltd.com'', ''Navin Nyalapelli'', ''Updated Employee'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 12:23:15'', ''support@qtsoftwareltd.com''),
(3, 655571, ''nnavin@qtsoftwareltd.com'', ''Navin Nyalapelli'', ''Badge Issued'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 14:44:25'', ''support@qtsoftwareltd.com''),
(4, 655571, ''nnavin@qtsoftwareltd.com'', ''Navin Nyalapelli'', ''Badge Issued'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 14:46:08'', ''support@qtsoftwareltd.com''),
(5, 655571, ''nnavin@qtsoftwareltd.com'', ''Navin Nyalapelli'', ''Badge Issued'', ''Browser:Chrome 67.0.3396 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-07 14:47:15'', ''support@qtsoftwareltd.com''),
(6, 655571, ''nnavin@qtsoftwareltd.com'', ''NavinNyalapelli'', ''Employee Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:52:01'', ''nnavin@qtsoftwareltd.com''),
(7, 655571, ''nnavin@qtsoftwareltd.com'', ''Navin Nyalapelli'', ''Updated Employee'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:52:07'', ''nnavin@qtsoftwareltd.com''),
(8, 655571, ''nnavin@qtsoftwareltd.com'', ''Navin Nyalapelli'', ''Approved Employee'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:52:35'', ''support@qtsoftwareltd.com''),
(9, 655571, ''nnavin@qtsoftwareltd.com'', ''NavinNyalapelli'', ''Employee Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:52:50'', ''nnavin@qtsoftwareltd.com''),
(10, 655571, ''nnavin@qtsoftwareltd.com'', ''NavinNyalapelli'', ''Employee Login'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:53:02'', ''nnavin@qtsoftwareltd.com''),
(11, 655571, ''nnavin@qtsoftwareltd.com'', ''NavinNyalapelli'', ''Employee Logout'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 14:56:56'', ''nnavin@qtsoftwareltd.com''),
(12, 655571, ''nnavin@qtsoftwareltd.com'', ''Navin Nyalapelli'', ''Blocked Employee'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 15:47:54'', ''support@qtsoftwareltd.com''),
(13, 655571, ''nnavin@qtsoftwareltd.com'', ''Navin Nyalapelli'', ''Unblocked Employee'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 15:47:58'', ''support@qtsoftwareltd.com'');

-- --------------------------------------------------------

--
-- Table structure for table `app_visitors`
--

CREATE TABLE `app_visitors` (
  `visitor_id` varchar(8) NOT NULL,
  `visitor_type` varchar(10) NOT NULL,
  `visitor_auth_key` varchar(255) NOT NULL,
  `offices_office_id` int(11) NOT NULL,
  `visitor_purpose` varchar(255) NOT NULL,
  `users_user_id` int(11) NOT NULL,
  `visitor_title` varchar(3) NOT NULL,
  `visitor_firstname` varchar(100) NOT NULL,
  `visitor_middlename` varchar(100) NOT NULL,
  `visitor_lastname` varchar(100) NOT NULL,
  `visitor_gender` varchar(6) NOT NULL,
  `visitor_date_of_birth` date NOT NULL,
  `visitor_profession` varchar(255) NOT NULL,
  `visitor_company` varchar(255) NOT NULL,
  `visitor_position` varchar(255) NOT NULL,
  `visitor_address` varchar(255) NOT NULL,
  `visitor_area` varchar(255) NOT NULL,
  `visitor_landmark` varchar(255) NOT NULL,
  `visitor_city` varchar(255) NOT NULL,
  `visitor_state` varchar(255) NOT NULL,
  `visitor_country` varchar(255) NOT NULL,
  `visitor_zipcode` varchar(255) NOT NULL,
  `visitor_location_latitude` decimal(30,6) NOT NULL,
  `visitor_location_longitude` decimal(30,6) NOT NULL,
  `visitor_contact_phone_number` varchar(13) NOT NULL,
  `visitor_contact_email_id` varchar(100) NOT NULL,
  `visitor_profile_photo_file_path` varchar(100) NOT NULL,
  `visitor_identity_type` varchar(255) NOT NULL,
  `visitor_identity_number` varchar(255) NOT NULL,
  `visitor_identity_file_path` varchar(100) NOT NULL,
  `visitor_armed` varchar(3) NOT NULL,
  `visitor_created_at` datetime NOT NULL,
  `visitor_created_by` varchar(255) NOT NULL,
  `visitor_updated_at` datetime NOT NULL,
  `visitor_updated_by` varchar(255) NOT NULL,
  `visitor_requested_at` datetime NOT NULL,
  `visitor_requested_by` varchar(255) NOT NULL,
  `visitor_approved_at` datetime NOT NULL,
  `visitor_approved_by` varchar(255) NOT NULL,
  `visitor_entered_at` datetime NOT NULL,
  `visitor_entered_by` varchar(255) NOT NULL,
  `visitor_exited_at` datetime NOT NULL,
  `visitor_exited_by` varchar(255) NOT NULL,
  `visitor_status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_visitors`
--

INSERT INTO `app_visitors` (`visitor_id`, `visitor_type`, `visitor_auth_key`, `offices_office_id`, `visitor_purpose`, `users_user_id`, `visitor_title`, `visitor_firstname`, `visitor_middlename`, `visitor_lastname`, `visitor_gender`, `visitor_date_of_birth`, `visitor_profession`, `visitor_company`, `visitor_position`, `visitor_address`, `visitor_area`, `visitor_landmark`, `visitor_city`, `visitor_state`, `visitor_country`, `visitor_zipcode`, `visitor_location_latitude`, `visitor_location_longitude`, `visitor_contact_phone_number`, `visitor_contact_email_id`, `visitor_profile_photo_file_path`, `visitor_identity_type`, `visitor_identity_number`, `visitor_identity_file_path`, `visitor_armed`, `visitor_created_at`, `visitor_created_by`, `visitor_updated_at`, `visitor_updated_by`, `visitor_requested_at`, `visitor_requested_by`, `visitor_approved_at`, `visitor_approved_by`, `visitor_entered_at`, `visitor_entered_by`, `visitor_exited_at`, `visitor_exited_by`, `visitor_status`) VALUES
(''27378413'', ''visitor'', ''vez49G4JMdhNNLZsmC9Yg8RZtBqIP8cm'', 474063, ''Meeting'', 0, '''', ''Navin'', '''', ''Nyalapelli'', ''male'', ''0001-01-01'', '''', '''', '''', '''', '''', '''', '''', '''', '''', '''', ''0.000000'', ''0.000000'', '''', '''', '''', ''passport'', ''R12345'', '''', ''no'', ''2018-08-08 15:53:10'', ''support@qtsoftwareltd.com'', ''2018-08-08 15:53:10'', ''support@qtsoftwareltd.com'', ''0001-01-01 00:00:00'', '''', ''2018-08-08 15:53:10'', ''support@qtsoftwareltd.com'', ''2018-08-08 15:53:10'', ''support@qtsoftwareltd.com'', ''0001-01-01 00:00:00'', '''', ''active'');

-- --------------------------------------------------------

--
-- Table structure for table `app_visitor_logs`
--

CREATE TABLE `app_visitor_logs` (
  `visitor_log_id` int(11) NOT NULL,
  `visitors_visitor_id` varchar(8) NOT NULL,
  `visitors_visitor_email_id` varchar(100) NOT NULL,
  `visitors_visitor_name` varchar(100) NOT NULL,
  `visitor_log_message` varchar(255) NOT NULL,
  `visitor_log_browser` longtext NOT NULL,
  `visitor_log_ip_address` varchar(30) NOT NULL,
  `visitor_log_updated_at` datetime NOT NULL,
  `visitor_log_updated_by` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `app_visitor_logs`
--

INSERT INTO `app_visitor_logs` (`visitor_log_id`, `visitors_visitor_id`, `visitors_visitor_email_id`, `visitors_visitor_name`, `visitor_log_message`, `visitor_log_browser`, `visitor_log_ip_address`, `visitor_log_updated_at`, `visitor_log_updated_by`) VALUES
(1, ''27378413'', '''', ''Navin Nyalapelli'', ''Created Visitor'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 15:53:10'', ''support@qtsoftwareltd.com''),
(2, ''27378413'', '''', ''Navin Nyalapelli'', ''Entered Visitor'', ''Browser:Chrome 68.0.3440 Device:Other OS:Mac OS X 10.13.5'', ''127.0.0.1'', ''2018-08-08 15:53:10'', ''support@qtsoftwareltd.com'');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, ''Can add backups'', 1, ''add_backups''),
(2, ''Can change backups'', 1, ''change_backups''),
(3, ''Can delete backups'', 1, ''delete_backups''),
(4, ''Can add access_ permissions'', 2, ''add_access_permissions''),
(5, ''Can change access_ permissions'', 2, ''change_access_permissions''),
(6, ''Can delete access_ permissions'', 2, ''delete_access_permissions''),
(7, ''Can add door_ logs'', 3, ''add_door_logs''),
(8, ''Can change door_ logs'', 3, ''change_door_logs''),
(9, ''Can delete door_ logs'', 3, ''delete_door_logs''),
(10, ''Can add doors'', 4, ''add_doors''),
(11, ''Can change doors'', 4, ''change_doors''),
(12, ''Can delete doors'', 4, ''delete_doors''),
(13, ''Can add failed_ login'', 5, ''add_failed_login''),
(14, ''Can change failed_ login'', 5, ''change_failed_login''),
(15, ''Can delete failed_ login'', 5, ''delete_failed_login''),
(16, ''Can add fixed_ badge_ logs'', 6, ''add_fixed_badge_logs''),
(17, ''Can change fixed_ badge_ logs'', 6, ''change_fixed_badge_logs''),
(18, ''Can delete fixed_ badge_ logs'', 6, ''delete_fixed_badge_logs''),
(19, ''Can add fixed_ badges'', 7, ''add_fixed_badges''),
(20, ''Can change fixed_ badges'', 7, ''change_fixed_badges''),
(21, ''Can delete fixed_ badges'', 7, ''delete_fixed_badges''),
(22, ''Can add office_ logs'', 8, ''add_office_logs''),
(23, ''Can change office_ logs'', 8, ''change_office_logs''),
(24, ''Can delete office_ logs'', 8, ''delete_office_logs''),
(25, ''Can add offices'', 9, ''add_offices''),
(26, ''Can change offices'', 9, ''change_offices''),
(27, ''Can delete offices'', 9, ''delete_offices''),
(28, ''Can add operator_ access_ permissions'', 10, ''add_operator_access_permissions''),
(29, ''Can change operator_ access_ permissions'', 10, ''change_operator_access_permissions''),
(30, ''Can delete operator_ access_ permissions'', 10, ''delete_operator_access_permissions''),
(31, ''Can add operator_ logs'', 11, ''add_operator_logs''),
(32, ''Can change operator_ logs'', 11, ''change_operator_logs''),
(33, ''Can delete operator_ logs'', 11, ''delete_operator_logs''),
(34, ''Can add operators'', 12, ''add_operators''),
(35, ''Can change operators'', 12, ''change_operators''),
(36, ''Can delete operators'', 12, ''delete_operators''),
(37, ''Can add templates'', 13, ''add_templates''),
(38, ''Can change templates'', 13, ''change_templates''),
(39, ''Can delete templates'', 13, ''delete_templates''),
(40, ''Can add user_ attendances'', 14, ''add_user_attendances''),
(41, ''Can change user_ attendances'', 14, ''change_user_attendances''),
(42, ''Can delete user_ attendances'', 14, ''delete_user_attendances''),
(43, ''Can add user_ logs'', 15, ''add_user_logs''),
(44, ''Can change user_ logs'', 15, ''change_user_logs''),
(45, ''Can delete user_ logs'', 15, ''delete_user_logs''),
(46, ''Can add users'', 16, ''add_users''),
(47, ''Can change users'', 16, ''change_users''),
(48, ''Can delete users'', 16, ''delete_users''),
(49, ''Can add visitor_ logs'', 17, ''add_visitor_logs''),
(50, ''Can change visitor_ logs'', 17, ''change_visitor_logs''),
(51, ''Can delete visitor_ logs'', 17, ''delete_visitor_logs''),
(52, ''Can add visitors'', 18, ''add_visitors''),
(53, ''Can change visitors'', 18, ''change_visitors''),
(54, ''Can delete visitors'', 18, ''delete_visitors''),
(55, ''Can add log entry'', 19, ''add_logentry''),
(56, ''Can change log entry'', 19, ''change_logentry''),
(57, ''Can delete log entry'', 19, ''delete_logentry''),
(58, ''Can add permission'', 20, ''add_permission''),
(59, ''Can change permission'', 20, ''change_permission''),
(60, ''Can delete permission'', 20, ''delete_permission''),
(61, ''Can add group'', 21, ''add_group''),
(62, ''Can change group'', 21, ''change_group''),
(63, ''Can delete group'', 21, ''delete_group''),
(64, ''Can add user'', 22, ''add_user''),
(65, ''Can change user'', 22, ''change_user''),
(66, ''Can delete user'', 22, ''delete_user''),
(67, ''Can add content type'', 23, ''add_contenttype''),
(68, ''Can change content type'', 23, ''change_contenttype''),
(69, ''Can delete content type'', 23, ''delete_contenttype''),
(70, ''Can add session'', 24, ''add_session''),
(71, ''Can change session'', 24, ''change_session''),
(72, ''Can delete session'', 24, ''delete_session''),
(73, ''Can add site'', 25, ''add_site''),
(74, ''Can change site'', 25, ''change_site''),
(75, ''Can delete site'', 25, ''delete_site'');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(19, ''admin'', ''logentry''),
(2, ''app'', ''access_permissions''),
(1, ''app'', ''backups''),
(4, ''app'', ''doors''),
(3, ''app'', ''door_logs''),
(5, ''app'', ''failed_login''),
(7, ''app'', ''fixed_badges''),
(6, ''app'', ''fixed_badge_logs''),
(9, ''app'', ''offices''),
(8, ''app'', ''office_logs''),
(12, ''app'', ''operators''),
(10, ''app'', ''operator_access_permissions''),
(11, ''app'', ''operator_logs''),
(13, ''app'', ''templates''),
(16, ''app'', ''users''),
(14, ''app'', ''user_attendances''),
(15, ''app'', ''user_logs''),
(18, ''app'', ''visitors''),
(17, ''app'', ''visitor_logs''),
(21, ''auth'', ''group''),
(20, ''auth'', ''permission''),
(22, ''auth'', ''user''),
(23, ''contenttypes'', ''contenttype''),
(24, ''sessions'', ''session''),
(25, ''sites'', ''site'');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, ''contenttypes'', ''0001_initial'', ''2018-08-06 14:06:23''),
(2, ''auth'', ''0001_initial'', ''2018-08-06 14:06:23''),
(3, ''admin'', ''0001_initial'', ''2018-08-06 14:06:23''),
(4, ''admin'', ''0002_logentry_remove_auto_add'', ''2018-08-06 14:06:23''),
(5, ''app'', ''0001_initial'', ''2018-08-06 14:06:24''),
(6, ''contenttypes'', ''0002_remove_content_type_name'', ''2018-08-06 14:06:24''),
(7, ''auth'', ''0002_alter_permission_name_max_length'', ''2018-08-06 14:06:24''),
(8, ''auth'', ''0003_alter_user_email_max_length'', ''2018-08-06 14:06:24''),
(9, ''auth'', ''0004_alter_user_username_opts'', ''2018-08-06 14:06:24''),
(10, ''auth'', ''0005_alter_user_last_login_null'', ''2018-08-06 14:06:24''),
(11, ''auth'', ''0006_require_contenttypes_0002'', ''2018-08-06 14:06:24''),
(12, ''auth'', ''0007_alter_validators_add_error_messages'', ''2018-08-06 14:06:24''),
(13, ''auth'', ''0008_alter_user_username_max_length'', ''2018-08-06 14:06:24''),
(14, ''auth'', ''0009_alter_user_last_name_max_length'', ''2018-08-06 14:06:24''),
(15, ''sessions'', ''0001_initial'', ''2018-08-06 14:06:24''),
(16, ''sites'', ''0001_initial'', ''2018-08-06 14:06:24''),
(17, ''sites'', ''0002_alter_domain_unique'', ''2018-08-06 14:06:24''),
(18, ''app'', ''0002_doors_door_location'', ''2018-08-08 09:30:25'');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
(''144tu4tc9vtcxgjiaghlf6aw7wks4jmf'', ''MDkxZjgyYzA5ZTE4OTI3YTg1NDY4NWIxZDRlZWU1ZTU1OGJlNjUwNDp7Im5leHQiOiIvYmFja2VuZC91c2Vycy9jcmVhdGUvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9'', ''2018-08-08 15:20:04''),
(''2y390vdkoxuxf4ba0mbx51lfnuu6qz5v'', ''NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 15:03:49''),
(''2z9y3pz56lv10dukjm7vjhhyvu8rz2dr'', ''ODg3OTVhYjQ4YmM2OTE5ODQ4YzJmMjcxZjY5NzdiODcyZjQzMzExYjp7Im5leHQiOiIvYmFja2VuZC91c2Vycy9pbmRleC8iLCJfb3BlcmF0b3JzX2lkIjoiMSIsIl9vcGVyYXRvcnNfYmFja2VuZCI6bnVsbCwiX29wZXJhdG9yc19oYXNoIjoiZTBiZmExZGVhMDRiZTMwZDE1ZjdmNDFlYjhlMzkyOTViMGUzOTdhMCIsIl9zZXNzaW9uX2V4cGlyeSI6MzYwMH0='', ''2018-08-08 15:18:53''),
(''37pl8gztxvczsx5egk5s9ksftzu5hhoc'', ''ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 14:36:29''),
(''3rphekofqstdploguuxtiwaarr46uxen'', ''ODg3OTVhYjQ4YmM2OTE5ODQ4YzJmMjcxZjY5NzdiODcyZjQzMzExYjp7Im5leHQiOiIvYmFja2VuZC91c2Vycy9pbmRleC8iLCJfb3BlcmF0b3JzX2lkIjoiMSIsIl9vcGVyYXRvcnNfYmFja2VuZCI6bnVsbCwiX29wZXJhdG9yc19oYXNoIjoiZTBiZmExZGVhMDRiZTMwZDE1ZjdmNDFlYjhlMzkyOTViMGUzOTdhMCIsIl9zZXNzaW9uX2V4cGlyeSI6MzYwMH0='', ''2018-08-07 13:21:33''),
(''47gj3kdr71oelzox3aqhninrovwxx6e8'', ''ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 14:14:53''),
(''4tabd5h8vbaige63va830cgyu325mbxh'', ''ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 14:20:28''),
(''5bvo7s9osrorqg63brmu4mdv1m2e4im4'', ''ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 14:56:52''),
(''5y1m5gq48c4bu5x1qop83unjwtdpimta'', ''ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 14:11:54''),
(''69yl4fippkm5wmohi3k8yi01zsren43f'', ''ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 14:14:18''),
(''8xy58s2j7gwbc295n0lt112u9q2xt2ok'', ''NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 10:30:38''),
(''b9ctnv7otcl7hfdh96cvadyr4aki2ze9'', ''NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 08:45:16''),
(''c5isfn067rab2ag0w94gdwmaby0enqrl'', ''NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-07 11:23:02''),
(''dhzq69yx4fu44mpl17mn8zq6p9j5bb57'', ''ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-20 15:07:02''),
(''f3dq6g4vntos9jg8y3s4jdh4zqk1f6ad'', ''ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 14:55:22''),
(''fs0mtf844h7m89yocqltlnolfush01yw'', ''ODg3OTVhYjQ4YmM2OTE5ODQ4YzJmMjcxZjY5NzdiODcyZjQzMzExYjp7Im5leHQiOiIvYmFja2VuZC91c2Vycy9pbmRleC8iLCJfb3BlcmF0b3JzX2lkIjoiMSIsIl9vcGVyYXRvcnNfYmFja2VuZCI6bnVsbCwiX29wZXJhdG9yc19oYXNoIjoiZTBiZmExZGVhMDRiZTMwZDE1ZjdmNDFlYjhlMzkyOTViMGUzOTdhMCIsIl9zZXNzaW9uX2V4cGlyeSI6MzYwMH0='', ''2018-08-08 15:19:03''),
(''hhpnwpk7p70pwxmf9piklr4ys8ssk8s0'', ''NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 14:02:42''),
(''i91g6d7mwlfaugoa02vwfmrhwg9g0pm3'', ''ZWU4MjQyMDgwZDE2ZTRjZTA3YjAyOWFlMzY0MDgxMTc1MjgzMmM4Yzp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyJ9'', ''2018-08-22 12:24:57''),
(''imu7uern1l6ev8rs5bbecoi0wsnrbs3f'', ''NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 14:52:33''),
(''juo7g57grljqd27ommxabcgfcvqd34mc'', ''NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 14:11:28''),
(''l110ddlqt9cgzzzo1rgnsi7cf212nybg'', ''YjNkNmE5MjMwYjA1MmFmNGFkODZhMTI5ZDg5YWUxMzU1Yzc0ODI0Nzp7Im5leHQiOiIvYmFja2VuZC92aXNpdG9ycy9zY2FuLzAvIn0='', ''2018-08-22 10:30:43''),
(''ldewali9zuyej9metb7vw60aph2w9rkv'', ''NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 15:05:07''),
(''m4rnyltg0rsompbtxbbh9fwcb55t89e0'', ''NDNjYjgxMGFkMDMwOWY3NzkxNDhjNzdjOTZiOGJkZjYxN2ExNWY2Mzp7Im5leHQiOiIvYmFja2VuZC9vZmZpY2VzL2luZGV4LyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-07 08:55:41''),
(''mjhjviny1gu5gx8vp7lopriqpxd99381'', ''MDgzZmI3YjQzZDIzYjBhYWJjOWVmODQ2M2Y5OTI0ODhhYTNkMTUwNzp7Im5leHQiOiIvYmFja2VuZC92aXNpdG9ycy9zY2FuLzAvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9'', ''2018-08-08 11:30:46''),
(''n9pi65y8xuyjht0dq842vpqzu5fhme00'', ''MDkxZjgyYzA5ZTE4OTI3YTg1NDY4NWIxZDRlZWU1ZTU1OGJlNjUwNDp7Im5leHQiOiIvYmFja2VuZC91c2Vycy9jcmVhdGUvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9'', ''2018-08-08 15:26:43''),
(''ox45jpk0g6whyde105yb05r18zd276kc'', ''NDNjYjgxMGFkMDMwOWY3NzkxNDhjNzdjOTZiOGJkZjYxN2ExNWY2Mzp7Im5leHQiOiIvYmFja2VuZC9vZmZpY2VzL2luZGV4LyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-07 09:59:44''),
(''p3qqak6gbm784i2gfumu6l2vzxubzcbi'', ''NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-07 07:55:20''),
(''pba66at4qekqg13njxunuqz7e5v69vcn'', ''NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-06 15:08:06''),
(''pmwgvyq3ezc3adxm1l3k64kx6iujb27p'', ''ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 14:22:14''),
(''s14je2lv4v77ei03bpci7el52wnnwkn3'', ''NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-06 18:47:26''),
(''wr2zrd70kjw7mln6onepyufnm3pkrqaq'', ''NDNjYjgxMGFkMDMwOWY3NzkxNDhjNzdjOTZiOGJkZjYxN2ExNWY2Mzp7Im5leHQiOiIvYmFja2VuZC9vZmZpY2VzL2luZGV4LyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-06 16:32:01''),
(''yzqdxstqly8034wodo3r67n02ysbv9lk'', ''ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-08 14:45:41''),
(''zqauqj96afg3zkeijirqk257blmep5tp'', ''NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ=='', ''2018-08-07 15:10:22'');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, ''example.com'', ''example.com'');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_access_permissions`
--
ALTER TABLE `app_access_permissions`
  ADD PRIMARY KEY (`access_permission_name`);

--
-- Indexes for table `app_doors`
--
ALTER TABLE `app_doors`
  ADD PRIMARY KEY (`door_id`),
  ADD UNIQUE KEY `door_code` (`door_code`);

--
-- Indexes for table `app_door_logs`
--
ALTER TABLE `app_door_logs`
  ADD PRIMARY KEY (`door_log_id`);

--
-- Indexes for table `app_failed_login`
--
ALTER TABLE `app_failed_login`
  ADD PRIMARY KEY (`failed_login_id`);

--
-- Indexes for table `app_fixed_badges`
--
ALTER TABLE `app_fixed_badges`
  ADD PRIMARY KEY (`badge_id`);

--
-- Indexes for table `app_fixed_badge_logs`
--
ALTER TABLE `app_fixed_badge_logs`
  ADD PRIMARY KEY (`badge_log_id`);

--
-- Indexes for table `app_offices`
--
ALTER TABLE `app_offices`
  ADD PRIMARY KEY (`office_id`),
  ADD UNIQUE KEY `office_code` (`office_code`);

--
-- Indexes for table `app_office_logs`
--
ALTER TABLE `app_office_logs`
  ADD PRIMARY KEY (`office_log_id`);

--
-- Indexes for table `app_operators`
--
ALTER TABLE `app_operators`
  ADD PRIMARY KEY (`operator_id`),
  ADD UNIQUE KEY `operator_username` (`operator_username`);

--
-- Indexes for table `app_operator_access_permissions`
--
ALTER TABLE `app_operator_access_permissions`
  ADD PRIMARY KEY (`operator_access_permission_id`),
  ADD KEY `app_operator_access__access_permissions_a_fed700a4_fk_app_acces` (`access_permissions_access_permission_name_id`),
  ADD KEY `app_operator_access__operators_operator_i_5e78e363_fk_app_opera` (`operators_operator_id_id`);

--
-- Indexes for table `app_operator_logs`
--
ALTER TABLE `app_operator_logs`
  ADD PRIMARY KEY (`operator_log_id`);

--
-- Indexes for table `app_templates`
--
ALTER TABLE `app_templates`
  ADD PRIMARY KEY (`template_id`);

--
-- Indexes for table `app_users`
--
ALTER TABLE `app_users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `user_username` (`user_username`);

--
-- Indexes for table `app_user_attendances`
--
ALTER TABLE `app_user_attendances`
  ADD PRIMARY KEY (`user_attendance_id`);

--
-- Indexes for table `app_user_logs`
--
ALTER TABLE `app_user_logs`
  ADD PRIMARY KEY (`user_log_id`);

--
-- Indexes for table `app_visitors`
--
ALTER TABLE `app_visitors`
  ADD PRIMARY KEY (`visitor_id`);

--
-- Indexes for table `app_visitor_logs`
--
ALTER TABLE `app_visitor_logs`
  ADD PRIMARY KEY (`visitor_log_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `django_site`
--
ALTER TABLE `django_site`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_door_logs`
--
ALTER TABLE `app_door_logs`
  MODIFY `door_log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `app_failed_login`
--
ALTER TABLE `app_failed_login`
  MODIFY `failed_login_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_fixed_badge_logs`
--
ALTER TABLE `app_fixed_badge_logs`
  MODIFY `badge_log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app_office_logs`
--
ALTER TABLE `app_office_logs`
  MODIFY `office_log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `app_operators`
--
ALTER TABLE `app_operators`
  MODIFY `operator_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `app_operator_access_permissions`
--
ALTER TABLE `app_operator_access_permissions`
  MODIFY `operator_access_permission_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT for table `app_operator_logs`
--
ALTER TABLE `app_operator_logs`
  MODIFY `operator_log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `app_user_attendances`
--
ALTER TABLE `app_user_attendances`
  MODIFY `user_attendance_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_user_logs`
--
ALTER TABLE `app_user_logs`
  MODIFY `user_log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `app_visitor_logs`
--
ALTER TABLE `app_visitor_logs`
  MODIFY `visitor_log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `django_site`
--
ALTER TABLE `django_site`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `app_operator_access_permissions`
--
ALTER TABLE `app_operator_access_permissions`
  ADD CONSTRAINT `app_operator_access__access_permissions_a_fed700a4_fk_app_acces` FOREIGN KEY (`access_permissions_access_permission_name_id`) REFERENCES `app_access_permissions` (`access_permission_name`),
  ADD CONSTRAINT `app_operator_access__operators_operator_i_5e78e363_fk_app_opera` FOREIGN KEY (`operators_operator_id_id`) REFERENCES `app_operators` (`operator_id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
