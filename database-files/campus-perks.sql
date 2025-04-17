DROP DATABASE IF EXISTS campusPerks_db;
CREATE DATABASE IF NOT EXISTS campusPerks_db;
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
    FOREIGN KEY (college) REFERENCES college(collegeName)
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

-- Bridge tables
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

-- Indices

-- finds all discounts for a store
-- beth smith, a business owner, would use this
CREATE INDEX idx_discount_store ON discount(storeId);

-- finds all discounts by date
-- bharat, a student, would use for current deals
CREATE INDEX idx_discount_dates ON discount(startDate, endDate);

-- finds all stores by college
-- glen howard, a club president, for campus deals
CREATE INDEX idx_store_college ON store(college);

-- finds all users by college
-- john doe, an admin, would use for analytics
CREATE INDEX idx_user_college ON user(college);

-- finds discounts that have been redeemed
-- beth smith, a business owner, would use to see popular discounts
CREATE INDEX idx_discount_used ON discount_used(discountId);

-- finds the discount history by user
-- bharat, a student,  would use for his saved deals
CREATE INDEX idx_user_discounts ON discount_used(username);

-- prevents duplicate business listings
CREATE UNIQUE INDEX idx_store_location ON store(locationStreet, locationCity, locationState, locationCountry);

-- prevents duplicate discount codes per store
CREATE UNIQUE INDEX idx_discount_code ON discount(storeId, code);



-- sample data

-- Locations
INSERT INTO location (streetAddress, city, state, country, zipCode) VALUES
('360 huntington ave', 'boston', 'ma', 'usa', '02115'),
('881 commonwealth ave', 'boston', 'ma', 'usa', '02215');

-- Colleges
INSERT INTO college (collegeName, location, domain) VALUES
('northeastern university', '360 huntington ave', 'northeastern.edu'),
('boston university', '881 commonwealth ave', 'bu.edu');

-- Users
INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate) VALUES
('beth_smith', 'beth', 'smith', 'farmers123', 'northeastern university', 'beth@farmershorse.com', '617-555-0101', '1988-05-20'),
('bharat_m', 'bharat', 'malipeddi', 'student123', 'northeastern university', 'bharat@neu.edu', '617-555-0102', '2000-11-15'),
('glen_howard', 'glen', 'howard', 'csclub456', 'northeastern university', 'glen@neu.edu', '617-555-0103', '2002-03-10');

-- Clubs
INSERT INTO club (name, college, numberOfUsers) VALUES
('cs club', 'northeastern university', 120),
('husky hackers', 'northeastern university', 85);

-- Stores
INSERT INTO store (name, locationStreet, locationCity, locationState, locationCountry, priceRange, hoursOfOperations, category, phoneNo, college) VALUES
('farmers horse coffee', '360 huntington ave', 'boston', 'ma', 'usa', '$$', '6am-8pm', 'cafe', '617-373-2000', 'northeastern university'),
('bu bookstore', '881 commonwealth ave', 'boston', 'ma', 'usa', '$$$', '9am-7pm', 'books', '617-353-2500', 'boston university');

-- Discounts
INSERT INTO discount (storeId, code, percentOff, item, startDate, endDate) VALUES
(1, 'COFFEE10', 10.00, 'any coffee drink', '2025-04-01', '2025-05-01'),
(1, 'PASTRY15', 15.00, 'any pastry', '2025-04-01', '2025-04-30'),
(2, 'TEXTBOOK5', 5.00, 'textbooks', '2025-04-01', '2025-06-01');

-- Admins
INSERT INTO admin (username, firstName, lastName, password, email, phoneNo) VALUES
('john_doe', 'john', 'doe', 'admin123', 'john@campusperks.com', '617-555-0301'),
('amanda_lee', 'amanda', 'lee', 'admin456', 'amanda@campusperks.com', '617-555-0302');

-- User-Club memberships
INSERT INTO user_club (username, clubId) VALUES
('glen_howard', 1),
('bharat_m', 1);

-- Discount used relationships
INSERT INTO discount_used (username, discountId) VALUES
('bharat_m', 1),
('bharat_m', 2),
('glen_howard', 1);

-- Club-Store partnerships
INSERT INTO club_store (clubId, storeId) VALUES
(1, 1);

