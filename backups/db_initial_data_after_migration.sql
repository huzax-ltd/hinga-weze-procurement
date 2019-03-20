-- phpMyAdmin SQL Dump
-- version 4.4.15.7
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 20, 2019 at 02:26 PM
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

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
