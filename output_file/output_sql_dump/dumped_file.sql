-- MySQL dump 10.13  Distrib 8.0.37, for Linux (x86_64)
--
-- Host: 172.25.0.1    Database: store_procedure
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `module_id` int NOT NULL DEFAULT '0',
  `product_id` int DEFAULT NULL,
  `product_type_id` int NOT NULL DEFAULT '0',
  `product_name` varchar(255) DEFAULT NULL,
  `product_type_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,77,29,'Ncell Topup via Bank','Card Server Payment'),(1,76,29,'SIM TV TOPUP VIA BANK','Card Server Payment'),(1,30,29,'NT Topup via Bank','Card Server Payment'),(1,133,29,'Wordlink Topup via Bank','Card Server Payment'),(1,89,29,'Smart Cell Topup via Bank','Card Server Payment'),(1,188,59,'Gajehada Khanepani','Water Payment : API'),(1,4,25,'Ncell Topup','Prepaid Bill Payment'),(1,19,35,'NT Prepaid Topup','Prepaid Topup'),(1,287,29,'Ncell Data Via Bank','Card Server Payment'),(1,125,59,'Ratnanagar Khanepani','Water Payment : API'),(1,73,59,'Pragatinagar Khanepani','Water Payment : API'),(1,203,59,'Khanepani Sansthan Pokhara, Hemja','Water Payment : API'),(1,2,12,'Send Money','Fund Transfer'),(1,106,59,'Shankarnagar Khanepani','Water Payment : API'),(1,382,59,'Hariwon Khanepani, Sarlahi','Water Payment : API'),(1,347,59,'Kahun Dharahara Khanepani','Water Payment : API'),(1,98,59,'Kawasoti Khanepani','Water Payment : API'),(1,165,59,'Jaluke Water Supply And Sanitation Users Organisation','Water Payment : API'),(1,178,59,'Rudrapur Khanepani','Water Payment : API'),(1,199,59,'Khanepani Sansthan Pokhara, Pardi','Water Payment : API'),(1,132,29,'Nepal Electricity Authority','Card Server Payment'),(1,88,37,'Smart Cell Topup','Topup'),(1,162,59,'Karahiya Khanepani upabhokta tatha Sarsafai Sanstha','Water Payment : API'),(2,43,11,'eSewa agent to BOK self','AGENT WITHDRAW SELF'),(1,280,59,'Charange Bhumigat Khanepani','Water Payment : API'),(1,75,70,'Nepal Electricity Authority','Nea Bill Payment'),(1,258,59,'Besisahar Khanepani','Water Payment : API'),(1,140,59,'Bharatpur Water Supply Management Board','Water Payment : API'),(1,93,59,'Itahari Khanepani','Water Payment : API'),(1,139,59,'Tulsipur Khanepani','Water Payment : API'),(1,21,24,'NT Postpaid Topup','Postpaid Topup'),(1,190,59,'Devdaha Khanepani','Water Payment : API'),(1,104,59,'Shivnagar Khanepani','Water Payment : API'),(2,11,2,'eSewa to NMB Bank','WITHDRAW'),(1,234,41,'Nepal Life Insurance Co. Ltd.','Insurance'),(1,200,59,'Khanepani Sansthan Pokhara, Bindiyabasini','Water Payment : API'),(1,118,59,'Mukundapur Khanepani','Water Payment : API'),(1,341,59,'Dhamilikuwa Khanepani','Water Payment : API'),(1,167,59,'Amarapuri Water Supply And Sanitation Users Organisation','Water Payment : API'),(1,257,92,'GIME Revenue TSA Account - eSewa','Government Payment'),(1,246,59,'Dudrakshya Khanepani','Water Payment : API'),(1,288,29,'Nepal Telecom Data Pack Service Via Bank','Card Server Payment'),(1,293,59,'Indrayani Khanepani','Water Payment : API'),(1,126,59,'Gaindakot Khanepani','Water Payment : API'),(1,158,59,'Motipur Khanepani','Water Payment : API'),(1,35,59,'Lekhnath Khanepani','Water Payment : API'),(1,161,68,'WorldLink','World Link Payment'),(1,87,59,'Balkot Khanepani','Water Payment : API'),(1,107,59,'Anandaban Shankarnagar Khanepani','Water Payment : API'),(1,325,80,'eScrow Service','Money Transfer'),(1,33,37,'Dish Home Topup','Topup'),(1,134,29,'Vianet Payment via Bank','Card Server Payment'),(1,206,59,'Khanepani Sansthan Butwal','Water Payment : API'),(2,9,2,'eSewa to Citizens Bank','WITHDRAW'),(1,315,4,'Saurya Airlines Request for Refund','Air Ticket'),(1,192,59,'Tamnagar Khanepani','Water Payment : API'),(2,57,12,'eSewa agent to NIC Asia','AGENT WITHDRAW'),(1,357,59,'Tamsariya Khanepani','Water Payment : API'),(1,369,59,'Balambu 7,8,9 Khanepani','Water Payment : API'),(1,256,59,'Pathari Khanepani','Water Payment : API'),(1,251,59,'Shree Khudunabari arjundhara Khanepani','Water Payment : API'),(1,127,59,'Parsa Khanepani','Water Payment : API'),(1,306,59,'Kerwani Khanepani','Water Payment : API'),(1,110,37,'NT FTTH','Topup'),(1,224,59,'GAURADAHA KHANEPANI','Water Payment : API'),(1,101,59,'Panchanagar Khanepani','Water Payment : API'),(1,252,92,'RBB Revenue TSA Account - eSewa','Government Payment'),(1,201,59,'Birtamod Khanepani','Water Payment : API'),(1,172,59,'Namuna Shivanagar Khanepani (Vijayanagar Khanepani)','Water Payment : API'),(1,193,59,'Surunga Khanepani','Water Payment : API'),(1,327,84,'Chhimek Laghubitta Bittiya Sanstha','Generic Token Payment'),(2,44,12,'eSewa agent to Century','AGENT WITHDRAW'),(2,47,12,'eSewa agent to Everest','AGENT WITHDRAW'),(1,218,37,'Ncell Pack','Topup'),(1,91,80,'Cash In','Money Transfer'),(1,197,59,'Damak Khanepani','Water Payment : API'),(1,214,43,'Nagarik Cable Link','ISP Payment'),(1,275,59,'Parasi Khanepani','Water Payment : API'),(1,232,59,'Lalbandi khanepani','Water Payment : API'),(1,116,59,'Karahiya Khanepani','Water Payment : API'),(1,318,43,'DishHome FIBERNET','ISP Payment'),(2,58,12,'eSewa agent to NMB','AGENT WITHDRAW'),(1,228,59,'SAINAMAINA KHANEPANI','Water Payment : API'),(1,316,95,'Fonepay Payment','Fonepay Settlement'),(2,68,12,'eSewa Agent to Global','AGENT WITHDRAW'),(1,311,59,'Godawari Khanepani','Water Payment : API'),(1,241,59,'Lekhnath Saha Lagani Project','Water Payment : API'),(1,236,59,'Naya Naikap Khanepani','Water Payment : API'),(1,307,59,'Siddhipur Khanepani','Water Payment : API'),(1,319,59,'Shiva Parbati Khanepani','Water Payment : API'),(2,82,12,'eSewa agent to NIBL','AGENT WITHDRAW'),(1,321,59,'Tikathali Khanepani','Water Payment : API'),(1,235,59,'Katahari Khanepani','Water Payment : API'),(1,85,59,'Indrapur Khanepani','Water Payment : API'),(1,137,59,'Pandobazar Khanepani Yojana Jal Upabhokta Samittee','Water Payment : API'),(1,86,59,'Kushma Shivalaya Khanepani','Water Payment : API'),(1,303,41,'SuryaJyoti Life Insurance Co. Ltd.','Insurance'),(1,149,59,'Baglung Khanepani','Water Payment : API'),(1,244,59,'Bhaluhi khanepani','Water Payment : API'),(1,191,59,'Bhupu Sainik Khanepani','Water Payment : API'),(1,100,59,'Katunje Khanepani','Water Payment : API'),(1,22,33,'NT ADSL Topup - Unlimited','ADSL Unlimited Topup'),(2,25,2,'eSewa to Mahalaxmi Bikas Bank','WITHDRAW'),(1,148,59,'Birendranagar Khanepani','Water Payment : API'),(1,259,92,'Kumari Bank Revenue TSA Account-eSewa','Government Payment'),(2,8,2,'eSewa to Everest Bank Ltd.','WITHDRAW'),(1,374,59,'Shivamandir Khanepani , Kawasoti','Water Payment : API'),(1,135,59,'Nayagaun Khanepani','Water Payment : API'),(1,332,59,'Brihat Khanepani','Water Payment : API'),(1,290,84,'Jeevan Bikas laghubitta Bittiya Sanstha','Generic Token Payment'),(1,84,59,'Mangadh Khanepani','Water Payment : API'),(1,154,59,'Sau Farsatikar Khanepani','Water Payment : API'),(1,147,59,'Beni Khanepani','Water Payment : API'),(1,92,5,'Vianet','Internet Bill'),(1,204,83,'Prabhu TV','TV Payment'),(1,105,59,'Surkhet Khanepani','Water Payment : API'),(1,243,59,'Kolhuwa Khanepani','Water Payment : API'),(1,266,59,'Lakhanpur Khanepani Tatha Sarsafai Upabhokta Samiti','Water Payment : API'),(1,270,59,'Tokha Khanepani','Water Payment : API'),(1,202,59,'Khanepani Sansthan Banepa','Water Payment : API'),(2,61,12,'eSewa agent to RBB','AGENT WITHDRAW'),(2,59,12,'eSewa agent to Prabhu','AGENT WITHDRAW'),(1,151,59,'Sandhikharka Khanepani Tatha Sarsaphai','Water Payment : API'),(1,131,59,'Nijgadh Khanepani','Water Payment : API'),(1,359,59,'Bidur khanepani','Water Payment : API'),(1,329,59,'Khanepani Sansthan Rajbiraj','Water Payment : API'),(2,7,2,'eSewa to NIC Asia Bank','WITHDRAW'),(1,157,59,'Urlabari Khanepani','Water Payment : API'),(1,31,47,'BUDDHA AIR','Airline Ticketing'),(2,67,12,'eSewa agent to Sunrise','AGENT WITHDRAW'),(1,323,59,'Sipadol Khanepani','Water Payment : API'),(2,5,2,'eSewa to Sunrise Bank Ltd.','WITHDRAW'),(1,283,37,'Nepal Telecom Data Pack Service','Topup'),(1,168,59,'Simara Khanepani','Water Payment : API'),(1,109,59,'Dhulikhel Khanepani','Water Payment : API'),(1,286,29,'Prabhu TV Via Bank','Card Server Payment'),(1,181,59,'Arungkhola Khanepani','Water Payment : API'),(1,260,18,'eSewa Travels and Tours Web','Epay'),(1,90,59,'Budhabare Khanepani','Water Payment : API'),(1,378,59,'Mayadevi Khanepani, Rupandehi','Water Payment : API'),(1,95,59,'Dadhikot Khanepani','Water Payment : API'),(1,83,47,'SHREE AIRLINES','Airline Ticketing'),(1,163,59,'Rajahar Water Supply And Sanitation Users\' Organisation','Water Payment : API'),(1,138,59,'KAKARVITTA KHANEPANI','Water Payment : API'),(1,143,59,'Gunjanagar Khanepani','Water Payment : API'),(1,304,41,'ASIAN LIFE INSURANCE COMPANY LTD.','Insurance'),(1,239,41,'Foreign Employment Welfare Fund','Insurance'),(1,373,41,'Sun Nepal Life - DOFE','Insurance'),(1,20,26,'NT Landline Payment','Landline Topup'),(1,284,59,'Radhakrishna Khanepani','Water Payment : API'),(1,296,59,'Gajedi 2 Bakalghad Khanepani','Water Payment : API'),(1,170,59,'Chandragadi Khanepani','Water Payment : API'),(2,54,12,'eSewa agent to Mahalaxmi','AGENT WITHDRAW'),(2,62,12,'eSewa agent to Sanima','AGENT WITHDRAW'),(2,39,12,'eSewa Agent to Nabil bank','AGENT WITHDRAW'),(1,119,59,'Waling Khanepani','Water Payment : API'),(1,343,59,'Naumule Khanepani','Water Payment : API'),(1,279,59,'Sundar Bazar Khanepani','Water Payment : API'),(1,171,59,'Sunawal Khanepani','Water Payment : API'),(1,194,59,'Dibyapuri Khanepani','Water Payment : API'),(2,130,26,'Linked Account Withdraw','Linked Account Withdraw'),(2,17,2,'eSewa to Garima Dev. Bank','WITHDRAW'),(2,46,12,'eSewa agent to Civil','AGENT WITHDRAW'),(1,129,59,'Attariya Khanepani','Water Payment : API'),(2,3,2,'eSewa to Global IME Bank','WITHDRAW'),(1,263,59,'Deurali Hupsekot Khanepani','Water Payment : API'),(1,342,43,'CG Communications','ISP Payment'),(1,150,59,'Belbari Khanepani','Water Payment : API'),(1,320,59,'Buddhanagar Khanepani','Water Payment : API'),(1,298,41,'RELIABLE NEPAL LIFE INSURANCE LIMITED','Insurance'),(1,375,59,'Phulbari Khanepani , Butwal','Water Payment : API'),(2,55,12,'eSewa agent to Muktinath','AGENT WITHDRAW'),(2,51,12,'eSewa agent to Laxmi','AGENT WITHDRAW'),(1,196,59,'Tikapur Khanepani','Water Payment : API'),(1,182,59,'Pragatinagar Khanepani','Water Payment : API'),(1,209,59,'Khanepani Sansthan Dhangadi','Water Payment : API'),(1,99,59,'Lubhoo Khanepani','Water Payment : API'),(2,50,12,'eSewa agent to Kumari','AGENT WITHDRAW'),(1,177,59,'Pa. Amawa Khanepani','Water Payment : API'),(1,136,81,'JYOTI LIFE INSURANCE COMPANY LTD','Convergent Payment'),(1,310,59,'Dumarwana Khanepani','Water Payment : API'),(1,345,43,'Dish Home Combo Package','ISP Payment'),(1,155,59,'Gothatar Bhaimal Khanepani','Water Payment : API'),(2,18,2,'eSewa to  Kamana Sewa Bikas Bank Ltd.','WITHDRAW'),(1,212,59,'Khanepani Sansthan Mahendranagar','Water Payment : API'),(2,56,12,'eSewa agent to Nepal Bank','AGENT WITHDRAW'),(2,66,12,'eSewa agent to Siddhartha','AGENT WITHDRAW'),(1,295,59,'Aalapot Khanepani','Water Payment : API'),(1,262,59,'Motipur Semlar Khanepani Upabhokta Tatha Sarsafai Sanstha','Water Payment : API'),(2,81,12,'eSewa agent to Nepal SBI Bank','AGENT WITHDRAW'),(1,312,59,'Jante Khanepani','Water Payment : API'),(1,328,59,'KUKL - MAHARAJGUNG','Water Payment : API'),(2,10,2,'eSewa to Rastriya Banijya Bank','WITHDRAW'),(1,350,59,'Jhalari Khanepani','Water Payment : API'),(1,254,59,'Netragunj Khanepani','Water Payment : API'),(1,211,59,'Khanepani Sansthan Biratnagar','Water Payment : API'),(2,71,12,'eSewa agent to Best finance','AGENT WITHDRAW'),(2,23,2,'eSewa to Siddhartha Bank Ltd.','WITHDRAW'),(2,12,2,'eSewa to Kumari Bank','WITHDRAW'),(1,248,90,'Manakamana Cable Car','Utility'),(1,264,43,'Subisu Cablenet','ISP Payment'),(2,52,12,'eSewa agent to Lumbini','AGENT WITHDRAW'),(1,123,59,'S S Khanepani and Suppliers','Water Payment : API'),(1,238,59,'Bardibas Khanepani','Water Payment : API'),(1,365,84,'Hulas Fin Service Ltd.','Generic Token Payment'),(1,300,41,'Gurans Life Insurance Co. Ltd.','Insurance'),(1,207,72,'M.A.W. Investment Pvt. Ltd.','Banks And Financial Services'),(1,230,59,'Chundevi Khanepani','Water Payment : API'),(1,223,18,'NEPAL S.B.I. - Meroshare','Epay'),(1,117,5,'Web Networks','Internet Bill'),(1,276,59,'Lasune Khanepani','Water Payment : API'),(1,309,59,'Danchhi Bhadrabas Khanepani','Water Payment : API'),(1,184,59,'Semlar khanepani','Water Payment : API'),(1,113,59,'Adarsha Nagar Khanepani','Water Payment : API'),(1,267,91,'eSewa Money Transfer Outside Valley','Remittance Service'),(1,289,29,'Broadlink Network Via Bank','Card Server Payment'),(1,324,59,'Sasambhu Thula Ghar Khanepani Tatha Sarsafai Upabhokta Samiti','Water Payment : API'),(1,141,59,'Paschim Kalikanagar Khanepani','Water Payment : API'),(1,219,18,'Sanima Capital - Meroshare','Epay'),(1,221,18,'Garima Capital Limited - Meroshare','Epay'),(1,299,41,'Sun Nepal Life Insurance Company Limited','Insurance'),(1,278,59,'Mulpani Shankhadevi Khanepani','Water Payment : API'),(1,240,59,'Katunje Subarneshowr Khanepani','Water Payment : API'),(1,348,59,'Bhate Dhikur Khanepani','Water Payment : API'),(1,114,59,'Suryabinayak Khanepani','Water Payment : API'),(1,336,59,'Khanepani Sansthan Taulihawa','Water Payment : API'),(2,1,2,'eSewa to Nabil bank','WITHDRAW'),(1,317,59,'Chandranigahpur Khanepani','Water Payment : API'),(1,102,59,'Banganga Khanepani','Water Payment : API'),(1,285,59,'Chisapani Khanepani','Water Payment : API'),(1,261,59,'Jhorahat Khanepani Tatha Sarsafai Mul Upabhokta Samiti','Water Payment : API'),(2,45,12,'eSewa agent to Citizen','AGENT WITHDRAW'),(1,160,59,'Ishworpur Khanepani','Water Payment : API'),(1,164,59,'Devsiddha khanepani Devinagar, Butwal','Water Payment : API'),(1,146,5,'Classic Tech','Internet Bill'),(1,301,41,'Mahalaxmi Life Insurance Co. Ltd.','Insurance'),(1,142,59,'Khairenitar Khanepani','Water Payment : API'),(1,128,59,'Piple Khanepani','Water Payment : API'),(1,360,59,'Shree Shanti Basti Khanepani','Water Payment : API'),(1,302,41,'PRABHU LIFE INSURANCE LIMITED','Insurance'),(1,159,59,'Triyuga Khanepani','Water Payment : API'),(1,354,59,'Dhobidhunga Tallo Bhangal Khanepani','Water Payment : API'),(1,381,59,'Karmaiya Khanepani, Sarlahi','Water Payment : API'),(1,32,47,'SAURYA AIRLINES','Airline Ticketing'),(1,97,18,'QFX Labim','Epay'),(1,326,59,'katrai Bajar Naya Khanepani','Water Payment : API'),(1,380,59,'Naharpur Khanepani , Butwal','Water Payment : API'),(1,352,59,'Chasidol Khanepani','Water Payment : API'),(1,242,59,'Ramnagar Brihat Khanepani','Water Payment : API'),(1,250,59,'Simkhola Khanepani','Water Payment : API'),(1,205,59,'Khanepani Sansthan Bhairahawa','Water Payment : API'),(1,213,59,'Khanepani Sansthan Birgunj','Water Payment : API'),(1,124,59,'Dhulabari Khanepani','Water Payment : API'),(2,60,12,'eSewa agent to Prime','AGENT WITHDRAW'),(1,361,84,'Jagdamba Credit & Investment.','Generic Token Payment'),(1,353,59,'Gagalphedi Khanepani','Water Payment : API'),(1,29,47,'YETI AIRLINES','Airline Ticketing'),(1,217,59,'DUHABI KHANEPANI YOJANA MUL UPOBHOKTA SAMITI','Water Payment : API'),(1,185,18,'American Life Insurance Co.','Epay'),(1,370,59,'SiddhaBageshwori Water Supply','Water Payment : API'),(1,277,59,'Belahani Khanepani','Water Payment : API'),(1,376,59,'Chainpur Khanepani (Kusum Khola)','Water Payment : API'),(1,156,59,'Kohalpur Khanepani','Water Payment : API'),(1,372,59,'Sano Patihani Khanepani','Water Payment : API'),(2,53,12,'eSewa agent to Machhapuchchhre','AGENT WITHDRAW'),(1,339,23,'Bussewa 5 -DIRECT','Travel'),(2,65,12,'eSewa agent to Shine Resunga','AGENT WITHDRAW'),(1,153,59,'Charali khanepani','Water Payment : API'),(2,6,2,'eSewa to Prabhu Bank Ltd.','WITHDRAW'),(1,269,59,'Ichangu Narayan Khanepani aayojana mul upabhokta samiti','Water Payment : API'),(1,233,18,'Sanima Reliance Life Insurance Ltd.','Epay'),(1,173,18,'Amarapuri Khanepani','Epay'),(1,176,18,'Anandaban Shankarnagar Water Supply and Sanitation Users\' Committee','Epay'),(1,344,18,'Bijayanagar Khanepani, Chitwan','Epay'),(1,187,18,'CHARALI SANA SAHARI KHANEPANI TATHA SARSAFAI UPAVOKTA SASTHA','Epay'),(1,282,18,'Charange Bhumigat Khanepani Tatha Sarsafai Sanstha','Epay'),(1,215,18,'Giandakot','Epay'),(1,108,18,'Itahari Khanepani Reconciliation','Epay'),(1,166,18,'Jaluke Khanepani','Epay'),(1,231,18,'Karahiya Khanepani','Epay'),(1,121,18,'Kawasoti Khanepani - Mobile Payment','Epay'),(1,305,18,'Kerwani Water Supply Consumers And Sanitation Association','Epay'),(1,273,18,'Khanepani sansthan Mahendranagar - set','Epay'),(1,272,18,'Khanepani Sansthan Pokhara, Hemja','Epay'),(1,225,18,'Khanepani Sansthan Pokhara, Pardi','Epay'),(1,281,18,'Lasune Khola Khanepani Tatha Sarsafai Upobhokta Samiti','Epay'),(1,80,18,'Lekhnath Khanepani Mobile Apps','Epay'),(1,366,18,'Machchhegaun Khanepani','Epay'),(1,216,18,'Mukundapur','Epay'),(1,335,18,'Padampokhari Khanepani, Hetauda-12, Pantale','Epay'),(1,367,18,'Raktedunga Khanepani','Epay'),(1,249,18,'Semlar khanepani','Epay'),(1,122,18,'Shankarnagar Khanepani - Mobile Payment','Epay'),(1,385,18,'Tamsariya Khanepani','Epay'),(1,333,18,'Pithuwa Khanepani','Epay'),(1,152,59,'Rampur Khanepani','Water Payment : API'),(1,111,59,'Sukkhad Darakh Khanepani','Water Payment : API'),(2,36,2,'eSewa to Nepal Bank Limited','WITHDRAW'),(1,363,59,'Jahada-Manhari Khanepani','Water Payment : API'),(1,271,59,'Jimma dada Khanepani','Water Payment : API'),(1,96,37,'Mero TV','Topup'),(1,253,59,'Parbat Beni Khanepani','Water Payment : API'),(1,294,59,'Narti Khanepani','Water Payment : API'),(2,49,12,'eSewa agent to Jyoti','AGENT WITHDRAW'),(1,322,59,'Badera Khanepani','Water Payment : API'),(1,94,18,'Sociair SMS','Epay'),(1,245,59,'Jansewa Khanepani','Water Payment : API'),(2,78,15,'Siddharthabank_Free Withdraw','FREE_WITHDRAW'),(1,377,59,'Suda Town Khanepani','Water Payment : API'),(2,38,2,'eSewa to ICFC Finance Limited','WITHDRAW'),(2,13,2,'eSewa to Machhapuchchhre Bank Ltd.','WITHDRAW'),(1,144,59,'Meghauli Khanepani','Water Payment : API'),(1,337,84,'Pals Network','Generic Token Payment'),(1,379,59,'Narayani Saha Lagani Khanepani , Nawalaparasi','Water Payment : API'),(1,351,59,'Bhagatpur Nimbukheda Khanepani','Water Payment : API'),(2,48,12,'eSewa agent to Garima','AGENT WITHDRAW'),(1,220,18,'Mega Capital Markets - Meroshare','Epay'),(1,334,18,'British Council Services Nepal pvt. Ltd','Epay'),(1,387,59,'Shree Lamki Sana Sahari Khanepani','Water Payment : API'),(2,26,2,'eSewa to Muktinath Bikas Bank','WITHDRAW'),(2,27,2,'eSewa to Laxmi Bank Ltd.','WITHDRAW'),(1,268,59,'Devchuli Khanepani Tatha Sarsafai Upabhokta Sanstha','Water Payment : API'),(1,346,43,'Dish Home Yearly Offer','ISP Payment'),(1,371,59,'Bojhepani Khanepani','Water Payment : API'),(1,362,59,'Bindabasini Mahankal Khanepani','Water Payment : API'),(1,313,47,'Buddha Air Request For Refund','Airline Ticketing'),(2,69,2,'eSewa to Nepal SBI Bank Ltd.','WITHDRAW'),(2,16,2,'eSewa to Sanima Bank Ltd.','WITHDRAW'),(1,355,59,'Chandragadi (Dosro) Khanepani','Water Payment : API'),(1,349,59,'Tindhara Khanepani','Water Payment : API'),(1,103,18,'QFX Civil','Epay'),(1,237,59,'Tinthana khanepani','Water Payment : API'),(2,74,2,'eSewa to Nepal Investment Bank Ltd.','WITHDRAW'),(1,189,59,'Padampur Khanepani','Water Payment : API'),(1,247,59,'Mahadevsthan Matatirtha Khanepani','Water Payment : API'),(1,356,59,'Sano Bharyang Silandol Khanepani','Water Payment : API'),(2,28,2,'eSewa to Prime Commercial Bank Ltd.','WITHDRAW'),(1,145,18,'IDP IELTS','Epay'),(1,115,83,'Sky TV','TV Payment'),(1,291,18,'Office of Rector, Curriculum Development Center, Tribhuvan University','Epay'),(2,15,2,'eSewa to Shine Resunga Dev. Bank','WITHDRAW'),(2,70,2,'eSewa to Manjushree Finance Limited','WITHDRAW'),(1,179,59,'Bhaluwang Khanepani','Water Payment : API'),(2,63,12,'eSewa agent to Saptakoshi','AGENT WITHDRAW'),(1,210,59,'Khanepani Sansthan Bhadrapur','Water Payment : API'),(1,386,59,'Golaghat Khanepani, Chitwan','Water Payment : API'),(2,37,2,'eSewa to Agriculture Development Bank Limited','WITHDRAW'),(1,34,58,'SIM TV','Sim Tv Payment'),(1,368,43,'WIFI Nepal Pvt. Ltd.','ISP Payment'),(1,208,59,'Khanepani Sansthan Janakpur','Water Payment : API'),(1,338,23,'Bussewa 10-DIRECT','Travel'),(1,384,84,'Deprosc Laghubitta Bittiya Sanstha Limited','Generic Token Payment'),(1,112,59,'Shanischare Khanepani','Water Payment : API'),(1,391,94,'SSF Payment - Foreign','Other State-Owned Entities'),(1,265,23,'Offer 14 Direct','Travel'),(1,222,18,'Online Securities - Meroshare','Epay'),(1,308,84,'Nirdhan Utthan Laghubitta Bittiya Sanstha','Generic Token Payment'),(1,390,59,'Bhorletar Khanepani, Lamjung','Water Payment : API'),(2,24,2,'eSewa to Jyoti Bikas Bank','WITHDRAW'),(1,388,18,'MDAC Sports Pvt. Ltd','Epay'),(1,330,59,'Khanepani Sansthan Lahan','Water Payment : API'),(1,331,59,'Khanepani Sansthan Gaushala','Water Payment : API'),(2,79,15,'Kumari  Bank_Free Withdraw','FREE_WITHDRAW'),(1,169,18,'Regal Cinemas Pvt. Ltd.','Epay'),(2,64,12,'eSewa agent to Shangrila','AGENT WITHDRAW'),(1,389,18,'Panauti Buspark','Epay'),(2,42,12,'eSewa Agent to ADBL','AGENT WITHDRAW'),(1,226,18,'ICAN - Final Examination Fee','Epay'),(1,195,59,'Gundu Khanepani','Water Payment : API'),(1,314,18,'Mahalxmi Life Insurance Temp Transfer','Epay'),(1,72,29,'Dish Home Topup via Bank','Card Server Payment'),(1,364,84,'Nerude Laghubitta Bittiya Sanstha Limited','Generic Token Payment'),(1,120,43,'Pokhara Internet','ISP Payment'),(1,14,28,'Nabil Bank Credit Card','Credit Card Payment'),(1,395,18,'Banganga and Gajehada bhupu sainik khanepani','Epay'),(1,183,18,'Bharatpur khanepani - chitwan','Epay'),(1,398,18,'Bhojepani Settlement','Epay'),(1,340,18,'Brihat Khanepani Bagmati','Epay'),(1,198,18,'Devdaha Khanepani - SET','Epay'),(1,186,18,'GAJEHADA KHANEPANI UPABHOKTA TATHA SARSAFAI SAMITI','Epay'),(1,292,18,'Indrayani Khanepani Tatha Sarsafai Upabhokta Samiti','Epay'),(1,396,18,'Jaluke KP Sett','Epay'),(1,399,18,'Kahun Dharahara Khanepani','Epay'),(1,174,18,'Karahiya Makrahar Khanepani','Epay'),(1,394,18,'Kawasoti settlement','Epay'),(1,274,18,'Khanepani Sansthan Pokhara, Bindiyabasini - Set','Epay'),(1,392,18,'Lekhnath Khanepani','Epay'),(1,255,18,'Lekhnath Saha Lagani','Epay'),(1,358,18,'Naumule Khanepani','Epay'),(1,180,18,'Paschim Kalikanagar Khanepani','Epay'),(1,175,18,'Pragatinagar Khanepani','Epay'),(1,397,18,'Shanischare Khanepani	-Sett','Epay'),(1,393,18,'Shankarnagar settlement','Epay'),(1,297,18,'SIDDHIPUR WATER AND SANITATION','Epay'),(1,227,18,'Simara Khanepani','Epay'),(1,229,59,'Thankot Khanepani','Water Payment : API'),(1,383,59,'Tankisinwari Khanepani','Water Payment : API'),(2,40,11,'eSewa agent to Global Self','AGENT WITHDRAW SELF'),(2,41,12,'eSewa Agent to ICFC','AGENT WITHDRAW');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-20 17:55:14
