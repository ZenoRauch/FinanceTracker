-- Create the database
CREATE DATABASE financetracker;

-- Use the database
USE financetracker;

-- Create the 'category' table
CREATE TABLE category (
    categoryid INT(10) PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

-- Create the 'account' table
CREATE TABLE account (
    accountid INT(10) PRIMARY KEY AUTO_INCREMENT,
    bank VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL
);

-- Create the 'transaction' table
CREATE TABLE transaction (
    transactionid INT(10) PRIMARY KEY AUTO_INCREMENT,
    date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    description VARCHAR(255),
    accountid INT(10),
    categoryid INT(10),
    paymentforperiod DATE,
    isprepayment BOOLEAN,
    FOREIGN KEY (accountid) REFERENCES account(accountid),
    FOREIGN KEY (categoryid) REFERENCES category(categoryid)
);

-- Create the 'budget' table
CREATE TABLE budget (
    budgetid INT(10) PRIMARY KEY AUTO_INCREMENT,
    startdate DATE NOT NULL,
    enddate DATE NOT NULL
);

-- Create the 'budgetentry' table
CREATE TABLE budgetentry (
    budgetentryid INT(10) PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(10, 2) NOT NULL,
    categoryid INT(10),
    budgetid INT(10),
    FOREIGN KEY (categoryid) REFERENCES category(categoryid),
    FOREIGN KEY (budgetid) REFERENCES budget(budgetid)
);
