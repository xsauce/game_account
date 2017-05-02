-- MySQL dump 10.13  Distrib 5.6.24, for osx10.10 (x86_64)
--
-- Host: localhost    Database: game_account
-- ------------------------------------------------------
-- Server version	5.6.16

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
-- Table structure for table `game_close_bill_history`
--

DROP TABLE IF EXISTS `game_close_bill_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game_close_bill_history` (
  `pkid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `close_bill_check_point` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `fee_rate` double(16,2) NOT NULL,
  `total_final_money` double(16,2) NOT NULL,
  `total_money` double(16,2) NOT NULL,
  `total_fee` double(16,2) NOT NULL,
  `total_game_count` int(11) NOT NULL,
  PRIMARY KEY (`pkid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_close_bill_history`
--

LOCK TABLES `game_close_bill_history` WRITE;
/*!40000 ALTER TABLE `game_close_bill_history` DISABLE KEYS */;
INSERT INTO `game_close_bill_history` VALUES (4,'2017-04-30 16:00:00','2017-05-01 21:52:43','1970-01-01 00:00:00',0.05,-1019.00,0.00,1019.00,9),(6,'2017-04-30 23:59:00','2017-05-01 21:55:37','1970-01-01 00:00:00',0.05,-1113.00,0.00,1113.00,10),(7,'2017-05-02 16:00:54','2017-05-02 16:24:01','1970-01-01 00:00:00',0.05,-691.50,0.00,691.50,7);
/*!40000 ALTER TABLE `game_close_bill_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_close_bill_history_detail`
--

DROP TABLE IF EXISTS `game_close_bill_history_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game_close_bill_history_detail` (
  `pkid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `player_id` varchar(255) NOT NULL,
  `final_money` double(16,2) NOT NULL,
  `money` double(16,2) NOT NULL,
  `fee` double(16,2) NOT NULL,
  `game_count` int(11) NOT NULL,
  `history_pkid` int(10) unsigned NOT NULL,
  PRIMARY KEY (`pkid`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_close_bill_history_detail`
--

LOCK TABLES `game_close_bill_history_detail` WRITE;
/*!40000 ALTER TABLE `game_close_bill_history_detail` DISABLE KEYS */;
INSERT INTO `game_close_bill_history_detail` VALUES (9,'2017-05-01 21:52:43','1970-01-01 00:00:00','suki',1288.50,1410.00,121.50,2,4),(10,'2017-05-01 21:52:43','1970-01-01 00:00:00','大西瓜',570.00,600.00,30.00,1,4),(11,'2017-05-01 21:52:43','1970-01-01 00:00:00','叶落纷飞',-334.50,-330.00,4.50,2,4),(12,'2017-05-01 21:52:43','1970-01-01 00:00:00','牛牛',-711.50,-480.00,231.50,5,4),(13,'2017-05-01 21:52:43','1970-01-01 00:00:00','悠宝宝',-610.50,-570.00,40.50,4,4),(14,'2017-05-01 21:52:43','1970-01-01 00:00:00','浩浩',1225.50,1290.00,64.50,1,4),(15,'2017-05-01 21:52:43','1970-01-01 00:00:00','clare',-3427.50,-3360.00,67.50,4,4),(16,'2017-05-01 21:52:43','1970-01-01 00:00:00','kimi',-142.50,-120.00,22.50,2,4),(17,'2017-05-01 21:52:43','1970-01-01 00:00:00','alvinpan',-2040.00,-1950.00,90.00,4,4),(18,'2017-05-01 21:52:43','1970-01-01 00:00:00','micheal',1266.00,1440.00,174.00,3,4),(19,'2017-05-01 21:52:43','1970-01-01 00:00:00','joy',484.50,510.00,25.50,1,4),(20,'2017-05-01 21:52:43','1970-01-01 00:00:00','au',-720.00,-720.00,0.00,1,4),(21,'2017-05-01 21:52:43','1970-01-01 00:00:00','vincent',2133.00,2280.00,147.00,6,4),(35,'2017-05-01 21:55:37','1970-01-01 00:00:00','suki',370.50,390.00,19.50,1,6),(36,'2017-05-01 21:55:37','1970-01-01 00:00:00','king',-768.00,-570.00,198.00,7,6),(37,'2017-05-01 21:55:37','1970-01-01 00:00:00','叶落纷飞',1626.00,1860.00,234.00,6,6),(38,'2017-05-01 21:55:37','1970-01-01 00:00:00','人生如梦',-1012.50,-990.00,22.50,2,6),(39,'2017-05-01 21:55:37','1970-01-01 00:00:00','clare',-840.00,-840.00,0.00,1,6),(40,'2017-05-01 21:55:37','1970-01-01 00:00:00','悠宝宝',2274.00,2460.00,186.00,5,6),(41,'2017-05-01 21:55:37','1970-01-01 00:00:00','浩浩',-3660.00,-3660.00,0.00,1,6),(42,'2017-05-01 21:55:37','1970-01-01 00:00:00','牛牛',-720.00,-720.00,0.00,1,6),(43,'2017-05-01 21:55:37','1970-01-01 00:00:00','kimi',2365.50,2490.00,124.50,3,6),(44,'2017-05-01 21:55:37','1970-01-01 00:00:00','alvinpan',643.50,750.00,106.50,3,6),(45,'2017-05-01 21:55:37','1970-01-01 00:00:00','micheal',-3312.00,-3270.00,42.00,4,6),(46,'2017-05-01 21:55:37','1970-01-01 00:00:00','vincent',-445.50,-390.00,55.50,5,6),(47,'2017-05-01 21:55:37','1970-01-01 00:00:00','笑笑',2365.50,2490.00,124.50,1,6),(48,'2017-05-02 16:24:01','1970-01-01 00:00:00','笑笑',769.50,810.00,40.50,2,7),(49,'2017-05-02 16:24:01','1970-01-01 00:00:00','叶落纷飞',2707.50,2850.00,142.50,2,7),(50,'2017-05-02 16:24:01','1970-01-01 00:00:00','topset',-270.00,-270.00,0.00,1,7),(51,'2017-05-02 16:24:01','1970-01-01 00:00:00','人生如梦',114.00,120.00,6.00,1,7),(52,'2017-05-02 16:24:01','1970-01-01 00:00:00','clare',1702.50,1920.00,217.50,6,7),(53,'2017-05-02 16:24:01','1970-01-01 00:00:00','悠宝宝',-508.50,-480.00,28.50,2,7),(54,'2017-05-02 16:24:01','1970-01-01 00:00:00','牛牛',-720.00,-720.00,0.00,1,7),(55,'2017-05-02 16:24:01','1970-01-01 00:00:00','kimi',1452.00,1530.00,78.00,3,7),(56,'2017-05-02 16:24:01','1970-01-01 00:00:00','alvinpan',-5340.00,-5310.00,30.00,4,7),(57,'2017-05-02 16:24:01','1970-01-01 00:00:00','micheal',700.50,810.00,109.50,4,7),(58,'2017-05-02 16:24:01','1970-01-01 00:00:00','alexander',-1299.00,-1260.00,39.00,2,7);
/*!40000 ALTER TABLE `game_close_bill_history_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_close_bill_history_game`
--

DROP TABLE IF EXISTS `game_close_bill_history_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game_close_bill_history_game` (
  `pkid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `history_pkid` int(10) unsigned NOT NULL,
  `game_pkid` int(10) unsigned NOT NULL,
  PRIMARY KEY (`pkid`),
  KEY `idx_close_bill` (`history_pkid`),
  KEY `idx_game_id` (`game_pkid`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_close_bill_history_game`
--

LOCK TABLES `game_close_bill_history_game` WRITE;
/*!40000 ALTER TABLE `game_close_bill_history_game` DISABLE KEYS */;
INSERT INTO `game_close_bill_history_game` VALUES (3,'2017-05-01 21:52:43','1970-01-01 00:00:00',4,22),(4,'2017-05-01 21:52:43','1970-01-01 00:00:00',4,23),(5,'2017-05-01 21:52:43','1970-01-01 00:00:00',4,24),(6,'2017-05-01 21:52:43','1970-01-01 00:00:00',4,25),(7,'2017-05-01 21:52:43','1970-01-01 00:00:00',4,26),(8,'2017-05-01 21:52:43','1970-01-01 00:00:00',4,27),(9,'2017-05-01 21:52:43','1970-01-01 00:00:00',4,28),(10,'2017-05-01 21:52:43','1970-01-01 00:00:00',4,29),(11,'2017-05-01 21:52:43','1970-01-01 00:00:00',4,30),(22,'2017-05-01 21:55:37','1970-01-01 00:00:00',6,1),(23,'2017-05-01 21:55:37','1970-01-01 00:00:00',6,2),(24,'2017-05-01 21:55:37','1970-01-01 00:00:00',6,3),(25,'2017-05-01 21:55:37','1970-01-01 00:00:00',6,4),(26,'2017-05-01 21:55:37','1970-01-01 00:00:00',6,5),(27,'2017-05-01 21:55:37','1970-01-01 00:00:00',6,6),(28,'2017-05-01 21:55:37','1970-01-01 00:00:00',6,7),(29,'2017-05-01 21:55:37','1970-01-01 00:00:00',6,8),(30,'2017-05-01 21:55:37','1970-01-01 00:00:00',6,9),(31,'2017-05-01 21:55:37','1970-01-01 00:00:00',6,10),(32,'2017-05-02 16:24:01','1970-01-01 00:00:00',7,38),(33,'2017-05-02 16:24:01','1970-01-01 00:00:00',7,39),(34,'2017-05-02 16:24:01','1970-01-01 00:00:00',7,40),(35,'2017-05-02 16:24:01','1970-01-01 00:00:00',7,41),(36,'2017-05-02 16:24:01','1970-01-01 00:00:00',7,42),(37,'2017-05-02 16:24:01','1970-01-01 00:00:00',7,43),(38,'2017-05-02 16:24:01','1970-01-01 00:00:00',7,44);
/*!40000 ALTER TABLE `game_close_bill_history_game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_info`
--

DROP TABLE IF EXISTS `game_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game_info` (
  `pkid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `game_id` varchar(255) NOT NULL,
  `score_to_money_rate` double(16,2) NOT NULL DEFAULT '30.00',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `game_finish_datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `game_status` int(2) NOT NULL DEFAULT '0' COMMENT '0未结算，1完成结算',
  PRIMARY KEY (`pkid`),
  UNIQUE KEY `uidx_game_id` (`game_id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_info`
--

LOCK TABLES `game_info` WRITE;
/*!40000 ALTER TABLE `game_info` DISABLE KEYS */;
INSERT INTO `game_info` VALUES (1,'716878',30.00,'2017-05-01 00:12:04','2017-05-01 21:55:37','2017-05-01 00:12:04',1),(2,'554267',30.00,'2017-05-01 00:12:04','2017-05-01 21:55:37','2017-05-01 00:12:04',1),(3,'974462',30.00,'2017-05-01 00:12:04','2017-05-01 21:55:37','2017-05-01 00:12:04',1),(4,'376217',30.00,'2017-05-01 00:12:04','2017-05-01 21:55:37','2017-05-01 00:12:04',1),(5,'440777',30.00,'2017-05-01 00:12:04','2017-05-01 21:55:37','2017-05-01 00:12:04',1),(6,'906311',30.00,'2017-05-01 00:12:04','2017-05-01 21:55:37','2017-05-01 00:12:04',1),(7,'205257',30.00,'2017-05-01 00:12:04','2017-05-01 21:55:37','2017-05-01 00:12:04',1),(8,'405740',30.00,'2017-05-01 00:12:04','2017-05-01 21:55:37','2017-05-01 00:12:04',1),(9,'414983',30.00,'2017-05-01 00:12:04','2017-05-01 21:55:37','2017-05-01 00:12:04',1),(10,'703563',30.00,'2017-05-01 00:12:04','2017-05-01 21:55:37','2017-05-01 00:12:04',1),(22,'261896',30.00,'2017-05-01 21:14:25','2017-05-01 21:52:43','2017-05-01 21:14:25',1),(23,'220794',30.00,'2017-05-01 21:15:52','2017-05-01 21:52:43','2017-05-01 21:15:52',1),(24,'861572',30.00,'2017-05-01 21:17:33','2017-05-01 21:52:43','2017-05-01 21:17:33',1),(25,'228736',30.00,'2017-05-01 21:20:08','2017-05-01 21:52:43','2017-05-01 21:20:08',1),(26,'130553',30.00,'2017-05-01 21:22:25','2017-05-01 21:52:43','2017-05-01 21:22:25',1),(27,'984187',30.00,'2017-05-01 21:23:38','2017-05-01 21:52:43','2017-05-01 21:23:38',1),(28,'181800',30.00,'2017-05-01 21:25:13','2017-05-01 21:52:43','2017-05-01 21:25:13',1),(29,'302172',30.00,'2017-05-01 21:26:08','2017-05-01 21:52:43','2017-05-01 21:26:08',1),(30,'937497',30.00,'2017-05-01 21:27:09','2017-05-01 21:52:43','2017-05-01 21:27:09',1),(38,'204219',30.00,'2017-05-02 16:22:54','2017-05-02 16:24:01','2017-05-02 16:22:54',1),(39,'575839',30.00,'2017-05-02 16:22:54','2017-05-02 16:24:01','2017-05-02 16:22:54',1),(40,'347622',30.00,'2017-05-02 16:22:54','2017-05-02 16:24:01','2017-05-02 16:22:54',1),(41,'943852',30.00,'2017-05-02 16:22:54','2017-05-02 16:24:01','2017-05-02 16:22:54',1),(42,'774924',30.00,'2017-05-02 16:22:54','2017-05-02 16:24:01','2017-05-02 16:22:54',1),(43,'268470',30.00,'2017-05-02 16:22:54','2017-05-02 16:24:01','2017-05-02 16:22:54',1),(44,'259861',30.00,'2017-05-02 16:22:54','2017-05-02 16:24:01','2017-05-02 16:22:54',1);
/*!40000 ALTER TABLE `game_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_result`
--

DROP TABLE IF EXISTS `game_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game_result` (
  `pkid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `player_id` varchar(255) NOT NULL,
  `player_score` double(16,2) NOT NULL,
  `game_pkid` int(10) unsigned NOT NULL,
  PRIMARY KEY (`pkid`),
  UNIQUE KEY `game_result_game_id_IDX` (`game_pkid`,`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=209 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_result`
--

LOCK TABLES `game_result` WRITE;
/*!40000 ALTER TABLE `game_result` DISABLE KEYS */;
INSERT INTO `game_result` VALUES (1,'2017-05-01 00:12:04','1970-01-01 00:00:00','叶落纷飞',-17.00,1),(2,'2017-05-01 00:12:04','1970-01-01 00:00:00','king',26.00,1),(3,'2017-05-01 00:12:04','1970-01-01 00:00:00','vincent',19.00,1),(4,'2017-05-01 00:12:04','1970-01-01 00:00:00','clare',-28.00,1),(5,'2017-05-01 00:12:04','1970-01-01 00:00:00','悠宝宝',-24.00,2),(6,'2017-05-01 00:12:04','1970-01-01 00:00:00','alvinpan',33.00,2),(7,'2017-05-01 00:12:04','1970-01-01 00:00:00','vincent',15.00,2),(8,'2017-05-01 00:12:04','1970-01-01 00:00:00','牛牛',-24.00,2),(9,'2017-05-01 00:12:04','1970-01-01 00:00:00','悠宝宝',90.00,3),(10,'2017-05-01 00:12:04','1970-01-01 00:00:00','alvinpan',-46.00,3),(11,'2017-05-01 00:12:04','1970-01-01 00:00:00','king',78.00,3),(12,'2017-05-01 00:12:04','1970-01-01 00:00:00','浩浩',-122.00,3),(13,'2017-05-01 00:12:04','1970-01-01 00:00:00','alvinpan',38.00,4),(14,'2017-05-01 00:12:04','1970-01-01 00:00:00','vincent',3.00,4),(15,'2017-05-01 00:12:04','1970-01-01 00:00:00','micheal',-58.00,4),(16,'2017-05-01 00:12:04','1970-01-01 00:00:00','kimi',17.00,4),(17,'2017-05-01 00:12:04','1970-01-01 00:00:00','king',28.00,5),(18,'2017-05-01 00:12:04','1970-01-01 00:00:00','kimi',35.00,5),(19,'2017-05-01 00:12:04','1970-01-01 00:00:00','micheal',-45.00,5),(20,'2017-05-01 00:12:04','1970-01-01 00:00:00','vincent',-18.00,5),(21,'2017-05-01 00:12:04','1970-01-01 00:00:00','micheal',-34.00,6),(22,'2017-05-01 00:12:04','1970-01-01 00:00:00','vincent',-32.00,6),(23,'2017-05-01 00:12:04','1970-01-01 00:00:00','suki',13.00,6),(24,'2017-05-01 00:12:04','1970-01-01 00:00:00','叶落纷飞',53.00,6),(25,'2017-05-01 00:12:04','1970-01-01 00:00:00','king',-37.00,7),(26,'2017-05-01 00:12:04','1970-01-01 00:00:00','悠宝宝',15.00,7),(27,'2017-05-01 00:12:04','1970-01-01 00:00:00','叶落纷飞',-6.00,7),(28,'2017-05-01 00:12:04','1970-01-01 00:00:00','micheal',28.00,7),(29,'2017-05-01 00:12:04','1970-01-01 00:00:00','叶落纷飞',-15.00,8),(30,'2017-05-01 00:12:04','1970-01-01 00:00:00','kimi',31.00,8),(31,'2017-05-01 00:12:04','1970-01-01 00:00:00','king',-35.00,8),(32,'2017-05-01 00:12:04','1970-01-01 00:00:00','悠宝宝',19.00,8),(33,'2017-05-01 00:12:04','1970-01-01 00:00:00','king',-37.00,9),(34,'2017-05-01 00:12:04','1970-01-01 00:00:00','叶落纷飞',103.00,9),(35,'2017-05-01 00:12:04','1970-01-01 00:00:00','悠宝宝',-18.00,9),(36,'2017-05-01 00:12:04','1970-01-01 00:00:00','人生如梦',-48.00,9),(37,'2017-05-01 00:12:04','1970-01-01 00:00:00','叶落纷飞',-56.00,10),(38,'2017-05-01 00:12:04','1970-01-01 00:00:00','笑笑',83.00,10),(39,'2017-05-01 00:12:04','1970-01-01 00:00:00','人生如梦',15.00,10),(40,'2017-05-01 00:12:04','1970-01-01 00:00:00','king',-42.00,10),(117,'2017-05-01 21:14:25','1970-01-01 00:00:00','micheal',-52.00,22),(118,'2017-05-01 21:14:25','1970-01-01 00:00:00','vincent',-11.00,22),(119,'2017-05-01 21:14:25','1970-01-01 00:00:00','浩浩',43.00,22),(120,'2017-05-01 21:14:25','1970-01-01 00:00:00','大西瓜',20.00,22),(121,'2017-05-01 21:15:52','1970-01-01 00:00:00','micheal',116.00,23),(122,'2017-05-01 21:15:52','1970-01-01 00:00:00','au',-24.00,23),(123,'2017-05-01 21:15:52','1970-01-01 00:00:00','vincent',51.00,23),(124,'2017-05-01 21:15:52','1970-01-01 00:00:00','牛牛',-143.00,23),(125,'2017-05-01 21:17:33','1970-01-01 00:00:00','vincent',-11.00,24),(126,'2017-05-01 21:17:33','1970-01-01 00:00:00','kimi',-19.00,24),(127,'2017-05-01 21:17:33','1970-01-01 00:00:00','叶落纷飞',3.00,24),(128,'2017-05-01 21:17:33','1970-01-01 00:00:00','悠宝宝',27.00,24),(129,'2017-05-01 21:20:08','1970-01-01 00:00:00','micheal',-16.00,25),(130,'2017-05-01 21:20:08','1970-01-01 00:00:00','悠宝宝',-6.00,25),(131,'2017-05-01 21:20:08','1970-01-01 00:00:00','vincent',5.00,25),(132,'2017-05-01 21:20:08','1970-01-01 00:00:00','joy',17.00,25),(133,'2017-05-01 21:22:25','1970-01-01 00:00:00','悠宝宝',-23.00,26),(134,'2017-05-01 21:22:25','1970-01-01 00:00:00','alvinpan',-86.00,26),(135,'2017-05-01 21:22:25','1970-01-01 00:00:00','clare',-29.00,26),(136,'2017-05-01 21:22:25','1970-01-01 00:00:00','牛牛',138.00,26),(137,'2017-05-01 21:23:38','1970-01-01 00:00:00','牛牛',-32.00,27),(138,'2017-05-01 21:23:38','1970-01-01 00:00:00','alvinpan',-39.00,27),(139,'2017-05-01 21:23:38','1970-01-01 00:00:00','clare',45.00,27),(140,'2017-05-01 21:23:38','1970-01-01 00:00:00','vincent',26.00,27),(141,'2017-05-01 21:25:13','1970-01-01 00:00:00','clare',-20.00,28),(142,'2017-05-01 21:25:13','1970-01-01 00:00:00','suki',-34.00,28),(143,'2017-05-01 21:25:13','1970-01-01 00:00:00','alvinpan',46.00,28),(144,'2017-05-01 21:25:13','1970-01-01 00:00:00','牛牛',8.00,28),(145,'2017-05-01 21:26:08','1970-01-01 00:00:00','叶落纷飞',-14.00,29),(146,'2017-05-01 21:26:08','1970-01-01 00:00:00','悠宝宝',-17.00,29),(147,'2017-05-01 21:26:08','1970-01-01 00:00:00','vincent',16.00,29),(148,'2017-05-01 21:26:08','1970-01-01 00:00:00','kimi',15.00,29),(149,'2017-05-01 21:27:09','1970-01-01 00:00:00','clare',-108.00,30),(150,'2017-05-01 21:27:09','1970-01-01 00:00:00','alvinpan',14.00,30),(151,'2017-05-01 21:27:09','1970-01-01 00:00:00','牛牛',13.00,30),(152,'2017-05-01 21:27:09','1970-01-01 00:00:00','suki',81.00,30),(181,'2017-05-02 16:22:54','1970-01-01 00:00:00','micheal',69.00,38),(182,'2017-05-02 16:22:54','1970-01-01 00:00:00','clare',63.00,38),(183,'2017-05-02 16:22:54','1970-01-01 00:00:00','alvinpan',-108.00,38),(184,'2017-05-02 16:22:54','1970-01-01 00:00:00','牛牛',-24.00,38),(185,'2017-05-02 16:22:54','1970-01-01 00:00:00','micheal',4.00,39),(186,'2017-05-02 16:22:54','1970-01-01 00:00:00','clare',11.00,39),(187,'2017-05-02 16:22:54','1970-01-01 00:00:00','alvinpan',-21.00,39),(188,'2017-05-02 16:22:54','1970-01-01 00:00:00','笑笑',6.00,39),(189,'2017-05-02 16:22:54','1970-01-01 00:00:00','micheal',-31.00,40),(190,'2017-05-02 16:22:54','1970-01-01 00:00:00','clare',-15.00,40),(191,'2017-05-02 16:22:54','1970-01-01 00:00:00','alvinpan',20.00,40),(192,'2017-05-02 16:22:54','1970-01-01 00:00:00','alexander',26.00,40),(193,'2017-05-02 16:22:54','1970-01-01 00:00:00','悠宝宝',19.00,41),(194,'2017-05-02 16:22:54','1970-01-01 00:00:00','人生如梦',4.00,41),(195,'2017-05-02 16:22:54','1970-01-01 00:00:00','clare',45.00,41),(196,'2017-05-02 16:22:54','1970-01-01 00:00:00','alvinpan',-68.00,41),(197,'2017-05-02 16:22:54','1970-01-01 00:00:00','叶落纷飞',13.00,42),(198,'2017-05-02 16:22:54','1970-01-01 00:00:00','clare',26.00,42),(199,'2017-05-02 16:22:54','1970-01-01 00:00:00','alexander',-68.00,42),(200,'2017-05-02 16:22:54','1970-01-01 00:00:00','kimi',29.00,42),(201,'2017-05-02 16:22:54','1970-01-01 00:00:00','叶落纷飞',82.00,43),(202,'2017-05-02 16:22:54','1970-01-01 00:00:00','clare',-66.00,43),(203,'2017-05-02 16:22:54','1970-01-01 00:00:00','kimi',-1.00,43),(204,'2017-05-02 16:22:54','1970-01-01 00:00:00','micheal',-15.00,43),(205,'2017-05-02 16:22:54','1970-01-01 00:00:00','悠宝宝',-35.00,44),(206,'2017-05-02 16:22:54','1970-01-01 00:00:00','topset',-9.00,44),(207,'2017-05-02 16:22:54','1970-01-01 00:00:00','笑笑',21.00,44),(208,'2017-05-02 16:22:54','1970-01-01 00:00:00','kimi',23.00,44);
/*!40000 ALTER TABLE `game_result` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-02 22:09:52
