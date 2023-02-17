CREATE DATABASE  IF NOT EXISTS `obchod` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `obchod`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: obchod
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.24-MariaDB

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
-- Table structure for table `objednavka`
--

DROP TABLE IF EXISTS `objednavka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `objednavka` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Datum_obj` datetime NOT NULL,
  `Prosla_platba` tinyint(1) NOT NULL,
  `pob_id` int(11) DEFAULT NULL,
  `uz_id` int(11) DEFAULT NULL,
  `prod_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `pob_id` (`pob_id`),
  KEY `uz_id` (`uz_id`),
  KEY `prod_id` (`prod_id`),
  CONSTRAINT `objednavka_ibfk_1` FOREIGN KEY (`pob_id`) REFERENCES `pobocka` (`ID`),
  CONSTRAINT `objednavka_ibfk_2` FOREIGN KEY (`uz_id`) REFERENCES `uzivatel` (`ID`),
  CONSTRAINT `objednavka_ibfk_3` FOREIGN KEY (`prod_id`) REFERENCES `produkt` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objednavka`
--

LOCK TABLES `objednavka` WRITE;
/*!40000 ALTER TABLE `objednavka` DISABLE KEYS */;
/*!40000 ALTER TABLE `objednavka` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `objednavky_uzivatel`
--

DROP TABLE IF EXISTS `objednavky_uzivatel`;
/*!50001 DROP VIEW IF EXISTS `objednavky_uzivatel`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `objednavky_uzivatel` AS SELECT 
 1 AS `ID`,
 1 AS `Jmeno`,
 1 AS `Prijmeni`,
 1 AS `Email`,
 1 AS `Pocet_objednavek`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `pobocka`
--

DROP TABLE IF EXISTS `pobocka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pobocka` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Adresa` varchar(100) NOT NULL,
  `Cislo_popisne` int(11) NOT NULL,
  `PSC` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pobocka`
--

LOCK TABLES `pobocka` WRITE;
/*!40000 ALTER TABLE `pobocka` DISABLE KEYS */;
/*!40000 ALTER TABLE `pobocka` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prace`
--

DROP TABLE IF EXISTS `prace`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prace` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `pob_id` int(11) DEFAULT NULL,
  `zam_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `pob_id` (`pob_id`),
  KEY `zam_id` (`zam_id`),
  CONSTRAINT `prace_ibfk_1` FOREIGN KEY (`pob_id`) REFERENCES `pobocka` (`ID`),
  CONSTRAINT `prace_ibfk_2` FOREIGN KEY (`zam_id`) REFERENCES `zamestnanec` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prace`
--

LOCK TABLES `prace` WRITE;
/*!40000 ALTER TABLE `prace` DISABLE KEYS */;
/*!40000 ALTER TABLE `prace` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `prehled_objednavky`
--

DROP TABLE IF EXISTS `prehled_objednavky`;
/*!50001 DROP VIEW IF EXISTS `prehled_objednavky`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `prehled_objednavky` AS SELECT 
 1 AS `Datum_obj`,
 1 AS `Nazev`,
 1 AS `Rozmer`,
 1 AS `Barva`,
 1 AS `Cena`,
 1 AS `Jmeno`,
 1 AS `Prijmeni`,
 1 AS `Email`,
 1 AS `Prosla_platba`,
 1 AS `Adresa`,
 1 AS `Cislo_popisne`,
 1 AS `PSC`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `produkt`
--

DROP TABLE IF EXISTS `produkt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produkt` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Nazev` varchar(50) DEFAULT NULL,
  `Barva` varchar(20) NOT NULL,
  `Rozmer` enum('S','M','L','XL','XXL') NOT NULL,
  `Cena` float NOT NULL,
  `Dostupnost` tinyint(1) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produkt`
--

LOCK TABLES `produkt` WRITE;
/*!40000 ALTER TABLE `produkt` DISABLE KEYS */;
/*!40000 ALTER TABLE `produkt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uzivatel`
--

DROP TABLE IF EXISTS `uzivatel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `uzivatel` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Jmeno` varchar(50) NOT NULL,
  `Prijmeni` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Datum_nar` date NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uzivatel`
--

LOCK TABLES `uzivatel` WRITE;
/*!40000 ALTER TABLE `uzivatel` DISABLE KEYS */;
/*!40000 ALTER TABLE `uzivatel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zamestnanec`
--

DROP TABLE IF EXISTS `zamestnanec`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zamestnanec` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Jmeno` varchar(20) NOT NULL,
  `Prijmeni` varchar(20) NOT NULL,
  `Zacatek_prace` date NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zamestnanec`
--

LOCK TABLES `zamestnanec` WRITE;
/*!40000 ALTER TABLE `zamestnanec` DISABLE KEYS */;
/*!40000 ALTER TABLE `zamestnanec` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `objednavky_uzivatel`
--

/*!50001 DROP VIEW IF EXISTS `objednavky_uzivatel`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `objednavky_uzivatel` AS select `uzivatel`.`ID` AS `ID`,`uzivatel`.`Jmeno` AS `Jmeno`,`uzivatel`.`Prijmeni` AS `Prijmeni`,`uzivatel`.`Email` AS `Email`,count(`objednavka`.`ID`) AS `Pocet_objednavek` from (`uzivatel` join `objednavka` on(`uzivatel`.`ID` = `objednavka`.`uz_id`)) group by `uzivatel`.`ID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `prehled_objednavky`
--

/*!50001 DROP VIEW IF EXISTS `prehled_objednavky`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `prehled_objednavky` AS select `objednavka`.`Datum_obj` AS `Datum_obj`,`produkt`.`Nazev` AS `Nazev`,`produkt`.`Rozmer` AS `Rozmer`,`produkt`.`Barva` AS `Barva`,`produkt`.`Cena` AS `Cena`,`uzivatel`.`Jmeno` AS `Jmeno`,`uzivatel`.`Prijmeni` AS `Prijmeni`,`uzivatel`.`Email` AS `Email`,`objednavka`.`Prosla_platba` AS `Prosla_platba`,`pobocka`.`Adresa` AS `Adresa`,`pobocka`.`Cislo_popisne` AS `Cislo_popisne`,`pobocka`.`PSC` AS `PSC` from (((`objednavka` join `produkt`) join `uzivatel`) join `pobocka`) where `objednavka`.`pob_id` = `pobocka`.`ID` and `objednavka`.`uz_id` = `uzivatel`.`ID` and `objednavka`.`prod_id` = `produkt`.`ID` */;
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

-- Dump completed on 2023-02-03 22:31:14
