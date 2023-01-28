CREATE DATABASE  IF NOT EXISTS `thought_db` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `thought_db`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: thought_db
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `thoughts`
--

DROP TABLE IF EXISTS `thoughts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thoughts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `contents` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_toughts_users_idx` (`user_id`),
  CONSTRAINT `fk_toughts_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thoughts`
--

LOCK TABLES `thoughts` WRITE;
/*!40000 ALTER TABLE `thoughts` DISABLE KEYS */;
INSERT INTO `thoughts` VALUES (1,'Pensando pensamientos ','2023-01-28 17:59:17','2023-01-28 17:59:17',1),(2,'PioPioPio','2023-01-28 17:59:24','2023-01-28 17:59:24',1),(3,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu gravida nulla, venenatis varius sapien. Aliquam at dui et enim ullamcorper ornare. Aliquam ac ante blandit, bibendum augue non, ullamcorper dui. Pellentesque laoreet accumsan elit, varius pretium tortor euismod eget. Donec dapibus maximus tortor eu condimentum. Donec dignissim varius ipsum, vel posuere risus aliquam a. Aenean at malesuada velit. Mauris commodo dolor leo, at gravida lacus dictum eu. Sed aliquam odio nec diam condimentum, vel luctus erat rhoncus. Cras ultrices dignissim erat, in varius nisl sagittis quis. Sed varius turpis non sapien porta convallis. Ut quis eros at turpis fermentum.','2023-01-28 17:59:55','2023-01-28 17:59:55',1),(4,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ligula.','2023-01-28 18:03:15','2023-01-28 18:03:15',2),(5,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin neque felis, feugiat quis eros at, fermentum vulputate lorem. Praesent varius maximus egestas. Proin fringilla tincidunt ipsum at molestie. Cras eu laoreet augue. Etiam pellentesque malesuada mi quis mollis. Maecenas nec vestibulum odio, non ornare erat. Aliquam vehicula massa vitae convallis.','2023-01-28 18:04:34','2023-01-28 18:04:34',3),(6,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin neque felis, feugiat quis eros at, fermentum vulputate lorem. Praesent varius maximus egestas. Proin fringilla tincidunt ipsum at molestie. Cras eu laoreet augue. Etiam pellentesque malesuada mi quis mollis. Maecenas nec vestibulum odio, non ornare erat. Aliquam vehicula massa vitae convallis.','2023-01-28 18:04:36','2023-01-28 18:04:36',3),(7,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin neque felis, feugiat quis eros at, fermentum vulputate lorem. Praesent varius maximus egestas. Proin fringilla tincidunt ipsum at molestie. Cras eu laoreet augue. Etiam pellentesque malesuada mi quis mollis. Maecenas nec vestibulum odio, non ornare erat. Aliquam vehicula massa vitae convallis.','2023-01-28 18:04:37','2023-01-28 18:04:37',3);
/*!40000 ALTER TABLE `thoughts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-28 18:13:57
