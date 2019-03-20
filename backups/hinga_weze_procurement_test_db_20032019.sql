-- phpMyAdmin SQL Dump
-- version 4.4.15.7
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 20, 2019 at 12:47 PM
-- Server version: 5.6.37
-- PHP Version: 7.1.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hinga_weze_procurement_test_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_access_permissions`
--

CREATE TABLE IF NOT EXISTS `app_access_permissions` (
  `access_permission_name` varchar(100) NOT NULL,
  `access_permission_details` varchar(255) NOT NULL,
  `access_permission_created_at` datetime(6) NOT NULL,
  `access_permission_updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_access_permissions`
--

INSERT INTO `app_access_permissions` (`access_permission_name`, `access_permission_details`, `access_permission_created_at`, `access_permission_updated_at`) VALUES
('dashboard-view', 'dashboard-view', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('log-delete', 'log-delete', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('log-view', 'log-view', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('operator-create', 'operator-create', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('operator-delete', 'operator-delete', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('operator-update', 'operator-update', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('operator-view', 'operator-view', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('order-create', 'order-create', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('order-delete', 'order-delete', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('order-update', 'order-update', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('order-view', 'order-view', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('settings-view', 'settings-view', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `app_failed_login`
--

CREATE TABLE IF NOT EXISTS `app_failed_login` (
  `failed_login_id` int(11) NOT NULL,
  `failed_login_username` varchar(255) NOT NULL,
  `failed_login_password` varchar(255) NOT NULL,
  `failed_login_from` varchar(10) NOT NULL,
  `failed_login_ip_address` varchar(100) NOT NULL,
  `failed_login_attempted_at` datetime(6) NOT NULL,
  `failed_login_status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `app_notifications`
--

