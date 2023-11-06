-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 25 oct. 2023 à 15:17
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `store`
--

-- --------------------------------------------------------

--
-- Structure de la table `clients`
--

DROP TABLE IF EXISTS `clients`;
CREATE TABLE IF NOT EXISTS `clients` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `LastName` text,
  `FirstName` text,
  `Address` text,
  `City` text,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `clients`
--

INSERT INTO `clients` (`Id`, `LastName`, `FirstName`, `Address`, `City`) VALUES
(1, 'Durand', 'Philippe', '3 rue des plantes', 'Rennes'),
(2, 'Duval', 'Christophe', '15 rue Foch', 'Caen'),
(3, 'Duron', 'Michel', '12 rue de Montmorency', 'Hérouville-St-Clair'),
(4, 'Dupont', 'Christine', '2 rue de poterie', 'Valognes'),
(5, 'Dupond', 'Valérie', '', 'Caen'),
(6, 'Truc', 'Toto', '5 rue des fleurs', 'Caen'),
(7, 'Bydull', 'Machin', 'où ça ?', 'Neptune'),
(8, 'C', 'C', 'C', 'C'),
(9, 'Ca', 'Marche', 'youpi', 'yah'),
(10, 'Pouet', 'Pouet', 'Pouet', 'Pouet'),
(11, 'P', 'P', 'P', 'P');

-- --------------------------------------------------------

--
-- Structure de la table `lineorders`
--

DROP TABLE IF EXISTS `lineorders`;
CREATE TABLE IF NOT EXISTS `lineorders` (
  `OrderId` int NOT NULL,
  `ProductReference` varchar(50) NOT NULL,
  `Quantity` int NOT NULL,
  PRIMARY KEY (`OrderId`,`ProductReference`),
  KEY `ProductReference` (`ProductReference`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `lineorders`
--

INSERT INTO `lineorders` (`OrderId`, `ProductReference`, `Quantity`) VALUES
(1, '06589', 2),
(1, '07145', 2),
(1, '08596', 1),
(2, '02445', 3),
(2, '06589', 1),
(2, '07145', 4),
(5, '09784', 5),
(8, '08645', 2),
(9, '09784', 3),
(10, '08645', 7),
(11, '06589', 5),
(12, '06589', 2),
(12, '08645', 3),
(12, '09784', 4),
(12, '11111', 6);

-- --------------------------------------------------------

--
-- Structure de la table `orders`
--

DROP TABLE IF EXISTS `orders`;
CREATE TABLE IF NOT EXISTS `orders` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Date` text,
  `ClientId` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `ClientId` (`ClientId`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `orders`
--

INSERT INTO `orders` (`Id`, `Date`, `ClientId`) VALUES
(1, '2008-11-18', 1),
(2, '2008-11-19', 3),
(3, '2022-01-20', 5),
(4, '2022-03-02', 6),
(5, '2020-02-20', 2),
(6, '2020-02-19', 3),
(7, '2022-03-02', 7),
(8, '2022-03-01', 7),
(9, '2020-02-15', 6),
(10, '2020-02-15', 2),
(11, '2020-02-03', 7),
(12, '2020-02-03', 2),
(13, '2023-11-11', 8),
(14, '4321-21-21', 6);

-- --------------------------------------------------------

--
-- Structure de la table `products`
--

DROP TABLE IF EXISTS `products`;
CREATE TABLE IF NOT EXISTS `products` (
  `Reference` varchar(50) NOT NULL,
  `Designation` text NOT NULL,
  `Price` float NOT NULL,
  `Stock` int NOT NULL,
  PRIMARY KEY (`Reference`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `products`
--

INSERT INTO `products` (`Reference`, `Designation`, `Price`, `Stock`) VALUES
('00123', 'Boules verre', 17.5, 2),
('00124', 'Boules cristals', 31, 3),
('00125', 'Boules verre', 18, 7),
('02445', 'Guirlande électrique', 11.2, 10),
('03456', 'Boules verre', 18.5, 4),
('06589', 'Guirlande boules rouges 2m', 6, 2),
('07145', 'Renne peluche 5 cm', 3, 15),
('07850', 'Bonnet Père Noël', 7.95, 27),
('08596', 'Sapin blanc 1m50', 43, 11),
('08645', 'Sapin vert 1m50', 41, 9),
('09784', 'Boules porcelaine', 16, 1),
('11111', 'Fourchette', 65, 12);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `lineorders`
--
ALTER TABLE `lineorders`
  ADD CONSTRAINT `lineorders_ibfk_1` FOREIGN KEY (`ProductReference`) REFERENCES `products` (`Reference`),
  ADD CONSTRAINT `lineorders_ibfk_2` FOREIGN KEY (`OrderId`) REFERENCES `orders` (`Id`);

--
-- Contraintes pour la table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`ClientId`) REFERENCES `clients` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
