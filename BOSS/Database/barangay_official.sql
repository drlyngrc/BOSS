-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 06, 2023 at 03:07 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `barangay_official`
--

-- --------------------------------------------------------

--
-- Table structure for table `addressinfo`
--

CREATE TABLE `addressinfo` (
  `AddressCode` int(11) NOT NULL,
  `AddressID` varchar(10) DEFAULT NULL,
  `BarangayID` varchar(8) DEFAULT NULL,
  `HouseholdNo` varchar(8) DEFAULT NULL,
  `Zone` varchar(8) DEFAULT NULL,
  `StreetName` varchar(30) DEFAULT NULL,
  `City` varchar(30) DEFAULT NULL,
  `Province` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `addressinfo`
--

INSERT INTO `addressinfo` (`AddressCode`, `AddressID`, `BarangayID`, `HouseholdNo`, `Zone`, `StreetName`, `City`, `Province`) VALUES
(1, 'AD-00001', 'ID-00001', '0456', '4', 'Ilat North', 'San Pascual', 'Batangas'),
(2, 'AD-00002', 'ID-00002', '0123', '2', 'RR Station', 'Batangas City', 'Batangas'),
(3, 'AD-00003', 'ID-00003', '0234', '2', 'RR Station', 'Batangas City', 'Batangas'),
(4, 'AD-00004', 'ID-00004', '0345', '3', 'Purok 3', 'Batangas City', 'Batangas'),
(5, 'AD-00005', 'ID-00005', '0234', '2', 'RR Station', 'Batangas City', 'Batangas');

--
-- Triggers `addressinfo`
--
DELIMITER $$
CREATE TRIGGER `before_insert_AddressInfo` BEFORE INSERT ON `addressinfo` FOR EACH ROW BEGIN
    SET NEW.AddressID = CONCAT('AD-', LPAD((SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='AddressInfo'), 5, '0'));
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `admininfo`
--

CREATE TABLE `admininfo` (
  `AdminID` varchar(10) NOT NULL,
  `AdminLN` varchar(20) DEFAULT NULL,
  `AdminFN` varchar(20) DEFAULT NULL,
  `AdminMN` varchar(20) DEFAULT NULL,
  `AdminPosition` varchar(20) DEFAULT NULL,
  `AdminPassword` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admininfo`
--

INSERT INTO `admininfo` (`AdminID`, `AdminLN`, `AdminFN`, `AdminMN`, `AdminPosition`, `AdminPassword`) VALUES
('AM-00001', 'Barican', 'John Andrei', 'Agrabio', 'SK Chairman', 'testing00001'),
('AM-00002', 'Lalongisip', 'Darlyne Grace', 'Magbatoc', 'SK Councilor', 'konsi'),
('AM-00003', 'Magnaye', 'James Michael', 'De Villa', 'Mayor', 'james'),
('AM-00004', 'Guinoban', 'Glenn', 'Maranan', 'Barangay Captain', 'glenn'),
('AM-00005', 'Zamora', 'Clarence', 'C', 'Barangay Councilor', 'clar');

-- --------------------------------------------------------

--
-- Table structure for table `adultinfo`
--

CREATE TABLE `adultinfo` (
  `EmployeeCode` int(11) NOT NULL,
  `EmployeeID` varchar(10) DEFAULT NULL,
  `BarangayID` varchar(8) DEFAULT NULL,
  `EmploymentStatus` varchar(15) DEFAULT NULL,
  `MonthlyIncome` decimal(8,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adultinfo`
--

INSERT INTO `adultinfo` (`EmployeeCode`, `EmployeeID`, `BarangayID`, `EmploymentStatus`, `MonthlyIncome`) VALUES
(1, 'ES-00001', 'ID-00001', 'Employed', 120.00),
(2, 'ES-00002', 'ID-00003', 'Employed', 8000.00),
(3, 'ES-00003', 'ID-00005', 'Employed', 10000.00);

--
-- Triggers `adultinfo`
--
DELIMITER $$
CREATE TRIGGER `before_insert_AdultInfo` BEFORE INSERT ON `adultinfo` FOR EACH ROW BEGIN
    SET NEW.EmployeeID = CONCAT('ES-', LPAD((SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='AdultInfo'), 5, '0'));
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `appointmentcode` int(11) NOT NULL,
  `appointmentid` varchar(10) DEFAULT NULL,
  `barangayid` varchar(8) DEFAULT NULL,
  `Purpose` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`appointmentcode`, `appointmentid`, `barangayid`, `Purpose`, `date`, `status`) VALUES
(7, 'AP-00007', 'ID-00001', 'a', '2023-12-07', 'Pending');

--
-- Triggers `appointment`
--
DELIMITER $$
CREATE TRIGGER `before_insert_appointment` BEFORE INSERT ON `appointment` FOR EACH ROW BEGIN
    SET NEW.appointmentcode = NULL; 
    SET NEW.appointmentid = CONCAT('AP-', LPAD((SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='appointment'), 5, '0'));
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `caseinfo`
--

CREATE TABLE `caseinfo` (
  `CaseCode` int(11) NOT NULL,
  `CaseID` varchar(10) DEFAULT NULL,
  `BID` varchar(8) DEFAULT NULL,
  `CaseDesc` varchar(40) DEFAULT NULL,
  `CaseStatus` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `caseinfo`
--

INSERT INTO `caseinfo` (`CaseCode`, `CaseID`, `BID`, `CaseDesc`, `CaseStatus`) VALUES
(1, '23-00001', 'ID-00001', 'Loittering', 'Clear'),
(2, '23-00002', 'ID-00003', 'Family feud', 'Suspended');

--
-- Triggers `caseinfo`
--
DELIMITER $$
CREATE TRIGGER `before_insert_CaseInfo` BEFORE INSERT ON `caseinfo` FOR EACH ROW BEGIN
    SET NEW.CaseID = CONCAT('23-', LPAD((SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='CaseInfo'), 5, '0'));
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `files`
--

CREATE TABLE `files` (
  `id` int(11) NOT NULL,
  `filename` int(11) NOT NULL,
  `filepath` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `logininfo`
--

CREATE TABLE `logininfo` (
  `BarangayCode` int(11) NOT NULL,
  `BarangayID` varchar(8) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  `Email` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `logininfo`
--

INSERT INTO `logininfo` (`BarangayCode`, `BarangayID`, `Password`, `Email`) VALUES
(1, 'ID-00001', 'dar', 'dar@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `medicalinfo`
--

CREATE TABLE `medicalinfo` (
  `MedicalCode` int(11) NOT NULL,
  `MedicalID` varchar(10) DEFAULT NULL,
  `BarangayID` varchar(8) DEFAULT NULL,
  `BMIClassification` varchar(15) DEFAULT NULL,
  `MedicalCondition` varchar(20) DEFAULT NULL,
  `COVIDVaccinated` varchar(5) DEFAULT NULL,
  `MaintenanceMedicine` varchar(5) DEFAULT NULL,
  `PhysicalFitness` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `medicalinfo`
--

INSERT INTO `medicalinfo` (`MedicalCode`, `MedicalID`, `BarangayID`, `BMIClassification`, `MedicalCondition`, `COVIDVaccinated`, `MaintenanceMedicine`, `PhysicalFitness`) VALUES
(1, 'MD-00001', 'ID-00001', 'Normal', 'None', 'Yes', 'No', 'PF'),
(2, 'MD-00002', 'ID-00002', 'Normal', 'Asthma', 'Yes', 'No', 'NPF'),
(3, 'MD-00003', 'ID-00003', 'Normal', 'Hypertension', 'Yes', 'Yes', 'PF'),
(4, 'MD-00004', 'ID-00004', 'Underweight', 'None', 'Yes', 'Yes', 'PF');

--
-- Triggers `medicalinfo`
--
DELIMITER $$
CREATE TRIGGER `before_insert_MedicalInfo` BEFORE INSERT ON `medicalinfo` FOR EACH ROW BEGIN
    SET NEW.MedicalID = CONCAT('MD-', LPAD((SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='MedicalInfo'), 5, '0'));
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `residentinfo`
--

CREATE TABLE `residentinfo` (
  `BarangayID` varchar(8) NOT NULL,
  `Category` varchar(10) DEFAULT NULL,
  `LastName` varchar(20) DEFAULT NULL,
  `FirstName` varchar(20) DEFAULT NULL,
  `MiddleName` varchar(20) DEFAULT NULL,
  `Sex` varchar(8) DEFAULT NULL,
  `Birthdate` date DEFAULT NULL,
  `Birthplace` varchar(30) DEFAULT NULL,
  `Religion` varchar(20) DEFAULT NULL,
  `CivilStat` varchar(20) DEFAULT NULL,
  `Citizenship` varchar(10) DEFAULT NULL,
  `VoterPrecinct` varchar(8) DEFAULT NULL,
  `ContactNo` varchar(15) DEFAULT NULL,
  `profile_picture` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `residentinfo`
--

INSERT INTO `residentinfo` (`BarangayID`, `Category`, `LastName`, `FirstName`, `MiddleName`, `Sex`, `Birthdate`, `Birthplace`, `Religion`, `CivilStat`, `Citizenship`, `VoterPrecinct`, `ContactNo`, `profile_picture`) VALUES
('ID-00001', 'Adult', 'Wilson', 'George', 'Wright', 'Female', '2000-01-01', 'Hospital', 'Catholic', 'Single', 'Filipino', '063B', '09876543212', ''),
('ID-00002', 'Student', 'Park', 'Sandara', 'Gomez', 'Female', '1999-08-09', 'Lipa City', 'Roman Catholic', 'Single', 'Filipino', '060A', '09475162458', ''),
('ID-00003', 'Adult', 'Tumambing', 'Emma', 'Abacan', 'Female', '1967-09-24', 'Batangas City', 'Roman Catholic', 'Married', 'Filipino', '060B', '09512348982', ''),
('ID-00004', 'Student', 'Marino', 'Marvey', 'Vittorio', 'Male', '2002-12-01', 'Lipa City', 'Roman Catholic', 'Single', 'Filipino', '061B', '09154236781', ''),
('ID-00005', 'Adult', 'Tumambing', 'Rolando', 'Herbas', 'Male', '1966-08-08', 'PGH', 'Roman Catholic', 'Married', 'Filipino', '061A', '09162458791', ''),
('ID-00006', 'Adult', 'Duterte', 'Rodrigo', 'Roa', 'Male', '2001-02-11', 'Batangas City', 'Born Again Christian', 'Single', 'Filipino', '066A', '09995031535', 'uploads\\samplephoto.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `studentinfo`
--

CREATE TABLE `studentinfo` (
  `StudentCode` int(11) NOT NULL,
  `StudentID` varchar(10) DEFAULT NULL,
  `BarangayID` varchar(8) DEFAULT NULL,
  `YearLevel` varchar(15) DEFAULT NULL,
  `School` varchar(25) DEFAULT NULL,
  `AcademicYear` varchar(10) DEFAULT NULL,
  `Scholarship` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `studentinfo`
--

INSERT INTO `studentinfo` (`StudentCode`, `StudentID`, `BarangayID`, `YearLevel`, `School`, `AcademicYear`, `Scholarship`) VALUES
(1, 'SD-00001', 'ID-00002', '3rd Yr', 'BSU', '2023-2024', 'EBD'),
(2, 'SD-00002', 'ID-00004', '3rd Yr', 'UB', '2023-2024', 'EBD');

--
-- Triggers `studentinfo`
--
DELIMITER $$
CREATE TRIGGER `before_insert_StudentInfo` BEFORE INSERT ON `studentinfo` FOR EACH ROW BEGIN
    SET NEW.StudentID = CONCAT('SD-', LPAD((SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='StudentInfo'), 5, '0'));
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addressinfo`
--
ALTER TABLE `addressinfo`
  ADD PRIMARY KEY (`AddressCode`),
  ADD KEY `BarangayID` (`BarangayID`);

--
-- Indexes for table `admininfo`
--
ALTER TABLE `admininfo`
  ADD PRIMARY KEY (`AdminID`);

--
-- Indexes for table `adultinfo`
--
ALTER TABLE `adultinfo`
  ADD PRIMARY KEY (`EmployeeCode`),
  ADD KEY `BarangayID` (`BarangayID`);

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`appointmentcode`),
  ADD KEY `barangayid` (`barangayid`);

--
-- Indexes for table `caseinfo`
--
ALTER TABLE `caseinfo`
  ADD PRIMARY KEY (`CaseCode`),
  ADD KEY `BID` (`BID`);

--
-- Indexes for table `files`
--
ALTER TABLE `files`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `logininfo`
--
ALTER TABLE `logininfo`
  ADD PRIMARY KEY (`BarangayCode`),
  ADD KEY `BarangayID` (`BarangayID`);

--
-- Indexes for table `medicalinfo`
--
ALTER TABLE `medicalinfo`
  ADD PRIMARY KEY (`MedicalCode`),
  ADD KEY `BarangayID` (`BarangayID`);

--
-- Indexes for table `residentinfo`
--
ALTER TABLE `residentinfo`
  ADD PRIMARY KEY (`BarangayID`);

--
-- Indexes for table `studentinfo`
--
ALTER TABLE `studentinfo`
  ADD PRIMARY KEY (`StudentCode`),
  ADD KEY `BarangayID` (`BarangayID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addressinfo`
--
ALTER TABLE `addressinfo`
  MODIFY `AddressCode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `adultinfo`
--
ALTER TABLE `adultinfo`
  MODIFY `EmployeeCode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `appointmentcode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `caseinfo`
--
ALTER TABLE `caseinfo`
  MODIFY `CaseCode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `files`
--
ALTER TABLE `files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `logininfo`
--
ALTER TABLE `logininfo`
  MODIFY `BarangayCode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `medicalinfo`
--
ALTER TABLE `medicalinfo`
  MODIFY `MedicalCode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `studentinfo`
--
ALTER TABLE `studentinfo`
  MODIFY `StudentCode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `addressinfo`
--
ALTER TABLE `addressinfo`
  ADD CONSTRAINT `addressinfo_ibfk_1` FOREIGN KEY (`BarangayID`) REFERENCES `residentinfo` (`BarangayID`);

--
-- Constraints for table `adultinfo`
--
ALTER TABLE `adultinfo`
  ADD CONSTRAINT `adultinfo_ibfk_1` FOREIGN KEY (`BarangayID`) REFERENCES `residentinfo` (`BarangayID`);

--
-- Constraints for table `appointment`
--
ALTER TABLE `appointment`
  ADD CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`barangayid`) REFERENCES `residentinfo` (`BarangayID`);

--
-- Constraints for table `caseinfo`
--
ALTER TABLE `caseinfo`
  ADD CONSTRAINT `caseinfo_ibfk_1` FOREIGN KEY (`BID`) REFERENCES `residentinfo` (`BarangayID`);

--
-- Constraints for table `logininfo`
--
ALTER TABLE `logininfo`
  ADD CONSTRAINT `logininfo_ibfk_1` FOREIGN KEY (`BarangayID`) REFERENCES `residentinfo` (`BarangayID`);

--
-- Constraints for table `medicalinfo`
--
ALTER TABLE `medicalinfo`
  ADD CONSTRAINT `medicalinfo_ibfk_1` FOREIGN KEY (`BarangayID`) REFERENCES `residentinfo` (`BarangayID`);

--
-- Constraints for table `studentinfo`
--
ALTER TABLE `studentinfo`
  ADD CONSTRAINT `studentinfo_ibfk_1` FOREIGN KEY (`BarangayID`) REFERENCES `residentinfo` (`BarangayID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
