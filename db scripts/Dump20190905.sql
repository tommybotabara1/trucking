CREATE DATABASE  IF NOT EXISTS `trucking` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `trucking`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: trucking
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add table1',7,'add_table1'),(26,'Can change table1',7,'change_table1'),(27,'Can delete table1',7,'delete_table1'),(28,'Can view table1',7,'view_table1');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$9uSNiw4C4vfF$N+4l4kwsKc3k4YKlLNOnywnaav/sYtHBzvOU9V9vt3M=','2019-02-12 10:22:29.482884',1,'admin','','','admin@example.com',1,1,'2019-01-16 01:40:11.204004');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `breakdown`
--

DROP TABLE IF EXISTS `breakdown`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `breakdown` (
  `breakdownID` int(11) NOT NULL AUTO_INCREMENT,
  `breakdownDate` date DEFAULT NULL,
  `plateNumber` varchar(10) DEFAULT NULL,
  `wayBillNo` varchar(10) DEFAULT NULL,
  `customer` varchar(30) DEFAULT NULL,
  `client` varchar(30) DEFAULT NULL,
  `cashAdvance` float DEFAULT NULL,
  `totalLiq` float DEFAULT NULL,
  `unliquidated` float DEFAULT NULL,
  `salary` float DEFAULT NULL,
  PRIMARY KEY (`breakdownID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `breakdown`
--

LOCK TABLES `breakdown` WRITE;
/*!40000 ALTER TABLE `breakdown` DISABLE KEYS */;
INSERT INTO `breakdown` VALUES (3,'2019-09-24',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `breakdown` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `canteen`
--

DROP TABLE IF EXISTS `canteen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `canteen` (
  `canteenID` int(11) NOT NULL AUTO_INCREMENT,
  `payRollPeriodForm` date DEFAULT NULL,
  `payRollPeriodTo` date DEFAULT NULL,
  `employeeName` varchar(30) DEFAULT NULL,
  `takeHomePay` float DEFAULT NULL,
  `canteenName` varchar(30) DEFAULT NULL,
  `baraks` varchar(30) DEFAULT NULL,
  `others` varchar(30) DEFAULT NULL,
  `coopSavings` float DEFAULT NULL,
  `coopLoan` float DEFAULT NULL,
  `coopCP` float DEFAULT NULL,
  `coopRice` float DEFAULT NULL,
  `actualSalary` float DEFAULT NULL,
  PRIMARY KEY (`canteenID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canteen`
--

LOCK TABLES `canteen` WRITE;
/*!40000 ALTER TABLE `canteen` DISABLE KEYS */;
INSERT INTO `canteen` VALUES (3,NULL,NULL,'asd',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `canteen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `clientID` int(11) NOT NULL,
  `clientName` varchar(30) NOT NULL,
  PRIMARY KEY (`clientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'Awit'),(2,'Yes'),(3,'Test'),(4,'Yesy'),(5,'Yes'),(6,'Test2'),(7,'Test3'),(8,'Test4'),(9,'Test5'),(10,'Test6');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `customerID` int(11) NOT NULL,
  `customerName` varchar(30) NOT NULL,
  PRIMARY KEY (`customerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (19,'Wew');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `damages`
--

DROP TABLE IF EXISTS `damages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `damages` (
  `damagesID` int(11) NOT NULL AUTO_INCREMENT,
  `employeeName` varchar(30) DEFAULT NULL,
  `typeOfDamage` varchar(30) DEFAULT NULL,
  `personalCashAdv` float DEFAULT NULL,
  `caDate` date DEFAULT NULL,
  PRIMARY KEY (`damagesID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `damages`
--

LOCK TABLES `damages` WRITE;
/*!40000 ALTER TABLE `damages` DISABLE KEYS */;
/*!40000 ALTER TABLE `damages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direct_payroll`
--

DROP TABLE IF EXISTS `direct_payroll`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direct_payroll` (
  `directPayrollID` int(11) NOT NULL AUTO_INCREMENT,
  `employeeNo` int(15) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `commission` float DEFAULT NULL,
  `otherCommAdditional` float DEFAULT NULL,
  `otherCommAdjustment` float DEFAULT NULL,
  `grossPay` float DEFAULT NULL,
  `netPay` float DEFAULT NULL,
  `rate` float DEFAULT NULL,
  `incentives` float DEFAULT NULL,
  `takeHomePay` float DEFAULT NULL,
  PRIMARY KEY (`directPayrollID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direct_payroll`
--

LOCK TABLES `direct_payroll` WRITE;
/*!40000 ALTER TABLE `direct_payroll` DISABLE KEYS */;
INSERT INTO `direct_payroll` VALUES (1,1,'tommybotabara',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `direct_payroll` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'trucking','table1');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-01-16 01:37:13.217607'),(2,'auth','0001_initial','2019-01-16 01:37:15.580489'),(3,'admin','0001_initial','2019-01-16 01:37:16.561315'),(4,'admin','0002_logentry_remove_auto_add','2019-01-16 01:37:16.576897'),(5,'admin','0003_logentry_add_action_flag_choices','2019-01-16 01:37:16.608166'),(6,'contenttypes','0002_remove_content_type_name','2019-01-16 01:37:17.147737'),(7,'auth','0002_alter_permission_name_max_length','2019-01-16 01:37:17.371078'),(8,'auth','0003_alter_user_email_max_length','2019-01-16 01:37:17.641172'),(9,'auth','0004_alter_user_username_opts','2019-01-16 01:37:17.656790'),(10,'auth','0005_alter_user_last_login_null','2019-01-16 01:37:17.939784'),(11,'auth','0006_require_contenttypes_0002','2019-01-16 01:37:17.955420'),(12,'auth','0007_alter_validators_add_error_messages','2019-01-16 01:37:17.971054'),(13,'auth','0008_alter_user_username_max_length','2019-01-16 01:37:18.263635'),(14,'auth','0009_alter_user_last_name_max_length','2019-01-16 01:37:18.519914'),(15,'sessions','0001_initial','2019-01-16 01:37:18.707370'),(16,'trucking','0001_initial','2019-01-16 01:40:53.993177');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `driver`
--

DROP TABLE IF EXISTS `driver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `driver` (
  `driverID` int(11) NOT NULL,
  `driverName` varchar(30) NOT NULL,
  `phoneNumber` varchar(10) NOT NULL,
  `SSS` varchar(20) NOT NULL,
  `taxID` varchar(20) NOT NULL,
  PRIMARY KEY (`driverID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `driver`
--

LOCK TABLES `driver` WRITE;
/*!40000 ALTER TABLE `driver` DISABLE KEYS */;
INSERT INTO `driver` VALUES (1,'Bob','1234567890','123','1'),(2,'Mark','1111111111','11111111111111111111','11111111111111111111'),(3,'Mac','2222222222','22222222222222222222','22222222222222222222'),(4,'Class','4444444444','44444444444444444444','44444444444444444444'),(5,'Warwick','6666666666','66666666666666666666','66666666666666666666'),(6,'Nutella','7777777777','77777777777777777777','77777777777777777777'),(7,'Hotdog','8888888888','88888888888888888888','88888888888888888888'),(8,'Water','9999999999','99999999999999999999','99999999999999999999'),(9,'Test1','9999999999','99999999999999999999','99999999999999999999'),(10,'Test2','9999999999','99999999999999999999','99999999999999999999'),(11,'Test3','1111111111','11111111111111111111','11111111111111111111'),(12,'Test4','1111111111','11111111111111111111','11111111111111111111'),(13,'Test5','1111111111','11111111111111111111','11111111111111111111'),(14,'Test6','1111111111','11111111111111111111','11111111111111111111'),(15,'Test7','1111111111','11111111111111111111','11111111111111111111'),(16,'Test8','1111111111','11111111111111111111','11111111111111111111'),(17,'Test9','1234567890','12345678976543212345','12345678976543212345'),(18,'Yes','1234567009','12345678907654321111','12345678907654321345');
/*!40000 ALTER TABLE `driver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `split_amounts`
--

DROP TABLE IF EXISTS `split_amounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `split_amounts` (
  `splitAmountID` int(11) NOT NULL AUTO_INCREMENT,
  `dboID` int(11) NOT NULL,
  `type` varchar(45) NOT NULL,
  `amount` float DEFAULT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`splitAmountID`),
  KEY `dboID_idx` (`dboID`),
  CONSTRAINT `dboID` FOREIGN KEY (`dboID`) REFERENCES `table1` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `split_amounts`
--

LOCK TABLES `split_amounts` WRITE;
/*!40000 ALTER TABLE `split_amounts` DISABLE KEYS */;
INSERT INTO `split_amounts` VALUES (52,18,'Entry Fee',15,'receipt'),(53,18,'Entry Fee',50,'receipt'),(54,18,'Entry Fee',23.5,'receipt'),(55,18,'Parking',15,'test'),(56,18,'Parking',2.5,'test'),(58,18,'Toll Fee',265,'test'),(59,18,'Toll Fee',0.5,'test'),(60,18,'Others',0.5,'test');
/*!40000 ALTER TABLE `split_amounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statement_of_account`
--

DROP TABLE IF EXISTS `statement_of_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `statement_of_account` (
  `statementOfAccountID` int(11) NOT NULL AUTO_INCREMENT,
  `month` varchar(15) DEFAULT NULL,
  `soaNo` varchar(15) DEFAULT NULL,
  `customer` varchar(30) DEFAULT NULL,
  `particulars` varchar(50) DEFAULT NULL,
  `invoiceDate` date DEFAULT NULL,
  `invoiceReceiveDate` date DEFAULT NULL,
  `receivedBy` varchar(30) DEFAULT NULL,
  `totalSales` float DEFAULT NULL,
  `arNo` varchar(15) DEFAULT NULL,
  `paidAmount` float DEFAULT NULL,
  `datePaid` date DEFAULT NULL,
  `varianceDiff` float DEFAULT NULL,
  `accountsTitle` varchar(50) DEFAULT NULL,
  `remarks` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`statementOfAccountID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statement_of_account`
--

LOCK TABLES `statement_of_account` WRITE;
/*!40000 ALTER TABLE `statement_of_account` DISABLE KEYS */;
/*!40000 ALTER TABLE `statement_of_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table1`
--

DROP TABLE IF EXISTS `table1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `table1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `callTime` time DEFAULT NULL,
  `date` date DEFAULT NULL,
  `origin` varchar(30) DEFAULT NULL,
  `destination` varchar(30) DEFAULT NULL,
  `client` int(11) DEFAULT NULL,
  `customer` int(11) DEFAULT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `plateNo` varchar(10) DEFAULT NULL,
  `WBNo` varchar(10) DEFAULT NULL,
  `driver` int(11) DEFAULT NULL,
  `helper` varchar(30) DEFAULT NULL,
  `truckType` varchar(20) DEFAULT NULL,
  `qty` float DEFAULT NULL,
  `driverSal` float DEFAULT NULL,
  `helperSal` float DEFAULT NULL,
  `billing` float DEFAULT NULL,
  `receivedBy` varchar(45) DEFAULT NULL,
  `receivedDateTime` datetime DEFAULT NULL,
  `entryFee` float DEFAULT NULL,
  `parking` float DEFAULT NULL,
  `tollFee` float DEFAULT NULL,
  `others` float DEFAULT NULL,
  `totalLiq` float DEFAULT NULL,
  `truckBudget` float DEFAULT NULL,
  `unliq` float DEFAULT NULL,
  `addLDriverSal` float DEFAULT NULL,
  `caHelper` float DEFAULT NULL,
  `addL` float DEFAULT NULL,
  `diesel` float DEFAULT NULL,
  `revenue` float DEFAULT NULL,
  `billedDate` date DEFAULT NULL,
  `phase` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `driverID_idx` (`driver`),
  KEY `clientID_idx` (`client`),
  KEY `customerID_idx` (`customer`),
  CONSTRAINT `clientID` FOREIGN KEY (`client`) REFERENCES `client` (`clientID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `customerID` FOREIGN KEY (`customer`) REFERENCES `customer` (`customerID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `driverID` FOREIGN KEY (`driver`) REFERENCES `driver` (`driverID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table1`
--

LOCK TABLES `table1` WRITE;
/*!40000 ALTER TABLE `table1` DISABLE KEYS */;
INSERT INTO `table1` VALUES (18,'01:00:00','2019-01-01','Abra, Danglas','Abra, Lagangilang',3,19,'tye','ABC1234567','ABC1234567',6,'Dad','FWD',10,10.5,10.5,1000,'test','2019-11-11 23:11:00',88.5,17.5,265.5,0.5,372,100,-272,10,10,5,3,589,'2019-09-12',NULL),(19,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,NULL,0,NULL,NULL,NULL,NULL,0,NULL,NULL);
/*!40000 ALTER TABLE `table1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tariff`
--

DROP TABLE IF EXISTS `tariff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tariff` (
  `tariffID` int(11) NOT NULL AUTO_INCREMENT,
  `airDestination` float DEFAULT NULL,
  `airDriver46Wheeler` float DEFAULT NULL,
  `airHelper46Wheeler` float DEFAULT NULL,
  `airDriver6Forwarder` float DEFAULT NULL,
  `airHelper6Forwarder` float DEFAULT NULL,
  `airDriver10Wheeler` float DEFAULT NULL,
  `airHelper10Wheeler` float DEFAULT NULL,
  `seaDestination` float DEFAULT NULL,
  `seaDriver46Wheeler` float DEFAULT NULL,
  `seaHelper46Wheeler` float DEFAULT NULL,
  `seaDriver6Forwarder` float DEFAULT NULL,
  `seaHelper6Forwarder` float DEFAULT NULL,
  `seaDriver10Wheeler` float DEFAULT NULL,
  `seaHelper10Wheeler` float DEFAULT NULL,
  PRIMARY KEY (`tariffID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tariff`
--

LOCK TABLES `tariff` WRITE;
/*!40000 ALTER TABLE `tariff` DISABLE KEYS */;
INSERT INTO `tariff` VALUES (5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `tariff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `truck_budget`
--

DROP TABLE IF EXISTS `truck_budget`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `truck_budget` (
  `truckBudgetID` int(11) NOT NULL AUTO_INCREMENT,
  `travelDate` date DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `particulars` varchar(50) DEFAULT NULL,
  `for` varchar(30) DEFAULT NULL,
  `client` varchar(30) DEFAULT NULL,
  `purchaseOrderOR` varchar(30) DEFAULT NULL,
  `liquidated` float DEFAULT NULL,
  `unliquidated` float DEFAULT NULL,
  PRIMARY KEY (`truckBudgetID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `truck_budget`
--

LOCK TABLES `truck_budget` WRITE;
/*!40000 ALTER TABLE `truck_budget` DISABLE KEYS */;
/*!40000 ALTER TABLE `truck_budget` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinformation`
--

DROP TABLE IF EXISTS `userinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinformation` (
  `userid` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `role` varchar(45) DEFAULT NULL,
  `employeeID` int(11) DEFAULT NULL,
  `phoneNumber` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinformation`
--

LOCK TABLES `userinformation` WRITE;
/*!40000 ALTER TABLE `userinformation` DISABLE KEYS */;
INSERT INTO `userinformation` VALUES (1,'Testing','12345',12345,'12345'),(2,'Testing2','123456',123456,'123456'),(3,'Testing3','1234567',12345678,'123456789');
/*!40000 ALTER TABLE `userinformation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'trucking'
--

--
-- Dumping routines for database 'trucking'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-05 22:37:38
