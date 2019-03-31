-- phpMyAdmin SQL Dump
-- version 4.4.15.7
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 31, 2019 at 12:30 AM
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
('inventory-create', 'inventory-create', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('inventory-delete', 'inventory-delete', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('inventory-update', 'inventory-update', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('inventory-view', 'inventory-view', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
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
('product-create', 'product-create', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('product-delete', 'product-delete', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('product-update', 'product-update', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('product-view', 'product-view', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000'),
('settings-view', 'settings-view', '2018-01-01 00:00:00.000000', '2018-01-01 00:00:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `app_attachments`
--

CREATE TABLE IF NOT EXISTS `app_attachments` (
  `attachment_id` int(11) NOT NULL,
  `attachment_model` varchar(255) NOT NULL,
  `attachment_model_id` int(11) NOT NULL,
  `attachment_type` varchar(255) NOT NULL,
  `attachment_type_id` int(11) NOT NULL,
  `attachment_number` int(11) NOT NULL,
  `attachment_file_name` varchar(255) NOT NULL,
  `attachment_file_path` varchar(100) NOT NULL,
  `attachment_file_size` varchar(255) NOT NULL,
  `attachment_file_type` varchar(255) NOT NULL,
  `attachment_file_uploaded_at` datetime(6) NOT NULL,
  `attachment_file_uploaded_id` varchar(100) NOT NULL,
  `attachment_file_uploaded_by` varchar(100) NOT NULL,
  `attachment_file_uploaded_department` varchar(255) NOT NULL,
  `attachment_file_uploaded_role` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_attachments`
--

INSERT INTO `app_attachments` (`attachment_id`, `attachment_model`, `attachment_model_id`, `attachment_type`, `attachment_type_id`, `attachment_number`, `attachment_file_name`, `attachment_file_path`, `attachment_file_size`, `attachment_file_type`, `attachment_file_uploaded_at`, `attachment_file_uploaded_id`, `attachment_file_uploaded_by`, `attachment_file_uploaded_department`, `attachment_file_uploaded_role`) VALUES
(1, 'orders', 1, 'order-email', 0, 0, 'Hinga_Weze_Process_Diagram.pdf', 'orders/order_email_69550384_1553984565798.pdf', '307873', 'application/pdf', '2019-03-30 22:22:45.000000', '21', 'Procurement Officer', 'DAF', 'Procurement Officer'),
(2, 'emails', 1, 'emails', 1, 1, 'Hinga_Weze_Process_Diagram.pdf', 'orders/order_email_69550384_1553984565798.pdf', '307873', 'application/pdf', '2019-03-30 22:27:23.000000', '21', 'Procurement Officer', 'DAF', 'Procurement Officer'),
(7, 'orders', 1, 'order-proposal-business-license', 14456092, 0, 'logo.png', 'orders/order_proposal_business_license_69550384_1553985902867.png', '8389', 'image/png', '2019-03-30 22:45:02.000000', '', '', '', ''),
(8, 'orders', 1, 'order-proposal-offer-letter', 14456092, 0, 'logo.png', 'orders/order_proposal_offer_letter_69550384_1553985909842.png', '8389', 'image/png', '2019-03-30 22:45:09.000000', '', '', '', ''),
(9, 'orders', 1, 'order-proposal-quotation', 14456092, 0, 'logo.png', 'orders/order_proposal_quotation_69550384_1553985915538.png', '8389', 'image/png', '2019-03-30 22:45:15.000000', '', '', '', ''),
(10, 'orders', 1, 'order-proposal-reference-document', 14456092, 1, 'logo.png', 'orders/order_proposal_reference_document_69550384_1553985922276.png', '8389', 'image/png', '2019-03-30 22:45:22.000000', '', '', '', ''),
(11, 'orders', 1, 'order-purchase', 0, 0, 'logo.png', 'orders/order_purchase_69550384_1553986494419.png', '8389', 'image/png', '2019-03-30 22:54:54.000000', '21', 'Procurement Officer', 'DAF', 'Procurement Officer');

-- --------------------------------------------------------

--
-- Table structure for table `app_emails`
--

CREATE TABLE IF NOT EXISTS `app_emails` (
  `email_id` int(11) NOT NULL,
  `email_from` varchar(255) NOT NULL,
  `email_from_name` varchar(255) NOT NULL,
  `email_to` varchar(255) NOT NULL,
  `email_cc` varchar(255) NOT NULL,
  `email_subject` varchar(255) NOT NULL,
  `email_message` longtext NOT NULL,
  `email_created_at` datetime(6) NOT NULL,
  `email_created_id` varchar(100) NOT NULL,
  `email_created_by` varchar(100) NOT NULL,
  `email_created_department` varchar(255) NOT NULL,
  `email_created_role` varchar(255) NOT NULL,
  `email_updated_at` datetime(6) NOT NULL,
  `email_updated_id` varchar(100) NOT NULL,
  `email_updated_by` varchar(100) NOT NULL,
  `email_updated_department` varchar(255) NOT NULL,
  `email_updated_role` varchar(255) NOT NULL,
  `email_sent_at` datetime(6) NOT NULL,
  `email_delivered_at` datetime(6) NOT NULL,
  `email_status` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_emails`
--

INSERT INTO `app_emails` (`email_id`, `email_from`, `email_from_name`, `email_to`, `email_cc`, `email_subject`, `email_message`, `email_created_at`, `email_created_id`, `email_created_by`, `email_created_department`, `email_created_role`, `email_updated_at`, `email_updated_id`, `email_updated_by`, `email_updated_department`, `email_updated_role`, `email_sent_at`, `email_delivered_at`, `email_status`) VALUES
(1, 'support@techcible.com', 'Cultivating New Frontiers in Agriculture', 'nyalapellinavin@gmail.com', '', 'Request for proposal', '<p>Dear vendors,</p>\r\n<p>Please submit your proposals within one week.</p>\r\n<p>Link to submit your proposals:&nbsp;<a title="Submit your proposal" href="../../../../order-proposals/create/1/0/" target="_blank" rel="noopener">Submit your proposal</a></p>\r\n<p>&nbsp;</p>\r\n<p>Thank you.</p>\r\n<p>Cultivating New Frontiers in Agriculture (CNFA)</p>', '2019-03-30 22:27:23.000000', '21', 'Procurement Officer', 'DAF', 'Procurement Officer', '2019-03-30 22:27:23.000000', '21', 'Procurement Officer', 'DAF', 'Procurement Officer', '2019-03-30 22:27:35.000000', '2019-03-30 22:27:35.000000', 'delivered');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_failed_login`
--

INSERT INTO `app_failed_login` (`failed_login_id`, `failed_login_username`, `failed_login_password`, `failed_login_from`, `failed_login_ip_address`, `failed_login_attempted_at`, `failed_login_status`) VALUES
(1, 'opm@cnfa.com', 'Kigali2123', 'backend', '127.0.0.1', '2019-03-30 22:21:15.000000', 1);

-- --------------------------------------------------------

--
-- Table structure for table `app_inventory`
--

CREATE TABLE IF NOT EXISTS `app_inventory` (
  `inventory_id` int(11) NOT NULL,
  `inventory_order_purchase_no` varchar(100) NOT NULL,
  `inventory_order_proposal_id` varchar(255) NOT NULL,
  `inventory_order_proposal_supplier_title` varchar(255) NOT NULL,
  `inventory_created_at` datetime(6) NOT NULL,
  `inventory_created_id` varchar(100) NOT NULL,
  `inventory_created_by` varchar(100) NOT NULL,
  `inventory_created_department` varchar(255) NOT NULL,
  `inventory_created_role` varchar(255) NOT NULL,
  `inventory_updated_at` datetime(6) NOT NULL,
  `inventory_updated_id` varchar(100) NOT NULL,
  `inventory_updated_by` varchar(100) NOT NULL,
  `inventory_updated_department` varchar(255) NOT NULL,
  `inventory_updated_role` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_inventory`
--

INSERT INTO `app_inventory` (`inventory_id`, `inventory_order_purchase_no`, `inventory_order_proposal_id`, `inventory_order_proposal_supplier_title`, `inventory_created_at`, `inventory_created_id`, `inventory_created_by`, `inventory_created_department`, `inventory_created_role`, `inventory_updated_at`, `inventory_updated_id`, `inventory_updated_by`, `inventory_updated_department`, `inventory_updated_role`) VALUES
(1, 'PO - 123456', '1', 'Navin Nyalapelli', '2019-03-30 22:57:42.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', '2019-03-30 22:57:42.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin');

-- --------------------------------------------------------

--
-- Table structure for table `app_inventory_items`
--

CREATE TABLE IF NOT EXISTS `app_inventory_items` (
  `inventory_item_id` int(11) NOT NULL,
  `inventory_inventory_id` int(11) NOT NULL,
  `products_product_id` int(11) NOT NULL,
  `inventory_item_product_type` varchar(255) NOT NULL,
  `inventory_item_product_code` varchar(8) NOT NULL,
  `inventory_item_product_tag` varchar(255) NOT NULL,
  `inventory_item_product_category` varchar(255) NOT NULL,
  `inventory_item_product_title` varchar(100) NOT NULL,
  `inventory_item_product_sub_title` varchar(255) NOT NULL,
  `inventory_item_product_quantity_initial` decimal(10,0) NOT NULL,
  `inventory_item_product_quantity_ordered` decimal(10,0) NOT NULL,
  `inventory_item_product_quantity_balance` decimal(10,0) NOT NULL,
  `inventory_item_product_quantity_unit` varchar(255) NOT NULL,
  `inventory_item_product_currency` varchar(255) NOT NULL,
  `inventory_item_product_unit_price` decimal(10,0) NOT NULL,
  `inventory_item_product_rate_price` decimal(10,0) NOT NULL,
  `inventory_item_product_usd_price` decimal(10,0) NOT NULL,
  `inventory_item_product_usaid_equipment_price` decimal(10,0) NOT NULL,
  `inventory_item_product_small_equipment_price` decimal(10,0) NOT NULL,
  `inventory_item_project` varchar(255) NOT NULL,
  `inventory_item_voucher_reference` varchar(255) NOT NULL,
  `inventory_item_location` varchar(255) NOT NULL,
  `inventory_item_equipment_holder_status` varchar(255) NOT NULL,
  `inventory_item_staff_name` varchar(255) NOT NULL,
  `inventory_item_room_number` varchar(255) NOT NULL,
  `inventory_item_present_condition` varchar(255) NOT NULL,
  `inventory_item_disposal_date` date NOT NULL,
  `inventory_item_verified_date` date NOT NULL,
  `inventory_item_remark` varchar(255) NOT NULL,
  `inventory_item_created_at` datetime(6) NOT NULL,
  `inventory_item_created_id` varchar(100) NOT NULL,
  `inventory_item_created_by` varchar(100) NOT NULL,
  `inventory_item_created_department` varchar(255) NOT NULL,
  `inventory_item_created_role` varchar(255) NOT NULL,
  `inventory_item_updated_at` datetime(6) NOT NULL,
  `inventory_item_updated_id` varchar(100) NOT NULL,
  `inventory_item_updated_by` varchar(100) NOT NULL,
  `inventory_item_updated_department` varchar(255) NOT NULL,
  `inventory_item_updated_role` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_inventory_items`
--

INSERT INTO `app_inventory_items` (`inventory_item_id`, `inventory_inventory_id`, `products_product_id`, `inventory_item_product_type`, `inventory_item_product_code`, `inventory_item_product_tag`, `inventory_item_product_category`, `inventory_item_product_title`, `inventory_item_product_sub_title`, `inventory_item_product_quantity_initial`, `inventory_item_product_quantity_ordered`, `inventory_item_product_quantity_balance`, `inventory_item_product_quantity_unit`, `inventory_item_product_currency`, `inventory_item_product_unit_price`, `inventory_item_product_rate_price`, `inventory_item_product_usd_price`, `inventory_item_product_usaid_equipment_price`, `inventory_item_product_small_equipment_price`, `inventory_item_project`, `inventory_item_voucher_reference`, `inventory_item_location`, `inventory_item_equipment_holder_status`, `inventory_item_staff_name`, `inventory_item_room_number`, `inventory_item_present_condition`, `inventory_item_disposal_date`, `inventory_item_verified_date`, `inventory_item_remark`, `inventory_item_created_at`, `inventory_item_created_id`, `inventory_item_created_by`, `inventory_item_created_department`, `inventory_item_created_role`, `inventory_item_updated_at`, `inventory_item_updated_id`, `inventory_item_updated_by`, `inventory_item_updated_department`, `inventory_item_updated_role`) VALUES
(1, 1, 1, 'asset', '50162978', 'HW001', 'Furniture', '3 Door filling cabinet', '', 0, 20, 20, '', 'RWF', 3000, 0, 0, 0, 0, 'Feed the Future Rwanda Hinga Weze', '', '', '', 'Navin Nyalapelli', '', 'good', '0001-01-01', '2019-04-01', 'good', '0001-01-01 00:00:00.000000', '', '', '', '', '0001-01-01 00:00:00.000000', '', '', '', ''),
(2, 1, 2, 'asset', '59173245', 'HW002', 'Furniture', 'Round meeting table 150 cmx75cm/Glass Top', '', 0, 20, 20, '', 'RWF', 2000, 0, 0, 0, 0, 'Feed the Future Rwanda Hinga Weze', '', '', '', 'Navin Nyalapelli', '', 'good', '0001-01-01', '2019-04-01', 'good', '0001-01-01 00:00:00.000000', '', '', '', '', '0001-01-01 00:00:00.000000', '', '', '', '');

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
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_notifications`
--

INSERT INTO `app_notifications` (`notification_id`, `notification_model_id`, `notification_model_type`, `notification_from_type`, `notification_from_id`, `notification_to_type`, `notification_to_id`, `notification_message`, `notification_url`, `notification_created_at`, `notification_read_at`, `notification_fixed_at`, `notification_status`) VALUES
(1, 1, 'order', 'operator', 19, 'operator', 18, 'Created a purchase request to review.', '/backend/orders/view/1/', '2019-03-30 22:11:52.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(2, 1, 'order', 'operator', 18, 'operator', 19, 'Approved your purchase request at level 1.', '/backend/orders/view/1/', '2019-03-30 22:12:28.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(3, 1, 'order', 'operator', 18, 'operator', 17, 'Created a purchase request to review.', '/backend/orders/view/1/', '2019-03-30 22:12:28.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(4, 1, 'order', 'operator', 18, 'operator', 19, 'Approved your purchase request at level 2.', '/backend/orders/view/1/', '2019-03-30 22:12:52.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(5, 1, 'order', 'operator', 17, 'operator', 18, 'Approved your purchase request at level 2.', '/backend/orders/view/1/', '2019-03-30 22:12:52.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(6, 1, 'order', 'operator', 17, 'operator', 7, 'Created a purchase request to review.', '/backend/orders/view/1/', '2019-03-30 22:12:52.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(7, 1, 'order', 'operator', 18, 'operator', 19, 'Approved your purchase request at level 3.', '/backend/orders/view/1/', '2019-03-30 22:13:28.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(8, 1, 'order', 'operator', 17, 'operator', 18, 'Approved your purchase request at level 3.', '/backend/orders/view/1/', '2019-03-30 22:13:28.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(9, 1, 'order', 'operator', 7, 'operator', 17, 'Approved your purchase request at level 3.', '/backend/orders/view/1/', '2019-03-30 22:13:28.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(10, 1, 'order', 'operator', 7, 'operator', 20, 'Created a purchase request to review.', '/backend/orders/view/1/', '2019-03-30 22:13:28.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(11, 1, 'order', 'operator', 20, 'operator', 10, 'Created a purchase request to review.', '/backend/orders/view/1/', '2019-03-30 22:19:28.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(12, 1, 'order', 'operator', 10, 'operator', 3, 'A purchase request has been sent for approval.', '/backend/orders/view/1/', '2019-03-30 22:20:12.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(13, 1, 'order', 'operator', 3, 'operator', 19, 'Your purchase order request has been approved by COP.', '/backend/orders/view/1/', '2019-03-30 22:20:51.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(14, 1, 'order', 'operator', 3, 'operator', 18, 'Your purchase order request has been approved by COP.', '/backend/orders/view/1/', '2019-03-30 22:20:51.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(15, 1, 'order', 'operator', 3, 'operator', 17, 'Your purchase order request has been approved by COP.', '/backend/orders/view/1/', '2019-03-30 22:20:51.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(16, 1, 'order', 'operator', 3, 'operator', 7, 'Your purchase order request has been approved by COP.', '/backend/orders/view/1/', '2019-03-30 22:20:51.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(17, 1, 'order', 'operator', 3, 'operator', 20, 'A purchase request has been sent by COP to process ahead.', '/backend/orders/view/1/', '2019-03-30 22:20:51.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(18, 1, 'order', 'operator', 20, 'operator', 21, 'Assigned a purchase request to process ahead.', '/backend/orders/view/1/', '2019-03-30 22:21:32.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(19, 1, 'order-proposal', 'supplier', 1, 'operator', 21, 'Submitted a proposal to evaluate.', '/backend/order-proposals/view/internal/1/', '2019-03-30 22:47:22.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(20, 1, 'order-proposal', 'operator', 21, 'operator', 3, 'Some vendors are selected to review.', '/backend/order-proposals/index/1/', '2019-03-30 22:48:42.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(21, 1, 'order-proposal', 'operator', 21, 'operator', 20, 'Some vendors are selected to review.', '/backend/order-proposals/index/1/', '2019-03-30 22:48:42.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(22, 1, 'order-proposal', 'supplier', 1, 'operator', 21, 'Acknowledged proposal to generate purchase order.', '/backend/order-proposals/view/internal/1/', '2019-03-30 22:49:39.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(23, 1, 'order', 'supplier', 1, 'operator', 21, 'Acknowledged purchase order.', '/backend/orders/view/1/', '2019-03-30 22:56:02.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(24, 1, 'product-request', 'operator', 24, 'operator', 24, 'A stock request has been sent for approval.', '/backend/product-requests/view/1/', '2019-03-30 23:02:29.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(25, 1, 'product-request', 'operator', 24, 'operator', 24, 'Your stock request has been reviewed.', '/backend/product-requests/view/1/', '2019-03-30 23:02:35.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread'),
(26, 1, 'product-request', 'operator', 24, 'operator', 24, 'Your stock request has been approved.', '/backend/product-requests/view/1/', '2019-03-30 23:02:41.000000', '0001-01-01 00:00:00.000000', '0001-01-01 00:00:00.000000', 'unread');

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
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_operators`
--

INSERT INTO `app_operators` (`operator_id`, `operator_type`, `operator_department`, `operator_role`, `operator_parent_id`, `operator_username`, `operator_auth_key`, `operator_password_hash`, `operator_password_reset_token`, `operator_name`, `operator_gender`, `operator_contact_phone_number`, `operator_contact_email_id`, `operator_profile_photo_file_path`, `operator_created_at`, `operator_created_by`, `operator_updated_at`, `operator_updated_by`, `operator_status`) VALUES
(1, 'super-admin', 'NONE', 'NONE', 0, 'support@huzax.com', 'xc48ITBOTVBu87185KUSK2TlKxKiLJiw', 'pbkdf2_sha256$120000$slxVGFEthWuq$AqS7ZymOOeSEof9mPJ2ITXXQvwkIdHIv5Ko2DvKN+Hw=', '', 'Tech Support', 'male', '250726875122', 'support@techcible.com', '', '2018-01-01 00:00:00.000000', 'support@techcible.com', '2019-03-31 00:24:31.000000', 'support@huzax.com', 'active'),
(2, 'admin', 'NONE', 'NONE', 0, 'admin@huzax.com', 'xc48ITBOTVBu87185KUSK2TlKxKiLJij', 'pbkdf2_sha256$120000$0AZewnnKGdCy$jqU6YkCayb2sJIL48xCDb5lf9bl8uvGEmskIPALXX0c=', '', 'Admin Support', 'male', '250726875122', 'support@techcible.com', '', '2018-01-01 00:00:00.000000', 'support@techcible.com', '2019-03-30 20:59:24.000000', 'support@huzax.com', 'inactive'),
(3, 'admin', 'NONE', 'COP', 0, 'cop@cnfa.com', 'zfBKwMdmxoZAcJOIfXDcJF7v5jA0Bd1N', 'pbkdf2_sha256$120000$Eymsl3uiJOdI$mj0tiVMeqYQAaap3jMz3qCLXDae0I4SQ1DPQDMOHriU=', '', 'COP', 'male', '250726875122', 'cop@cnfa.com', '', '2019-03-16 07:57:21.000000', 'support@techcible.com', '2019-03-30 22:50:03.000000', 'cop@cnfa.com', 'inactive'),
(5, 'other', 'DCOP', 'Adviser', 0, 'adviser1@cnfa.com', 'm2FBIi9jFgsotH4jL8gojAMj8FVD49mR', 'pbkdf2_sha256$120000$hiBmCt5ioxTd$oJwNv3s/4xPw6NDvFlrKa7NOSdz92d+ygw4cLWJt9k4=', '', 'Adviser', '', '', 'adviser1@cnfa.com', '', '2019-03-16 08:04:08.000000', 'support@techcible.com', '2019-03-30 20:59:32.000000', 'support@huzax.com', 'inactive'),
(6, 'other', 'BFM', 'Adviser', 0, 'adviser2@cnfa.com', 'KBxQW7R5NQb2qHiTvLqMRYiLGHmu1Qfm', 'pbkdf2_sha256$120000$5sOWMyo0bcw2$7PAh4Jbis2l8sDwmOtj8HVx5/y3BICiK23XOkfL4h3s=', '', 'Adviser', '', '', 'adviser2@cnfa.com', '', '2019-03-16 08:05:00.000000', 'support@techcible.com', '2019-03-30 20:59:39.000000', 'support@huzax.com', 'inactive'),
(7, 'other', 'DCOP', 'Director', 0, 'director1@cnfa.com', 'yXs4Zu4k1Vejuq6Ir9Qirk6GPt0fhy9H', 'pbkdf2_sha256$120000$zKG9xhAHvVuF$U8RTkaT07AkCbwn//KB0JqjN1i9r7wLjIygdWSMGr1s=', '', 'Director', '', '', 'director1@cnfa.com', '', '2019-03-16 08:05:58.000000', 'support@techcible.com', '2019-03-30 22:13:33.000000', 'director1@cnfa.com', 'inactive'),
(8, 'other', 'BFM', 'Director', 0, 'director2@cnfa.com', '9TWyuEGtw5j7ncV4mKjuq6Qu8UF4dSHW', 'pbkdf2_sha256$120000$jGmwRUev0HMU$ou194WQR7+9urs9AlbS0rfHYRgKaMbRfysNs0ZI2oP8=', '', 'Director', '', '', 'director2@cnfa.com', '', '2019-03-16 08:06:39.000000', 'support@techcible.com', '2019-03-30 21:00:30.000000', 'support@huzax.com', 'inactive'),
(9, 'other', 'NUTRITION', 'Director', 0, 'director3@cnfa.com', 'NQGsWXCzOwPfrCgKL72viC5WOl5P6zPR', 'pbkdf2_sha256$120000$N9cHTVgnGVob$OSCAR1jpAy7ZIK3vdFFhT/Xjv6po80DIsP4GgNTRBOs=', '', 'Director', '', '', 'director3@cnfa.com', '', '2019-03-16 08:07:19.000000', 'support@techcible.com', '2019-03-30 21:00:38.000000', 'support@huzax.com', 'inactive'),
(10, 'other', 'DAF', 'Director', 0, 'director4@cnfa.com', 'IFw1OhUnpK4vC0oNZ1eLIJl90Sf7XTq5', 'pbkdf2_sha256$120000$bNioT9HzoclL$mHjy+C3GGtZIDIiXpy2O1Rhxkw0e7YVmrtsR/lD/olQ=', '', 'Director', '', '', 'director4@cnfa.com', '', '2019-03-16 08:12:24.000000', 'support@techcible.com', '2019-03-30 22:20:17.000000', 'director4@cnfa.com', 'inactive'),
(11, 'other', 'MAE', 'Director', 0, 'director5@cnfa.com', 'YhzflTHiofZKw8h0KL8K1vaDW1y9bM0t', 'pbkdf2_sha256$120000$tnJXqsha0u4i$9Txi1Zv7f3JWTu/+jAFhpzuf6IFEQqtt6/AODJ2sJ50=', '', 'Director', '', '', 'director5@cnfa.com', '', '2019-03-16 08:13:44.000000', 'support@techcible.com', '2019-03-30 21:00:54.000000', 'support@huzax.com', 'inactive'),
(12, 'other', 'GRANT-MANAGER', 'Director', 0, 'director6@cnfa.com', 'WGyenjMVldyjtY6IuduKgMic6Sv8uLHd', 'pbkdf2_sha256$120000$dDwenlddMmm3$8yjIaf4fEZcBSGMJxxl+UbN7h9eOBSIrrVuC4XY6q2g=', '', 'Director', '', '', 'director6@cnfa.com', '', '2019-03-16 08:14:51.000000', 'support@techcible.com', '2019-03-30 21:01:01.000000', 'support@huzax.com', 'inactive'),
(13, 'other', 'NUTRITION', 'Adviser', 0, 'adviser3@cnfa.com', 'crqq8IEyuDmHPD3oVwTuGo3T65ceM4pg', 'pbkdf2_sha256$120000$Jbp41wC6dyn3$t/2qpFees4Q48zWPeCQV6QI/7YTJ0ibHPVexhNvjCL8=', '', 'Adviser', '', '', 'adviser3@cnfa.com', '', '2019-03-16 08:15:40.000000', 'support@techcible.com', '2019-03-30 20:59:47.000000', 'support@huzax.com', 'inactive'),
(14, 'other', 'DAF', 'Adviser', 0, 'adviser4@cnfa.com', 'hUSqCUUgjNGyBBIDaP0o6A1l6mrN37Ip', 'pbkdf2_sha256$120000$J2NH4VXhJo4S$qgGPOMm2RILElmt3Xu5wmS60VjR3f5fsFS54/GHkKh4=', '', 'Adviser', '', '', 'adviser4@cnfa.com', '', '2019-03-16 08:16:26.000000', 'support@techcible.com', '2019-03-30 20:59:54.000000', 'support@huzax.com', 'inactive'),
(15, 'other', 'MAE', 'Adviser', 0, 'adviser5@cnfa.com', '9tJk7cacK1akmXqhOEz4JTHAR45zfDVz', 'pbkdf2_sha256$120000$3TicMHgC7qhK$cm+d3HIdjlyfIRcrqvNiWosGxuBxKdT/SIWB0I26x7M=', '', 'Adviser', '', '', 'adviser5@cnfa.com', '', '2019-03-16 08:17:09.000000', 'support@techcible.com', '2019-03-30 21:00:01.000000', 'support@huzax.com', 'inactive'),
(16, 'other', 'GRANT-MANAGER', 'Adviser', 0, 'adviser6@cnfa.com', 'i1NZqNTjmBOk7bQKGIBf6SEhaIT3Nh2p', 'pbkdf2_sha256$120000$XPY2v6TZ3Klp$gulavsu3OJwW1g/NnbMcsvWX/7ONtrtf6rDI1/bLfi4=', '', 'Adviser', '', '', 'adviser6@cnfa.com', '', '2019-03-16 08:17:59.000000', 'support@techcible.com', '2019-03-30 21:00:08.000000', 'support@huzax.com', 'inactive'),
(17, 'other', 'DCOP', 'Regional Manager', 7, 'regionalmanager1@cnfa.com', 'fl84IgzQrCCgLZkbH8roEEKCGbTPVdrd', 'pbkdf2_sha256$120000$s5mFzxFEDDgf$CDmsswwmruURZ2+iv542Ka3O3sXR/90711Q1ZMzxNWA=', '', 'Regional Manager', '', '', 'regionalmanager1@cnfa.com', '', '2019-03-16 08:19:40.000000', 'support@techcible.com', '2019-03-30 22:12:58.000000', 'regionalmanager1@cnfa.com', 'inactive'),
(18, 'other', 'DCOP', 'District Manager', 17, 'districtmanager1@cnfa.com', 'WZMXduZfBvG5ESN5b7OTuqK1pRL0PW4Y', 'pbkdf2_sha256$120000$b3SROpuoCkRL$23rXmqtmwX+goy2XNf3tjIMZMhXiD3mKAiClunuZriE=', '', 'District Manager', '', '', 'districtmanager1@cnfa.com', '', '2019-03-16 08:32:00.000000', 'support@techcible.com', '2019-03-30 22:12:32.000000', 'districtmanager1@cnfa.com', 'inactive'),
(19, 'other', 'DCOP', 'Field Officer', 18, 'fieldofficer1@cnfa.com', 'PUS4HCyX8xWAa7TECQCmpl1wgm5xNslI', 'pbkdf2_sha256$120000$iuJFIb6vPXZT$zGaoYk5X+P7Xp3hss6S5jG5XQXXlBlhgR22mctGgwNI=', '', 'Field Officer', '', '', 'fieldofficer1@cnfa.com', '', '2019-03-16 08:33:35.000000', 'support@techcible.com', '2019-03-30 22:11:57.000000', 'fieldofficer1@cnfa.com', 'inactive'),
(20, 'other', 'DAF', 'OPM', 0, 'opm@cnfa.com', '3DrkUbJ1eBynRQRT1mNEBxzXaMEgKDw5', 'pbkdf2_sha256$120000$TOAT1aTMLU4h$CTTi/TbdiAr7x/NfRYVdk0Ujeg2F/UskTgwn2bLBSFE=', '', 'OPM', '', '', 'opm@cnfa.com', '', '2019-03-16 08:36:57.000000', 'support@techcible.com', '2019-03-30 22:21:35.000000', 'opm@cnfa.com', 'inactive'),
(21, 'other', 'DAF', 'Procurement Officer', 0, 'procurementofficer1@cnfa.com', 'GfQdxXaUMDorx5Wo27v8c75LYlWx11zr', 'pbkdf2_sha256$120000$pD0uidNxvO1u$4s4wmz0lye1rL71erk7xb92XJuoIWUuS7mZ+vq90sAY=', '', 'Procurement Officer', '', '', 'procurementofficer1@cnfa.com', '', '2019-03-16 08:37:59.000000', 'support@techcible.com', '2019-03-30 22:56:39.000000', 'procurementofficer1@cnfa.com', 'inactive'),
(23, 'other', 'DAF', 'HR Manager', 0, 'hrmanager1@cnfa.com', 'dBMR8fCY6yug3I1rkz5ZpktOc48pz6RR', 'pbkdf2_sha256$120000$TMLiQbkkz5LN$2qcxT1idd+asvL2uujrnVsTOSoU3xEYxepdD9amOgdE=', '', 'HR Manager', '', '', 'hrmanager1@cnfa.com', '', '2019-03-16 08:39:32.000000', 'support@techcible.com', '2019-03-30 21:01:23.000000', 'support@huzax.com', 'inactive'),
(24, 'other', 'DAF', 'Stock Admin', 0, 'stockadmin1@cnfa.com', 'ncwJxatJBg54mKl18sL0kgf7EsdubiHR', 'pbkdf2_sha256$120000$zkQcmUHnElCn$JCIOcawtp4zAk2YRVkGF0hfqlmKchPTvS3Jr8i7uSeE=', '', 'Stock Admin', '', '', 'stockadmin1@cnfa.com', '', '2019-03-16 08:40:30.000000', 'support@techcible.com', '2019-03-30 22:56:55.000000', 'stockadmin1@cnfa.com', 'active'),
(25, 'other', 'DAF', 'Accountant Manager', 0, 'accountmanager1@cnfa.com', 'O1QK8kXYngR3RZlESI0IDet9sl6LzCYx', 'pbkdf2_sha256$120000$px6RvRkRb2wg$5NJKiiWIYEU4qCuZeOoStvQ/n639jN+W4oNCDwo1z44=', '', 'Account Manager', '', '', 'accountmanager1@cnfa.com', '', '2019-03-16 08:41:12.000000', 'support@techcible.com', '2019-03-30 20:58:57.000000', 'support@huzax.com', 'inactive'),
(26, 'other', 'DAF', 'Accountant Officer', 25, 'accountofficer1@cnfa.com', 'CcgpIa40PPdlkLqZrzjxFcNAlClRqeuF', 'pbkdf2_sha256$120000$FW7zTpkCPKZF$DgWpE9Bx6NZEL8uLa03ec3o7AnA+84EI7z5r4OwttcY=', '', 'Account Officer', '', '', 'accountofficer1@cnfa.com', '', '2019-03-16 08:42:05.000000', 'support@techcible.com', '2019-03-30 20:59:04.000000', 'support@huzax.com', 'inactive'),
(27, 'other', 'DAF', 'Accountant Officer', 25, 'accountofficer2@cnfa.com', '8TyWRDz6jRkEI4ig86twAMBEzOxx5ulh', 'pbkdf2_sha256$120000$teGe2geOciiR$w5U1LWqZQKwjGuRhs+s+JK9jeaEacRXzulnOcRpim7c=', '', 'Account Officer', '', '', 'accountofficer2@cnfa.com', '', '2019-03-16 08:45:28.000000', 'support@techcible.com', '2019-03-30 20:59:12.000000', 'support@huzax.com', 'inactive'),
(28, 'other', 'DAF', 'Receptionist', 0, 'receptionist1@cnfa.com', 'q0wQd0IE85vOqvYYsjkogVnExcyfVhYp', 'pbkdf2_sha256$120000$rFHfw9Tf3CLW$WZVLYXXng7r8dDUmiSiidybySglt3twtJ9pGmLtz1FE=', '', 'Receptionist', '', '', 'receptionist1@cnfa.com', '', '2019-03-31 00:26:11.000000', 'support@huzax.com', '2019-03-31 00:28:06.000000', 'support@huzax.com', 'inactive');

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
) ENGINE=InnoDB AUTO_INCREMENT=392 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_operator_access_permissions`
--

INSERT INTO `app_operator_access_permissions` (`operator_access_permission_id`, `operator_access_permission_updated_at`, `operator_access_permission_updated_by`, `access_permissions_access_permission_name_id`, `operators_operator_id_id`) VALUES
(210, '2019-03-30 20:58:57.000000', 'support@huzax.com', 'order-create', 25),
(211, '2019-03-30 20:58:57.000000', 'support@huzax.com', 'order-update', 25),
(212, '2019-03-30 20:58:57.000000', 'support@huzax.com', 'order-view', 25),
(213, '2019-03-30 20:58:57.000000', 'support@huzax.com', 'order-delete', 25),
(214, '2019-03-30 20:58:57.000000', 'support@huzax.com', 'product-delete', 25),
(215, '2019-03-30 20:59:04.000000', 'support@huzax.com', 'order-create', 26),
(216, '2019-03-30 20:59:04.000000', 'support@huzax.com', 'order-update', 26),
(217, '2019-03-30 20:59:04.000000', 'support@huzax.com', 'order-view', 26),
(218, '2019-03-30 20:59:04.000000', 'support@huzax.com', 'order-delete', 26),
(219, '2019-03-30 20:59:04.000000', 'support@huzax.com', 'product-delete', 26),
(220, '2019-03-30 20:59:12.000000', 'support@huzax.com', 'order-create', 27),
(221, '2019-03-30 20:59:12.000000', 'support@huzax.com', 'order-update', 27),
(222, '2019-03-30 20:59:12.000000', 'support@huzax.com', 'order-view', 27),
(223, '2019-03-30 20:59:12.000000', 'support@huzax.com', 'order-delete', 27),
(224, '2019-03-30 20:59:12.000000', 'support@huzax.com', 'product-delete', 27),
(225, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'settings-view', 2),
(226, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'log-delete', 2),
(227, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'log-view', 2),
(228, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'dashboard-view', 2),
(229, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'operator-create', 2),
(230, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'operator-update', 2),
(231, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'operator-delete', 2),
(232, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'operator-view', 2),
(233, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'order-create', 2),
(234, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'order-update', 2),
(235, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'order-view', 2),
(236, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'order-delete', 2),
(237, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'product-delete', 2),
(238, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'product-create', 2),
(239, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'product-update', 2),
(240, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'product-view', 2),
(241, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'inventory-create', 2),
(242, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'inventory-update', 2),
(243, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'inventory-view', 2),
(244, '2019-03-30 20:59:24.000000', 'support@huzax.com', 'inventory-delete', 2),
(245, '2019-03-30 20:59:32.000000', 'support@huzax.com', 'order-create', 5),
(246, '2019-03-30 20:59:32.000000', 'support@huzax.com', 'order-update', 5),
(247, '2019-03-30 20:59:32.000000', 'support@huzax.com', 'order-view', 5),
(248, '2019-03-30 20:59:32.000000', 'support@huzax.com', 'order-delete', 5),
(249, '2019-03-30 20:59:32.000000', 'support@huzax.com', 'product-delete', 5),
(250, '2019-03-30 20:59:39.000000', 'support@huzax.com', 'order-create', 6),
(251, '2019-03-30 20:59:39.000000', 'support@huzax.com', 'order-update', 6),
(252, '2019-03-30 20:59:39.000000', 'support@huzax.com', 'order-view', 6),
(253, '2019-03-30 20:59:39.000000', 'support@huzax.com', 'order-delete', 6),
(254, '2019-03-30 20:59:39.000000', 'support@huzax.com', 'product-delete', 6),
(255, '2019-03-30 20:59:47.000000', 'support@huzax.com', 'order-create', 13),
(256, '2019-03-30 20:59:47.000000', 'support@huzax.com', 'order-update', 13),
(257, '2019-03-30 20:59:47.000000', 'support@huzax.com', 'order-view', 13),
(258, '2019-03-30 20:59:47.000000', 'support@huzax.com', 'order-delete', 13),
(259, '2019-03-30 20:59:47.000000', 'support@huzax.com', 'product-delete', 13),
(260, '2019-03-30 20:59:54.000000', 'support@huzax.com', 'order-create', 14),
(261, '2019-03-30 20:59:54.000000', 'support@huzax.com', 'order-update', 14),
(262, '2019-03-30 20:59:54.000000', 'support@huzax.com', 'order-view', 14),
(263, '2019-03-30 20:59:54.000000', 'support@huzax.com', 'order-delete', 14),
(264, '2019-03-30 20:59:54.000000', 'support@huzax.com', 'product-delete', 14),
(265, '2019-03-30 21:00:01.000000', 'support@huzax.com', 'order-create', 15),
(266, '2019-03-30 21:00:01.000000', 'support@huzax.com', 'order-update', 15),
(267, '2019-03-30 21:00:01.000000', 'support@huzax.com', 'order-view', 15),
(268, '2019-03-30 21:00:01.000000', 'support@huzax.com', 'order-delete', 15),
(269, '2019-03-30 21:00:01.000000', 'support@huzax.com', 'product-delete', 15),
(270, '2019-03-30 21:00:08.000000', 'support@huzax.com', 'order-create', 16),
(271, '2019-03-30 21:00:08.000000', 'support@huzax.com', 'order-update', 16),
(272, '2019-03-30 21:00:08.000000', 'support@huzax.com', 'order-view', 16),
(273, '2019-03-30 21:00:08.000000', 'support@huzax.com', 'order-delete', 16),
(274, '2019-03-30 21:00:08.000000', 'support@huzax.com', 'product-delete', 16),
(275, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'settings-view', 3),
(276, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'log-delete', 3),
(277, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'log-view', 3),
(278, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'dashboard-view', 3),
(279, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'operator-create', 3),
(280, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'operator-update', 3),
(281, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'operator-delete', 3),
(282, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'operator-view', 3),
(283, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'order-create', 3),
(284, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'order-update', 3),
(285, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'order-view', 3),
(286, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'order-delete', 3),
(287, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'product-delete', 3),
(288, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'product-create', 3),
(289, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'product-update', 3),
(290, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'product-view', 3),
(291, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'inventory-create', 3),
(292, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'inventory-update', 3),
(293, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'inventory-view', 3),
(294, '2019-03-30 21:00:15.000000', 'support@huzax.com', 'inventory-delete', 3),
(295, '2019-03-30 21:00:23.000000', 'support@huzax.com', 'order-create', 7),
(296, '2019-03-30 21:00:23.000000', 'support@huzax.com', 'order-update', 7),
(297, '2019-03-30 21:00:23.000000', 'support@huzax.com', 'order-view', 7),
(298, '2019-03-30 21:00:23.000000', 'support@huzax.com', 'order-delete', 7),
(299, '2019-03-30 21:00:23.000000', 'support@huzax.com', 'product-delete', 7),
(300, '2019-03-30 21:00:30.000000', 'support@huzax.com', 'order-create', 8),
(301, '2019-03-30 21:00:30.000000', 'support@huzax.com', 'order-update', 8),
(302, '2019-03-30 21:00:30.000000', 'support@huzax.com', 'order-view', 8),
(303, '2019-03-30 21:00:30.000000', 'support@huzax.com', 'order-delete', 8),
(304, '2019-03-30 21:00:30.000000', 'support@huzax.com', 'product-delete', 8),
(305, '2019-03-30 21:00:38.000000', 'support@huzax.com', 'order-create', 9),
(306, '2019-03-30 21:00:38.000000', 'support@huzax.com', 'order-update', 9),
(307, '2019-03-30 21:00:38.000000', 'support@huzax.com', 'order-view', 9),
(308, '2019-03-30 21:00:38.000000', 'support@huzax.com', 'order-delete', 9),
(309, '2019-03-30 21:00:38.000000', 'support@huzax.com', 'product-delete', 9),
(310, '2019-03-30 21:00:47.000000', 'support@huzax.com', 'order-create', 10),
(311, '2019-03-30 21:00:47.000000', 'support@huzax.com', 'order-update', 10),
(312, '2019-03-30 21:00:47.000000', 'support@huzax.com', 'order-view', 10),
(313, '2019-03-30 21:00:47.000000', 'support@huzax.com', 'order-delete', 10),
(314, '2019-03-30 21:00:47.000000', 'support@huzax.com', 'product-delete', 10),
(315, '2019-03-30 21:00:54.000000', 'support@huzax.com', 'order-create', 11),
(316, '2019-03-30 21:00:54.000000', 'support@huzax.com', 'order-update', 11),
(317, '2019-03-30 21:00:54.000000', 'support@huzax.com', 'order-view', 11),
(318, '2019-03-30 21:00:54.000000', 'support@huzax.com', 'order-delete', 11),
(319, '2019-03-30 21:00:54.000000', 'support@huzax.com', 'product-delete', 11),
(320, '2019-03-30 21:01:01.000000', 'support@huzax.com', 'order-create', 12),
(321, '2019-03-30 21:01:01.000000', 'support@huzax.com', 'order-update', 12),
(322, '2019-03-30 21:01:01.000000', 'support@huzax.com', 'order-view', 12),
(323, '2019-03-30 21:01:01.000000', 'support@huzax.com', 'order-delete', 12),
(324, '2019-03-30 21:01:02.000000', 'support@huzax.com', 'product-delete', 12),
(325, '2019-03-30 21:01:08.000000', 'support@huzax.com', 'order-create', 18),
(326, '2019-03-30 21:01:08.000000', 'support@huzax.com', 'order-update', 18),
(327, '2019-03-30 21:01:08.000000', 'support@huzax.com', 'order-view', 18),
(328, '2019-03-30 21:01:08.000000', 'support@huzax.com', 'order-delete', 18),
(329, '2019-03-30 21:01:08.000000', 'support@huzax.com', 'product-delete', 18),
(330, '2019-03-30 21:01:16.000000', 'support@huzax.com', 'order-create', 19),
(331, '2019-03-30 21:01:16.000000', 'support@huzax.com', 'order-update', 19),
(332, '2019-03-30 21:01:16.000000', 'support@huzax.com', 'order-view', 19),
(333, '2019-03-30 21:01:16.000000', 'support@huzax.com', 'order-delete', 19),
(334, '2019-03-30 21:01:16.000000', 'support@huzax.com', 'product-delete', 19),
(335, '2019-03-30 21:01:23.000000', 'support@huzax.com', 'order-create', 23),
(336, '2019-03-30 21:01:23.000000', 'support@huzax.com', 'order-update', 23),
(337, '2019-03-30 21:01:23.000000', 'support@huzax.com', 'order-view', 23),
(338, '2019-03-30 21:01:23.000000', 'support@huzax.com', 'order-delete', 23),
(339, '2019-03-30 21:01:23.000000', 'support@huzax.com', 'product-delete', 23),
(340, '2019-03-30 21:01:31.000000', 'support@huzax.com', 'order-create', 20),
(341, '2019-03-30 21:01:31.000000', 'support@huzax.com', 'order-update', 20),
(342, '2019-03-30 21:01:31.000000', 'support@huzax.com', 'order-view', 20),
(343, '2019-03-30 21:01:31.000000', 'support@huzax.com', 'order-delete', 20),
(344, '2019-03-30 21:01:31.000000', 'support@huzax.com', 'product-delete', 20),
(345, '2019-03-30 21:01:39.000000', 'support@huzax.com', 'order-create', 21),
(346, '2019-03-30 21:01:39.000000', 'support@huzax.com', 'order-update', 21),
(347, '2019-03-30 21:01:39.000000', 'support@huzax.com', 'order-view', 21),
(348, '2019-03-30 21:01:39.000000', 'support@huzax.com', 'order-delete', 21),
(349, '2019-03-30 21:01:39.000000', 'support@huzax.com', 'product-delete', 21),
(350, '2019-03-30 21:01:49.000000', 'support@huzax.com', 'order-create', 17),
(351, '2019-03-30 21:01:49.000000', 'support@huzax.com', 'order-update', 17),
(352, '2019-03-30 21:01:49.000000', 'support@huzax.com', 'order-view', 17),
(353, '2019-03-30 21:01:49.000000', 'support@huzax.com', 'order-delete', 17),
(354, '2019-03-30 21:01:49.000000', 'support@huzax.com', 'product-delete', 17),
(355, '2019-03-30 21:02:04.000000', 'support@huzax.com', 'order-create', 24),
(356, '2019-03-30 21:02:04.000000', 'support@huzax.com', 'order-update', 24),
(357, '2019-03-30 21:02:04.000000', 'support@huzax.com', 'order-view', 24),
(358, '2019-03-30 21:02:04.000000', 'support@huzax.com', 'order-delete', 24),
(359, '2019-03-30 21:02:04.000000', 'support@huzax.com', 'product-delete', 24),
(360, '2019-03-30 21:02:04.000000', 'support@huzax.com', 'product-create', 24),
(361, '2019-03-30 21:02:04.000000', 'support@huzax.com', 'product-update', 24),
(362, '2019-03-30 21:02:04.000000', 'support@huzax.com', 'product-view', 24),
(363, '2019-03-30 21:02:04.000000', 'support@huzax.com', 'inventory-create', 24),
(364, '2019-03-30 21:02:04.000000', 'support@huzax.com', 'inventory-update', 24),
(365, '2019-03-30 21:02:04.000000', 'support@huzax.com', 'inventory-view', 24),
(366, '2019-03-30 21:02:04.000000', 'support@huzax.com', 'inventory-delete', 24),
(367, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'settings-view', 1),
(368, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'log-delete', 1),
(369, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'log-view', 1),
(370, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'dashboard-view', 1),
(371, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'operator-create', 1),
(372, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'operator-update', 1),
(373, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'operator-delete', 1),
(374, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'operator-view', 1),
(375, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'order-create', 1),
(376, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'order-update', 1),
(377, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'order-view', 1),
(378, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'order-delete', 1),
(379, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'product-delete', 1),
(380, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'product-create', 1),
(381, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'product-update', 1),
(382, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'product-view', 1),
(383, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'inventory-create', 1),
(384, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'inventory-update', 1),
(385, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'inventory-view', 1),
(386, '2019-03-30 21:02:11.000000', 'support@huzax.com', 'inventory-delete', 1),
(387, '2019-03-31 00:26:11.000000', 'support@huzax.com', 'order-create', 28),
(388, '2019-03-31 00:26:11.000000', 'support@huzax.com', 'order-update', 28),
(389, '2019-03-31 00:26:11.000000', 'support@huzax.com', 'order-view', 28),
(390, '2019-03-31 00:26:11.000000', 'support@huzax.com', 'order-delete', 28),
(391, '2019-03-31 00:26:11.000000', 'support@huzax.com', 'product-delete', 28);

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
  `order_procurement_method` varchar(255) NOT NULL,
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
  `order_status` varchar(255) NOT NULL,
  `order_supplier_updated_at` datetime(6) NOT NULL,
  `order_supplier_updated_by` varchar(100) NOT NULL,
  `order_supplier_updated_department` varchar(255) NOT NULL,
  `order_supplier_updated_id` varchar(100) NOT NULL,
  `order_supplier_updated_role` varchar(255) NOT NULL,
  `order_email_to_supplier_message` longtext NOT NULL,
  `order_email_to_supplier_subject` varchar(255) NOT NULL,
  `order_email_to_supplier_proposal_submission_url` varchar(255) NOT NULL,
  `order_email_to_supplier_updated_at` datetime(6) NOT NULL,
  `order_email_to_supplier_updated_by` varchar(100) NOT NULL,
  `order_email_to_supplier_updated_department` varchar(255) NOT NULL,
  `order_email_to_supplier_updated_id` varchar(100) NOT NULL,
  `order_email_to_supplier_updated_role` varchar(255) NOT NULL,
  `order_proposal_selected_at` datetime(6) NOT NULL,
  `order_proposal_selected_by` varchar(100) NOT NULL,
  `order_proposal_selected_department` varchar(255) NOT NULL,
  `order_proposal_selected_id` varchar(100) NOT NULL,
  `order_proposal_selected_role` varchar(255) NOT NULL,
  `order_cancelled_at` datetime(6) NOT NULL,
  `order_cancelled_by` varchar(100) NOT NULL,
  `order_cancelled_department` varchar(255) NOT NULL,
  `order_cancelled_id` varchar(100) NOT NULL,
  `order_cancelled_role` varchar(255) NOT NULL,
  `order_acknowledged_at` datetime(6) NOT NULL,
  `order_acknowledged_by` varchar(100) NOT NULL,
  `order_acknowledged_department` varchar(255) NOT NULL,
  `order_acknowledged_id` varchar(100) NOT NULL,
  `order_acknowledged_role` varchar(255) NOT NULL,
  `order_invoice_approval_updated_at` datetime(6) NOT NULL,
  `order_invoice_approval_updated_by` varchar(100) NOT NULL,
  `order_invoice_approval_updated_department` varchar(255) NOT NULL,
  `order_invoice_approval_updated_id` varchar(100) NOT NULL,
  `order_invoice_approval_updated_role` varchar(255) NOT NULL,
  `order_invoice_cop_approval_updated_at` datetime(6) NOT NULL,
  `order_invoice_cop_approval_updated_by` varchar(100) NOT NULL,
  `order_invoice_cop_approval_updated_department` varchar(255) NOT NULL,
  `order_invoice_cop_approval_updated_id` varchar(100) NOT NULL,
  `order_invoice_cop_approval_updated_role` varchar(255) NOT NULL,
  `order_invoice_daf_approval_updated_at` datetime(6) NOT NULL,
  `order_invoice_daf_approval_updated_by` varchar(100) NOT NULL,
  `order_invoice_daf_approval_updated_department` varchar(255) NOT NULL,
  `order_invoice_daf_approval_updated_id` varchar(100) NOT NULL,
  `order_invoice_daf_approval_updated_role` varchar(255) NOT NULL,
  `order_invoice_payment_voucher_uploaded_at` datetime(6) NOT NULL,
  `order_invoice_payment_voucher_uploaded_by` varchar(100) NOT NULL,
  `order_invoice_payment_voucher_uploaded_department` varchar(255) NOT NULL,
  `order_invoice_payment_voucher_uploaded_id` varchar(100) NOT NULL,
  `order_invoice_payment_voucher_uploaded_role` varchar(255) NOT NULL,
  `order_invoice_reviewed_at` datetime(6) NOT NULL,
  `order_invoice_reviewed_by` varchar(100) NOT NULL,
  `order_invoice_reviewed_department` varchar(255) NOT NULL,
  `order_invoice_reviewed_id` varchar(100) NOT NULL,
  `order_invoice_reviewed_role` varchar(255) NOT NULL,
  `order_invoice_uploaded_at` datetime(6) NOT NULL,
  `order_invoice_uploaded_by` varchar(100) NOT NULL,
  `order_invoice_uploaded_department` varchar(255) NOT NULL,
  `order_invoice_uploaded_id` varchar(100) NOT NULL,
  `order_invoice_uploaded_role` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_orders`
--

INSERT INTO `app_orders` (`order_id`, `order_code`, `order_requester_name`, `order_project_name`, `order_project_code`, `order_project_geo_code`, `order_charge_code`, `order_award_number`, `order_requisition_number`, `order_donor`, `order_description`, `order_anticipated_award_mechanism`, `order_anticipated_start_date`, `order_anticipated_end_date`, `order_special_considerations`, `order_procurement_method`, `order_procurement_method_updated_at`, `order_procurement_method_updated_id`, `order_procurement_method_updated_by`, `order_procurement_method_updated_department`, `order_procurement_method_updated_role`, `order_no_of_items`, `order_total_price`, `order_equipment_price`, `order_tax_price`, `order_grand_total_price`, `order_currency`, `order_supplier_category`, `order_proposal_id`, `order_proposal_due_date`, `order_purchase_no`, `order_invoice_no`, `order_created_at`, `order_created_id`, `order_created_by`, `order_created_department`, `order_created_role`, `order_updated_at`, `order_updated_id`, `order_updated_by`, `order_updated_department`, `order_updated_role`, `order_requested_at`, `order_requested_id`, `order_requested_by`, `order_requested_department`, `order_requested_role`, `order_approval_no_of_levels`, `order_reviewed_at`, `order_reviewed_id`, `order_reviewed_by`, `order_reviewed_department`, `order_reviewed_role`, `order_approved_at`, `order_approved_id`, `order_approved_by`, `order_approved_role`, `order_approved_department`, `order_assigned_at`, `order_assigned_id`, `order_assigned_by`, `order_assigned_department`, `order_assigned_role`, `order_assigned_to_at`, `order_assigned_to_by`, `order_assigned_to_id`, `order_assigned_to_department`, `order_assigned_to_role`, `order_proposal_generated_at`, `order_proposal_generated_id`, `order_proposal_generated_by`, `order_proposal_generated_department`, `order_proposal_generated_role`, `order_proposal_requested_at`, `order_proposal_requested_id`, `order_proposal_requested_by`, `order_proposal_requested_department`, `order_proposal_requested_role`, `order_purchase_generated_at`, `order_purchase_generated_id`, `order_purchase_generated_by`, `order_purchase_generated_department`, `order_purchase_generated_role`, `order_paid_at`, `order_paid_id`, `order_paid_by`, `order_paid_department`, `order_paid_role`, `order_closed_at`, `order_closed_id`, `order_closed_by`, `order_closed_department`, `order_closed_role`, `order_status`, `order_supplier_updated_at`, `order_supplier_updated_by`, `order_supplier_updated_department`, `order_supplier_updated_id`, `order_supplier_updated_role`, `order_email_to_supplier_message`, `order_email_to_supplier_subject`, `order_email_to_supplier_proposal_submission_url`, `order_email_to_supplier_updated_at`, `order_email_to_supplier_updated_by`, `order_email_to_supplier_updated_department`, `order_email_to_supplier_updated_id`, `order_email_to_supplier_updated_role`, `order_proposal_selected_at`, `order_proposal_selected_by`, `order_proposal_selected_department`, `order_proposal_selected_id`, `order_proposal_selected_role`, `order_cancelled_at`, `order_cancelled_by`, `order_cancelled_department`, `order_cancelled_id`, `order_cancelled_role`, `order_acknowledged_at`, `order_acknowledged_by`, `order_acknowledged_department`, `order_acknowledged_id`, `order_acknowledged_role`, `order_invoice_approval_updated_at`, `order_invoice_approval_updated_by`, `order_invoice_approval_updated_department`, `order_invoice_approval_updated_id`, `order_invoice_approval_updated_role`, `order_invoice_cop_approval_updated_at`, `order_invoice_cop_approval_updated_by`, `order_invoice_cop_approval_updated_department`, `order_invoice_cop_approval_updated_id`, `order_invoice_cop_approval_updated_role`, `order_invoice_daf_approval_updated_at`, `order_invoice_daf_approval_updated_by`, `order_invoice_daf_approval_updated_department`, `order_invoice_daf_approval_updated_id`, `order_invoice_daf_approval_updated_role`, `order_invoice_payment_voucher_uploaded_at`, `order_invoice_payment_voucher_uploaded_by`, `order_invoice_payment_voucher_uploaded_department`, `order_invoice_payment_voucher_uploaded_id`, `order_invoice_payment_voucher_uploaded_role`, `order_invoice_reviewed_at`, `order_invoice_reviewed_by`, `order_invoice_reviewed_department`, `order_invoice_reviewed_id`, `order_invoice_reviewed_role`, `order_invoice_uploaded_at`, `order_invoice_uploaded_by`, `order_invoice_uploaded_department`, `order_invoice_uploaded_id`, `order_invoice_uploaded_role`) VALUES
(1, '69550384', 'Aaron Gatabazi', 'Feed the Future Rwanda Hinga Weze', 'TBD', '935', 'TBD', 'AID-696-C-17-00001', 'HW/2019-02-0047', 'USAID', 'Request for Fiber optic internet connectivity at HW Head office', 'Service agreement', '2019-04-01', '2019-04-30', 'N/A', 'Single Sourcing', '2019-03-30 22:19:28.000000', '20', 'OPM', 'DAF', 'OPM', 2, 100000, 0, 0, 100000, 'RWF', 'Category 1', 1, '0001-01-01', 'PO - 123456', '0', '2019-03-30 21:11:25.000000', '19', 'Field Officer', 'DCOP', 'Field Officer', '2019-03-30 21:11:25.000000', '19', 'Field Officer', 'DCOP', 'Field Officer', '2019-03-30 22:11:52.000000', '19', 'Field Officer', 'DCOP', 'Field Officer', 4, '2019-03-30 22:20:12.000000', '10', 'Director', 'DAF', 'Director', '2019-03-30 22:20:51.000000', '3', 'COP', 'COP', 'NONE', '2019-03-30 22:21:32.000000', '20', 'OPM', 'DAF', 'OPM', '2019-03-30 22:21:32.000000', 'Procurement Officer', '21', 'DAF', 'Procurement Officer', '2019-03-30 22:24:44.000000', '21', 'Procurement Officer', 'DAF', 'Procurement Officer', '2019-03-30 22:24:44.000000', '21', 'Procurement Officer', 'DAF', 'Procurement Officer', '2019-03-30 22:54:54.000000', '21', 'Procurement Officer', 'DAF', 'Procurement Officer', '0001-01-01 00:00:00.000000', '', '', '', '', '0001-01-01 00:00:00.000000', '', '', '', '', 'acknowledged', '2019-03-30 22:22:01.000000', 'Procurement Officer', 'DAF', '21', 'Procurement Officer', '<p>Dear vendors,</p>\r\n<p>Please submit your proposals within one week.</p>\r\n<p>Link to submit your proposals:&nbsp;<a title="Submit your proposal" href="../../../../order-proposals/create/1/0/" target="_blank" rel="noopener">Submit your proposal</a></p>\r\n<p>&nbsp;</p>\r\n<p>Thank you.</p>\r\n<p>Cultivating New Frontiers in Agriculture (CNFA)</p>', 'Request for proposal', '', '0001-01-01 00:00:00.000000', 'Procurement Officer', 'DAF', '21', 'Procurement Officer', '2019-03-30 22:49:22.000000', 'COP', 'NONE', '3', 'COP', '0001-01-01 00:00:00.000000', '', '', '', '', '2019-03-30 22:56:02.000000', '', '', '', '', '0001-01-01 00:00:00.000000', '', '', '', '', '0001-01-01 00:00:00.000000', '', '', '', '', '0001-01-01 00:00:00.000000', '', '', '', '', '0001-01-01 00:00:00.000000', '', '', '', '', '0001-01-01 00:00:00.000000', '', '', '', '', '0001-01-01 00:00:00.000000', '', '', '', '');

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_order_approvals`
--

INSERT INTO `app_order_approvals` (`order_approval_id`, `orders_order_id`, `order_approval_level`, `order_approval_created_at`, `order_approval_created_id`, `order_approval_created_by`, `order_approval_created_department`, `order_approval_created_role`, `order_approval_updated_at`, `order_approval_updated_id`, `order_approval_updated_by`, `order_approval_updated_department`, `order_approval_updated_role`, `order_approval_status`) VALUES
(1, 1, 1, '2019-03-30 22:11:52.000000', '19', 'Field Officer', 'DCOP', 'Field Officer', '2019-03-30 22:12:28.000000', '18', 'District Manager', 'DCOP', 'District Manager', 'approved'),
(2, 1, 2, '2019-03-30 22:12:28.000000', '18', 'District Manager', 'DCOP', 'District Manager', '2019-03-30 22:12:52.000000', '17', 'Regional Manager', 'DCOP', 'Regional Manager', 'approved'),
(3, 1, 3, '2019-03-30 22:12:52.000000', '17', 'Regional Manager', 'DCOP', 'Regional Manager', '2019-03-30 22:13:28.000000', '7', 'Director', 'DCOP', 'Director', 'approved'),
(4, 1, 4, '2019-03-30 22:13:28.000000', '7', 'Director', 'DCOP', 'Director', '2019-03-30 22:13:28.000000', '20', 'OPM', 'DAF', 'OPM', 'pending');

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
  `order_item_currency` varchar(255) NOT NULL,
  `order_item_duration` int(11) NOT NULL,
  `order_item_usaid_approval` tinyint(1) NOT NULL,
  `order_item_created_at` datetime(6) NOT NULL,
  `order_item_created_id` varchar(100) NOT NULL,
  `order_item_created_by` varchar(100) NOT NULL,
  `order_item_created_department` varchar(255) NOT NULL,
  `order_item_created_role` varchar(255) NOT NULL,
  `order_item_updated_at` datetime(6) NOT NULL,
  `order_item_updated_id` varchar(100) NOT NULL,
  `order_item_updated_by` varchar(100) NOT NULL,
  `order_item_updated_department` varchar(255) NOT NULL,
  `order_item_updated_role` varchar(255) NOT NULL,
  `order_item_received_at` datetime(6) NOT NULL,
  `order_item_received_id` varchar(100) NOT NULL,
  `order_item_received_by` varchar(100) NOT NULL,
  `order_item_received_department` varchar(255) NOT NULL,
  `order_item_received_role` varchar(255) NOT NULL,
  `order_item_status` varchar(255) NOT NULL,
  `order_item_type` varchar(255) NOT NULL,
  `order_item_type_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_order_items`
--

INSERT INTO `app_order_items` (`order_item_id`, `orders_order_id`, `order_item_title`, `order_item_sub_title`, `order_item_quantity_ordered`, `order_item_quantity_unit`, `order_item_unit_price`, `order_item_total_price`, `order_item_currency`, `order_item_duration`, `order_item_usaid_approval`, `order_item_created_at`, `order_item_created_id`, `order_item_created_by`, `order_item_created_department`, `order_item_created_role`, `order_item_updated_at`, `order_item_updated_id`, `order_item_updated_by`, `order_item_updated_department`, `order_item_updated_role`, `order_item_received_at`, `order_item_received_id`, `order_item_received_by`, `order_item_received_department`, `order_item_received_role`, `order_item_status`, `order_item_type`, `order_item_type_id`) VALUES
(1, 1, '3 Door filling cabinet', '', 20, '', 3000, 60000, 'RWF', 0, 1, '2019-03-30 22:05:39.000000', '19', 'Field Officer', 'DCOP', 'Field Officer', '2019-03-30 22:11:07.000000', '19', 'Field Officer', 'DCOP', 'Field Officer', '2019-03-30 22:57:42.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', 'received', 'asset', 1),
(2, 1, 'Round meeting table 150 cmx75cm/Glass Top', '', 20, '', 2000, 40000, 'RWF', 0, 1, '2019-03-30 22:11:36.000000', '19', 'Field Officer', 'DCOP', 'Field Officer', '2019-03-30 22:11:36.000000', '19', 'Field Officer', 'DCOP', 'Field Officer', '2019-03-30 22:57:42.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', 'received', 'asset', 2);

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
  `order_proposal_code` varchar(8) NOT NULL,
  `order_proposal_supplier_category` varchar(255) NOT NULL,
  `order_proposal_supplier_title` varchar(255) NOT NULL,
  `order_proposal_supplier_details` varchar(255) NOT NULL,
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
  `order_proposal_updated_department` varchar(255) NOT NULL,
  `order_proposal_supplier_address_av_no` varchar(255) NOT NULL,
  `order_proposal_supplier_address_country` varchar(255) NOT NULL,
  `order_proposal_supplier_address_district` varchar(255) NOT NULL,
  `order_proposal_supplier_address_plot_no` varchar(255) NOT NULL,
  `order_proposal_supplier_address_sector` varchar(255) NOT NULL,
  `order_proposal_supplier_address_street` varchar(255) NOT NULL,
  `order_proposal_supplier_bank_account_details` varchar(255) NOT NULL,
  `order_proposal_supplier_company_type` varchar(255) NOT NULL,
  `order_proposal_supplier_legal_representatives` varchar(255) NOT NULL,
  `order_proposal_supplier_previous_reference1_contact_email_id` varchar(100) NOT NULL,
  `order_proposal_supplier_previous_reference1_contact_number` varchar(13) NOT NULL,
  `order_proposal_supplier_previous_reference1_contact_person` varchar(255) NOT NULL,
  `order_proposal_supplier_previous_reference1_name` varchar(255) NOT NULL,
  `order_proposal_supplier_previous_reference2_contact_email_id` varchar(100) NOT NULL,
  `order_proposal_supplier_previous_reference2_contact_number` varchar(13) NOT NULL,
  `order_proposal_supplier_previous_reference2_contact_person` varchar(255) NOT NULL,
  `order_proposal_supplier_previous_reference2_name` varchar(255) NOT NULL,
  `order_proposal_supplier_previous_reference3_contact_email_id` varchar(100) NOT NULL,
  `order_proposal_supplier_previous_reference3_contact_number` varchar(13) NOT NULL,
  `order_proposal_supplier_previous_reference3_contact_person` varchar(255) NOT NULL,
  `order_proposal_supplier_previous_reference3_name` varchar(255) NOT NULL,
  `order_proposal_supplier_proposal_title` varchar(255) NOT NULL,
  `order_proposal_supplier_rf_number` varchar(255) NOT NULL,
  `order_proposal_supplier_tin_number` varchar(255) NOT NULL,
  `order_proposal_cost_currency` varchar(255) NOT NULL,
  `order_proposal_selected_at` datetime(6) NOT NULL,
  `order_proposal_selected_by` varchar(100) NOT NULL,
  `order_proposal_selected_department` varchar(255) NOT NULL,
  `order_proposal_selected_id` varchar(100) NOT NULL,
  `order_proposal_selected_role` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_order_proposals`
--

INSERT INTO `app_order_proposals` (`order_proposal_id`, `orders_order_id`, `order_proposal_code`, `order_proposal_supplier_category`, `order_proposal_supplier_title`, `order_proposal_supplier_details`, `order_proposal_supplier_contact_phone_number`, `order_proposal_supplier_contact_email_id`, `order_proposal_cost`, `order_proposal_evaluated_score`, `order_proposal_evaluation_details`, `order_proposal_created_at`, `order_proposal_created_id`, `order_proposal_created_by`, `order_proposal_created_role`, `order_proposal_updated_at`, `order_proposal_updated_id`, `order_proposal_updated_by`, `order_proposal_updated_role`, `order_proposal_evaluated_at`, `order_proposal_evaluated_id`, `order_proposal_evaluated_by`, `order_proposal_evaluated_role`, `order_proposal_approval_updated_at`, `order_proposal_approval_updated_id`, `order_proposal_approval_updated_by`, `order_proposal_approval_updated_role`, `order_proposal_acknowledged_at`, `order_proposal_acknowledged_id`, `order_proposal_acknowledged_by`, `order_proposal_acknowledged_role`, `order_proposal_status`, `order_proposal_acknowledged_department`, `order_proposal_approval_updated_department`, `order_proposal_created_department`, `order_proposal_evaluated_department`, `order_proposal_updated_department`, `order_proposal_supplier_address_av_no`, `order_proposal_supplier_address_country`, `order_proposal_supplier_address_district`, `order_proposal_supplier_address_plot_no`, `order_proposal_supplier_address_sector`, `order_proposal_supplier_address_street`, `order_proposal_supplier_bank_account_details`, `order_proposal_supplier_company_type`, `order_proposal_supplier_legal_representatives`, `order_proposal_supplier_previous_reference1_contact_email_id`, `order_proposal_supplier_previous_reference1_contact_number`, `order_proposal_supplier_previous_reference1_contact_person`, `order_proposal_supplier_previous_reference1_name`, `order_proposal_supplier_previous_reference2_contact_email_id`, `order_proposal_supplier_previous_reference2_contact_number`, `order_proposal_supplier_previous_reference2_contact_person`, `order_proposal_supplier_previous_reference2_name`, `order_proposal_supplier_previous_reference3_contact_email_id`, `order_proposal_supplier_previous_reference3_contact_number`, `order_proposal_supplier_previous_reference3_contact_person`, `order_proposal_supplier_previous_reference3_name`, `order_proposal_supplier_proposal_title`, `order_proposal_supplier_rf_number`, `order_proposal_supplier_tin_number`, `order_proposal_cost_currency`, `order_proposal_selected_at`, `order_proposal_selected_by`, `order_proposal_selected_department`, `order_proposal_selected_id`, `order_proposal_selected_role`) VALUES
(1, 1, '14456092', 'Category 1', 'Navin Nyalapelli', '', '250726875122', 'nyalapellinavin@gmail.com', 100000, 98, 'good', '0001-01-01 00:00:00.000000', '0', '', '', '0001-01-01 00:00:00.000000', '0', '', '', '2019-03-30 22:48:34.000000', '21', 'Procurement Officer', 'Procurement Officer', '2019-03-30 22:48:42.000000', '21', 'Procurement Officer', 'Procurement Officer', '2019-03-30 22:49:39.000000', '', '', '', 'acknowledged', '', 'DAF', '', 'DAF', '', '14', 'Rwanda', 'Kigali', 'KG 369', 'Gacuriro', 'Great Seasons Hotel', '', 'individual', 'Navin Nyalapelli', 'nyalapellinavin@gmail.com', '250726875122', 'Navin Nyalapelli', 'Navin Nyalapelli', '', '', '', '', '', '', '', '', 'Agriculture', 'RFQ - 1234', 'TIN - 123456', 'RWF', '2019-03-30 22:49:22.000000', 'COP', 'NONE', '3', 'COP');

-- --------------------------------------------------------

--
-- Table structure for table `app_products`
--

CREATE TABLE IF NOT EXISTS `app_products` (
  `product_id` int(11) NOT NULL,
  `product_type` varchar(255) NOT NULL,
  `product_code` varchar(8) NOT NULL,
  `product_tag` varchar(255) NOT NULL,
  `product_category` varchar(255) NOT NULL,
  `product_title` varchar(100) NOT NULL,
  `product_sub_title` varchar(255) NOT NULL,
  `product_quantity_available` decimal(10,0) NOT NULL,
  `product_quantity_unit` varchar(255) NOT NULL,
  `product_updated_at` datetime(6) NOT NULL,
  `product_updated_id` varchar(100) NOT NULL,
  `product_updated_by` varchar(100) NOT NULL,
  `product_updated_department` varchar(255) NOT NULL,
  `product_updated_role` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1003 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_products`
--

INSERT INTO `app_products` (`product_id`, `product_type`, `product_code`, `product_tag`, `product_category`, `product_title`, `product_sub_title`, `product_quantity_available`, `product_quantity_unit`, `product_updated_at`, `product_updated_id`, `product_updated_by`, `product_updated_department`, `product_updated_role`) VALUES
(1, 'asset', '50162978', 'HW001', 'Furniture', '3 Door filling cabinet', '', 10, '', '2019-03-30 23:02:51.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin'),
(2, 'asset', '59173245', 'HW002', 'Furniture', 'Round meeting table 150 cmx75cm/Glass Top', '', 15, '', '2019-03-30 23:02:51.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin'),
(3, 'asset', '72269092', 'HW003', 'Furniture', 'Executive office desk', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(4, 'asset', '25092813', 'HW004', 'Furniture', 'Metallic three seat chair (Airport chair) for visitors', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(5, 'asset', '11096453', 'HW005', 'IT Equipment', 'HP Printer desketjet pro 2130', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(6, 'asset', '26410570', 'HW006', 'Furniture', 'Executive Leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(7, 'asset', '56863420', 'HW007', 'Furniture', 'Executive visitor chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(8, 'asset', '85922083', 'HW008', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(9, 'asset', '65097133', 'HW009', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(10, 'asset', '54182710', 'HW010', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(11, 'asset', '55544435', 'HW011', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(12, 'asset', '78561546', 'HW012', 'Furniture', 'Notice Board', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(13, 'asset', '33958001', 'HW013', 'Furniture', 'White Board', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(14, 'asset', '24198182', 'HW014', 'Furniture', 'Coat Hanger', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(15, 'asset', '11926720', 'HW015', 'Furniture', 'High back chair mess chair 7021', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(16, 'asset', '72028274', 'HW016', 'Furniture', 'High Back Fabric Chair-Size: 55*65*110cm @ C114-H (No 12)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(17, 'asset', '44911356', 'HW017', 'Furniture', 'High back chair mess chair 7021', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(18, 'asset', '66955589', 'HW018', 'Furniture', 'Full closed filling cabinet', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(19, 'asset', '14737808', 'HW019', 'Furniture', '04 way workstation with glass partition- square shape as per attached quotation', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(20, 'asset', '60537238', 'HW020', 'Furniture', 'High back chair mess chair 7021', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(21, 'asset', '13940098', 'HW021', 'Furniture', 'Full closed filling cabinet', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(22, 'asset', '17140892', 'HW022', 'Furniture', 'Coat Hanger', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(23, 'asset', '67121566', 'HW023', 'Furniture', 'Conference table 08-10 pers', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(24, 'asset', '87774849', 'HW024', 'Furniture', 'High back chair mess chair 7021', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(25, 'asset', '29267391', 'HW025', 'Furniture', 'Coat Hanger', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(26, 'asset', '28284068', 'HW026', 'Furniture', 'High Back Fabric Chair-Size: 55*65*110cm @ C114-H (No 12)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(27, 'asset', '66048340', 'HW027', 'Furniture', 'ORTHOPADIC CHAIR (N06)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(28, 'asset', '89032296', 'HW028', 'Furniture', '04 way workstation with glass partition- square shape as per attached quotation', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(29, 'asset', '12225428', 'HW029', 'Furniture', 'ORTHOPADIC CHAIR (N06)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(30, 'asset', '99053348', 'HW030', 'Furniture', 'Office Desk + its Fixed drawers', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(31, 'asset', '92191524', 'HW031', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(32, 'asset', '40243172', 'HW032', 'Furniture', 'High Back Fabric Chair-Size: 55*65*110cm @ C114-H (No 12)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(33, 'asset', '11908948', 'HW033', 'Furniture', 'Metallic three seat chair (Airport chair) for visitors', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(34, 'asset', '67733356', 'HW034', 'Furniture', 'High Back Fabric Chair mesh', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(35, 'asset', '11150310', 'HW035', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(36, 'asset', '11259425', 'HW036', 'Furniture', 'Executive Filling cabinet Three doors', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(37, 'asset', '52522412', 'HW037', 'Furniture', 'Coat Hanger', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(38, 'asset', '45884879', 'HW038', 'Furniture', 'Sofa (set for four seats)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(39, 'asset', '85815746', 'HW039', 'Furniture', 'L-Shape Desk', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(40, 'asset', '98747140', 'HW040', 'Furniture', 'L-Shape Desk', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(41, 'asset', '83194203', 'HW041', 'Furniture', 'Executive Leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(42, 'asset', '72356682', 'HW042', 'Furniture', 'Round meeting table', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(43, 'asset', '46143816', 'HW043', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(44, 'asset', '79186446', 'HW044', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(45, 'asset', '94090901', 'HW045', 'Furniture', 'Coat Hanger', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(46, 'asset', '45600238', 'HW046', 'IT Equipment', 'HP LASERJET Pro MFP M 227 fdw', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(47, 'asset', '70154704', 'HW047', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(48, 'asset', '26268210', 'HW048', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(49, 'asset', '17363030', 'HW049', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(50, 'asset', '97227343', 'HW050', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(51, 'asset', '85196206', 'HW051', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(52, 'asset', '81337940', 'HW052', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(53, 'asset', '25323380', 'HW053', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(54, 'asset', '44500425', 'HW054', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(55, 'asset', '88850304', 'HW055', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(56, 'asset', '22409317', 'HW056', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(57, 'asset', '38176908', 'HW057', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(58, 'asset', '56638445', 'HW058', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(59, 'asset', '68232698', 'HW059', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(60, 'asset', '18947752', 'HW060', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(61, 'asset', '20400183', 'HW061', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(62, 'asset', '41706200', 'HW062', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(63, 'asset', '76664846', 'HW063', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(64, 'asset', '99850770', 'HW064', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(65, 'asset', '53679015', 'HW065', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(66, 'asset', '33465205', 'HW066', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(67, 'asset', '70823910', 'HW067', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(68, 'asset', '72880909', 'HW068', 'Furniture', 'High Back Fabric Chair mesh', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(69, 'asset', '59330760', 'HW069', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(70, 'asset', '46939856', 'HW070', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(71, 'asset', '71491726', 'HW071', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(72, 'asset', '93821934', 'HW072', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(73, 'asset', '68544015', 'HW073', 'Furniture', 'Office desk ld 1480', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(74, 'asset', '32775641', 'HW074', 'Furniture', 'Office desk ld 1480', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(75, 'asset', '26806067', 'HW075', 'Furniture', 'Office desk ld 1480', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(76, 'asset', '24387280', 'HW076', 'Furniture', 'Office desk ld 1480', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(77, 'asset', '60475924', 'HW077', 'Furniture', 'Office desk ld 1480', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(78, 'asset', '54114028', 'HW078', 'Furniture', 'Office desk ld 1480', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(79, 'asset', '36242652', 'HW079', 'Furniture', 'Office desk ld 1480', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(80, 'asset', '29537711', 'HW080', 'Furniture', 'Office desk ld 1480', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(81, 'asset', '70584086', 'HW081', 'Furniture', 'Office desk ld 1280', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(82, 'asset', '29510088', 'HW082', 'Furniture', 'Office desk ld 1280', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(83, 'asset', '54504608', 'HW083', 'Furniture', 'Conner connector cnt90ah', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(84, 'asset', '42162353', 'HW084', 'Furniture', 'Conner connector cnt90ah', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(85, 'asset', '11300776', 'HW085', 'Furniture', 'Conner connector cnt90ah', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(86, 'asset', '56985976', 'HW086', 'Furniture', 'Conner connector cnt90ah', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(87, 'asset', '91441838', 'HW087', 'Office Equipment', 'Projectors Sony VPL DX 220', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(88, 'asset', '69158186', 'HW088', 'Furniture', 'Notice Board', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(89, 'asset', '34772451', 'HW089', 'Furniture', 'White Board', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(90, 'asset', '46398962', 'HW090', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(91, 'asset', '97224450', 'HW091', 'Office Equipment', 'Water Dispensor', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(92, 'asset', '63069134', 'HW092', 'Furniture', 'Executive coffee table', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(93, 'asset', '19579098', 'HW093', 'Furniture', 'ORTHOPADIC CHAIR (N06)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(94, 'asset', '36669491', 'HW094', 'Furniture', 'Coat Hanger', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(95, 'asset', '18455807', 'HW095', 'Furniture', 'L-Shape Desk', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(96, 'asset', '23188946', 'HW096', 'Furniture', '04 way workstation with glass partition- square shape as per attached quotation', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(97, 'asset', '45721852', 'HW097', 'Furniture', 'High Back Fabric Chair-Size: 55*65*110cm @ C114-H (No 12)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(98, 'asset', '73029742', 'HW098', 'Furniture', 'ORTHOPADIC CHAIR (N06)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(99, 'asset', '70962425', 'HW099', 'Furniture', 'ORTHOPADIC CHAIR (N06)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(100, 'asset', '37391710', 'HW100', 'Furniture', 'Full closed filling cabinet', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(101, 'asset', '43268062', 'HW101', 'Furniture', 'L-Shape Desk', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(102, 'asset', '15835468', 'HW102', 'Furniture', 'High Back Fabric Chair mesh', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(103, 'asset', '64442818', 'HW103', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(104, 'asset', '99545572', 'HW104', 'Furniture', 'Full closed filling cabinet', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(105, 'asset', '68743198', 'HW105', 'Furniture', 'Coat Hanger', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(106, 'asset', '10197763', 'HW106', 'Furniture', 'Office Desk + its Fixed drawers', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(107, 'asset', '86203729', 'HW107', 'Furniture', 'Office Desk + its Fixed drawers', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(108, 'asset', '43156745', 'HW108', 'Furniture', 'High Back Fabric Chair mesh', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(109, 'asset', '82617236', 'HW109', 'Furniture', 'Standard Table With 3 Fixed Drawer 1600W x 7500 x 750H Beech @STL-OT16075', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(110, 'asset', '27901919', 'HW110', 'Furniture', 'Office desk 1400 with fixed drwawers', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(111, 'asset', '42487202', 'HW111', 'Furniture', 'High Back Fabric Chair-Size: 55*65*110cm @ C114-H (No 12)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(112, 'asset', '46500405', 'HW112', 'Furniture', 'Office Desk + its Fixed drawers', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(113, 'asset', '77419799', 'HW113', 'Furniture', 'Office Desk + its Fixed drawers', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(114, 'asset', '98473334', 'HW114', 'Furniture', 'High Back Fabric Chair-Size: 55*65*110cm @ C114-H (No 12)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(115, 'asset', '20404304', 'HW115', 'Furniture', 'Executive Leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(116, 'asset', '75506550', 'HW116', 'Furniture', 'Standard Table With 3 Fixed Drawer 1600W x 7500 x 750H Beech @STL-OT16075', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(117, 'asset', '90495651', 'HW117', 'Furniture', '4 Drawers filling cabinet', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(118, 'asset', '91410312', 'HW118', 'Furniture', 'Full closed filling cabinet', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(119, 'asset', '82837102', 'HW119', 'Furniture', 'Coat Hanger', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(120, 'asset', '52447281', 'HW120', 'IT Equipment', 'HP LASERJET Pro MFP M 227 fdw', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(121, 'asset', '50051323', 'HW121', 'Furniture', 'Metallic three seat chair (Airport chair) for visitors', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(122, 'asset', '62131844', 'HW122', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(123, 'asset', '83542106', 'HW123', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(124, 'asset', '45256975', 'HW124', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(125, 'asset', '24714630', 'HW125', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(126, 'asset', '83548734', 'HW126', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(127, 'asset', '63010776', 'HW127', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(128, 'asset', '88014549', 'HW128', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(129, 'asset', '44995696', 'HW129', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(130, 'asset', '98690942', 'HW130', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(131, 'asset', '58251261', 'HW131', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(132, 'asset', '81922241', 'HW132', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(133, 'asset', '42609467', 'HW133', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(134, 'asset', '12597414', 'HW134', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(135, 'asset', '96741895', 'HW135', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(136, 'asset', '97509723', 'HW136', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(137, 'asset', '46685294', 'HW137', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(138, 'asset', '83237103', 'HW138', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(139, 'asset', '71419873', 'HW139', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(140, 'asset', '77114858', 'HW140', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(141, 'asset', '74122582', 'HW141', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(142, 'asset', '36895612', 'HW142', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(143, 'asset', '56593349', 'HW143', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(144, 'asset', '26534395', 'HW144', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(145, 'asset', '99604120', 'HW145', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(146, 'asset', '12585190', 'HW146', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(147, 'asset', '97110298', 'HW147', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(148, 'asset', '22039193', 'HW148', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(149, 'asset', '80398952', 'HW149', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(150, 'asset', '37240036', 'HW150', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(151, 'asset', '81090827', 'HW151', 'IT Equipment', 'HPLaptop Elitebook 840 i5', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(152, 'asset', '56511698', 'HW152', 'Furniture', 'Reception desk including side attachment and Counter top', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(153, 'asset', '61956450', 'HW153', 'Furniture', 'High Back Fabric Chair mesh', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(154, 'asset', '26780731', 'HW154', 'Furniture', 'Full closed filling cabinet', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(155, 'asset', '13543994', 'HW155', 'IT Equipment', 'HP Printer officejet 7510', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(156, 'asset', '25920310', 'HW156', 'IT Equipment', 'HP LASERJET Pro MFP M 227 fdw', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(157, 'asset', '19315662', 'HW157', 'Office Equipment', 'Binding Machine', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(158, 'asset', '80413989', 'HW158', 'Office Equipment', 'Paper Cutter', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(159, 'asset', '11001873', 'HW159', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(160, 'asset', '37000353', 'HW160', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(161, 'asset', '22349013', 'HW161', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(162, 'asset', '10797540', 'HW162', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(163, 'asset', '68231970', 'HW163', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(164, 'asset', '36615255', 'HW164', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(165, 'asset', '90721704', 'HW165', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(166, 'asset', '78292056', 'HW166', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(167, 'asset', '77083546', 'HW167', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(168, 'asset', '37720148', 'HW168', 'Furniture', 'Office Desk + its Fixed drawers', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(169, 'asset', '61288116', 'HW169', 'Kitchen Materials', 'Coffee maker (Expresso)', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(170, 'asset', '20902294', 'HW170', 'Kitchen Materials', 'Kettle', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(171, 'asset', '89619983', 'HW171', 'Kitchen Materials', 'Gas stove', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(172, 'asset', '99932094', 'HW172', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(173, 'asset', '88125189', 'HW173', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(174, 'asset', '60091761', 'HW174', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:16.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(175, 'asset', '48651681', 'HW175', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(176, 'asset', '23062219', 'HW176', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(177, 'asset', '54271437', 'HW177', 'Furniture', 'Cantiliver leather chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(178, 'asset', '40240177', 'HW178', 'Office Equipment', 'Projectors Sony VPL DX 221', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(179, 'asset', '50154030', 'HW179', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(180, 'asset', '55575228', 'HW180', 'Office Equipment', 'Canon Camera SX 420 IS', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(181, 'asset', '67704991', 'HW181', 'Office Equipment', 'Canon Camera SX 420 IS', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(182, 'asset', '58435056', 'HW182', 'Office Equipment', 'Canon Camera SX 420 IS', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(183, 'asset', '99480262', 'HW183', 'Office Equipment', 'Canon Camera SX 420 IS', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(184, 'asset', '34836919', 'HW184', 'Office Equipment', 'Canon Camera SX 420 IS', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(185, 'asset', '10253073', 'HW185', 'IT Equipment', 'HP LASERJET Pro MFP M 227 fdw', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(186, 'asset', '38656540', 'HW186', 'IT Equipment', 'Access Point Linksys N300', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(187, 'asset', '74787832', 'HW187', 'IT Equipment', 'Access Point Linksys N301', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(188, 'asset', '13890704', 'HW188', 'IT Equipment', 'Access Point Linksys N302', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(189, 'asset', '36778066', 'HW189', 'IT Equipment', 'Access Point Linksys N304', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(190, 'asset', '20770197', 'HW190', 'IT Equipment', 'Unifi APL', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(191, 'asset', '48670641', 'HW191', 'IT Equipment', 'Linksysys AC 1900', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(192, 'asset', '81635996', 'HW192', 'IT Equipment', 'Access Point Linksys N303', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(193, 'asset', '34337644', 'HW193', 'IT Equipment', 'Canon Camera SX 420 IS', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(194, 'asset', '93998041', 'HW194', 'Office Equipment', 'Canon Camera SX 420 IS', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(195, 'asset', '84529466', 'HW195', 'Office Equipment', 'Canon Camera SX 420 IS', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(196, 'asset', '46088143', 'HW196', 'Office Equipment', 'Canon Camera SX 420 IS', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(197, 'asset', '26139842', 'HW197', 'Office Equipment', 'Canon Camera SX 420 IS', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(198, 'asset', '29027059', 'HW198', 'IT Equipment', 'Hp Deskejt 2130', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(199, 'asset', '10406685', 'HW199', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(200, 'asset', '48835139', 'HW200', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(201, 'asset', '50819303', 'HW201', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(202, 'asset', '85482468', 'HW202', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(203, 'asset', '39454568', 'HW203', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(204, 'asset', '97623135', 'HW204', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(205, 'asset', '22928751', 'HW205', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(206, 'asset', '40896389', 'HW206', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(207, 'asset', '45646946', 'HW207', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(208, 'asset', '90163004', 'HW208', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(209, 'asset', '52581366', 'HW209', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(210, 'asset', '41443939', 'HW210', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(211, 'asset', '41336175', 'HW211', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(212, 'asset', '96550771', 'HW212', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(213, 'asset', '39889136', 'HW213', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(214, 'asset', '87815150', 'HW214', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(215, 'asset', '85790859', 'HW215', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(216, 'asset', '20209350', 'HW216', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(217, 'asset', '28329557', 'HW217', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(218, 'asset', '13840781', 'HW218', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(219, 'asset', '33568926', 'HW219', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(220, 'asset', '79305434', 'HW220', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(221, 'asset', '92651521', 'HW221', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(222, 'asset', '79511997', 'HW222', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(223, 'asset', '48955446', 'HW223', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(224, 'asset', '17580353', 'HW224', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(225, 'asset', '85845648', 'HW225', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(226, 'asset', '77302573', 'HW226', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(227, 'asset', '17052341', 'HW227', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(228, 'asset', '19423181', 'HW228', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(229, 'asset', '20801181', 'HW229', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(230, 'asset', '10075190', 'HW230', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(231, 'asset', '58744757', 'HW231', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(232, 'asset', '27468420', 'HW232', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(233, 'asset', '25111600', 'HW233', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(234, 'asset', '39717411', 'HW234', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(235, 'asset', '22433204', 'HW235', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(236, 'asset', '22272990', 'HW236', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(237, 'asset', '32301012', 'HW237', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(238, 'asset', '33287702', 'HW238', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(239, 'asset', '34700369', 'HW239', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(240, 'asset', '98227861', 'HW240', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(241, 'asset', '76290513', 'HW241', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(242, 'asset', '26156016', 'HW242', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(243, 'asset', '94390216', 'HW243', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(244, 'asset', '78271804', 'HW244', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(245, 'asset', '30031548', 'HW245', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(246, 'asset', '87209142', 'HW246', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(247, 'asset', '94794765', 'HW247', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(248, 'asset', '49848314', 'HW248', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(249, 'asset', '76548030', 'HW249', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(250, 'asset', '29539756', 'HW250', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(251, 'asset', '40477971', 'HW251', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(252, 'asset', '24845547', 'HW252', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(253, 'asset', '19728471', 'HW253', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(254, 'asset', '60054883', 'HW254', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(255, 'asset', '57504203', 'HW255', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(256, 'asset', '67313120', 'HW256', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(257, 'asset', '28850960', 'HW257', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(258, 'asset', '55411068', 'HW258', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(259, 'asset', '45675016', 'HW259', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(260, 'asset', '64890715', 'HW260', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(261, 'asset', '83148878', 'HW261', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(262, 'asset', '49551138', 'HW262', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(263, 'asset', '81992106', 'HW263', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(264, 'asset', '20850818', 'HW264', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(265, 'asset', '80586702', 'HW265', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(266, 'asset', '18073849', 'HW266', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(267, 'asset', '13676863', 'HW267', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(268, 'asset', '85457871', 'HW268', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(269, 'asset', '72722887', 'HW269', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(270, 'asset', '83407218', 'HW270', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(271, 'asset', '32733224', 'HW271', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(272, 'asset', '91910109', 'HW272', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(273, 'asset', '30179842', 'HW273', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(274, 'asset', '15578161', 'HW274', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(275, 'asset', '92111608', 'HW275', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(276, 'asset', '54601447', 'HW276', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(277, 'asset', '14127980', 'HW277', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(278, 'asset', '26609597', 'HW278', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(279, 'asset', '57570240', 'HW279', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(280, 'asset', '79935084', 'HW280', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(281, 'asset', '20881384', 'HW281', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(282, 'asset', '76505699', 'HW282', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(283, 'asset', '53878380', 'HW283', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(284, 'asset', '52943440', 'HW284', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(285, 'asset', '66035756', 'HW285', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(286, 'asset', '33719723', 'HW286', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(287, 'asset', '76963580', 'HW287', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(288, 'asset', '38292072', 'HW288', 'IT Equipment', 'MTN Modem', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(289, 'asset', '70473479', 'HW289', 'Office Equipment', 'Screen Projector', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(290, 'asset', '40046923', 'HW290', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(291, 'asset', '41080649', 'HW291', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(292, 'asset', '80461753', 'HW292', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(293, 'asset', '61647553', 'HW293', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(294, 'asset', '48536133', 'HW294', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(295, 'asset', '78792156', 'HW295', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(296, 'asset', '73097025', 'HW296', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(297, 'asset', '24448003', 'HW297', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(298, 'asset', '95403555', 'HW298', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(299, 'asset', '66558477', 'HW299', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(300, 'asset', '58858023', 'HW300', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(301, 'asset', '36747509', 'HW301', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(302, 'asset', '11159438', 'HW302', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(303, 'asset', '75702527', 'HW303', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(304, 'asset', '55357143', 'HW304', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(305, 'asset', '34386245', 'HW305', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(306, 'asset', '76466949', 'HW306', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(307, 'asset', '46291305', 'HW307', 'IT Equipment', 'HP Laptop 250 I3', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(308, 'asset', '36241603', 'HW308', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(309, 'asset', '34094455', 'HW309', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(310, 'asset', '50690418', 'HW310', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(311, 'asset', '21462958', 'HW311', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(312, 'asset', '75951618', 'HW312', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(313, 'asset', '49828713', 'HW313', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(314, 'asset', '67469694', 'HW314', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(315, 'asset', '11490554', 'HW315', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(316, 'asset', '15481542', 'HW316', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(317, 'asset', '72801928', 'HW317', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE');
INSERT INTO `app_products` (`product_id`, `product_type`, `product_code`, `product_tag`, `product_category`, `product_title`, `product_sub_title`, `product_quantity_available`, `product_quantity_unit`, `product_updated_at`, `product_updated_id`, `product_updated_by`, `product_updated_department`, `product_updated_role`) VALUES
(318, 'asset', '64159899', 'HW318', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(319, 'asset', '56839574', 'HW319', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(320, 'asset', '97277481', 'HW320', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(321, 'asset', '74504518', 'HW321', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(322, 'asset', '95192848', 'HW322', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(323, 'asset', '19033614', 'HW323', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(324, 'asset', '33734249', 'HW324', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(325, 'asset', '94251292', 'HW325', 'Furniture', 'Office desk/L-shape/Size :120x120x75,Lockable 3 Drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(326, 'asset', '51697741', 'HW326', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(327, 'asset', '99880442', 'HW327', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(328, 'asset', '99382579', 'HW328', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(329, 'asset', '49407908', 'HW329', 'Furniture', 'Three seat chair or airport chair /seater for three peaple ,Seat width:45c;metallic', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(330, 'asset', '14769072', 'HW330', 'Furniture', 'Reception Table with Top Encounter', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(331, 'asset', '99744336', 'HW331', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(332, 'asset', '51428031', 'HW332', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(333, 'asset', '96506304', 'HW333', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(334, 'asset', '59272068', 'HW334', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(335, 'asset', '43906249', 'HW335', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(336, 'asset', '38537611', 'HW336', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(337, 'asset', '56789690', 'HW337', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(338, 'asset', '38456825', 'HW338', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(339, 'asset', '82892014', 'HW339', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(340, 'asset', '58880408', 'HW340', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(341, 'asset', '87601817', 'HW341', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(342, 'asset', '10626037', 'HW342', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(343, 'asset', '24193653', 'HW343', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(344, 'asset', '23748295', 'HW344', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(345, 'asset', '39749739', 'HW345', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(346, 'asset', '97785227', 'HW346', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(347, 'asset', '94185304', 'HW347', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(348, 'asset', '44347601', 'HW348', 'Furniture', 'Office desk/L-shape/Size :120x120x75,Lockable 3 Drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(349, 'asset', '65845742', 'HW349', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(350, 'asset', '21275408', 'HW350', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(351, 'asset', '58300748', 'HW351', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(352, 'asset', '13914773', 'HW352', 'Furniture', 'Three seat chair or airport chair /seater for three peaple ,Seat width:45c;metallic', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(353, 'asset', '49720746', 'HW353', 'Furniture', 'Reception Table with Top Encounter', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(354, 'asset', '21465172', 'HW354', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(355, 'asset', '11498118', 'HW355', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(356, 'asset', '15441049', 'HW356', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(357, 'asset', '48008771', 'HW357', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(358, 'asset', '23891429', 'HW358', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(359, 'asset', '53489141', 'HW359', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(360, 'asset', '75657696', 'HW360', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(361, 'asset', '14548952', 'HW361', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(362, 'asset', '42686278', 'HW362', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(363, 'asset', '39818956', 'HW363', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(364, 'asset', '66382327', 'HW364', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(365, 'asset', '24507079', 'HW365', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(366, 'asset', '44821870', 'HW366', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(367, 'asset', '36526184', 'HW367', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(368, 'asset', '87624472', 'HW368', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(369, 'asset', '58226115', 'HW369', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(370, 'asset', '35532777', 'HW370', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(371, 'asset', '65739767', 'HW371', 'Furniture', 'Office desk/L-shape/Size :120x120x75,Lockable 3 Drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(372, 'asset', '26037421', 'HW372', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(373, 'asset', '25320661', 'HW373', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(374, 'asset', '16409590', 'HW374', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(375, 'asset', '27806430', 'HW375', 'Furniture', 'Three seat chair or airport chair /seater for three peaple ,Seat width:45c;metallic', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(376, 'asset', '11493630', 'HW376', 'Furniture', 'Reception Table with Top Encounter', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(377, 'asset', '11256398', 'HW377', 'Furniture', 'Office desk 140x75x75_three drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(378, 'asset', '19564115', 'HW378', 'Furniture', 'Office desk 140x75x75_three drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(379, 'asset', '82743201', 'HW379', 'Furniture', 'Office desk 140x75x75_three drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(380, 'asset', '31684451', 'HW380', 'Furniture', 'Office desk 140x75x75_three drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(381, 'asset', '88135471', 'HW381', 'Furniture', 'Office desk 140x75x75_three drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(382, 'asset', '91624545', 'HW382', 'Furniture', 'Office desk 140x75x75_three drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(383, 'asset', '43833624', 'HW383', 'Furniture', 'Office desk 140x75x75_three drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(384, 'asset', '28425690', 'HW384', 'Furniture', 'Office desk 140x75x75_three drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(385, 'asset', '60586481', 'HW385', 'Furniture', 'Office desk 140x75x75_three drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(386, 'asset', '63404943', 'HW386', 'Furniture', 'Medium Back Mesh Chair or Medium Office Chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(387, 'asset', '48198559', 'HW387', 'Furniture', 'Medium Back Mesh Chair or Medium Office Chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(388, 'asset', '12768615', 'HW388', 'Furniture', 'Medium Back Mesh Chair or Medium Office Chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(389, 'asset', '33804902', 'HW389', 'Furniture', 'Medium Back Mesh Chair or Medium Office Chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(390, 'asset', '87707042', 'HW390', 'Furniture', 'Medium Back Mesh Chair or Medium Office Chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(391, 'asset', '70042576', 'HW391', 'Furniture', 'Medium Back Mesh Chair or Medium Office Chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(392, 'asset', '58902300', 'HW392', 'Furniture', 'Medium Back Mesh Chair or Medium Office Chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(393, 'asset', '56605541', 'HW393', 'Furniture', 'Medium Back Mesh Chair or Medium Office Chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(394, 'asset', '93243240', 'HW394', 'Furniture', 'Medium Back Mesh Chair or Medium Office Chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(395, 'asset', '21056583', 'HW395', 'Furniture', 'Medium Back Mesh Chair or Medium Office Chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(396, 'asset', '30547726', 'HW396', 'Furniture', 'Medium Back Mesh Chair or Medium Office Chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(397, 'asset', '95055351', 'HW397', 'Furniture', 'Medium Back Mesh Chair or Medium Office Chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(398, 'asset', '39153836', 'HW398', 'Furniture', 'Full closed filling cabinet', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(399, 'asset', '71834739', 'HW399', 'Furniture', 'Full closed filling cabinet', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(400, 'asset', '37533998', 'HW400', 'Furniture', 'Full closed filling cabinet', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(401, 'asset', '73648297', 'HW401', 'Furniture', 'Full closed filling cabinet', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(402, 'asset', '27133942', 'HW402', 'Furniture', 'Three seat chair (three seats waiting chairs)', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(403, 'asset', '67209745', 'HW403', 'Furniture', 'Three seat chair (three seats waiting chairs)', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(404, 'asset', '53384431', 'HW404', 'Furniture', 'Reception desk', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(405, 'asset', '54082222', 'HW405', 'Furniture', 'Office Table-140x120x125', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(406, 'asset', '70417286', 'HW406', 'Furniture', 'Office Table-140x120x126', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(407, 'asset', '71147254', 'HW407', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(408, 'asset', '99077011', 'HW408', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(409, 'asset', '77490888', 'HW409', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(410, 'asset', '40854323', 'HW410', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(411, 'asset', '77776871', 'HW411', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(412, 'asset', '81756555', 'HW412', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(413, 'asset', '49951785', 'HW413', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(414, 'asset', '92886804', 'HW414', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(415, 'asset', '59500658', 'HW415', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(416, 'asset', '22584709', 'HW416', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(417, 'asset', '18052803', 'HW417', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(418, 'asset', '11177990', 'HW418', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(419, 'asset', '31071669', 'HW419', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(420, 'asset', '52452042', 'HW420', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(421, 'asset', '65662047', 'HW421', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(422, 'asset', '34496400', 'HW422', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(423, 'asset', '63890067', 'HW423', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(424, 'asset', '38227464', 'HW424', 'Furniture', 'Office desk/L-shape/Size :120x120x75,Lockable 3 Drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(425, 'asset', '47270452', 'HW425', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(426, 'asset', '87337913', 'HW426', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(427, 'asset', '91689919', 'HW427', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(428, 'asset', '37571994', 'HW428', 'Furniture', 'Three seat chair or airport chair /seater for three peaple ,Seat width:45c;metallic', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(429, 'asset', '15340053', 'HW429', 'Furniture', 'Reception Table with Top Encounter', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(430, 'asset', '36998068', 'HW430', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(431, 'asset', '23508123', 'HW431', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(432, 'asset', '40372023', 'HW432', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(433, 'asset', '22096590', 'HW433', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(434, 'asset', '44373089', 'HW434', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(435, 'asset', '15021344', 'HW435', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(436, 'asset', '36712843', 'HW436', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(437, 'asset', '12137351', 'HW437', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(438, 'asset', '49062610', 'HW438', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(439, 'asset', '66089346', 'HW439', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(440, 'asset', '44693530', 'HW440', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(441, 'asset', '47203564', 'HW441', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(442, 'asset', '26724595', 'HW442', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(443, 'asset', '47494291', 'HW443', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(444, 'asset', '57465587', 'HW444', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(445, 'asset', '17947168', 'HW445', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(446, 'asset', '15230749', 'HW446', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(447, 'asset', '35290841', 'HW447', 'Furniture', 'Office desk/L-shape/Size :120x120x75,Lockable 3 Drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(448, 'asset', '82005273', 'HW448', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(449, 'asset', '76504567', 'HW449', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(450, 'asset', '39569043', 'HW450', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(451, 'asset', '47138511', 'HW451', 'Furniture', 'Three seat chair or airport chair /seater for three peaple ,Seat width:45c;metallic', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(452, 'asset', '73363050', 'HW452', 'Furniture', 'Reception Table with Top Encounter', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(453, 'asset', '71745886', 'HW453', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(454, 'asset', '97310519', 'HW454', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(455, 'asset', '62844506', 'HW455', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(456, 'asset', '36350736', 'HW456', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(457, 'asset', '85027073', 'HW457', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:17.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(458, 'asset', '34151861', 'HW458', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(459, 'asset', '90306301', 'HW459', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(460, 'asset', '84293898', 'HW460', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(461, 'asset', '25563647', 'HW461', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(462, 'asset', '24237881', 'HW462', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(463, 'asset', '18407024', 'HW463', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(464, 'asset', '65616988', 'HW464', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(465, 'asset', '73308329', 'HW465', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(466, 'asset', '87769497', 'HW466', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(467, 'asset', '25602213', 'HW467', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(468, 'asset', '70246303', 'HW468', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(469, 'asset', '33052061', 'HW469', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(470, 'asset', '29630167', 'HW470', 'Furniture', 'Office desk/L-shape/Size :120x120x75,Lockable 3 Drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(471, 'asset', '34812317', 'HW471', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(472, 'asset', '68399461', 'HW472', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(473, 'asset', '25049469', 'HW473', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(474, 'asset', '24685003', 'HW474', 'Furniture', 'Three seat chair or airport chair /seater for three peaple ,Seat width:45c;metallic', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(475, 'asset', '94609717', 'HW475', 'Furniture', 'Reception Table with Top Encounter', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(476, 'asset', '93917689', 'HW476', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(477, 'asset', '48039930', 'HW477', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(478, 'asset', '19852270', 'HW478', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(479, 'asset', '98990837', 'HW479', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(480, 'asset', '38046198', 'HW480', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(481, 'asset', '69491650', 'HW481', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(482, 'asset', '15817263', 'HW482', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(483, 'asset', '47478546', 'HW483', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(484, 'asset', '12906975', 'HW484', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(485, 'asset', '42371478', 'HW485', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(486, 'asset', '92903890', 'HW486', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(487, 'asset', '68187178', 'HW487', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(488, 'asset', '90225412', 'HW488', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(489, 'asset', '36689201', 'HW489', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(490, 'asset', '61297648', 'HW490', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(491, 'asset', '37867547', 'HW491', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(492, 'asset', '48705040', 'HW492', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(493, 'asset', '75622828', 'HW493', 'Furniture', 'Office desk/L-shape/Size :120x120x75,Lockable 3 Drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(494, 'asset', '88363223', 'HW494', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(495, 'asset', '97690253', 'HW495', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(496, 'asset', '28408766', 'HW496', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(497, 'asset', '56206624', 'HW497', 'Furniture', 'Three seat chair or airport chair /seater for three peaple ,Seat width:45c;metallic', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(498, 'asset', '28977285', 'HW498', 'Furniture', 'Reception Table with Top Encounter', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(499, 'asset', '56577361', 'HW499', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(500, 'asset', '55608212', 'HW500', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(501, 'asset', '28041880', 'HW501', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(502, 'asset', '69883437', 'HW502', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(503, 'asset', '79875697', 'HW503', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(504, 'asset', '15000447', 'HW504', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(505, 'asset', '18434877', 'HW505', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(506, 'asset', '42697600', 'HW506', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(507, 'asset', '10161292', 'HW507', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(508, 'asset', '98982028', 'HW508', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(509, 'asset', '36452919', 'HW509', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(510, 'asset', '48143419', 'HW510', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(511, 'asset', '27191887', 'HW511', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(512, 'asset', '75893377', 'HW512', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(513, 'asset', '75956099', 'HW513', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(514, 'asset', '35861715', 'HW514', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(515, 'asset', '47096103', 'HW515', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(516, 'asset', '84916270', 'HW516', 'Furniture', 'Office desk/L-shape/Size :120x120x75,Lockable 3 Drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(517, 'asset', '54195929', 'HW517', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(518, 'asset', '87866508', 'HW518', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(519, 'asset', '28685942', 'HW519', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(520, 'asset', '99757318', 'HW520', 'Furniture', 'Three seat chair or airport chair /seater for three peaple ,Seat width:45c;metallic', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(521, 'asset', '95973830', 'HW521', 'Furniture', 'Reception Table with Top Encounter', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(522, 'asset', '70167188', 'HW522', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(523, 'asset', '79657260', 'HW523', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(524, 'asset', '38877355', 'HW524', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(525, 'asset', '37933040', 'HW525', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(526, 'asset', '98036680', 'HW526', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(527, 'asset', '22693651', 'HW527', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(528, 'asset', '10671308', 'HW528', 'Furniture', 'Office Desk 140x75x75_One unit drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(529, 'asset', '74742420', 'HW529', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(530, 'asset', '28290288', 'HW530', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(531, 'asset', '43459515', 'HW531', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(532, 'asset', '52459625', 'HW532', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(533, 'asset', '18301201', 'HW533', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(534, 'asset', '49599352', 'HW534', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(535, 'asset', '34250606', 'HW535', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(536, 'asset', '43985648', 'HW536', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(537, 'asset', '44528003', 'HW537', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(538, 'asset', '28200454', 'HW538', 'Furniture', 'Stacking Chair/or Vistor chair', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(539, 'asset', '40192488', 'HW539', 'Furniture', 'Office desk/L-shape/Size :120x120x75,Lockable 3 Drawers', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(540, 'asset', '43831752', 'HW540', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(541, 'asset', '29289656', 'HW541', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(542, 'asset', '28393112', 'HW542', 'Furniture', 'Full Closed filling cabinet/180X80X40 cm Size Beech Color, 2 Doors,', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(543, 'asset', '66868539', 'HW543', 'Furniture', 'Three seat chair or airport chair /seater for three peaple ,Seat width:45c;metallic', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(544, 'asset', '59549210', 'HW544', 'Furniture', 'Reception Table with Top Encounter', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(545, 'asset', '60954419', 'HW545', 'IT Equipment', 'Copier Canon Imagerunner 2204', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(546, 'asset', '66347312', 'HW546', 'IT Equipment', 'Copier Canon Imagerunner 2204', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(547, 'asset', '48293529', 'HW547', 'IT Equipment', 'Copier Canon Imagerunner 2204', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(548, 'asset', '77978577', 'HW548', 'IT Equipment', 'Copier Canon Imagerunner 2204', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(549, 'asset', '98713031', 'HW549', 'IT Equipment', 'Copier Canon Imagerunner 2204', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(550, 'asset', '51339468', 'HW550', 'IT Equipment', 'Copier Canon Imagerunner 2204', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(551, 'asset', '93976362', 'HW551', 'IT Equipment', 'Copier Canon Imagerunner 2204', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(552, 'asset', '64473888', 'HW552', 'IT Equipment', 'Copier Canon Imagerunner 2204', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(553, 'asset', '16451153', 'HW553', 'IT Equipment', 'Copier Canon Imagerunner 2204', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(554, 'asset', '15809830', 'HW554', 'IT Equipment', 'Copier Canon Imagerunner 2204', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(555, 'asset', '47410288', 'HW555', 'Office Equipment', 'Stabilizer', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(556, 'asset', '18065718', 'HW556', 'Office Equipment', 'Stabilizer', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(557, 'asset', '55692653', 'HW557', 'Office Equipment', 'Stabilizer', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(558, 'asset', '53319132', 'HW558', 'Office Equipment', 'Stabilizer', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(559, 'asset', '52031317', 'HW559', 'Office Equipment', 'Stabilizer', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(560, 'asset', '60056520', 'HW560', 'Office Equipment', 'Stabilizer', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(561, 'asset', '71248466', 'HW561', 'Office Equipment', 'Stabilizer', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(562, 'asset', '86865840', 'HW562', 'Office Equipment', 'Stabilizer', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(563, 'asset', '59728785', 'HW563', 'Office Equipment', 'Stabilizer', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(564, 'asset', '79398509', 'HW564', 'Office Equipment', 'Stabilizer', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(565, 'asset', '61153026', 'HW565', 'Office Equipment', 'Water dispensor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(566, 'asset', '85230566', 'HW566', 'Office Equipment', 'Water dispensor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(567, 'asset', '55154196', 'HW567', 'Office Equipment', 'Water dispensor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(568, 'asset', '57796673', 'HW568', 'Office Equipment', 'Water dispensor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(569, 'asset', '85159039', 'HW569', 'Office Equipment', 'Water dispensor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(570, 'asset', '77936725', 'HW570', 'Office Equipment', 'Water dispensor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(571, 'asset', '20307720', 'HW571', 'Office Equipment', 'Water dispensor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(572, 'asset', '48022357', 'HW572', 'Office Equipment', 'Water dispensor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(573, 'asset', '16991546', 'HW573', 'Office Equipment', 'Water dispensor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(574, 'asset', '78527523', 'HW574', 'Office Equipment', 'Water dispensor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(575, 'asset', '67141561', 'HW575', 'Office Equipment', 'Water dispensor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(576, 'asset', '71460260', 'HW576', 'Office Equipment', 'Water dispensor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(577, 'asset', '71668825', 'HW577', 'Kitchen Materials', 'Gas Stove', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(578, 'asset', '47582105', 'HW578', 'Kitchen Materials', 'Gas Stove', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(579, 'asset', '25233459', 'HW579', 'Kitchen Materials', 'Gas Stove', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(580, 'asset', '17906358', 'HW580', 'Kitchen Materials', 'Gas Stove', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(581, 'asset', '64369813', 'HW581', 'Kitchen Materials', 'Gas Stove', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(582, 'asset', '86772759', 'HW582', 'Kitchen Materials', 'Gas Stove', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(583, 'asset', '65444263', 'HW583', 'Kitchen Materials', 'Gas Stove', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(584, 'asset', '94650861', 'HW584', 'Kitchen Materials', 'Gas Stove', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(585, 'asset', '57331694', 'HW585', 'Kitchen Materials', 'Gas Stove', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(586, 'asset', '13169196', 'HW586', 'Kitchen Materials', 'Gas Stove', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(587, 'asset', '69076459', 'HW587', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(588, 'asset', '87450307', 'HW588', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(589, 'asset', '43889734', 'HW589', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(590, 'asset', '55910725', 'HW590', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(591, 'asset', '34046187', 'HW591', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(592, 'asset', '83361479', 'HW592', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(593, 'asset', '88232807', 'HW593', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(594, 'asset', '34716220', 'HW594', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(595, 'asset', '69506374', 'HW595', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(596, 'asset', '71831967', 'HW596', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(597, 'asset', '78891151', 'HW597', 'Furniture', 'Noticeboard', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(598, 'asset', '24209372', 'HW598', 'Furniture', 'Noticeboard', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(599, 'asset', '90313240', 'HW599', 'Furniture', 'Noticeboard', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(600, 'asset', '35270879', 'HW600', 'Furniture', 'Noticeboard', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(601, 'asset', '21620277', 'HW601', 'Furniture', 'Noticeboard', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(602, 'asset', '55161953', 'HW602', 'Furniture', 'Noticeboard', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(603, 'asset', '97694748', 'HW603', 'Furniture', 'Noticeboard', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE');
INSERT INTO `app_products` (`product_id`, `product_type`, `product_code`, `product_tag`, `product_category`, `product_title`, `product_sub_title`, `product_quantity_available`, `product_quantity_unit`, `product_updated_at`, `product_updated_id`, `product_updated_by`, `product_updated_department`, `product_updated_role`) VALUES
(604, 'asset', '66461655', 'HW604', 'Furniture', 'Noticeboard', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(605, 'asset', '96957628', 'HW605', 'Furniture', 'Noticeboard', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(606, 'asset', '31026185', 'HW606', 'Furniture', 'Noticeboard', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(607, 'asset', '98824082', 'HW607', 'Furniture', 'Noticeboard', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(608, 'asset', '84168302', 'HW608', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(609, 'asset', '49676748', 'HW609', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(610, 'asset', '48427822', 'HW610', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(611, 'asset', '53856520', 'HW611', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(612, 'asset', '62913383', 'HW612', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(613, 'asset', '80233588', 'HW613', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(614, 'asset', '49429318', 'HW614', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(615, 'asset', '94976949', 'HW615', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(616, 'asset', '36936193', 'HW616', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(617, 'asset', '97827350', 'HW617', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(618, 'asset', '96512287', 'HW618', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(619, 'asset', '91433834', 'HW619', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(620, 'asset', '99430803', 'HW620', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(621, 'asset', '56263611', 'HW621', 'Furniture', 'White board', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(622, 'asset', '37457071', 'HW622', 'Furniture', 'Conference Table 2400 WX1200DX750H', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(623, 'asset', '69919829', 'HW623', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(624, 'asset', '78639798', 'HW624', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(625, 'asset', '70750924', 'HW625', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(626, 'asset', '75495252', 'HW626', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(627, 'asset', '56553605', 'HW627', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(628, 'asset', '47985145', 'HW628', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(629, 'asset', '43298314', 'HW629', 'IT Equipment', 'HP Laptop 840 I5', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(630, 'asset', '44193767', 'HW630', 'IT Equipment', 'HP Laptop 840 I5', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(631, 'asset', '92546847', 'HW631', 'IT Equipment', 'HP Laptop 840 I5', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(632, 'asset', '78737093', 'HW632', 'IT Equipment', 'HP Laptop 840 I5', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(633, 'asset', '30784100', 'HW633', 'IT Equipment', 'HP Laptop 840 I5', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(634, 'asset', '80071501', 'HW634', 'Furniture', 'Conference Table 2400 WX1200DX750H', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(635, 'asset', '28777164', 'HW635', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(636, 'asset', '28578231', 'HW636', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(637, 'asset', '70858645', 'HW637', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(638, 'asset', '26653145', 'HW638', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(639, 'asset', '45436051', 'HW639', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(640, 'asset', '71715641', 'HW640', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(641, 'asset', '18706221', 'HW641', 'Furniture', 'Conference Table 2400 WX1200DX750H', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(642, 'asset', '69788192', 'HW642', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(643, 'asset', '34099413', 'HW643', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(644, 'asset', '24911050', 'HW644', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(645, 'asset', '78935768', 'HW645', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(646, 'asset', '56483422', 'HW646', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(647, 'asset', '17406961', 'HW647', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(648, 'asset', '35918853', 'HW648', 'Furniture', 'Conference Table 2400 WX1200DX750H', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(649, 'asset', '41338634', 'HW649', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(650, 'asset', '35718124', 'HW650', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(651, 'asset', '82511909', 'HW651', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(652, 'asset', '33044002', 'HW652', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(653, 'asset', '67470476', 'HW653', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(654, 'asset', '84295832', 'HW654', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(655, 'asset', '58450061', 'HW655', 'Furniture', 'Conference Table 2400 WX1200DX750H', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(656, 'asset', '40049541', 'HW656', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(657, 'asset', '28619394', 'HW657', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(658, 'asset', '26960990', 'HW658', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(659, 'asset', '80269777', 'HW659', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(660, 'asset', '92132444', 'HW660', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(661, 'asset', '59761516', 'HW661', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(662, 'asset', '50715216', 'HW662', 'Furniture', 'Conference Table 2400 WX1200DX750H', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(663, 'asset', '24503072', 'HW663', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(664, 'asset', '82339838', 'HW664', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(665, 'asset', '21897401', 'HW665', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(666, 'asset', '30539476', 'HW666', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(667, 'asset', '91597049', 'HW667', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(668, 'asset', '60567322', 'HW668', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(669, 'asset', '91278689', 'HW669', 'Furniture', 'Conference Table 2400 WX1200DX750H', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(670, 'asset', '18056631', 'HW670', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(671, 'asset', '97015973', 'HW671', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(672, 'asset', '89991089', 'HW672', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(673, 'asset', '89206660', 'HW673', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(674, 'asset', '44722609', 'HW674', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(675, 'asset', '45726687', 'HW675', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(676, 'asset', '86886088', 'HW676', 'Furniture', 'Conference Table 2400 WX1200DX750H', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(677, 'asset', '56888490', 'HW677', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(678, 'asset', '46459040', 'HW678', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(679, 'asset', '40767913', 'HW679', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(680, 'asset', '92032986', 'HW680', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(681, 'asset', '85121465', 'HW681', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(682, 'asset', '29068471', 'HW682', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(683, 'asset', '45478423', 'HW683', 'Furniture', 'Conference Table 2400 WX1200DX750H', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(684, 'asset', '41437420', 'HW684', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(685, 'asset', '35343299', 'HW685', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(686, 'asset', '51944719', 'HW686', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(687, 'asset', '87405885', 'HW687', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(688, 'asset', '70755303', 'HW688', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(689, 'asset', '79702189', 'HW689', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(690, 'asset', '49642510', 'HW690', 'Furniture', 'Conference Table 2400 WX1200DX750H', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(691, 'asset', '59520004', 'HW691', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(692, 'asset', '68117872', 'HW692', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(693, 'asset', '66751477', 'HW693', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(694, 'asset', '98448122', 'HW694', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(695, 'asset', '62766241', 'HW695', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(696, 'asset', '51305518', 'HW696', 'Furniture', 'Stacking Chair Black Colour', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(697, 'asset', '29604500', 'HW697', 'Furniture', 'Key Holder', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(698, 'asset', '83400565', 'HW698', 'IT Equipment', 'Sumsung Galaxy S9', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(699, 'asset', '47210127', 'HW699', 'Office Equipment', 'FAN', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(700, 'asset', '90206524', 'HW700', 'Office Equipment', 'Air condition 18000 TU wall Daikin', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(701, 'asset', '34388491', 'HW701', 'Office Equipment', 'Air condition 18000 TU wall Daikin', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(702, 'asset', '55954369', 'HW702', 'Office Equipment', 'DC/AC INVERTER CHARGER 7. 5KVA-220 VAC SINE WAVE ONLINE', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(703, 'asset', '78799496', 'HW703', 'Vehicles', 'TOYOTA HILUX DC 4X4, 2.4 L.. IT 966 RF', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(704, 'asset', '42364842', 'HW704', 'Vehicles', 'TOYOTA HILUX DC 4X4, 2.4 L.. IT 967 RF', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(705, 'asset', '10302504', 'HW705', 'Vehicles', 'TOYOTA HILUX DC 4X4, 2.4 L.. IT 968 RF', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(706, 'asset', '22007197', 'HW706', 'Vehicles', 'TOYOTA HILUX DC 4X4, 2.4 L.. IT 969 RF', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(707, 'asset', '93203209', 'HW707', 'Kitchen Materials', 'Shafing dishes', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(708, 'asset', '51595936', 'HW708', 'Kitchen Materials', 'Shafing dishes', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(709, 'asset', '42029530', 'HW709', 'Kitchen Materials', 'Shafing dishes', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(710, 'asset', '38525517', 'HW710', 'Kitchen Materials', 'Shafing dishes', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(711, 'asset', '49073861', 'HW711', 'Kitchen Materials', 'Shafing dishes for soup', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(712, 'asset', '44557180', 'HW712', 'Kitchen Materials', 'Shafing dishes for soup', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(713, 'asset', '52698958', 'HW713', 'Kitchen Materials', 'Fridge aardee big (ARRFD 260N)', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(714, 'asset', '62564909', 'HW714', 'Kitchen Materials', 'Gas cooker 5 burner without gas oven (steel)', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(715, 'asset', '20177426', 'HW715', 'Kitchen Materials', 'Gas cooker 4 burners with oven (supergeneral)', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(716, 'asset', '33421784', 'HW716', 'Kitchen Materials', 'Microwave, super general', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(717, 'asset', '50764318', 'HW717', 'Kitchen Materials', 'Juice extractor', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(718, 'asset', '35498490', 'HW718', 'Kitchen Materials', 'Blender', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(719, 'asset', '11867162', 'HW719', 'Furniture', 'White board 120*90', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(720, 'asset', '13534839', 'HW720', 'Furniture', 'White board 120*90', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(721, 'asset', '25968675', 'HW721', 'Furniture', 'White board 120*90', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(722, 'asset', '65997049', 'HW722', 'Furniture', 'Noticeboard 120*90', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(723, 'asset', '36922315', 'HW723', 'Furniture', 'Noticeboard 120*90', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(724, 'asset', '15765731', 'HW724', 'Furniture', 'Noticeboard 120*90', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(725, 'asset', '90318582', 'HW725', 'Furniture', 'Noticeboard 120*90', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(726, 'asset', '59360579', 'HW726', 'Furniture', 'Noticeboard 120*90', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(727, 'asset', '68951335', 'HW727', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(728, 'asset', '63157442', 'HW728', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(729, 'asset', '14859491', 'HW729', 'Furniture', 'Flip Chart Stand', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(730, 'asset', '34209952', 'HW730', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(731, 'asset', '53911702', 'HW731', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(732, 'asset', '96429698', 'HW732', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(733, 'asset', '10768201', 'HW733', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(734, 'asset', '58266824', 'HW734', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(735, 'asset', '32269866', 'HW735', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(736, 'asset', '73150337', 'HW736', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(737, 'asset', '32917675', 'HW737', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(738, 'asset', '54921085', 'HW738', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(739, 'asset', '67045096', 'HW739', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(740, 'asset', '43298902', 'HW740', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:18.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(741, 'asset', '98423118', 'HW741', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(742, 'asset', '94880243', 'HW742', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(743, 'asset', '39445731', 'HW743', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(744, 'asset', '74091139', 'HW744', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(745, 'asset', '15386405', 'HW745', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(746, 'asset', '86738004', 'HW746', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(747, 'asset', '11358174', 'HW747', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(748, 'asset', '90905002', 'HW748', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(749, 'asset', '30524099', 'HW749', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(750, 'asset', '80962860', 'HW750', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(751, 'asset', '46806666', 'HW751', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(752, 'asset', '83811389', 'HW752', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(753, 'asset', '81790901', 'HW753', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(754, 'asset', '24984015', 'HW754', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(755, 'asset', '73625801', 'HW755', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(756, 'asset', '69193251', 'HW756', 'IT Equipment', 'Lenovo laptops core i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(757, 'asset', '94167170', 'HW757', 'IT Equipment', 'Hp Probook 450 core i5', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(758, 'asset', '37990369', 'HW758', 'IT Equipment', 'Hp Probook 450 core i5', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(759, 'asset', '17626232', 'HW759', 'IT Equipment', 'Hp Probook 450 core i5', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(760, 'asset', '59338629', 'HW760', 'IT Equipment', 'Hp Probook 450 core i5', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(761, 'asset', '48458650', 'HW761', 'IT Equipment', 'Hp Probook 450 core i5', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(762, 'asset', '63980686', 'HW762', 'IT Equipment', 'Hp Probook 450 core i5', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(763, 'asset', '11518148', 'HW763', 'IT Equipment', 'Hp Probook 450 core i5', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(764, 'asset', '46102521', 'HW764', 'IT Equipment', 'HP Laserjet Pro M 227 FDW,MFP', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(765, 'asset', '51267775', 'HW765', 'IT Equipment', 'HP Laserjet Pro M 227 FDW,MFP', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(766, 'asset', '28283704', 'HW766', 'IT Equipment', 'HP Laserjet Pro M 227 FDW,MFP', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(767, 'asset', '39896552', 'HW767', 'IT Equipment', 'HP Laserjet Pro M 227 FDW,MFP', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(768, 'asset', '62816820', 'HW768', 'IT Equipment', 'HP Laserjet Pro M 227 FDW,MFP', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(769, 'asset', '48397482', 'HW769', 'Furniture', 'Office desk 140*75 one units with 3 drawers', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(770, 'asset', '90213810', 'HW770', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(771, 'asset', '61794478', 'HW771', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(772, 'asset', '63023348', 'HW772', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(773, 'asset', '63646884', 'HW773', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(774, 'asset', '87286282', 'HW774', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(775, 'asset', '25812728', 'HW775', 'Furniture', 'High Back Mesh Chair or Mesh Medium Back, with armrest and back', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(776, 'asset', '66151438', 'HW776', 'Furniture', 'Stacking chair/Visitor chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(777, 'asset', '60149191', 'HW777', 'Furniture', 'Stacking chair/Visitor chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(778, 'asset', '61661642', 'HW778', 'Furniture', 'Stacking chair/Visitor chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(779, 'asset', '93901262', 'HW779', 'Furniture', 'Stacking chair/Visitor chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(780, 'asset', '45634260', 'HW780', 'Furniture', 'Stacking chair/Visitor chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(781, 'asset', '79166667', 'HW781', 'Furniture', 'Stacking chair/Visitor chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(782, 'asset', '97484975', 'HW782', 'Furniture', 'Four way station/L-sharp , Lockable 3 drawers', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(783, 'asset', '70168954', 'HW783', 'Furniture', 'Full closed Filing cabined 180*80*40 cm', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(784, 'asset', '15227389', 'HW784', 'Furniture', 'Four drawers filing/Metallic', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(785, 'asset', '25852164', 'HW785', 'Furniture', 'Reception table 120', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(786, 'asset', '85679608', 'HW786', 'Furniture', 'Executive orthopedic chair for DCOP', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(787, 'asset', '33379534', 'HW787', 'Furniture', 'Executive table-100 cm or 120 cm', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(788, 'asset', '52714489', 'HW788', 'Furniture', 'Semi executive desk or L-Shape desk', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(789, 'asset', '57948916', 'HW789', 'Office Equipment', 'Safe', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(790, 'asset', '44608384', 'HW790', 'Furniture', 'Mobile Toilet with Stand', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(791, 'asset', '71441897', 'HW791', 'Furniture', 'Mobile Toilet with Stand', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(792, 'asset', '17940452', 'HW792', 'Furniture', 'Mobile Toilet with Stand', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(793, 'asset', '59643876', 'HW793', 'Furniture', 'Mobile Toilet with Stand', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(794, 'asset', '91409167', 'HW794', 'Furniture', 'Mobile Toilet with Stand', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(795, 'asset', '56888541', 'HW795', 'Furniture', 'High Back Mesh Chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(796, 'asset', '15627040', 'HW796', 'Furniture', 'High Back Mesh Chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(797, 'asset', '74247874', 'HW797', 'Furniture', 'High Back Mesh Chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(798, 'asset', '53456373', 'HW798', 'Furniture', 'High Back Mesh Chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(799, 'asset', '63610570', 'HW799', 'Furniture', 'High Back Mesh Chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(800, 'asset', '71673205', 'HW800', 'Furniture', 'High Back Mesh Chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(801, 'asset', '65641899', 'HW801', 'Furniture', 'High Back Mesh Chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(802, 'asset', '33037918', 'HW802', 'Furniture', 'High Back Mesh Chair', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(803, 'asset', '86426893', 'HW803', 'Furniture', 'Four way office workstation', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(804, 'asset', '20942674', 'HW804', 'Furniture', 'Four way office workstation', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(805, 'asset', '46857756', 'HW805', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(806, 'asset', '15825057', 'HW806', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(807, 'asset', '60275300', 'HW807', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(808, 'asset', '76899605', 'HW808', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(809, 'asset', '91648018', 'HW809', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(810, 'asset', '15210123', 'HW810', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(811, 'asset', '93549651', 'HW811', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(812, 'asset', '64410103', 'HW812', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(813, 'asset', '10485305', 'HW813', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(814, 'asset', '17112304', 'HW814', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(815, 'asset', '98652187', 'HW815', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(816, 'asset', '72344423', 'HW816', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(817, 'asset', '59375579', 'HW817', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(818, 'asset', '96568005', 'HW818', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(819, 'asset', '49972777', 'HW819', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(820, 'asset', '99050659', 'HW820', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(821, 'asset', '94510299', 'HW821', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(822, 'asset', '34906936', 'HW822', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(823, 'asset', '57768312', 'HW823', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(824, 'asset', '99281526', 'HW824', 'IT Equipment', 'Tablet Techno Droipad 7D', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(825, 'asset', '12107778', 'HW825', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(826, 'asset', '64449577', 'HW826', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(827, 'asset', '46221129', 'HW827', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(828, 'asset', '50655749', 'HW828', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(829, 'asset', '54656151', 'HW829', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(830, 'asset', '43998290', 'HW830', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(831, 'asset', '76674990', 'HW831', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(832, 'asset', '83045522', 'HW832', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(833, 'asset', '23694004', 'HW833', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(834, 'asset', '33673606', 'HW834', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(835, 'asset', '60555972', 'HW835', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(836, 'asset', '47091217', 'HW836', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(837, 'asset', '46344688', 'HW837', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(838, 'asset', '20321178', 'HW838', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(839, 'asset', '24810140', 'HW839', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(840, 'asset', '79180737', 'HW840', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(841, 'asset', '45026868', 'HW841', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(842, 'asset', '68077583', 'HW842', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(843, 'asset', '64519294', 'HW843', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(844, 'asset', '67527855', 'HW844', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(845, 'asset', '27728649', 'HW845', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(846, 'asset', '69123869', 'HW846', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(847, 'asset', '55338392', 'HW847', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(848, 'asset', '92443544', 'HW848', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(849, 'asset', '43000887', 'HW849', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(850, 'asset', '81331602', 'HW850', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(851, 'asset', '34509451', 'HW851', 'IT Equipment', 'Tablet Samsung Galaxy Tab A', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(852, 'asset', '77307471', 'HW852', 'IT Equipment', 'Rack 12U', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(853, 'asset', '49231906', 'HW853', 'IT Equipment', 'HP Proliant DL380Gen9 (Server)', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(854, 'asset', '83333192', 'HW854', 'IT Equipment', 'D-Link Switch for 24 Ports', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(855, 'asset', '23020358', 'HW855', 'IT Equipment', 'APC Smart-UPS C 100w', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(856, 'asset', '24774066', 'HW856', 'IT Equipment', 'Cisco ASA5506-SEC-BUN-K9 (Router and Firewall)', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(857, 'asset', '17653118', 'HW857', 'Office Equipment', 'Digital Camera Capture 40 meters', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(858, 'asset', '52130053', 'HW858', 'Office Equipment', 'Digital Camera Capture 40 meters', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(859, 'asset', '39280932', 'HW859', 'Office Equipment', 'Digital Camera Capture 40 meters', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(860, 'asset', '15653427', 'HW860', 'Office Equipment', 'Digital Camera Capture 40 meters', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(861, 'asset', '99410388', 'HW861', 'Office Equipment', 'Digital Camera Capture 40 meters', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(862, 'asset', '85163394', 'HW862', 'Office Equipment', 'Digital Camera Capture 40 meters', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(863, 'asset', '48866039', 'HW863', 'Office Equipment', 'Digital Camera Capture 40 meters', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(864, 'asset', '41475049', 'HW864', 'Office Equipment', 'Digital Camera Capture 40 meters', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(865, 'asset', '73316825', 'HW865', 'IT Equipment', 'Channel POE NVR', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(866, 'asset', '53853929', 'HW866', 'IT Equipment', 'Screen /Monitor 32 Inches', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(867, 'asset', '26502935', 'HW867', 'IT Equipment', 'Patch Pannel-24 ports', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(868, 'asset', '40313948', 'HW868', 'IT Equipment', 'HUAWEIETS 325 LAND Line', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(869, 'asset', '96588702', 'HW869', 'Office Equipment', 'Scanner Machine SCANSNAP IX500', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(870, 'asset', '97275055', 'HW870', 'Office Equipment', 'Scanner Machine SCANSNAP IX500', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(871, 'asset', '80125047', 'HW871', 'Office Equipment', 'Scanner Machine SCANSNAP IX500', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(872, 'asset', '19299695', 'HW872', 'Office Equipment', 'Jabra Speakrs', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(873, 'asset', '89654763', 'HW873', 'Office Equipment', 'Jabra Speakrs', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(874, 'asset', '22742313', 'HW874', 'Office Equipment', 'Jabra Speakrs', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(875, 'asset', '36366355', 'HW875', 'Vehicles', 'Moto Yamaha AG100--Plate RIT323B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(876, 'asset', '69061717', 'HW876', 'Vehicles', 'Moto Yamaha AG100--Plate RIT324B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(877, 'asset', '96369086', 'HW877', 'Vehicles', 'Moto Yamaha AG100--Plate RIT325B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(878, 'asset', '66701972', 'HW878', 'Vehicles', 'Moto Yamaha AG100--Plate RIT326B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(879, 'asset', '14813785', 'HW879', 'Vehicles', 'Moto Yamaha AG100--Plate RIT327B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(880, 'asset', '32964319', 'HW880', 'Vehicles', 'Moto Yamaha AG100--Plate RIT328B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(881, 'asset', '19338810', 'HW881', 'Vehicles', 'Moto Yamaha AG100--Plate RIT329B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(882, 'asset', '12417631', 'HW882', 'Vehicles', 'Moto Yamaha AG100--Plate RIT330B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(883, 'asset', '28638263', 'HW883', 'Vehicles', 'Moto Yamaha AG100--Plate RIT331B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(884, 'asset', '63397384', 'HW884', 'Vehicles', 'Moto Yamaha AG100--Plate RIT332B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(885, 'asset', '95634498', 'HW885', 'Vehicles', 'Moto Yamaha AG100--Plate RIT333B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(886, 'asset', '87111417', 'HW886', 'Vehicles', 'Moto Yamaha AG100--Plate RIT334B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(887, 'asset', '84724230', 'HW887', 'Vehicles', 'Moto Yamaha AG100--Plate RIT335B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(888, 'asset', '39868414', 'HW888', 'Vehicles', 'Moto Yamaha AG100--Plate RIT336B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(889, 'asset', '57130080', 'HW889', 'Vehicles', 'Moto Yamaha AG100--Plate RIT337B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(890, 'asset', '54336148', 'HW890', 'Vehicles', 'Moto Yamaha AG100--Plate RIT338B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(891, 'asset', '53408940', 'HW891', 'Vehicles', 'Moto Yamaha AG100--Plate RIT339B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(892, 'asset', '96270608', 'HW892', 'Vehicles', 'Moto Yamaha AG100--Plate RIT340B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(893, 'asset', '24935657', 'HW893', 'Vehicles', 'Moto Yamaha AG100--Plate RIT341B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(894, 'asset', '18348527', 'HW894', 'Vehicles', 'Moto Yamaha AG100--Plate RIT342B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(895, 'asset', '98649998', 'HW895', 'Vehicles', 'Moto Yamaha AG100--Plate RIT343B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(896, 'asset', '78698040', 'HW896', 'Vehicles', 'Moto Yamaha AG100--Plate RIT344B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(897, 'asset', '63170881', 'HW897', 'Vehicles', 'Moto Yamaha AG100--Plate RIT345B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(898, 'asset', '80572234', 'HW898', 'Vehicles', 'Moto Yamaha AG100--Plate RIT346B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(899, 'asset', '30006752', 'HW899', 'Vehicles', 'Moto Yamaha AG100--Plate RIT347B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(900, 'asset', '65527780', 'HW900', 'Vehicles', 'Moto Yamaha AG100--Plate RIT348B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(901, 'asset', '48709243', 'HW901', 'Vehicles', 'Moto Yamaha AG100--Plate RIT349B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(902, 'asset', '85242110', 'HW902', 'Vehicles', 'Moto Yamaha AG100--Plate RIT350B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(903, 'asset', '69878474', 'HW903', 'Vehicles', 'Moto Yamaha AG100--Plate RIT351B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(904, 'asset', '56747343', 'HW904', 'Vehicles', 'Moto Yamaha AG100--Plate RIT352B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(905, 'asset', '33988555', 'HW905', 'Vehicles', 'Moto Yamaha AG100--Plate RIT353B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(906, 'asset', '48327091', 'HW906', 'Vehicles', 'Moto Yamaha AG100--Plate RIT354B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(907, 'asset', '76529963', 'HW907', 'Vehicles', 'Moto Yamaha AG100--Plate RIT355B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(908, 'asset', '74594025', 'HW908', 'Vehicles', 'Moto Yamaha AG100--Plate RIT356B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(909, 'asset', '68164811', 'HW909', 'Vehicles', 'Moto Yamaha AG100--Plate RIT357B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(910, 'asset', '83496157', 'HW910', 'Vehicles', 'Moto Yamaha AG100--Plate RIT358B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(911, 'asset', '20996169', 'HW911', 'Vehicles', 'Moto Yamaha AG100--Plate RIT359B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(912, 'asset', '16950894', 'HW912', 'Vehicles', 'Moto Yamaha AG100--Plate RIT360B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(913, 'asset', '74063865', 'HW913', 'Vehicles', 'Moto Yamaha AG100--Plate RIT361B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(914, 'asset', '77299281', 'HW914', 'Vehicles', 'Moto Yamaha AG100--Plate RIT362B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(915, 'asset', '89975950', 'HW915', 'Vehicles', 'Moto Yamaha AG100--Plate RIT363B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(916, 'asset', '61753358', 'HW916', 'Vehicles', 'Moto Yamaha AG100--Plate RIT364B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(917, 'asset', '84184006', 'HW917', 'Vehicles', 'Moto Yamaha AG100--Plate RIT365B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE');
INSERT INTO `app_products` (`product_id`, `product_type`, `product_code`, `product_tag`, `product_category`, `product_title`, `product_sub_title`, `product_quantity_available`, `product_quantity_unit`, `product_updated_at`, `product_updated_id`, `product_updated_by`, `product_updated_department`, `product_updated_role`) VALUES
(918, 'asset', '87343123', 'HW918', 'Vehicles', 'Moto Yamaha AG100--Plate RIT366B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(919, 'asset', '43242504', 'HW919', 'Vehicles', 'Moto Yamaha AG100--Plate RIT367B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(920, 'asset', '86423019', 'HW920', 'Vehicles', 'Moto Yamaha AG100--Plate RIT368B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(921, 'asset', '23739388', 'HW921', 'Vehicles', 'Moto Yamaha AG100--Plate RIT369B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(922, 'asset', '31343651', 'HW922', 'Vehicles', 'Moto Yamaha AG100--Plate RIT370B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(923, 'asset', '57405859', 'HW923', 'Vehicles', 'Moto Yamaha AG100--Plate RIT371B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(924, 'asset', '46511803', 'HW924', 'Vehicles', 'Moto Yamaha AG100--Plate RIT372B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(925, 'asset', '18125949', 'HW925', 'Vehicles', 'Moto Yamaha AG100--Plate RIT373B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(926, 'asset', '40569310', 'HW926', 'Vehicles', 'Moto Yamaha AG100--Plate RIT374B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(927, 'asset', '30101616', 'HW927', 'Vehicles', 'Moto Yamaha AG100--Plate RIT375B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(928, 'asset', '27365745', 'HW928', 'Vehicles', 'Moto Yamaha AG100--Plate RIT376B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(929, 'asset', '11021440', 'HW929', 'Vehicles', 'Moto Yamaha AG100--Plate RIT377B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(930, 'asset', '70118996', 'HW930', 'Vehicles', 'Moto Yamaha AG100--Plate RIT378B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(931, 'asset', '23240124', 'HW931', 'Vehicles', 'Moto Yamaha AG100--Plate RIT379B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(932, 'asset', '32954297', 'HW932', 'Vehicles', 'Moto Yamaha AG100--Plate RIT380B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(933, 'asset', '92107049', 'HW933', 'Vehicles', 'Moto Yamaha AG100--Plate RIT381B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(934, 'asset', '89427525', 'HW934', 'Vehicles', 'Moto Yamaha AG100--Plate RIT382B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(935, 'asset', '33924345', 'HW935', 'Vehicles', 'Moto Yamaha AG100--Plate RIT383B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(936, 'asset', '79813173', 'HW936', 'Vehicles', 'Moto Yamaha AG100--Plate RIT384B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(937, 'asset', '98146958', 'HW937', 'Vehicles', 'Moto Yamaha AG100--Plate RIT385B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(938, 'asset', '40220476', 'HW938', 'Vehicles', 'Moto Yamaha AG100--Plate RIT386B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(939, 'asset', '40147677', 'HW939', 'Vehicles', 'Moto Yamaha AG100--Plate RIT387B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(940, 'asset', '69359543', 'HW940', 'Vehicles', 'Moto Yamaha AG100--Plate RIT388B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(941, 'asset', '63675387', 'HW941', 'Vehicles', 'Moto Yamaha AG100--Plate RIT389B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(942, 'asset', '11792947', 'HW942', 'Vehicles', 'Moto Yamaha AG100--Plate RIT390B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(943, 'asset', '95762494', 'HW943', 'Vehicles', 'Moto Yamaha AG100--Plate RIT391B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(944, 'asset', '39471532', 'HW944', 'Vehicles', 'Moto Yamaha AG100--Plate RIT392B', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(945, 'asset', '14710375', 'HW945', 'Office Equipment', 'Garmin GPS 64s', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(946, 'asset', '94077534', 'HW946', 'Office Equipment', 'Garmin GPS 64s', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(947, 'asset', '86584431', 'HW947', 'Office Equipment', 'Garmin GPS 64s', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(948, 'asset', '56538647', 'HW948', 'Office Equipment', 'Garmin GPS 64s', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(949, 'asset', '14760693', 'HW949', 'Office Equipment', 'Garmin GPS 64s', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(950, 'asset', '85838501', 'HW950', 'Office Equipment', 'Garmin GPS 64s', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(951, 'asset', '55566045', 'HW951', 'Office Equipment', 'Garmin GPS 64s', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(952, 'asset', '32949161', 'HW952', 'Office Equipment', 'Garmin GPS 64s', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(953, 'asset', '58230366', 'HW953', 'Office Equipment', 'Garmin GPS 64s', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(954, 'asset', '33642692', 'HW954', 'Office Equipment', 'Garmin GPS 64s', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(955, 'asset', '97332485', 'HW955', 'Office Equipment', 'Garmin GPS 64s', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(956, 'asset', '24243505', 'HW956', 'Office Equipment', 'Garmin GPS 64s', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(957, 'asset', '76206212', 'HW957', 'IT Equipment', 'Hp Probook 450 core i5', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(958, 'asset', '72659388', 'HW958', 'IT Equipment', 'Hp Probook 450 core i5', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(959, 'asset', '44536121', 'HW959', 'IT Equipment', 'Hp Probook 450 core i5', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(960, 'asset', '30148807', 'HW960', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(961, 'asset', '74149935', 'HW961', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(962, 'asset', '51503153', 'HW962', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(963, 'asset', '90430379', 'HW963', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(964, 'asset', '42754588', 'HW964', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(965, 'asset', '84443198', 'HW965', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(966, 'asset', '10589236', 'HW966', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(967, 'asset', '71929757', 'HW967', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(968, 'asset', '24312330', 'HW968', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(969, 'asset', '70652680', 'HW969', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(970, 'asset', '47302516', 'HW970', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(971, 'asset', '98692091', 'HW971', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(972, 'asset', '14979848', 'HW972', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(973, 'asset', '45775137', 'HW973', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(974, 'asset', '61379596', 'HW974', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(975, 'asset', '32715135', 'HW975', 'IT Equipment', 'Lenovo v 130 i3', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(976, 'asset', '53696436', 'HW976', 'IT Equipment', 'ACER PROJECTOR X118', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(977, 'asset', '93744126', 'HW977', 'IT Equipment', 'ACER PROJECTOR X118', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(978, 'asset', '23844049', 'HW978', 'IT Equipment', 'ACER PROJECTOR X118', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(979, 'asset', '21891875', 'HW979', 'IT Equipment', 'ACER PROJECTOR X118', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(980, 'asset', '97603066', 'HW980', 'IT Equipment', 'ACER PROJECTOR X118', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(981, 'asset', '56519379', 'HW981', 'IT Equipment', 'ACER PROJECTOR X118', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(982, 'asset', '70178369', 'HW982', 'IT Equipment', 'ACER PROJECTOR X118', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(983, 'asset', '49056472', 'HW983', 'IT Equipment', 'ACER PROJECTOR X118', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(984, 'asset', '28495868', 'HW984', 'IT Equipment', 'ACER PROJECTOR X118', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(985, 'asset', '41947702', 'HW985', 'IT Equipment', 'ACER PROJECTOR X118', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(986, 'asset', '93736034', 'HW986', 'IT Equipment', 'Screen Projector', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(987, 'asset', '84660369', 'HW987', 'IT Equipment', 'Screen Projector', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(988, 'asset', '34150494', 'HW988', 'IT Equipment', 'Screen Projector', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(989, 'asset', '60449196', 'HW989', 'IT Equipment', 'Screen Projector', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(990, 'asset', '13306347', 'HW990', 'IT Equipment', 'Screen Projector', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(991, 'asset', '79624553', 'HW991', 'IT Equipment', 'Screen Projector', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(992, 'asset', '62286306', 'HW992', 'IT Equipment', 'Screen Projector', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(993, 'asset', '39420446', 'HW993', 'IT Equipment', 'Screen Projector', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(994, 'asset', '39500243', 'HW994', 'IT Equipment', 'Screen Projector', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(995, 'asset', '71585996', 'HW995', 'IT Equipment', 'Screen Projector', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(996, 'asset', '36670282', 'HW996', 'Vehicles', 'Vehicle', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(997, 'asset', '68817666', 'HW997', 'Vehicles', 'Vehicle', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(998, 'asset', '86176962', 'HW998', 'Vehicles', 'Vehicle', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(999, 'asset', '29597748', 'HW999', 'IT Equipment', 'LG 43-inches Full HD Smart TV', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(1000, 'asset', '93175140', 'HW1000', 'IT Equipment', 'Linksys N300 WI-FI Access point Model WAP 3004', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(1001, 'asset', '76485954', 'HW1001', 'IT Equipment', 'Linksys N300 WI-FI Access point Model WAP 3004', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE'),
(1002, 'asset', '29142752', 'HW1002', 'IT Equipment', 'Linksys N300 WI-FI Access point Model WAP 3004', '', 0, '', '2019-03-28 14:09:19.000000', '1', 'Tech Support', 'NONE', 'NONE');

-- --------------------------------------------------------

--
-- Table structure for table `app_product_requests`
--

CREATE TABLE IF NOT EXISTS `app_product_requests` (
  `product_request_id` int(11) NOT NULL,
  `product_request_code` varchar(8) NOT NULL,
  `product_request_project` varchar(255) NOT NULL,
  `product_request_details` varchar(255) NOT NULL,
  `product_request_no_of_items` decimal(10,0) NOT NULL,
  `product_request_created_at` datetime(6) NOT NULL,
  `product_request_created_id` varchar(100) NOT NULL,
  `product_request_created_by` varchar(100) NOT NULL,
  `product_request_created_department` varchar(255) NOT NULL,
  `product_request_created_role` varchar(255) NOT NULL,
  `product_request_updated_at` datetime(6) NOT NULL,
  `product_request_updated_id` varchar(100) NOT NULL,
  `product_request_updated_by` varchar(100) NOT NULL,
  `product_request_updated_department` varchar(255) NOT NULL,
  `product_request_updated_role` varchar(255) NOT NULL,
  `product_request_requested_at` datetime(6) NOT NULL,
  `product_request_requested_id` varchar(100) NOT NULL,
  `product_request_requested_by` varchar(100) NOT NULL,
  `product_request_requested_department` varchar(255) NOT NULL,
  `product_request_requested_role` varchar(255) NOT NULL,
  `product_request_reviewed_at` datetime(6) NOT NULL,
  `product_request_reviewed_id` varchar(100) NOT NULL,
  `product_request_reviewed_by` varchar(100) NOT NULL,
  `product_request_reviewed_department` varchar(255) NOT NULL,
  `product_request_reviewed_role` varchar(255) NOT NULL,
  `product_request_approved_updated_at` datetime(6) NOT NULL,
  `product_request_approved_updated_id` varchar(100) NOT NULL,
  `product_request_approved_updated_by` varchar(100) NOT NULL,
  `product_request_approved_updated_department` varchar(255) NOT NULL,
  `product_request_approved_updated_role` varchar(255) NOT NULL,
  `product_request_closed_at` datetime(6) NOT NULL,
  `product_request_closed_id` varchar(100) NOT NULL,
  `product_request_closed_by` varchar(100) NOT NULL,
  `product_request_closed_department` varchar(255) NOT NULL,
  `product_request_closed_role` varchar(255) NOT NULL,
  `product_request_cancelled_at` datetime(6) NOT NULL,
  `product_request_cancelled_id` varchar(100) NOT NULL,
  `product_request_cancelled_by` varchar(100) NOT NULL,
  `product_request_cancelled_department` varchar(255) NOT NULL,
  `product_request_cancelled_role` varchar(255) NOT NULL,
  `product_request_status` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_product_requests`
--

INSERT INTO `app_product_requests` (`product_request_id`, `product_request_code`, `product_request_project`, `product_request_details`, `product_request_no_of_items`, `product_request_created_at`, `product_request_created_id`, `product_request_created_by`, `product_request_created_department`, `product_request_created_role`, `product_request_updated_at`, `product_request_updated_id`, `product_request_updated_by`, `product_request_updated_department`, `product_request_updated_role`, `product_request_requested_at`, `product_request_requested_id`, `product_request_requested_by`, `product_request_requested_department`, `product_request_requested_role`, `product_request_reviewed_at`, `product_request_reviewed_id`, `product_request_reviewed_by`, `product_request_reviewed_department`, `product_request_reviewed_role`, `product_request_approved_updated_at`, `product_request_approved_updated_id`, `product_request_approved_updated_by`, `product_request_approved_updated_department`, `product_request_approved_updated_role`, `product_request_closed_at`, `product_request_closed_id`, `product_request_closed_by`, `product_request_closed_department`, `product_request_closed_role`, `product_request_cancelled_at`, `product_request_cancelled_id`, `product_request_cancelled_by`, `product_request_cancelled_department`, `product_request_cancelled_role`, `product_request_status`) VALUES
(1, '37687620', 'Agriculture', 'testing stock request', 2, '2019-03-30 23:01:35.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', '2019-03-30 23:01:35.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', '2019-03-30 23:02:29.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', '2019-03-30 23:02:35.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', '2019-03-30 23:02:41.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', '0001-01-01 00:00:00.000000', '', '', '', '', '0001-01-01 00:00:00.000000', '', '', '', '', 'approved');

-- --------------------------------------------------------

--
-- Table structure for table `app_product_request_items`
--

CREATE TABLE IF NOT EXISTS `app_product_request_items` (
  `product_request_item_id` int(11) NOT NULL,
  `product_requests_product_request_id` int(11) NOT NULL,
  `products_product_id` int(11) NOT NULL,
  `product_request_item_product_type` varchar(255) NOT NULL,
  `product_request_item_product_code` varchar(8) NOT NULL,
  `product_request_item_product_tag` varchar(255) NOT NULL,
  `product_request_item_product_category` varchar(255) NOT NULL,
  `product_request_item_product_title` varchar(100) NOT NULL,
  `product_request_item_product_sub_title` varchar(255) NOT NULL,
  `product_request_item_product_quantity_initial` decimal(10,0) NOT NULL,
  `product_request_item_product_quantity_ordered` decimal(10,0) NOT NULL,
  `product_request_item_product_quantity_balance` decimal(10,0) NOT NULL,
  `product_request_item_product_quantity_unit` varchar(255) NOT NULL,
  `product_request_item_created_at` datetime(6) NOT NULL,
  `product_request_item_created_id` varchar(100) NOT NULL,
  `product_request_item_created_by` varchar(100) NOT NULL,
  `product_request_item_created_department` varchar(255) NOT NULL,
  `product_request_item_created_role` varchar(255) NOT NULL,
  `product_request_item_updated_at` datetime(6) NOT NULL,
  `product_request_item_updated_id` varchar(100) NOT NULL,
  `product_request_item_updated_by` varchar(100) NOT NULL,
  `product_request_item_updated_department` varchar(255) NOT NULL,
  `product_request_item_updated_role` varchar(255) NOT NULL,
  `product_request_item_received_at` datetime(6) NOT NULL,
  `product_request_item_received_id` varchar(100) NOT NULL,
  `product_request_item_received_by` varchar(100) NOT NULL,
  `product_request_item_received_department` varchar(255) NOT NULL,
  `product_request_item_received_role` varchar(255) NOT NULL,
  `product_request_item_status` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_product_request_items`
--

INSERT INTO `app_product_request_items` (`product_request_item_id`, `product_requests_product_request_id`, `products_product_id`, `product_request_item_product_type`, `product_request_item_product_code`, `product_request_item_product_tag`, `product_request_item_product_category`, `product_request_item_product_title`, `product_request_item_product_sub_title`, `product_request_item_product_quantity_initial`, `product_request_item_product_quantity_ordered`, `product_request_item_product_quantity_balance`, `product_request_item_product_quantity_unit`, `product_request_item_created_at`, `product_request_item_created_id`, `product_request_item_created_by`, `product_request_item_created_department`, `product_request_item_created_role`, `product_request_item_updated_at`, `product_request_item_updated_id`, `product_request_item_updated_by`, `product_request_item_updated_department`, `product_request_item_updated_role`, `product_request_item_received_at`, `product_request_item_received_id`, `product_request_item_received_by`, `product_request_item_received_department`, `product_request_item_received_role`, `product_request_item_status`) VALUES
(1, 1, 1, 'asset', '50162978', 'HW001', 'Furniture', '3 Door filling cabinet', '', 20, 10, 10, '', '2019-03-30 23:01:51.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', '2019-03-30 23:01:51.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', '2019-03-30 23:02:51.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', 'received'),
(2, 1, 2, 'asset', '59173245', 'HW002', 'Furniture', 'Round meeting table 150 cmx75cm/Glass Top', '', 20, 5, 15, '', '2019-03-30 23:02:22.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', '2019-03-30 23:02:22.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', '2019-03-30 23:02:51.000000', '24', 'Stock Admin', 'DAF', 'Stock Admin', 'received');

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

CREATE TABLE IF NOT EXISTS `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
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
) ENGINE=InnoDB AUTO_INCREMENT=138 DEFAULT CHARSET=latin1;

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
(84, 'Can view notifications', 21, 'view_notifications'),
(85, 'Can add notifications timeline', 22, 'add_notificationstimeline'),
(86, 'Can change notifications timeline', 22, 'change_notificationstimeline'),
(87, 'Can delete notifications timeline', 22, 'delete_notificationstimeline'),
(88, 'Can view notifications timeline', 22, 'view_notificationstimeline'),
(89, 'Can add Token', 23, 'add_token'),
(90, 'Can change Token', 23, 'change_token'),
(91, 'Can delete Token', 23, 'delete_token'),
(92, 'Can view Token', 23, 'view_token'),
(93, 'Can add attachment', 24, 'add_attachment'),
(94, 'Can change attachment', 24, 'change_attachment'),
(95, 'Can delete attachment', 24, 'delete_attachment'),
(96, 'Can view attachment', 24, 'view_attachment'),
(97, 'Can delete foreign attachments', 24, 'delete_foreign_attachments'),
(98, 'Can add emails', 25, 'add_emails'),
(99, 'Can change emails', 25, 'change_emails'),
(100, 'Can delete emails', 25, 'delete_emails'),
(101, 'Can view emails', 25, 'view_emails'),
(102, 'Can add attachments', 26, 'add_attachments'),
(103, 'Can change attachments', 26, 'change_attachments'),
(104, 'Can delete attachments', 26, 'delete_attachments'),
(105, 'Can view attachments', 26, 'view_attachments'),
(106, 'Can add inventory', 27, 'add_inventory'),
(107, 'Can change inventory', 27, 'change_inventory'),
(108, 'Can delete inventory', 27, 'delete_inventory'),
(109, 'Can view inventory', 27, 'view_inventory'),
(110, 'Can add inventory items', 28, 'add_inventoryitems'),
(111, 'Can change inventory items', 28, 'change_inventoryitems'),
(112, 'Can delete inventory items', 28, 'delete_inventoryitems'),
(113, 'Can view inventory items', 28, 'view_inventoryitems'),
(114, 'Can add product request items', 29, 'add_productrequestitems'),
(115, 'Can change product request items', 29, 'change_productrequestitems'),
(116, 'Can delete product request items', 29, 'delete_productrequestitems'),
(117, 'Can view product request items', 29, 'view_productrequestitems'),
(118, 'Can add product requests', 30, 'add_productrequests'),
(119, 'Can change product requests', 30, 'change_productrequests'),
(120, 'Can delete product requests', 30, 'delete_productrequests'),
(121, 'Can view product requests', 30, 'view_productrequests'),
(122, 'Can add products', 31, 'add_products'),
(123, 'Can change products', 31, 'change_products'),
(124, 'Can delete products', 31, 'delete_products'),
(125, 'Can view products', 31, 'view_products'),
(126, 'Can add inventory_ items', 28, 'add_inventory_items'),
(127, 'Can change inventory_ items', 28, 'change_inventory_items'),
(128, 'Can delete inventory_ items', 28, 'delete_inventory_items'),
(129, 'Can view inventory_ items', 28, 'view_inventory_items'),
(130, 'Can add product_ request_ items', 29, 'add_product_request_items'),
(131, 'Can change product_ request_ items', 29, 'change_product_request_items'),
(132, 'Can delete product_ request_ items', 29, 'delete_product_request_items'),
(133, 'Can view product_ request_ items', 29, 'view_product_request_items'),
(134, 'Can add product_ requests', 30, 'add_product_requests'),
(135, 'Can change product_ requests', 30, 'change_product_requests'),
(136, 'Can delete product_ requests', 30, 'delete_product_requests'),
(137, 'Can view product_ requests', 30, 'view_product_requests');

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
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'admin', 'logentry'),
(2, 'app', 'access_permissions'),
(26, 'app', 'attachments'),
(1, 'app', 'backups'),
(25, 'app', 'emails'),
(3, 'app', 'failed_login'),
(27, 'app', 'inventory'),
(28, 'app', 'inventory_items'),
(21, 'app', 'notifications'),
(22, 'app', 'notificationstimeline'),
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
(31, 'app', 'products'),
(30, 'app', 'product_requests'),
(29, 'app', 'product_request_items'),
(24, 'attachments', 'attachment'),
(9, 'auth', 'group'),
(8, 'auth', 'permission'),
(10, 'auth', 'user'),
(23, 'authtoken', 'token'),
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
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=latin1;

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
(31, 'app', '0014_auto_20190319_1829', '2019-03-19 18:29:16.392389'),
(32, 'app', '0015_auto_20190322_0955', '2019-03-22 09:55:36.331144'),
(33, 'app', '0016_auto_20190323_1734', '2019-03-23 17:34:47.629319'),
(34, 'authtoken', '0001_initial', '2019-03-23 17:34:47.694179'),
(35, 'authtoken', '0002_auto_20160226_1747', '2019-03-23 17:34:47.787983'),
(36, 'app', '0017_auto_20190324_1055', '2019-03-24 10:55:30.304748'),
(37, 'app', '0018_auto_20190324_1125', '2019-03-24 11:25:28.075902'),
(40, 'app', '0019_auto_20190325_0755', '2019-03-25 07:55:57.944661'),
(41, 'app', '0020_auto_20190325_1435', '2019-03-25 14:35:58.591294'),
(42, 'app', '0021_auto_20190326_0732', '2019-03-26 07:32:13.155915'),
(43, 'app', '0022_auto_20190326_0957', '2019-03-26 09:57:57.431629'),
(44, 'app', '0023_auto_20190326_1813', '2019-03-26 18:13:30.252795'),
(45, 'app', '0024_emails', '2019-03-27 09:04:55.707853'),
(46, 'app', '0025_attachments', '2019-03-27 09:13:13.630372'),
(47, 'app', '0026_auto_20190327_1647', '2019-03-27 16:47:31.814493'),
(48, 'app', '0027_auto_20190327_1743', '2019-03-27 17:43:55.126291'),
(49, 'app', '0028_auto_20190327_1928', '2019-03-27 19:28:14.788268'),
(50, 'app', '0029_auto_20190327_1958', '2019-03-27 19:58:08.259676'),
(51, 'app', '0030_auto_20190327_2223', '2019-03-27 22:23:16.532029'),
(52, 'app', '0031_auto_20190328_1225', '2019-03-28 12:25:46.154086'),
(53, 'app', '0032_order_items_order_item_type_id', '2019-03-28 14:39:26.084674'),
(54, 'app', '0033_auto_20190330_0736', '2019-03-30 07:36:41.972354'),
(55, 'app', '0034_auto_20190330_0952', '2019-03-30 09:52:27.777731'),
(56, 'app', '0035_auto_20190330_1011', '2019-03-30 10:12:02.891225'),
(57, 'app', '0036_auto_20190330_1901', '2019-03-30 19:01:18.526835'),
(58, 'app', '0037_auto_20190330_2054', '2019-03-30 20:54:19.930837'),
(59, 'app', '0038_auto_20190331_0006', '2019-03-31 00:06:39.452125');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
-- Indexes for table `app_attachments`
--
ALTER TABLE `app_attachments`
  ADD PRIMARY KEY (`attachment_id`);

--
-- Indexes for table `app_emails`
--
ALTER TABLE `app_emails`
  ADD PRIMARY KEY (`email_id`);

--
-- Indexes for table `app_failed_login`
--
ALTER TABLE `app_failed_login`
  ADD PRIMARY KEY (`failed_login_id`);

--
-- Indexes for table `app_inventory`
--
ALTER TABLE `app_inventory`
  ADD PRIMARY KEY (`inventory_id`),
  ADD UNIQUE KEY `app_inventory_inventory_order_purchase_no_b8fb3d92_uniq` (`inventory_order_purchase_no`);

--
-- Indexes for table `app_inventory_items`
--
ALTER TABLE `app_inventory_items`
  ADD PRIMARY KEY (`inventory_item_id`);

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
  ADD PRIMARY KEY (`order_proposal_id`),
  ADD UNIQUE KEY `order_proposal_code` (`order_proposal_code`);

--
-- Indexes for table `app_products`
--
ALTER TABLE `app_products`
  ADD PRIMARY KEY (`product_id`),
  ADD UNIQUE KEY `product_code` (`product_code`);

--
-- Indexes for table `app_product_requests`
--
ALTER TABLE `app_product_requests`
  ADD PRIMARY KEY (`product_request_id`),
  ADD UNIQUE KEY `product_request_code` (`product_request_code`);

--
-- Indexes for table `app_product_request_items`
--
ALTER TABLE `app_product_request_items`
  ADD PRIMARY KEY (`product_request_item_id`);

--
-- Indexes for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

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
-- AUTO_INCREMENT for table `app_attachments`
--
ALTER TABLE `app_attachments`
  MODIFY `attachment_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `app_emails`
--
ALTER TABLE `app_emails`
  MODIFY `email_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `app_failed_login`
--
ALTER TABLE `app_failed_login`
  MODIFY `failed_login_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `app_inventory`
--
ALTER TABLE `app_inventory`
  MODIFY `inventory_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `app_inventory_items`
--
ALTER TABLE `app_inventory_items`
  MODIFY `inventory_item_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `app_notifications`
--
ALTER TABLE `app_notifications`
  MODIFY `notification_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=27;
--
-- AUTO_INCREMENT for table `app_operators`
--
ALTER TABLE `app_operators`
  MODIFY `operator_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=29;
--
-- AUTO_INCREMENT for table `app_operator_access_permissions`
--
ALTER TABLE `app_operator_access_permissions`
  MODIFY `operator_access_permission_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=392;
--
-- AUTO_INCREMENT for table `app_operator_logs`
--
ALTER TABLE `app_operator_logs`
  MODIFY `operator_log_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `app_orders`
--
ALTER TABLE `app_orders`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `app_order_approvals`
--
ALTER TABLE `app_order_approvals`
  MODIFY `order_approval_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `app_order_items`
--
ALTER TABLE `app_order_items`
  MODIFY `order_item_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
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
  MODIFY `order_proposal_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `app_products`
--
ALTER TABLE `app_products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1003;
--
-- AUTO_INCREMENT for table `app_product_requests`
--
ALTER TABLE `app_product_requests`
  MODIFY `product_request_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `app_product_request_items`
--
ALTER TABLE `app_product_request_items`
  MODIFY `product_request_item_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=138;
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=32;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=60;
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
-- Constraints for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

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