CREATE TABLE IF NOT EXISTS `app_notifications` (
  `notification_id` int(11) NOT NULL,
  `notification_model_id` int(11) NOT NULL,
  `notification_model_type` varchar(20) NOT NULL,
  `notification_from_type` varchar(20) NOT NULL,
  `notification_from_id` int(11) NOT NULL,
  `notification_to_type` varchar(20) NOT NULL,
  `notification_to_id` int(11) NOT NULL,
  `notification_message` varchar(255) NOT NULL,
  `notification_url` varchar(255) NOT NULL,
  `notification_created_at` datetime(6) NOT NULL,
  `notification_read_at` datetime(6) NOT NULL,
  `notification_fixed_at` datetime(6) NOT NULL,
  `notification_status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `app_operators`
--

CREATE TABLE IF NOT EXISTS `app_operators` (
  `operator_id` int(11) NOT NULL,
  `operator_type` varchar(20) NOT NULL,
  `operator_department` varchar(255) NOT NULL,
  `operator_role` varchar(255) NOT NULL,
  `operator_parent_id` int(11) NOT NULL,
  `operator_username` varchar(100) NOT NULL,
  `operator_auth_key` varchar(255) NOT NULL,
  `operator_password_hash` varchar(255) NOT NULL,
  `operator_password_reset_token` varchar(255) NOT NULL,
  `operator_name` varchar(100) NOT NULL,
  `operator_gender` varchar(6) NOT NULL,
  `operator_contact_phone_number` varchar(17) NOT NULL,
  `operator_contact_email_id` varchar(100) NOT NULL,
  `operator_profile_photo_file_path` varchar(255) NOT NULL,
  `operator_created_at` datetime(6) NOT NULL,
  `operator_created_by` varchar(255) NOT NULL,
  `operator_updated_at` datetime(6) NOT NULL,
  `operator_updated_by` varchar(255) NOT NULL,
  `operator_status` varchar(20) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_operators`
--

INSERT INTO `app_operators` (`operator_id`, `operator_type`, `operator_department`, `operator_role`, `operator_parent_id`, `operator_username`, `operator_auth_key`, `operator_password_hash`, `operator_password_reset_token`, `operator_name`, `operator_gender`, `operator_contact_phone_number`, `operator_contact_email_id`, `operator_profile_photo_file_path`, `operator_created_at`, `operator_created_by`, `operator_updated_at`, `operator_updated_by`, `operator_status`) VALUES
(1, 'super-admin', 'NONE', 'NONE', 0, 'support@huzax.com', 'xc48ITBOTVBu87185KUSK2TlKxKiLJiw', 'pbkdf2_sha256$120000$slxVGFEthWuq$AqS7ZymOOeSEof9mPJ2ITXXQvwkIdHIv5Ko2DvKN+Hw=', '', 'Tech Support', 'male', '250726875122', 'support@techcible.com', '', '2018-01-01 00:00:00.000000', 'support@techcible.com', '2019-03-20 12:46:43.000000', 'support@huzax.com', 'active'),
(2, 'admin', 'NONE', 'NONE', 0, 'admin@huzax.com', 'xc48ITBOTVBu87185KUSK2TlKxKiLJij', 'pbkdf2_sha256$120000$0AZewnnKGdCy$jqU6YkCayb2sJIL48xCDb5lf9bl8uvGEmskIPALXX0c=', '', 'Admin Support', 'male', '250726875122', 'support@techcible.com', '', '2018-01-01 00:00:00.000000', 'support@techcible.com', '2019-03-20 12:42:48.000000', 'support@huzax.com', 'inactive'),
(3, 'admin', 'NONE', 'COP', 0, 'cop@cnfa.com', 'zfBKwMdmxoZAcJOIfXDcJF7v5jA0Bd1N', 'pbkdf2_sha256$120000$Eymsl3uiJOdI$mj0tiVMeqYQAaap3jMz3qCLXDae0I4SQ1DPQDMOHriU=', '', 'COP', 'male', '250726875122', 'cop@cnfa.com', '', '2019-03-16 07:57:21.000000', 'support@techcible.com', '2019-03-20 12:44:15.000000', 'support@huzax.com', 'inactive'),
(5, 'other', 'DCOP', 'Adviser', 0, 'adviser1@cnfa.com', 'm2FBIi9jFgsotH4jL8gojAMj8FVD49mR', 'pbkdf2_sha256$120000$hiBmCt5ioxTd$oJwNv3s/4xPw6NDvFlrKa7NOSdz92d+ygw4cLWJt9k4=', '', 'Adviser', '', '', 'adviser1@cnfa.com', '', '2019-03-16 08:04:08.000000', 'support@techcible.com', '2019-03-20 12:43:00.000000', 'support@huzax.com', 'inactive'),
(6, 'other', 'BFM', 'Adviser', 0, 'adviser2@cnfa.com', 'KBxQW7R5NQb2qHiTvLqMRYiLGHmu1Qfm', 'pbkdf2_sha256$120000$5sOWMyo0bcw2$7PAh4Jbis2l8sDwmOtj8HVx5/y3BICiK23XOkfL4h3s=', '', 'Adviser', '', '', 'adviser2@cnfa.com', '', '2019-03-16 08:05:00.000000', 'support@techcible.com', '2019-03-20 12:43:20.000000', 'support@huzax.com', 'inactive'),
(7, 'other', 'DCOP', 'Director', 0, 'director1@cnfa.com', 'yXs4Zu4k1Vejuq6Ir9Qirk6GPt0fhy9H', 'pbkdf2_sha256$120000$zKG9xhAHvVuF$U8RTkaT07AkCbwn//KB0JqjN1i9r7wLjIygdWSMGr1s=', '', 'Director', '', '', 'director1@cnfa.com', '', '2019-03-16 08:05:58.000000', 'support@techcible.com', '2019-03-20 12:44:25.000000', 'support@huzax.com', 'inactive'),
(8, 'other', 'BFM', 'Director', 0, 'director2@cnfa.com', '9TWyuEGtw5j7ncV4mKjuq6Qu8UF4dSHW', 'pbkdf2_sha256$120000$jGmwRUev0HMU$ou194WQR7+9urs9AlbS0rfHYRgKaMbRfysNs0ZI2oP8=', '', 'Director', '', '', 'director2@cnfa.com', '', '2019-03-16 08:06:39.000000', 'support@techcible.com', '2019-03-20 12:44:35.000000', 'support@huzax.com', 'inactive'),
(9, 'other', 'NUTRITION', 'Director', 0, 'director3@cnfa.com', 'NQGsWXCzOwPfrCgKL72viC5WOl5P6zPR', 'pbkdf2_sha256$120000$N9cHTVgnGVob$OSCAR1jpAy7ZIK3vdFFhT/Xjv6po80DIsP4GgNTRBOs=', '', 'Director', '', '', 'director3@cnfa.com', '', '2019-03-16 08:07:19.000000', 'support@techcible.com', '2019-03-20 12:44:46.000000', 'support@huzax.com', 'inactive'),
(10, 'other', 'DAF', 'Director', 0, 'director4@cnfa.com', 'IFw1OhUnpK4vC0oNZ1eLIJl90Sf7XTq5', 'pbkdf2_sha256$120000$bNioT9HzoclL$mHjy+C3GGtZIDIiXpy2O1Rhxkw0e7YVmrtsR/lD/olQ=', '', 'Director', '', '', 'director4@cnfa.com', '', '2019-03-16 08:12:24.000000', 'support@techcible.com', '2019-03-20 12:44:56.000000', 'support@huzax.com', 'inactive'),
(11, 'other', 'MAE', 'Director', 0, 'director5@cnfa.com', 'YhzflTHiofZKw8h0KL8K1vaDW1y9bM0t', 'pbkdf2_sha256$120000$tnJXqsha0u4i$9Txi1Zv7f3JWTu/+jAFhpzuf6IFEQqtt6/AODJ2sJ50=', '', 'Director', '', '', 'director5@cnfa.com', '', '2019-03-16 08:13:44.000000', 'support@techcible.com', '2019-03-20 12:45:07.000000', 'support@huzax.com', 'inactive'),
(12, 'other', 'GRANT-MANAGER', 'Director', 0, 'director6@cnfa.com', 'WGyenjMVldyjtY6IuduKgMic6Sv8uLHd', 'pbkdf2_sha256$120000$dDwenlddMmm3$8yjIaf4fEZcBSGMJxxl+UbN7h9eOBSIrrVuC4XY6q2g=', '', 'Director', '', '', 'director6@cnfa.com', '', '2019-03-16 08:14:51.000000', 'support@techcible.com', '2019-03-20 12:45:17.000000', 'support@huzax.com', 'inactive'),
(13, 'other', 'NUTRITION', 'Adviser', 0, 'adviser3@cnfa.com', 'crqq8IEyuDmHPD3oVwTuGo3T65ceM4pg', 'pbkdf2_sha256$120000$Jbp41wC6dyn3$t/2qpFees4Q48zWPeCQV6QI/7YTJ0ibHPVexhNvjCL8=', '', 'Adviser', '', '', 'adviser3@cnfa.com', '', '2019-03-16 08:15:40.000000', 'support@techcible.com', '2019-03-20 12:43:30.000000', 'support@huzax.com', 'inactive'),
(14, 'other', 'DAF', 'Adviser', 0, 'adviser4@cnfa.com', 'hUSqCUUgjNGyBBIDaP0o6A1l6mrN37Ip', 'pbkdf2_sha256$120000$J2NH4VXhJo4S$qgGPOMm2RILElmt3Xu5wmS60VjR3f5fsFS54/GHkKh4=', '', 'Adviser', '', '', 'adviser4@cnfa.com', '', '2019-03-16 08:16:26.000000', 'support@techcible.com', '2019-03-20 12:43:40.000000', 'support@huzax.com', 'inactive'),
(15, 'other', 'MAE', 'Adviser', 0, 'adviser5@cnfa.com', '9tJk7cacK1akmXqhOEz4JTHAR45zfDVz', 'pbkdf2_sha256$120000$3TicMHgC7qhK$cm+d3HIdjlyfIRcrqvNiWosGxuBxKdT/SIWB0I26x7M=', '', 'Adviser', '', '', 'adviser5@cnfa.com', '', '2019-03-16 08:17:09.000000', 'support@techcible.com', '2019-03-20 12:43:54.000000', 'support@huzax.com', 'inactive'),
(16, 'other', 'GRANT-MANAGER', 'Adviser', 0, 'adviser6@cnfa.com', 'i1NZqNTjmBOk7bQKGIBf6SEhaIT3Nh2p', 'pbkdf2_sha256$120000$XPY2v6TZ3Klp$gulavsu3OJwW1g/NnbMcsvWX/7ONtrtf6rDI1/bLfi4=', '', 'Adviser', '', '', 'adviser6@cnfa.com', '', '2019-03-16 08:17:59.000000', 'support@techcible.com', '2019-03-20 12:44:04.000000', 'support@huzax.com', 'inactive'),
(17, 'other', 'DCOP', 'Regional Manager', 7, 'regionalmanager1@cnfa.com', 'fl84IgzQrCCgLZkbH8roEEKCGbTPVdrd', 'pbkdf2_sha256$120000$s5mFzxFEDDgf$CDmsswwmruURZ2+iv542Ka3O3sXR/90711Q1ZMzxNWA=', '', 'Regional Manager', '', '', 'regionalmanager1@cnfa.com', '', '2019-03-16 08:19:40.000000', 'support@techcible.com', '2019-03-20 12:46:21.000000', 'support@huzax.com', 'inactive'),
(18, 'other', 'DCOP', 'District Manager', 17, 'districtmanager1@cnfa.com', 'WZMXduZfBvG5ESN5b7OTuqK1pRL0PW4Y', 'pbkdf2_sha256$120000$b3SROpuoCkRL$23rXmqtmwX+goy2XNf3tjIMZMhXiD3mKAiClunuZriE=', '', 'District Manager', '', '', 'districtmanager1@cnfa.com', '', '2019-03-16 08:32:00.000000', 'support@techcible.com', '2019-03-20 12:45:28.000000', 'support@huzax.com', 'inactive'),
(19, 'other', 'DCOP', 'Field Officer', 18, 'fieldofficer1@cnfa.com', 'PUS4HCyX8xWAa7TECQCmpl1wgm5xNslI', 'pbkdf2_sha256$120000$iuJFIb6vPXZT$zGaoYk5X+P7Xp3hss6S5jG5XQXXlBlhgR22mctGgwNI=', '', 'Field Officer', '', '', 'fieldofficer1@cnfa.com', '', '2019-03-16 08:33:35.000000', 'support@techcible.com', '2019-03-20 12:45:38.000000', 'support@huzax.com', 'inactive'),
(20, 'other', 'DAF', 'OPM', 0, 'opm@cnfa.com', '3DrkUbJ1eBynRQRT1mNEBxzXaMEgKDw5', 'pbkdf2_sha256$120000$TOAT1aTMLU4h$CTTi/TbdiAr7x/NfRYVdk0Ujeg2F/UskTgwn2bLBSFE=', '', 'OPM', '', '', 'opm@cnfa.com', '', '2019-03-16 08:36:57.000000', 'support@techcible.com', '2019-03-20 12:46:00.000000', 'support@huzax.com', 'inactive'),
(21, 'other', 'DAF', 'Procurement Officer', 0, 'procurementofficer1@cnfa.com', 'GfQdxXaUMDorx5Wo27v8c75LYlWx11zr', 'pbkdf2_sha256$120000$pD0uidNxvO1u$4s4wmz0lye1rL71erk7xb92XJuoIWUuS7mZ+vq90sAY=', '', 'Procurement Officer', '', '', 'procurementofficer1@cnfa.com', '', '2019-03-16 08:37:59.000000', 'support@techcible.com', '2019-03-20 12:46:10.000000', 'support@huzax.com', 'inactive'),
(23, 'other', 'DAF', 'HR Manager', 0, 'hrmanager1@cnfa.com', 'dBMR8fCY6yug3I1rkz5ZpktOc48pz6RR', 'pbkdf2_sha256$120000$TMLiQbkkz5LN$2qcxT1idd+asvL2uujrnVsTOSoU3xEYxepdD9amOgdE=', '', 'HR Manager', '', '', 'hrmanager1@cnfa.com', '', '2019-03-16 08:39:32.000000', 'support@techcible.com', '2019-03-20 12:45:49.000000', 'support@huzax.com', 'inactive'),
(24, 'other', 'DAF', 'Stock Admin', 0, 'stockadmin1@cnfa.com', 'ncwJxatJBg54mKl18sL0kgf7EsdubiHR', 'pbkdf2_sha256$120000$zkQcmUHnElCn$JCIOcawtp4zAk2YRVkGF0hfqlmKchPTvS3Jr8i7uSeE=', '', 'Stock Admin', '', '', 'stockadmin1@cnfa.com', '', '2019-03-16 08:40:30.000000', 'support@techcible.com', '2019-03-20 12:46:33.000000', 'support@huzax.com', 'inactive'),
(25, 'other', 'DAF', 'Accountant Manager', 0, 'accountmanager1@cnfa.com', 'O1QK8kXYngR3RZlESI0IDet9sl6LzCYx', 'pbkdf2_sha256$120000$px6RvRkRb2wg$5NJKiiWIYEU4qCuZeOoStvQ/n639jN+W4oNCDwo1z44=', '', 'Account Manager', '', '', 'accountmanager1@cnfa.com', '', '2019-03-16 08:41:12.000000', 'support@techcible.com', '2019-03-20 12:42:15.000000', 'support@huzax.com', 'inactive'),
(26, 'other', 'DAF', 'Accountant Officer', 25, 'accountofficer1@cnfa.com', 'CcgpIa40PPdlkLqZrzjxFcNAlClRqeuF', 'pbkdf2_sha256$120000$FW7zTpkCPKZF$DgWpE9Bx6NZEL8uLa03ec3o7AnA+84EI7z5r4OwttcY=', '', 'Account Officer', '', '', 'accountofficer1@cnfa.com', '', '2019-03-16 08:42:05.000000', 'support@techcible.com', '2019-03-20 12:42:26.000000', 'support@huzax.com', 'inactive'),
(27, 'other', 'DAF', 'Accountant Officer', 25, 'accountofficer2@cnfa.com', '8TyWRDz6jRkEI4ig86twAMBEzOxx5ulh', 'pbkdf2_sha256$120000$teGe2geOciiR$w5U1LWqZQKwjGuRhs+s+JK9jeaEacRXzulnOcRpim7c=', '', 'Account Officer', '', '', 'accountofficer2@cnfa.com', '', '2019-03-16 08:45:28.000000', 'support@techcible.com', '2019-03-20 12:42:37.000000', 'support@huzax.com', 'inactive');

-- --------------------------------------------------------

--
-- Table structure for table `app_operator_access_permissions`
--

CREATE TABLE IF NOT EXISTS `app_operator_access_permissions` (
  `operator_access_permission_id` int(11) NOT NULL,
  `operator_access_permission_updated_at` datetime(6) NOT NULL,
  `operator_access_permission_updated_by` varchar(255) NOT NULL,
  `access_permissions_access_permission_name_id` varchar(100) NOT NULL,
  `operators_operator_id_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_operator_access_permissions`
--

INSERT INTO `app_operator_access_permissions` (`operator_access_permission_id`, `operator_access_permission_updated_at`, `operator_access_permission_updated_by`, `access_permissions_access_permission_name_id`, `operators_operator_id_id`) VALUES
(6, '2019-03-16 09:17:33.000000', 'support@techcible.com', 'order-create', 25),
(7, '2019-03-16 09:17:33.000000', 'support@techcible.com', 'order-update', 25),
(8, '2019-03-16 09:17:33.000000', 'support@techcible.com', 'order-view', 25),
(9, '2019-03-16 09:17:33.000000', 'support@techcible.com', 'order-delete', 25),
(10, '2019-03-16 09:17:46.000000', 'support@techcible.com', 'order-create', 26),
(11, '2019-03-16 09:17:46.000000', 'support@techcible.com', 'order-update', 26),
(12, '2019-03-16 09:17:46.000000', 'support@techcible.com', 'order-view', 26),
(13, '2019-03-16 09:17:46.000000', 'support@techcible.com', 'order-delete', 26),
(14, '2019-03-16 09:17:59.000000', 'support@techcible.com', 'order-create', 27),
(15, '2019-03-16 09:17:59.000000', 'support@techcible.com', 'order-update', 27),
(16, '2019-03-16 09:17:59.000000', 'support@techcible.com', 'order-view', 27),
(17, '2019-03-16 09:17:59.000000', 'support@techcible.com', 'order-delete', 27),
(19, '2019-03-16 09:19:00.000000', 'support@techcible.com', 'order-create', 5),
(20, '2019-03-16 09:19:00.000000', 'support@techcible.com', 'order-update', 5),
(21, '2019-03-16 09:19:00.000000', 'support@techcible.com', 'order-view', 5),
(22, '2019-03-16 09:19:00.000000', 'support@techcible.com', 'order-delete', 5),
(23, '2019-03-16 09:19:08.000000', 'support@techcible.com', 'order-create', 6),
(24, '2019-03-16 09:19:08.000000', 'support@techcible.com', 'order-update', 6),
(25, '2019-03-16 09:19:08.000000', 'support@techcible.com', 'order-view', 6),
(26, '2019-03-16 09:19:08.000000', 'support@techcible.com', 'order-delete', 6),
(27, '2019-03-16 09:19:16.000000', 'support@techcible.com', 'order-create', 13),
(28, '2019-03-16 09:19:16.000000', 'support@techcible.com', 'order-update', 13),
(29, '2019-03-16 09:19:16.000000', 'support@techcible.com', 'order-view', 13),
(30, '2019-03-16 09:19:16.000000', 'support@techcible.com', 'order-delete', 13),
(31, '2019-03-16 09:19:23.000000', 'support@techcible.com', 'order-create', 14),
(32, '2019-03-16 09:19:23.000000', 'support@techcible.com', 'order-update', 14),
(33, '2019-03-16 09:19:23.000000', 'support@techcible.com', 'order-view', 14),
(34, '2019-03-16 09:19:23.000000', 'support@techcible.com', 'order-delete', 14),
(35, '2019-03-16 09:19:35.000000', 'support@techcible.com', 'order-create', 15),
(36, '2019-03-16 09:19:35.000000', 'support@techcible.com', 'order-update', 15),
(37, '2019-03-16 09:19:35.000000', 'support@techcible.com', 'order-view', 15),
(38, '2019-03-16 09:19:35.000000', 'support@techcible.com', 'order-delete', 15),
(39, '2019-03-16 09:19:43.000000', 'support@techcible.com', 'order-create', 16),
(40, '2019-03-16 09:19:43.000000', 'support@techcible.com', 'order-update', 16),
(41, '2019-03-16 09:19:43.000000', 'support@techcible.com', 'order-view', 16),
(42, '2019-03-16 09:19:43.000000', 'support@techcible.com', 'order-delete', 16),
(44, '2019-03-16 09:20:07.000000', 'support@techcible.com', 'order-create', 7),
(45, '2019-03-16 09:20:07.000000', 'support@techcible.com', 'order-update', 7),
(46, '2019-03-16 09:20:07.000000', 'support@techcible.com', 'order-view', 7),
(47, '2019-03-16 09:20:07.000000', 'support@techcible.com', 'order-delete', 7),
(48, '2019-03-16 09:20:15.000000', 'support@techcible.com', 'order-create', 8),
(49, '2019-03-16 09:20:15.000000', 'support@techcible.com', 'order-update', 8),
(50, '2019-03-16 09:20:15.000000', 'support@techcible.com', 'order-view', 8),
(51, '2019-03-16 09:20:15.000000', 'support@techcible.com', 'order-delete', 8),
(52, '2019-03-16 09:20:21.000000', 'support@techcible.com', 'order-create', 9),
(53, '2019-03-16 09:20:21.000000', 'support@techcible.com', 'order-update', 9),
(54, '2019-03-16 09:20:21.000000', 'support@techcible.com', 'order-view', 9),
(55, '2019-03-16 09:20:21.000000', 'support@techcible.com', 'order-delete', 9),
(56, '2019-03-16 09:20:28.000000', 'support@techcible.com', 'order-create', 10),
(57, '2019-03-16 09:20:28.000000', 'support@techcible.com', 'order-update', 10),
(58, '2019-03-16 09:20:28.000000', 'support@techcible.com', 'order-view', 10),
(59, '2019-03-16 09:20:28.000000', 'support@techcible.com', 'order-delete', 10),
(60, '2019-03-16 09:20:34.000000', 'support@techcible.com', 'order-create', 11),
(61, '2019-03-16 09:20:34.000000', 'support@techcible.com', 'order-update', 11),
(62, '2019-03-16 09:20:34.000000', 'support@techcible.com', 'order-view', 11),
(63, '2019-03-16 09:20:34.000000', 'support@techcible.com', 'order-delete', 11),
(64, '2019-03-16 09:20:40.000000', 'support@techcible.com', 'order-create', 12),
(65, '2019-03-16 09:20:40.000000', 'support@techcible.com', 'order-update', 12),
(66, '2019-03-16 09:20:40.000000', 'support@techcible.com', 'order-view', 12),
(67, '2019-03-16 09:20:40.000000', 'support@techcible.com', 'order-delete', 12),
(68, '2019-03-16 09:20:47.000000', 'support@techcible.com', 'order-create', 18),
(69, '2019-03-16 09:20:47.000000', 'support@techcible.com', 'order-update', 18),
(70, '2019-03-16 09:20:47.000000', 'support@techcible.com', 'order-view', 18),
(71, '2019-03-16 09:20:47.000000', 'support@techcible.com', 'order-delete', 18),
(72, '2019-03-16 09:20:54.000000', 'support@techcible.com', 'order-create', 19),
(73, '2019-03-16 09:20:54.000000', 'support@techcible.com', 'order-update', 19),
(74, '2019-03-16 09:20:54.000000', 'support@techcible.com', 'order-view', 19),
(75, '2019-03-16 09:20:54.000000', 'support@techcible.com', 'order-delete', 19),
(76, '2019-03-16 09:21:00.000000', 'support@techcible.com', 'order-create', 23),
(77, '2019-03-16 09:21:00.000000', 'support@techcible.com', 'order-update', 23),
(78, '2019-03-16 09:21:00.000000', 'support@techcible.com', 'order-view', 23),
(79, '2019-03-16 09:21:00.000000', 'support@techcible.com', 'order-delete', 23),
(80, '2019-03-16 09:21:07.000000', 'support@techcible.com', 'order-create', 20),
(81, '2019-03-16 09:21:07.000000', 'support@techcible.com', 'order-update', 20),
(82, '2019-03-16 09:21:07.000000', 'support@techcible.com', 'order-view', 20),
(83, '2019-03-16 09:21:07.000000', 'support@techcible.com', 'order-delete', 20),
(84, '2019-03-16 09:21:13.000000', 'support@techcible.com', 'order-create', 21),
(85, '2019-03-16 09:21:13.000000', 'support@techcible.com', 'order-update', 21),
(86, '2019-03-16 09:21:13.000000', 'support@techcible.com', 'order-view', 21),
(87, '2019-03-16 09:21:13.000000', 'support@techcible.com', 'order-delete', 21),
(88, '2019-03-16 09:21:22.000000', 'support@techcible.com', 'order-create', 17),
(89, '2019-03-16 09:21:22.000000', 'support@techcible.com', 'order-update', 17),
(90, '2019-03-16 09:21:22.000000', 'support@techcible.com', 'order-view', 17),
(91, '2019-03-16 09:21:22.000000', 'support@techcible.com', 'order-delete', 17),
(92, '2019-03-16 09:21:30.000000', 'support@techcible.com', 'order-create', 24),
(93, '2019-03-16 09:21:30.000000', 'support@techcible.com', 'order-update', 24),
(94, '2019-03-16 09:21:30.000000', 'support@techcible.com', 'order-view', 24),
(95, '2019-03-16 09:21:30.000000', 'support@techcible.com', 'order-delete', 24),
(97, '2019-03-16 09:24:43.000000', 'support@techcible.com', 'settings-view', 2),
(98, '2019-03-16 09:24:43.000000', 'support@techcible.com', 'log-delete', 2),
(99, '2019-03-16 09:24:43.000000', 'support@techcible.com', 'log-view', 2),
(100, '2019-03-16 09:24:43.000000', 'support@techcible.com', 'dashboard-view', 2),
(101, '2019-03-16 09:24:43.000000', 'support@techcible.com', 'operator-create', 2),
(102, '2019-03-16 09:24:43.000000', 'support@techcible.com', 'operator-update', 2),
(103, '2019-03-16 09:24:43.000000', 'support@techcible.com', 'operator-delete', 2),
(104, '2019-03-16 09:24:43.000000', 'support@techcible.com', 'operator-view', 2),
(105, '2019-03-16 09:24:43.000000', 'support@techcible.com', 'order-create', 2),
(106, '2019-03-16 09:24:43.000000', 'support@techcible.com', 'order-update', 2),
(107, '2019-03-16 09:24:43.000000', 'support@techcible.com', 'order-view', 2),
(108, '2019-03-16 09:24:43.000000', 'support@techcible.com', 'order-delete', 2),
(109, '2019-03-16 09:24:53.000000', 'support@techcible.com', 'settings-view', 3),
(110, '2019-03-16 09:24:53.000000', 'support@techcible.com', 'log-delete', 3),
(111, '2019-03-16 09:24:53.000000', 'support@techcible.com', 'log-view', 3),
(112, '2019-03-16 09:24:53.000000', 'support@techcible.com', 'dashboard-view', 3),
(113, '2019-03-16 09:24:53.000000', 'support@techcible.com', 'operator-create', 3),
(114, '2019-03-16 09:24:53.000000', 'support@techcible.com', 'operator-update', 3),
(115, '2019-03-16 09:24:53.000000', 'support@techcible.com', 'operator-delete', 3),
(116, '2019-03-16 09:24:53.000000', 'support@techcible.com', 'operator-view', 3),
(117, '2019-03-16 09:24:53.000000', 'support@techcible.com', 'order-create', 3),
(118, '2019-03-16 09:24:53.000000', 'support@techcible.com', 'order-update', 3),
(119, '2019-03-16 09:24:53.000000', 'support@techcible.com', 'order-view', 3),
(120, '2019-03-16 09:24:53.000000', 'support@techcible.com', 'order-delete', 3),
(121, '2019-03-16 09:46:31.000000', 'support@techcible.com', 'settings-view', 1),
(122, '2019-03-16 09:46:31.000000', 'support@techcible.com', 'log-delete', 1),
(123, '2019-03-16 09:46:31.000000', 'support@techcible.com', 'log-view', 1),
(124, '2019-03-16 09:46:31.000000', 'support@techcible.com', 'dashboard-view', 1),
(125, '2019-03-16 09:46:31.000000', 'support@techcible.com', 'operator-create', 1),
(126, '2019-03-16 09:46:31.000000', 'support@techcible.com', 'operator-update', 1),
(127, '2019-03-16 09:46:31.000000', 'support@techcible.com', 'operator-delete', 1),
(128, '2019-03-16 09:46:31.000000', 'support@techcible.com', 'operator-view', 1),
(129, '2019-03-16 09:46:31.000000', 'support@techcible.com', 'order-create', 1),
(130, '2019-03-16 09:46:31.000000', 'support@techcible.com', 'order-update', 1),
(131, '2019-03-16 09:46:31.000000', 'support@techcible.com', 'order-view', 1),
(132, '2019-03-16 09:46:31.000000', 'support@techcible.com', 'order-delete', 1);

-- --------------------------------------------------------

--
-- Table structure for table `app_operator_logs`
--

CREATE TABLE IF NOT EXISTS `app_operator_logs` (
  `operator_log_id` int(11) NOT NULL,
  `operators_operator_id` int(11) NOT NULL,
  `operators_operator_username` varchar(100) NOT NULL,
  `operators_operator_name` varchar(100) NOT NULL,
  `operator_log_message` varchar(255) NOT NULL,
  `operator_log_browser` longtext NOT NULL,
  `operator_log_ip_address` varchar(30) NOT NULL,
  `operator_log_updated_at` datetime(6) NOT NULL,
  `operator_log_updated_by` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `app_orders`
--

CREATE TABLE IF NOT EXISTS `app_orders` (
  `order_id` int(11) NOT NULL,
  `order_code` varchar(8) NOT NULL,
  `order_requester_name` varchar(100) NOT NULL,
  `order_project_name` varchar(100) NOT NULL,
  `order_project_code` varchar(100) NOT NULL,
  `order_project_geo_code` varchar(100) NOT NULL,
  `order_charge_code` varchar(100) NOT NULL,
  `order_award_number` varchar(100) NOT NULL,
  `order_requisition_number` varchar(100) NOT NULL,
  `order_donor` varchar(100) NOT NULL,
  `order_description` varchar(255) NOT NULL,
  `order_anticipated_award_mechanism` varchar(255) NOT NULL,
  `order_anticipated_start_date` date NOT NULL,
  `order_anticipated_end_date` date NOT NULL,
  `order_special_considerations` varchar(255) NOT NULL,
  `order_procurement_method` varchar(100) NOT NULL,
  `order_procurement_method_updated_at` datetime(6) NOT NULL,
  `order_procurement_method_updated_id` varchar(100) NOT NULL,
  `order_procurement_method_updated_by` varchar(100) NOT NULL,
  `order_procurement_method_updated_department` varchar(255) NOT NULL,
  `order_procurement_method_updated_role` varchar(255) NOT NULL,
  `order_no_of_items` decimal(10,0) NOT NULL,
  `order_total_price` decimal(10,0) NOT NULL,
  `order_equipment_price` decimal(10,0) NOT NULL,
  `order_tax_price` decimal(10,0) NOT NULL,
  `order_grand_total_price` decimal(10,0) NOT NULL,
  `order_currency` varchar(255) NOT NULL,
  `order_supplier_category` varchar(255) NOT NULL,
  `order_proposal_id` int(11) NOT NULL,
  `order_proposal_due_date` date NOT NULL,
  `order_purchase_no` varchar(100) NOT NULL,
  `order_invoice_no` varchar(100) NOT NULL,
  `order_created_at` datetime(6) NOT NULL,
  `order_created_id` varchar(100) NOT NULL,
  `order_created_by` varchar(100) NOT NULL,
  `order_created_department` varchar(255) NOT NULL,
  `order_created_role` varchar(255) NOT NULL,
  `order_updated_at` datetime(6) NOT NULL,
  `order_updated_id` varchar(100) NOT NULL,
  `order_updated_by` varchar(100) NOT NULL,
  `order_updated_department` varchar(255) NOT NULL,
  `order_updated_role` varchar(255) NOT NULL,
  `order_requested_at` datetime(6) NOT NULL,
  `order_requested_id` varchar(100) NOT NULL,
  `order_requested_by` varchar(100) NOT NULL,
  `order_requested_department` varchar(255) NOT NULL,
  `order_requested_role` varchar(255) NOT NULL,
  `order_approval_no_of_levels` int(11) NOT NULL,
  `order_reviewed_at` datetime(6) NOT NULL,
  `order_reviewed_id` varchar(100) NOT NULL,
  `order_reviewed_by` varchar(100) NOT NULL,
  `order_reviewed_department` varchar(255) NOT NULL,
  `order_reviewed_role` varchar(255) NOT NULL,
  `order_approved_at` datetime(6) NOT NULL,
  `order_approved_id` varchar(100) NOT NULL,
  `order_approved_by` varchar(100) NOT NULL,
  `order_approved_role` varchar(255) NOT NULL,
  `order_approved_department` varchar(255) NOT NULL,
  `order_assigned_at` datetime(6) NOT NULL,
  `order_assigned_id` varchar(100) NOT NULL,
  `order_assigned_by` varchar(100) NOT NULL,
  `order_assigned_department` varchar(255) NOT NULL,
  `order_assigned_role` varchar(255) NOT NULL,
  `order_assigned_to_at` datetime(6) NOT NULL,
  `order_assigned_to_by` varchar(100) NOT NULL,
  `order_assigned_to_id` varchar(100) NOT NULL,
  `order_assigned_to_department` varchar(255) NOT NULL,
  `order_assigned_to_role` varchar(255) NOT NULL,
  `order_proposal_generated_at` datetime(6) NOT NULL,
  `order_proposal_generated_id` varchar(100) NOT NULL,
  `order_proposal_generated_by` varchar(100) NOT NULL,
  `order_proposal_generated_department` varchar(255) NOT NULL,
  `order_proposal_generated_role` varchar(255) NOT NULL,
  `order_proposal_requested_at` datetime(6) NOT NULL,
  `order_proposal_requested_id` varchar(100) NOT NULL,
  `order_proposal_requested_by` varchar(100) NOT NULL,
  `order_proposal_requested_department` varchar(255) NOT NULL,
  `order_proposal_requested_role` varchar(255) NOT NULL,
  `order_purchase_generated_at` datetime(6) NOT NULL,
  `order_purchase_generated_id` varchar(100) NOT NULL,
  `order_purchase_generated_by` varchar(100) NOT NULL,
  `order_purchase_generated_department` varchar(255) NOT NULL,
  `order_purchase_generated_role` varchar(255) NOT NULL,
  `order_paid_at` datetime(6) NOT NULL,
  `order_paid_id` varchar(100) NOT NULL,
  `order_paid_by` varchar(100) NOT NULL,
  `order_paid_department` varchar(255) NOT NULL,
  `order_paid_role` varchar(255) NOT NULL,
  `order_closed_at` datetime(6) NOT NULL,
  `order_closed_id` varchar(100) NOT NULL,
  `order_closed_by` varchar(100) NOT NULL,
  `order_closed_department` varchar(255) NOT NULL,
  `order_closed_role` varchar(255) NOT NULL,
  `order_status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `app_order_approvals`
--

CREATE TABLE IF NOT EXISTS `app_order_approvals` (
  `order_approval_id` int(11) NOT NULL,
  `orders_order_id` int(11) NOT NULL,
  `order_approval_level` int(11) NOT NULL,
  `order_approval_created_at` datetime(6) NOT NULL,
  `order_approval_created_id` varchar(100) NOT NULL,
  `order_approval_created_by` varchar(100) NOT NULL,
  `order_approval_created_department` varchar(255) NOT NULL,
  `order_approval_created_role` varchar(255) NOT NULL,
  `order_approval_updated_at` datetime(6) NOT NULL,
  `order_approval_updated_id` varchar(100) NOT NULL,
  `order_approval_updated_by` varchar(100) NOT NULL,
  `order_approval_updated_department` varchar(255) NOT NULL,
  `order_approval_updated_role` varchar(255) NOT NULL,
  `order_approval_status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `app_order_attachments`
--

CREATE TABLE IF NOT EXISTS `app_order_attachments` (
  `order_attachment_id` int(11) NOT NULL,
  `orders_order_id` int(11) NOT NULL,
  `order_attachment_type` varchar(255) NOT NULL,
  `order_attachment_type_id` int(11) NOT NULL,
  `order_attachment_file_name` varchar(255) NOT NULL,
  `order_attachment_file_path` varchar(255) NOT NULL,
  `order_attachment_file_uploaded_at` datetime(6) NOT NULL,
  `order_attachment_file_uploaded_id` varchar(100) NOT NULL,
  `order_attachment_file_uploaded_by` varchar(100) NOT NULL,
  `order_attachment_file_uploaded_role` varchar(255) NOT NULL,
  `order_attachment_file_uploaded_department` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `app_order_items`
--

CREATE TABLE IF NOT EXISTS `app_order_items` (
  `order_item_id` int(11) NOT NULL,
  `orders_order_id` int(11) NOT NULL,
  `order_item_title` varchar(255) NOT NULL,
  `order_item_sub_title` varchar(255) NOT NULL,
  `order_item_quantity_ordered` decimal(10,0) NOT NULL,
  `order_item_quantity_unit` varchar(255) NOT NULL,
  `order_item_unit_price` decimal(10,0) NOT NULL,
  `order_item_total_price` decimal(10,0) NOT NULL,
  `order_item_usaid_approval` tinyint(1) NOT NULL,
  `order_item_created_at` datetime(6) NOT NULL,
  `order_item_created_id` varchar(100) NOT NULL,
  `order_item_created_by` varchar(100) NOT NULL,
  `order_item_created_role` varchar(255) NOT NULL,
  `order_item_updated_at` datetime(6) NOT NULL,
  `order_item_updated_id` varchar(100) NOT NULL,
  `order_item_updated_by` varchar(100) NOT NULL,
  `order_item_updated_role` varchar(255) NOT NULL,
  `order_item_received_at` datetime(6) NOT NULL,
  `order_item_received_id` varchar(100) NOT NULL,
  `order_item_received_by` varchar(100) NOT NULL,
  `order_item_received_role` varchar(255) NOT NULL,
  `order_item_status` varchar(255) NOT NULL,
  `order_item_currency` varchar(255) NOT NULL,
  `order_item_duration` int(11) NOT NULL,
  `order_item_created_department` varchar(255) NOT NULL,
  `order_item_received_department` varchar(255) NOT NULL,
  `order_item_updated_department` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `app_order_logs`
--

CREATE TABLE IF NOT EXISTS `app_order_logs` (
  `order_log_id` int(11) NOT NULL,
  `orders_order_id` int(11) NOT NULL,
  `order_log_message` varchar(255) NOT NULL,
  `order_log_browser` longtext NOT NULL,
  `order_log_ip_address` varchar(30) NOT NULL,
  `order_log_updated_at` datetime(6) NOT NULL,
  `order_log_updated_by` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `app_order_payments`
--

CREATE TABLE IF NOT EXISTS `app_order_payments` (
  `order_payment_id` int(11) NOT NULL,
  `orders_order_id` int(11) NOT NULL,
  `order_payment_paid_at` datetime(6) NOT NULL,
  `order_payment_paid_id` varchar(100) NOT NULL,
  `order_payment_paid_by` varchar(100) NOT NULL,
  `order_payment_paid_role` varchar(255) NOT NULL,
  `order_payment_paid_amount` decimal(10,0) NOT NULL,
  `order_payment_paid_pending` decimal(10,0) NOT NULL,
  `order_payment_paid_note` varchar(255) NOT NULL,
  `order_payment_paid_department` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `app_order_proposals`
--

CREATE TABLE IF NOT EXISTS `app_order_proposals` (
  `order_proposal_id` int(11) NOT NULL,
  `orders_order_id` int(11) NOT NULL,
  `order_proposal_supplier_category` varchar(255) NOT NULL,
  `order_proposal_supplier_title` varchar(255) NOT NULL,
  `order_proposal_supplier_details` varchar(255) NOT NULL,
  `order_proposal_supplier_address` varchar(255) NOT NULL,
  `order_proposal_supplier_contact_phone_number` varchar(13) NOT NULL,
  `order_proposal_supplier_contact_email_id` varchar(100) NOT NULL,
  `order_proposal_cost` decimal(10,0) NOT NULL,
  `order_proposal_evaluated_score` int(11) NOT NULL,
  `order_proposal_evaluation_details` varchar(255) NOT NULL,
  `order_proposal_created_at` datetime(6) NOT NULL,
  `order_proposal_created_id` varchar(100) NOT NULL,
  `order_proposal_created_by` varchar(100) NOT NULL,
  `order_proposal_created_role` varchar(255) NOT NULL,
  `order_proposal_updated_at` datetime(6) NOT NULL,
  `order_proposal_updated_id` varchar(100) NOT NULL,
  `order_proposal_updated_by` varchar(100) NOT NULL,
  `order_proposal_updated_role` varchar(255) NOT NULL,
  `order_proposal_evaluated_at` datetime(6) NOT NULL,
  `order_proposal_evaluated_id` varchar(100) NOT NULL,
  `order_proposal_evaluated_by` varchar(100) NOT NULL,
  `order_proposal_evaluated_role` varchar(255) NOT NULL,
  `order_proposal_approval_updated_at` datetime(6) NOT NULL,
  `order_proposal_approval_updated_id` varchar(100) NOT NULL,
  `order_proposal_approval_updated_by` varchar(100) NOT NULL,
  `order_proposal_approval_updated_role` varchar(255) NOT NULL,
  `order_proposal_acknowledged_at` datetime(6) NOT NULL,
  `order_proposal_acknowledged_id` varchar(100) NOT NULL,
  `order_proposal_acknowledged_by` varchar(100) NOT NULL,
  `order_proposal_acknowledged_role` varchar(255) NOT NULL,
  `order_proposal_status` varchar(255) NOT NULL,
  `order_proposal_acknowledged_department` varchar(255) NOT NULL,
  `order_proposal_approval_updated_department` varchar(255) NOT NULL,
  `order_proposal_created_department` varchar(255) NOT NULL,
  `order_proposal_evaluated_department` varchar(255) NOT NULL,
  `order_proposal_updated_department` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add backups', 1, 'add_backups'),
(2, 'Can change backups', 1, 'change_backups'),
(3, 'Can delete backups', 1, 'delete_backups'),
(4, 'Can view backups', 1, 'view_backups'),
(5, 'Can add access_ permissions', 2, 'add_access_permissions'),
(6, 'Can change access_ permissions', 2, 'change_access_permissions'),
(7, 'Can delete access_ permissions', 2, 'delete_access_permissions'),
(8, 'Can view access_ permissions', 2, 'view_access_permissions'),
(9, 'Can add failed_ login', 3, 'add_failed_login'),
(10, 'Can change failed_ login', 3, 'change_failed_login'),
(11, 'Can delete failed_ login', 3, 'delete_failed_login'),
(12, 'Can view failed_ login', 3, 'view_failed_login'),
(13, 'Can add operator_ access_ permissions', 4, 'add_operator_access_permissions'),
(14, 'Can change operator_ access_ permissions', 4, 'change_operator_access_permissions'),
(15, 'Can delete operator_ access_ permissions', 4, 'delete_operator_access_permissions'),
(16, 'Can view operator_ access_ permissions', 4, 'view_operator_access_permissions'),
(17, 'Can add operator_ logs', 5, 'add_operator_logs'),
(18, 'Can change operator_ logs', 5, 'change_operator_logs'),
(19, 'Can delete operator_ logs', 5, 'delete_operator_logs'),
(20, 'Can view operator_ logs', 5, 'view_operator_logs'),
(21, 'Can add operators', 6, 'add_operators'),
(22, 'Can change operators', 6, 'change_operators'),
(23, 'Can delete operators', 6, 'delete_operators'),
(24, 'Can view operators', 6, 'view_operators'),
(25, 'Can add log entry', 7, 'add_logentry'),
(26, 'Can change log entry', 7, 'change_logentry'),
(27, 'Can delete log entry', 7, 'delete_logentry'),
(28, 'Can view log entry', 7, 'view_logentry'),
(29, 'Can add permission', 8, 'add_permission'),
(30, 'Can change permission', 8, 'change_permission'),
(31, 'Can delete permission', 8, 'delete_permission'),
(32, 'Can view permission', 8, 'view_permission'),
(33, 'Can add group', 9, 'add_group'),
(34, 'Can change group', 9, 'change_group'),
(35, 'Can delete group', 9, 'delete_group'),
(36, 'Can view group', 9, 'view_group'),
(37, 'Can add user', 10, 'add_user'),
(38, 'Can change user', 10, 'change_user'),
(39, 'Can delete user', 10, 'delete_user'),
(40, 'Can view user', 10, 'view_user'),
(41, 'Can add content type', 11, 'add_contenttype'),
(42, 'Can change content type', 11, 'change_contenttype'),
(43, 'Can delete content type', 11, 'delete_contenttype'),
(44, 'Can view content type', 11, 'view_contenttype'),
(45, 'Can add session', 12, 'add_session'),
(46, 'Can change session', 12, 'change_session'),
(47, 'Can delete session', 12, 'delete_session'),
(48, 'Can view session', 12, 'view_session'),
(49, 'Can add site', 13, 'add_site'),
(50, 'Can change site', 13, 'change_site'),
(51, 'Can delete site', 13, 'delete_site'),
(52, 'Can view site', 13, 'view_site'),
(53, 'Can add order_ approvals', 14, 'add_order_approvals'),
(54, 'Can change order_ approvals', 14, 'change_order_approvals'),
(55, 'Can delete order_ approvals', 14, 'delete_order_approvals'),
(56, 'Can view order_ approvals', 14, 'view_order_approvals'),
(57, 'Can add order_ attachments', 15, 'add_order_attachments'),
(58, 'Can change order_ attachments', 15, 'change_order_attachments'),
(59, 'Can delete order_ attachments', 15, 'delete_order_attachments'),
(60, 'Can view order_ attachments', 15, 'view_order_attachments'),
(61, 'Can add order_ items', 16, 'add_order_items'),
(62, 'Can change order_ items', 16, 'change_order_items'),
(63, 'Can delete order_ items', 16, 'delete_order_items'),
(64, 'Can view order_ items', 16, 'view_order_items'),
(65, 'Can add order_ logs', 17, 'add_order_logs'),
(66, 'Can change order_ logs', 17, 'change_order_logs'),
(67, 'Can delete order_ logs', 17, 'delete_order_logs'),
(68, 'Can view order_ logs', 17, 'view_order_logs'),
(69, 'Can add order_ payments', 18, 'add_order_payments'),
(70, 'Can change order_ payments', 18, 'change_order_payments'),
(71, 'Can delete order_ payments', 18, 'delete_order_payments'),
(72, 'Can view order_ payments', 18, 'view_order_payments'),
(73, 'Can add order_ proposals', 19, 'add_order_proposals'),
(74, 'Can change order_ proposals', 19, 'change_order_proposals'),
(75, 'Can delete order_ proposals', 19, 'delete_order_proposals'),
(76, 'Can view order_ proposals', 19, 'view_order_proposals'),
(77, 'Can add orders', 20, 'add_orders'),
(78, 'Can change orders', 20, 'change_orders'),
(79, 'Can delete orders', 20, 'delete_orders'),
(80, 'Can view orders', 20, 'view_orders'),
(81, 'Can add notifications', 21, 'add_notifications'),
(82, 'Can change notifications', 21, 'change_notifications'),
(83, 'Can delete notifications', 21, 'delete_notifications'),
(84, 'Can view notifications', 21, 'view_notifications');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'admin', 'logentry'),
(2, 'app', 'access_permissions'),
(1, 'app', 'backups'),
(3, 'app', 'failed_login'),
(21, 'app', 'notifications'),
(6, 'app', 'operators'),
(4, 'app', 'operator_access_permissions'),
(5, 'app', 'operator_logs'),
(20, 'app', 'orders'),
(14, 'app', 'order_approvals'),
(15, 'app', 'order_attachments'),
(16, 'app', 'order_items'),
(17, 'app', 'order_logs'),
(18, 'app', 'order_payments'),
(19, 'app', 'order_proposals'),
(9, 'auth', 'group'),
(8, 'auth', 'permission'),
(10, 'auth', 'user'),
(11, 'contenttypes', 'contenttype'),
(12, 'sessions', 'session'),
(13, 'sites', 'site');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-03-12 08:56:40.750373'),
(2, 'auth', '0001_initial', '2019-03-12 08:56:41.133296'),
(3, 'admin', '0001_initial', '2019-03-12 08:56:41.215754'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-03-12 08:56:41.224580'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-03-12 08:56:41.232586'),
(6, 'app', '0001_initial', '2019-03-12 08:56:41.420848'),
(7, 'contenttypes', '0002_remove_content_type_name', '2019-03-12 08:56:41.491521'),
(8, 'auth', '0002_alter_permission_name_max_length', '2019-03-12 08:56:41.522428'),
(9, 'auth', '0003_alter_user_email_max_length', '2019-03-12 08:56:41.554350'),
(10, 'auth', '0004_alter_user_username_opts', '2019-03-12 08:56:41.567728'),
(11, 'auth', '0005_alter_user_last_login_null', '2019-03-12 08:56:41.593404'),
(12, 'auth', '0006_require_contenttypes_0002', '2019-03-12 08:56:41.596600'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2019-03-12 08:56:41.608891'),
(14, 'auth', '0008_alter_user_username_max_length', '2019-03-12 08:56:41.640074'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2019-03-12 08:56:41.673828'),
(16, 'sessions', '0001_initial', '2019-03-12 08:56:41.716737'),
(17, 'sites', '0001_initial', '2019-03-12 08:56:41.745688'),
(18, 'sites', '0002_alter_domain_unique', '2019-03-12 08:56:41.765490'),
(19, 'app', '0002_auto_20190312_0933', '2019-03-12 09:33:18.626864'),
(20, 'app', '0003_order_approvals_order_attachments_order_items_order_logs_order_payments_order_proposals_orders', '2019-03-12 14:46:06.169681'),
(21, 'app', '0004_auto_20190315_1519', '2019-03-15 15:19:34.412333'),
(22, 'app', '0005_notifications', '2019-03-16 07:02:06.159578'),
(23, 'app', '0006_auto_20190316_1420', '2019-03-16 14:20:26.290201'),
(24, 'app', '0007_auto_20190316_1541', '2019-03-16 15:41:39.148678'),
(25, 'app', '0008_auto_20190318_1011', '2019-03-18 10:11:49.634681'),
(26, 'app', '0009_auto_20190318_1317', '2019-03-18 13:17:51.307365'),
(27, 'app', '0010_auto_20190318_1612', '2019-03-18 16:12:56.756047'),
(28, 'app', '0011_auto_20190319_0734', '2019-03-19 07:34:04.561822'),
(29, 'app', '0012_auto_20190319_0921', '2019-03-19 09:21:48.169659'),
(30, 'app', '0013_auto_20190319_1351', '2019-03-19 13:51:57.111151'),
(31, 'app', '0014_auto_20190319_1829', '2019-03-19 18:29:16.392389');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('19qz7amypwkjnghkegu2wdx3am0wfs68', 'NTk0ODRlOTZkYjUzN2YwNDUwNzkzNjkwNDM3MmQ1NjRmODgwNTk5MDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjMiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6IjM2NGQ0MWYwNmYwM2YxNzFiZmU5OGJlOTljZmU1NzljMWFhOWQ1YTIiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-20 12:51:02.282044'),
('1qs528wwl8e042gachi0o4fo95v7n9de', 'YTAyNjMxMWM4ODUyYTNhMzA2OWFjMzNmMjZlMDdjYjhmNmMyNGI3Mzp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvdmlldy8xLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-18 14:30:32.906924'),
('20tweqnathnf72e0tbirs7vuvt89j3oz', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-16 13:06:49.772516'),
('2fh90n6xobofdxj1ovgif817czvanmvy', 'YTAyNjMxMWM4ODUyYTNhMzA2OWFjMzNmMjZlMDdjYjhmNmMyNGI3Mzp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvdmlldy8xLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-18 15:30:42.623381'),
('3lw0newf6z7w9ytmfxm8fzefyuw761ni', 'ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-19 14:45:52.914128'),
('3vswhha195ip33g8cxsl1owa0714wgwn', 'ODg1NDU1ZjIxNjdkM2ZlMGUwMDkyNmFiNWM1MGU1MjU0OTJmMWEwYTp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjIwIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJjNmFhMDUwMTFlNzk4YzBmM2VmYjA0ZjY2NmM4Y2Y4ZmYxOTQ3YjVhIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-20 07:50:50.490944'),
('4d6hsv4zth1auu5tlca775qbpy8mvy43', 'ZGE5YzNlYzI4NDUwZWYzNTNiMWU1ZmM5MzM2MDc0ZDU4NTFmNTkyZjp7Im5leHQiOiIvYmFja2VuZC9ub3RpZmljYXRpb25zL2luZGV4LyIsIl9vcGVyYXRvcnNfaWQiOiIxOCIsIl9vcGVyYXRvcnNfYmFja2VuZCI6bnVsbCwiX29wZXJhdG9yc19oYXNoIjoiOWM2ODMwMmIwOGVlNWI3ZmZkOWI0M2VlMzJhOGQ0NmI4MGY4ZDgxMCIsIl9zZXNzaW9uX2V4cGlyeSI6MzYwMH0=', '2019-03-19 17:30:50.468447'),
('72zjx9qlvlmnw6hf9tbxvgewr3xmahg7', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-15 18:40:14.130948'),
('78hvkvgkmbaikdpaxion03kw65q7ky3l', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-14 17:10:59.157067'),
('7eundzi11y8xc4vdvw968jry8oudc64m', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-19 15:48:15.840627'),
('7nr8ayzyi4vzfudtyj9edrkt8ddjc32n', 'MDJjNjJjZTc4YjZmNmY3YzZjMzE0MzA3NDI1YWY1YTlhZWMzMWNmYTp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvcHJvZmlsZS9jaGFuZ2UtcGFzc3dvcmQvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-15 15:31:51.066543'),
('7usuxi0xb85lg2b5e50o0uvgd468rspf', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-15 10:24:01.429661'),
('7wdriqo2ecla356xdxsaat80npx6uhch', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-15 08:03:08.595176'),
('7yitoz44f7lu0esb4ozghs6k28o0ai59', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-18 10:42:49.647239'),
('8cb6igt5rvsaahy9qsupsczkzhj7cq8x', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-19 08:14:05.290718'),
('8p7uftvfmbiyeo9ip78af2vbmyyr23l3', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-14 20:15:12.278679'),
('baimi684856k7gjhir3tqckjtvx7pcf3', 'ZGNjNGQwYmRkNDM1ZDk4YmIyOTc4ZTg2MzIxNDg1NjBkMWNkN2JjNjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvY3JlYXRlLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-16 08:39:35.940413'),
('cbjo2ogxvwnedlaiaebtkjlr8cdii1hc', 'NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-14 12:11:57.725911'),
('cwxt73shs4m7ndu93ay7r0h3jd4e2hn6', 'ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-19 12:17:16.847401'),
('d058knq2fy3hdzh17p9x8dvsko6bxuif', 'ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-16 14:08:46.633755'),
('d0yosndv2ze32t7ryjmst4zzif22fpba', 'ODcyNWY4MWIxOGE5YWMwNTE3NGVmN2JjMDNlYzAxZTQxZWZiYmQxOTp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjE4IiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiI5YzY4MzAyYjA4ZWU1YjdmZmQ5YjQzZWUzMmE4ZDQ2YjgwZjhkODEwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-19 16:30:18.737473'),
('d5lwfuttkbo17nsh48wfn10r4nbwk8u0', 'NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-15 14:31:22.293490'),
('d9o9mq9hvrcy2gen516ymkifqesvzhbs', 'OTNiMzAyMDYyMmY3MjlhNTRiMGNhNzc0ZjEyNzNjOTE0OWUzNGRkZjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvcHJvZmlsZS91cGRhdGUvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-14 15:25:59.823573'),
('den6dyuzsgosl70jwinztpyww7bf66is', 'YTAyNjMxMWM4ODUyYTNhMzA2OWFjMzNmMjZlMDdjYjhmNmMyNGI3Mzp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvdmlldy8xLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-19 13:42:00.017111'),
('e1pz6zytwwgpcsziqg0e9h3zq06j0bsw', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-19 16:49:23.418389'),
('ea4h98mtvzqplfbyeme68f1w48h75bp6', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-15 19:42:31.258019'),
('eev88tkmj739hk64w666p43lj25t9ct3', 'ZWUyZDAyODAyNTIzOTFjMWQwYTc2NTg5YTIwNmRhYmZjZWYxMjYwNDp7Il9vcGVyYXRvcnNfaWQiOiIyMCIsIl9vcGVyYXRvcnNfYmFja2VuZCI6bnVsbCwiX29wZXJhdG9yc19oYXNoIjoiYzZhYTA1MDExZTc5OGMwZjNlZmIwNGY2NjZjOGNmOGZmMTk0N2I1YSIsIl9zZXNzaW9uX2V4cGlyeSI6MzYwMH0=', '2019-03-19 20:08:25.347287'),
('enbmjqi14wgv4ydsbm0o9i339fhgofhz', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-16 15:16:16.451851'),
('evqognynvtbdwvj4co1ofp4hyqpcgca2', 'OTNiMzAyMDYyMmY3MjlhNTRiMGNhNzc0ZjEyNzNjOTE0OWUzNGRkZjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvcHJvZmlsZS91cGRhdGUvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-14 16:09:24.048575'),
('f1nqhpnvo94qtoky432gdipv9qnrfzk2', 'ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-14 09:18:18.705122'),
('f465q7203xyzlokxdq50g0u614sr3f2q', 'ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-13 14:31:00.869454'),
('fgto3rq3no1gqud3b10wwievxj1tyb9j', 'MjQ0NThlZThhZGZiMjMwMzRkYTUzYjYxMTM5ODYzMjg0MDQ0NWNjYTp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-18 19:33:31.397203'),
('fjjuh0vjzksxl4q6msla1fkxlto0a34p', 'MmE2NWUzZDYyNzI5YjZjYTkzMmQ4ZDcwY2Q5MGQ5ZWVlZmQ4OTY1ZDp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvY3JlYXRlLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-16 16:42:23.612536'),
('fll71udx51ndsj2eevrg2zf9j98parh3', 'NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-14 09:09:04.678711'),
('fnji05jcubhi2brjoee3oyf8yzt5ooj7', 'MWYzYjliM2U5ZDkxNmE5NzFhNjljZGQ1YmI3NTViYmIzMjI3NzI3Mzp7Im5leHQiOiIvYmFja2VuZC9ub3RpZmljYXRpb25zL2luZGV4LyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-19 19:31:32.172691'),
('gh03mkka50pqe9gbozlzj83t7dy7p9pf', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-15 10:47:24.175476'),
('gl4jtj9kpi93q2olsammwp2ixlgiomnj', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-14 19:09:39.170633'),
('gpgs67dievu32ovnt4gpxu7u0s0ltc88', 'ODBmYmNiMTJkOWY4YWI1Zjc1ZTU5ZjBkZmYxN2M2OWUyYWRjZGY1Mzp7Il9vcGVyYXRvcnNfaWQiOiIxNyIsIl9vcGVyYXRvcnNfYmFja2VuZCI6bnVsbCwiX29wZXJhdG9yc19oYXNoIjoiN2E5ZTVhMmEzZWU2Zjk2ZDYzMmMwNWY4YTBkOGVjMjdmMTY2NjMxOCIsIl9zZXNzaW9uX2V4cGlyeSI6MzYwMH0=', '2019-03-19 11:54:10.635631'),
('gsqigdwg5hylppsdagvr8948e5vytpzh', 'MjRlZjJlZDE4NjVjMDNlZDk4MmZhMDNjZTAzZGEwYzI4ZTBkZDRhMTp7Il9vcGVyYXRvcnNfaWQiOiI3IiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiI1NjljYzczYzU0YzQ2ZDUxNTFjMDRiMTUyZmQ2NTNkZDIxNmNjOTA1IiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-18 19:49:36.763184'),
('gta5ivutglcx56lhh7p1ikex3wnhjtax', 'Mzc2MDM2N2Y2NzM2ZmY1ZWMwMTgyNjA3ZDdlZGVmZTYzYzZjOGYxYjp7Il9vcGVyYXRvcnNfaWQiOiIzIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiIzNjRkNDFmMDZmMDNmMTcxYmZlOThiZTk5Y2ZlNTc5YzFhYTlkNWEyIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-20 10:48:27.287937'),
('gwyt406g77pjgagf8hobituwry5oi8ax', 'NzA0MTM3NDlhMTkyOTllZmNmYmJhMGRmNTQ3MTg5ODQ0ZTA1ZTRhYzp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIn0=', '2019-03-29 07:20:30.356615'),
('h1ybb8k2ot8966pxkpxxqyfytmk053yf', 'NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-20 13:41:28.389477'),
('hkxxt149b17hsxjgccn6p9489h6pqr0u', 'MjQ0NThlZThhZGZiMjMwMzRkYTUzYjYxMTM5ODYzMjg0MDQ0NWNjYTp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-19 17:49:46.665457'),
('hrwekk7y9yd309j9ca346w7jdtk0ojww', 'NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-15 08:21:03.253355'),
('j7xcy9tpk7hmqd93d86cj9tnthyt7119', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-16 10:46:23.058628'),
('jdqkn0mfueuh0t2ak0mim4bgwdl1aq9o', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-19 09:50:26.090599'),
('jlpz30opg4b93u0qkrd08wms6zblx2p0', 'MjQ0NThlZThhZGZiMjMwMzRkYTUzYjYxMTM5ODYzMjg0MDQ0NWNjYTp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-18 16:31:09.325708'),
('mhk1gd682erkep2p4xkup78xxqp52g4w', 'NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-15 16:37:09.033575'),
('nbdc1ix1csoxgsyd7428gmaj71l5ort5', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-15 08:29:38.207309'),
('nln82ka6fodbuw6g02r4tlkxmh1g23vk', 'NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-18 09:38:55.030039'),
('nzkktlt68ehr6cfcv8ui5phvcow4npof', 'OTk0ZWE2OTQ1MzU2NGEyNWU0NmRlZTM1ZmU2NjkyY2FhNWM0NzEwMjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvdmlldy8yMy8iLCJfb3BlcmF0b3JzX2lkIjoiMSIsIl9vcGVyYXRvcnNfYmFja2VuZCI6bnVsbCwiX29wZXJhdG9yc19oYXNoIjoiZTBiZmExZGVhMDRiZTMwZDE1ZjdmNDFlYjhlMzkyOTViMGUzOTdhMCIsIl9zZXNzaW9uX2V4cGlyeSI6MzYwMH0=', '2019-03-16 09:39:56.509070'),
('p352n3mkettybzr40d242ul6sl5h2nqt', 'NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-13 18:14:26.691142'),
('p3kao4tpfnrw61tfk4kj9wqnkpziptpv', 'ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-14 12:13:19.586982'),
('peb45ktz9oy11r1bsp1m8cmh8koitj1f', 'MjA4YmQxMTczMTgyNWVkNjc2NzIwYTQxZTIyOGIzNzYxMmE5ZGQ4Yzp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvcHJvZmlsZS92aWV3LyIsIl9vcGVyYXRvcnNfaWQiOiIxOSIsIl9vcGVyYXRvcnNfYmFja2VuZCI6bnVsbCwiX29wZXJhdG9yc19oYXNoIjoiNDZhNmNjZWY4MGY0N2FhOWFmMzI3NWFlNDQ1MmYwMGQyZWU1OGI0MCIsIl9zZXNzaW9uX2V4cGlyeSI6MzYwMH0=', '2019-03-19 08:14:24.728792'),
('pqw7yseuaovvk9rkgyd8ztq00romkb64', 'ZWMzYjE0ZmJhZjMxYmJmZmE0ZjU4Y2NiZjlhNzg5MWQyYmIxNmI0NDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvZGFzaGJvYXJkLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-14 10:46:35.786464'),
('qeiijt9kw2pofw359s8ow3renlebbnnm', 'OTNiMzAyMDYyMmY3MjlhNTRiMGNhNzc0ZjEyNzNjOTE0OWUzNGRkZjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvcHJvZmlsZS91cGRhdGUvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-14 14:24:28.172042'),
('qkqdc140kddaocwa5dl1kaj18x26sest', 'MjMzNzg4ZGU4YjUwOWFjY2RmZDMwMzUxNWMyZGZlYmRjMDAyMmZhMjp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjE5IiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiI0NmE2Y2NlZjgwZjQ3YWE5YWYzMjc1YWU0NDUyZjAwZDJlZTU4YjQwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-19 09:50:54.994779'),
('qsztz3xpks0yljq5l65qxvxa2o6c2o7j', 'NDUzNjI5NjYzMzM3Y2M5ZGY5N2UxN2JiNDAyNWMzYTQzOWY4ZjEyMDp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvdmlldy8xLyIsIl9vcGVyYXRvcnNfaWQiOiIxOCIsIl9vcGVyYXRvcnNfYmFja2VuZCI6bnVsbCwiX29wZXJhdG9yc19oYXNoIjoiOWM2ODMwMmIwOGVlNWI3ZmZkOWI0M2VlMzJhOGQ0NmI4MGY4ZDgxMCIsIl9zZXNzaW9uX2V4cGlyeSI6MzYwMH0=', '2019-03-19 14:46:11.730818'),
('rb9cy87u6rc82lurunyr3uy5xdlywea7', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-19 11:07:56.447354'),
('rt7szjuc0m1u9c5qp27a0dtuonm05ob9', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-14 18:08:50.448627'),
('sm8uxla4sppyi55j50cdlh7t0f78xo3j', 'NDFhODJjYTYwZjRkNmQyODFjNzM4YTFiMGZiZGUzMzZjMTczMDVhODp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvdmlldy9vcmRlci1pdGVtcy8xLyIsIl9vcGVyYXRvcnNfaWQiOiIzIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiIzNjRkNDFmMDZmMDNmMTcxYmZlOThiZTk5Y2ZlNTc5YzFhYTlkNWEyIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-20 11:50:22.571499'),
('u81nwxgwmccyton3w21ltpul0s0rehhb', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-14 19:59:13.724011'),
('ub6wwhk4frzjwv1r8lxbj8jyreb7c8rj', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-15 07:56:18.308718'),
('uunn0ur4bs641rghg4e5a7ykudpl6l86', 'OThhNDUzMTA2NDc1ZDhmZWY2ODI2NzdkMGYyZjAzYWMyZGZlYjRkZDp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvdmlldy8yLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-16 07:38:54.388357'),
('uuy8afbd2c1nssw9mv7sg0cizwdx0h8o', 'NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-16 18:17:47.024821'),
('w2zwclie17ldv778jeqohuguafynqgx8', 'OTNiMzAyMDYyMmY3MjlhNTRiMGNhNzc0ZjEyNzNjOTE0OWUzNGRkZjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvcHJvZmlsZS91cGRhdGUvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-14 13:23:02.819544'),
('w956645l31wo0hzwjem0t9n2wtgqwqy7', 'MjQ0NThlZThhZGZiMjMwMzRkYTUzYjYxMTM5ODYzMjg0MDQ0NWNjYTp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-18 18:32:38.877811'),
('weoahbepjy0xpacduwe2cyptjtuw8udd', 'MjQ0NThlZThhZGZiMjMwMzRkYTUzYjYxMTM5ODYzMjg0MDQ0NWNjYTp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-18 12:14:28.213947'),
('xktzx9oxpbhxv0dj0mi4qs80r76q76uj', 'NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-15 14:17:44.388532'),
('xlc825qt9uy5v2ybztd5in5ggn3f5ts2', 'ZWI0NzZkMTMxNjM3OGNiZGQ1ZmU0OTZlMzk0OWM0N2ZkYjFmODRjMDp7Il9vcGVyYXRvcnNfaWQiOiIxOSIsIl9vcGVyYXRvcnNfYmFja2VuZCI6bnVsbCwiX29wZXJhdG9yc19oYXNoIjoiNDZhNmNjZWY4MGY0N2FhOWFmMzI3NWFlNDQ1MmYwMGQyZWU1OGI0MCIsIl9zZXNzaW9uX2V4cGlyeSI6MzYwMH0=', '2019-03-18 16:13:04.131627'),
('y09s35u4h3xnamsj7iquj34h8lqwsih0', 'NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-15 16:34:54.981263'),
('y0o5sdq4ggdg3bkzi0o67bgjdcpdhz70', 'YTAyNjMxMWM4ODUyYTNhMzA2OWFjMzNmMjZlMDdjYjhmNmMyNGI3Mzp7Im5leHQiOiIvYmFja2VuZC9vcmRlcnMvdmlldy8xLyIsIl9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-18 13:14:45.933285'),
('y3knydtkdh8y5ywcvtm6dasual5hfd5l', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-20 10:32:32.228361'),
('yfrngwirsrxokiuefek1e39yulrieotm', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-15 12:11:21.812151'),
('ypj329a353zdalrj2uvqr9v5hbp5bvky', 'YjVhNmFlZGZkOWNiZTA3M2VkZjAzYjBiMmVhMzM2YzU4YTJmNDI5Mjp7Im5leHQiOiIvYmFja2VuZC9vcGVyYXRvcnMvaW5kZXgvIiwiX29wZXJhdG9yc19pZCI6IjEiLCJfb3BlcmF0b3JzX2JhY2tlbmQiOm51bGwsIl9vcGVyYXRvcnNfaGFzaCI6ImUwYmZhMWRlYTA0YmUzMGQxNWY3ZjQxZWI4ZTM5Mjk1YjBlMzk3YTAiLCJfc2Vzc2lvbl9leHBpcnkiOjM2MDB9', '2019-03-15 09:29:50.245321'),
('z4ebhn4xvzksaw2wunyl93cr1rqnijmb', 'NTJlYzZlM2UyYTYzNjVmYjkyMzBlNzgwM2ZiMGI1MTliZjg0OTM1Nzp7Il9vcGVyYXRvcnNfaWQiOiIxIiwiX29wZXJhdG9yc19iYWNrZW5kIjpudWxsLCJfb3BlcmF0b3JzX2hhc2giOiJlMGJmYTFkZWEwNGJlMzBkMTVmN2Y0MWViOGUzOTI5NWIwZTM5N2EwIiwiX3Nlc3Npb25fZXhwaXJ5IjozNjAwfQ==', '2019-03-13 13:40:37.195641');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_access_permissions`
--
ALTER TABLE `app_access_permissions`
  ADD PRIMARY KEY (`access_permission_name`);

--
-- Indexes for table `app_failed_login`
--
ALTER TABLE `app_failed_login`
  ADD PRIMARY KEY (`failed_login_id`);

--
-- Indexes for table `app_notifications`
--
ALTER TABLE `app_notifications`
  ADD PRIMARY KEY (`notification_id`);

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
-- Indexes for table `app_orders`
--
ALTER TABLE `app_orders`
  ADD PRIMARY KEY (`order_id`),
  ADD UNIQUE KEY `order_code` (`order_code`);

--
-- Indexes for table `app_order_approvals`
--
ALTER TABLE `app_order_approvals`
  ADD PRIMARY KEY (`order_approval_id`);

--
-- Indexes for table `app_order_attachments`
--
ALTER TABLE `app_order_attachments`
  ADD PRIMARY KEY (`order_attachment_id`);

--
-- Indexes for table `app_order_items`
--
ALTER TABLE `app_order_items`
  ADD PRIMARY KEY (`order_item_id`);

--
-- Indexes for table `app_order_logs`
--
ALTER TABLE `app_order_logs`
  ADD PRIMARY KEY (`order_log_id`);

--
-- Indexes for table `app_order_payments`
--
ALTER TABLE `app_order_payments`
  ADD PRIMARY KEY (`order_payment_id`);

--
-- Indexes for table `app_order_proposals`
--
ALTER TABLE `app_order_proposals`
  ADD PRIMARY KEY (`order_proposal_id`);

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
-- AUTO_INCREMENT for table `app_failed_login`
--
ALTER TABLE `app_failed_login`
  MODIFY `failed_login_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `app_notifications`
--
ALTER TABLE `app_notifications`
  MODIFY `notification_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `app_operators`
--
ALTER TABLE `app_operators`
  MODIFY `operator_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=28;
--
-- AUTO_INCREMENT for table `app_operator_access_permissions`
--
ALTER TABLE `app_operator_access_permissions`
  MODIFY `operator_access_permission_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=133;
--
-- AUTO_INCREMENT for table `app_operator_logs`
--
ALTER TABLE `app_operator_logs`
  MODIFY `operator_log_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `app_orders`
--
ALTER TABLE `app_orders`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `app_order_approvals`
--
ALTER TABLE `app_order_approvals`
  MODIFY `order_approval_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `app_order_attachments`
--
ALTER TABLE `app_order_attachments`
  MODIFY `order_attachment_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `app_order_items`
--
ALTER TABLE `app_order_items`
  MODIFY `order_item_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `app_order_logs`
--
ALTER TABLE `app_order_logs`
  MODIFY `order_log_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `app_order_payments`
--
ALTER TABLE `app_order_payments`
  MODIFY `order_payment_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `app_order_proposals`
--
ALTER TABLE `app_order_proposals`
  MODIFY `order_proposal_id` int(11) NOT NULL AUTO_INCREMENT;
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=85;
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=22;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=32;
--
-- AUTO_INCREMENT for table `django_site`
--
ALTER TABLE `django_site`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
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

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
