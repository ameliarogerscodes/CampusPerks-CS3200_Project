DROP DATABASE IF EXISTS campusPerks_db;
CREATE DATABASE campusPerks_db;
USE campusPerks_db;

DROP TABLE IF EXISTS discount_used;
DROP TABLE IF EXISTS user_club;
DROP TABLE IF EXISTS club_store;
DROP TABLE IF EXISTS discount;
DROP TABLE IF EXISTS admin;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS club;
DROP TABLE IF EXISTS college;
DROP TABLE IF EXISTS location;

-- Location table
CREATE TABLE location (
    streetAddress VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    zipCode VARCHAR(20) NOT NULL,
    PRIMARY KEY (streetAddress, city, state, country)
);

-- College table
CREATE TABLE college (
    collegeName VARCHAR(100) PRIMARY KEY,
    location VARCHAR(100) NOT NULL,
    noOfStores INT DEFAULT 0,
    noOfUsers INT DEFAULT 0,
    domain VARCHAR(50) NOT NULL
);

-- Club table
CREATE TABLE club (
    clubId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    college VARCHAR(100) NOT NULL,
    numberOfUsers INT DEFAULT 0,
    FOREIGN KEY (college) REFERENCES college(collegeName)
);

-- Store table
CREATE TABLE store (
    storeId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    locationStreet VARCHAR(100) NOT NULL,
    locationCity VARCHAR(50) NOT NULL,
    locationState VARCHAR(50) NOT NULL,
    locationCountry VARCHAR(50) NOT NULL,
    priceRange VARCHAR(20) NOT NULL,
    noOfDiscounts INT DEFAULT 0,
    hoursOfOperations VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    phoneNo VARCHAR(20) NOT NULL,
    website VARCHAR(100),
    starRating DECIMAL(2,1),
    delivery BOOLEAN DEFAULT FALSE,
    ageRestricted BOOLEAN DEFAULT FALSE,
    totalSales DECIMAL(12,2) DEFAULT 0.00,
    noOfOrders INT DEFAULT 0,
    college VARCHAR(100) NOT NULL,
    FOREIGN KEY (college) REFERENCES college(collegeName),
    FOREIGN KEY (locationStreet, locationCity, locationState, locationCountry)
        REFERENCES location(streetAddress, city, state, country)
);

-- Discount table
CREATE TABLE discount (
    discountId INT AUTO_INCREMENT PRIMARY KEY,
    storeId INT NOT NULL,
    code VARCHAR(50) NOT NULL,
    percentOff DECIMAL(5,2) NOT NULL,
    item VARCHAR(100) NOT NULL,
    startDate DATETIME NOT NULL,
    endDate DATETIME,
    ageRestricted BOOLEAN DEFAULT FALSE,
    minPurchase DECIMAL(10,2),
    bdayDiscount BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (storeId) REFERENCES store(storeId)
);

-- User table (updated to reference clubId)
CREATE TABLE user (
    username VARCHAR(50) PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    password VARCHAR(128) NOT NULL,
    college VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phoneNo VARCHAR(20) NOT NULL,
    birthdate DATE NOT NULL,
    age INT,
    discountsUsed INT DEFAULT 0,
    clubId INT,
    FOREIGN KEY (college) REFERENCES college(collegeName),
    FOREIGN KEY (clubId) REFERENCES club(clubId)
);

-- Admin table
CREATE TABLE admin (
    username VARCHAR(50) PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    password VARCHAR(128) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phoneNo VARCHAR(20) NOT NULL,
    supportUser BOOLEAN DEFAULT FALSE,
    supportClub BOOLEAN DEFAULT FALSE,
    supportStore BOOLEAN DEFAULT FALSE
);

-- Junction tables
CREATE TABLE user_club (
    username VARCHAR(50) NOT NULL,
    clubId INT NOT NULL,
    PRIMARY KEY (username, clubId),
    FOREIGN KEY (username) REFERENCES user(username),
    FOREIGN KEY (clubId) REFERENCES club(clubId)
);

CREATE TABLE discount_used (
    username VARCHAR(50) NOT NULL,
    discountId INT NOT NULL,
    PRIMARY KEY (username, discountId),
    FOREIGN KEY (username) REFERENCES user(username),
    FOREIGN KEY (discountId) REFERENCES discount(discountId)
);

CREATE TABLE club_store (
    clubId INT NOT NULL,
    storeId INT NOT NULL,
    PRIMARY KEY (clubId, storeId),
    FOREIGN KEY (clubId) REFERENCES club(clubId),
    FOREIGN KEY (storeId) REFERENCES store(storeId)
);

-- Indexes
CREATE INDEX idx_discount_store ON discount(storeId);
CREATE INDEX idx_discount_dates ON discount(startDate, endDate);
CREATE INDEX idx_store_college ON store(college);
CREATE INDEX idx_user_college ON user(college);
CREATE INDEX idx_discount_used ON discount_used(discountId);
CREATE INDEX idx_user_discounts ON discount_used(username);
CREATE UNIQUE INDEX idx_store_location ON store(locationStreet, locationCity, locationState, locationCountry);
CREATE UNIQUE INDEX idx_discount_code ON discount(storeId, code);