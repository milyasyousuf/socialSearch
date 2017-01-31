-- MySQL dump 10.13  Distrib 5.7.16, for Linux (x86_64)
--
-- Host: localhost    Database: searcher
-- ------------------------------------------------------
-- Server version	5.7.16-0ubuntu0.16.04.1

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
-- Temporary view structure for view `locationName`
--

DROP TABLE IF EXISTS `locationName`;
/*!50001 DROP VIEW IF EXISTS `locationName`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `locationName` AS SELECT 
 1 AS `location`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!50001 DROP VIEW IF EXISTS `tags`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `tags` AS SELECT 
 1 AS `tag`,
 1 AS `tagcount`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `twitterSearch`
--

DROP TABLE IF EXISTS `twitterSearch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `twitterSearch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tweet` varchar(255) CHARACTER SET utf8 NOT NULL,
  `create_at` varchar(50) DEFAULT NULL,
  `tweetLang` varchar(10) DEFAULT NULL,
  `tweetUser` varchar(30) CHARACTER SET utf8 NOT NULL,
  `tweetUserId` varchar(50) DEFAULT NULL,
  `hashtag` varchar(200) DEFAULT NULL,
  `tag` varchar(50) DEFAULT NULL,
  `score` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `twitterSearch`
--

LOCK TABLES `twitterSearch` WRITE;
/*!40000 ALTER TABLE `twitterSearch` DISABLE KEYS */;
/*!40000 ALTER TABLE `twitterSearch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `twitterTrends`
--

DROP TABLE IF EXISTS `twitterTrends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `twitterTrends` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `location` varchar(20) DEFAULT NULL,
  `woeid` varchar(10) DEFAULT NULL,
  `created_at` varchar(20) DEFAULT NULL,
  `trendStart` varchar(20) DEFAULT NULL,
  `trendname` varchar(255) CHARACTER SET utf8 NOT NULL,
  `tweet_volume` varchar(100) DEFAULT NULL,
  `rightnow` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `timeNow` varchar(30) DEFAULT NULL,
  `tag` varchar(20) DEFAULT NULL,
  `typeTweets` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `twitterTrends`
--

LOCK TABLES `twitterTrends` WRITE;
/*!40000 ALTER TABLE `twitterTrends` DISABLE KEYS */;
INSERT INTO `twitterTrends` VALUES (1,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','HBLvSSGC',NULL,'2017-01-02 06:25:33','2017-01-02 11:%',NULL,NULL),(2,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','Quetta',NULL,'2017-01-02 06:25:33','2017-01-02 11:%',NULL,NULL),(3,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','HappyNewYear','776611','2017-01-02 06:25:33','2017-01-02 11:%','neutral','465966.6'),(4,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','Istanbul','19093','2017-01-02 06:25:33','2017-01-02 11:%','neutral','11455.8'),(5,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','Javed Hashmi',NULL,'2017-01-02 06:25:33','2017-01-02 11:%',NULL,NULL),(6,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','',NULL,'2017-01-02 06:25:33','2017-01-02 11:%',NULL,NULL),(7,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','New Year s Eve','241850','2017-01-02 06:25:34','2017-01-02 11:%','weak_negative','96740.0'),(8,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','2nd Test',NULL,'2017-01-02 06:25:34','2017-01-02 11:%',NULL,NULL),(9,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','Arsenal','265456','2017-01-02 06:25:34','2017-01-02 11:%','weak_positive','159273.6'),(10,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','Giroud','528195','2017-01-02 06:25:34','2017-01-02 11:%','weak_positive','211278.0'),(11,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','Coldplay','18326','2017-01-02 06:25:34','2017-01-02 11:%','neutral','14660.8'),(12,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','GOD Bless','132043','2017-01-02 06:25:34','2017-01-02 11:%','weak_positive','105634.4'),(13,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','YesWeKhan',NULL,'2017-01-02 06:25:34','2017-01-02 11:%',NULL,NULL),(14,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','ShiaGenocideReport2016','14379','2017-01-02 06:25:34','2017-01-02 11:%','weak_positive','5751.6'),(15,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','BBCagainstCPEC',NULL,'2017-01-02 06:25:34','2017-01-02 11:%',NULL,NULL),(16,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','GuloonaPekhawar',NULL,'2017-01-02 06:25:34','2017-01-02 11:%',NULL,NULL),(17,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','Iraq',NULL,'2017-01-02 06:25:34','2017-01-02 11:%',NULL,NULL),(18,'Pakistan','23424922','2017-01-02T06:17:06Z','2017-01-02T06:25:23Z','PanamaCase',NULL,'2017-01-02 06:25:34','2017-01-02 11:%',NULL,NULL);
/*!40000 ALTER TABLE `twitterTrends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `words`
--

DROP TABLE IF EXISTS `words`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `words` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(50) DEFAULT NULL,
  `score` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `words`
--

LOCK TABLES `words` WRITE;
/*!40000 ALTER TABLE `words` DISABLE KEYS */;
/*!40000 ALTER TABLE `words` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `youtube`
--

DROP TABLE IF EXISTS `youtube`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `youtube` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `videoIds` varchar(100) DEFAULT NULL,
  `title` varchar(500) DEFAULT NULL,
  `viewCount` double DEFAULT NULL,
  `likeCount` double DEFAULT NULL,
  `dislikeCount` double DEFAULT NULL,
  `favoriteCount` double DEFAULT NULL,
  `commentCount` double DEFAULT NULL,
  `publishedTime` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `youtube`
--

LOCK TABLES `youtube` WRITE;
/*!40000 ALTER TABLE `youtube` DISABLE KEYS */;
/*!40000 ALTER TABLE `youtube` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `locationName`
--

/*!50001 DROP VIEW IF EXISTS `locationName`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `locationName` AS select `twitterTrends`.`location` AS `location` from `twitterTrends` group by `twitterTrends`.`location` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `tags`
--

/*!50001 DROP VIEW IF EXISTS `tags`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `tags` AS select `twitterSearch`.`tag` AS `tag`,count(`twitterSearch`.`tag`) AS `tagcount` from `twitterSearch` where (`twitterSearch`.`hashtag` = 'HBLvSSGC') group by `twitterSearch`.`tag` order by `tagcount` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-02-01  0:55:04
