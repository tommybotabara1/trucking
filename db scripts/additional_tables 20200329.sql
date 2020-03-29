CREATE TABLE `payables` (
  `payableID` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `invoiceNo` varchar(45) DEFAULT NULL,
  `documentDate` date DEFAULT NULL,
  `supplier` varchar(45) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `particulars` varchar(45) DEFAULT NULL,
  `checkVoucherNo` varchar(45) DEFAULT NULL,
  `checkVoucherDate` date DEFAULT NULL,
  `checkNo` int(11) DEFAULT NULL,
  `checkDate` date DEFAULT NULL,
  `checkReleasedDate` date DEFAULT NULL,
  `clearedDate` date DEFAULT NULL,
  `remarks` longtext,
  PRIMARY KEY (`payableID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

CREATE TABLE `liquidation` (
  `liquidationID` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `truckID` varchar(45) DEFAULT NULL,
  `amountReceived` float DEFAULT NULL,
  `liquidation` float DEFAULT NULL,
  `particulars` varchar(45) DEFAULT NULL,
  `remarks` longtext,
  PRIMARY KEY (`liquidationID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

CREATE TABLE `cash_monitoring` (
  `cashMonitoringID` int(11) NOT NULL AUTO_INCREMENT,
  `client` varchar(45) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `checkNo` varchar(45) DEFAULT NULL,
  `checkVoucherNo` varchar(45) DEFAULT NULL,
  `deposit` float DEFAULT NULL,
  `withdrawal` float DEFAULT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cashMonitoringID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE `cash_on_hand` (
  `cashOnHandID` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `truckID` varchar(45) DEFAULT NULL,
  `received` float DEFAULT NULL,
  `truckBudget` float DEFAULT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cashOnHandID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE `billing_statement_or` (
  `billingStatementORID` int(11) NOT NULL AUTO_INCREMENT,
  `month` date DEFAULT NULL,
  `invoiceNo` int(11) DEFAULT NULL,
  `customer` varchar(45) DEFAULT NULL,
  `particulars` varchar(45) DEFAULT NULL,
  `invoiceDate` date DEFAULT NULL,
  `invoiceReceivedDate` date DEFAULT NULL,
  `receivedBy` varchar(45) DEFAULT NULL,
  `totalSales` float DEFAULT NULL,
  `taxableSales` float DEFAULT NULL,
  `vat` float DEFAULT NULL,
  `creditableTax` float DEFAULT NULL,
  `orNo` int(11) DEFAULT NULL,
  `paidAmount` float DEFAULT NULL,
  `datePaid` date DEFAULT NULL,
  `varianceDiff` float DEFAULT NULL,
  `acctsTitle` varchar(45) DEFAULT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`billingStatementORID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

CREATE TABLE `billing_statement_ar` (
  `billingStatementARID` int(11) NOT NULL AUTO_INCREMENT,
  `month` date DEFAULT NULL,
  `soaNo` varchar(45) DEFAULT NULL,
  `customer` varchar(45) DEFAULT NULL,
  `particulars` varchar(45) DEFAULT NULL,
  `invoiceDate` date DEFAULT NULL,
  `invoiceReceivedDate` date DEFAULT NULL,
  `receivedBy` varchar(45) DEFAULT NULL,
  `totalSales` float DEFAULT NULL,
  `arNo` varchar(45) DEFAULT NULL,
  `paidAmount` float DEFAULT NULL,
  `datePaid` date DEFAULT NULL,
  `varianceDiff` float DEFAULT NULL,
  `acctsTitle` varchar(45) DEFAULT NULL,
  `remarks` longtext,
  PRIMARY KEY (`billingStatementARID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
