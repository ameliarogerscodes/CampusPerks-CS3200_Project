USE campusPerks_db;
INSERT INTO location (locationId, streetAddress, city, state, country, zipcode)
VALUES (1, '199 High St', 'Miami', 'Florida', 'USA', '02110'),
INSERT INTO location (locationId, streetAddress, city, state, country, zipcode)
VALUES (2, '458 Huntington Ave', 'Miami', 'New York', 'USA', '77777'),
INSERT INTO location (locationId, streetAddress, city, state, country, zipcode)
VALUES (3, '458 Huntington Ave', 'Chicago', 'New York', 'USA', '02110'),
INSERT INTO location (locationId, streetAddress, city, state, country, zipcode)
VALUES (4, '15 Fruit St', 'Boston', 'Massachusetts', 'USA', '90210'),
INSERT INTO location (locationId, streetAddress, city, state, country, zipcode)
VALUES (5, '458 Huntington Ave', 'San Francisco', 'Florida', 'USA', '11111');
INSERT INTO college (collegeName, locationId, noOfStores, noOfUsers, domain)
VALUES ('UCBerkeley', 3, 0, 0, '@UCBerkeley.edu'),
INSERT INTO college (collegeName, locationId, noOfStores, noOfUsers, domain)
VALUES ('Northeastern', 5, 0, 0, '@Northeastern.edu'),
INSERT INTO college (collegeName, locationId, noOfStores, noOfUsers, domain)
VALUES ('Northwestern', 2, 0, 0, '@Northwestern.edu'),
INSERT INTO college (collegeName, locationId, noOfStores, noOfUsers, domain)
VALUES ('UMiami', 5, 0, 0, '@UMiami.edu'),
INSERT INTO college (collegeName, locationId, noOfStores, noOfUsers, domain)
VALUES ('Fordham', 4, 0, 0, '@Fordham.edu');
INSERT INTO store (storeId, name, locationId, priceRange, noOfDiscounts,hoursOfOperations, category, phoneNo, website, starRating, delivery, ageRestricted,totalSales, noOfOrders, college, clubId)
VALUES (1, 'Aroma Joes', 1, '$$', 0, '11:00am-11:00pm', 'convenience', '+1-604-386-1763x6272', 'williams.org', 3, 1, 1, 7289, 106, 'Fordham', NULL),
INSERT INTO store (storeId, name, locationId, priceRange, noOfDiscounts,hoursOfOperations, category, phoneNo, website, starRating, delivery, ageRestricted,totalSales, noOfOrders, college, clubId)
VALUES (2, 'Star Market', 3, '$', 0, '10:00am-5:00pm', 'grocery', '958-733-5154x55061', 'lee.info', 5, 1, 1, 5122, 150, 'UMiami', NULL),
INSERT INTO store (storeId, name, locationId, priceRange, noOfDiscounts,hoursOfOperations, category, phoneNo, website, starRating, delivery, ageRestricted,totalSales, noOfOrders, college, clubId)
VALUES (3, 'Target', 3, '$', 0, '7:00am-12:00am', 'clothing', '+1-886-690-2346', 'gutierrez-jones.com', 4, 1, 1, 8006, 146, 'UCBerkeley', NULL),
INSERT INTO store (storeId, name, locationId, priceRange, noOfDiscounts,hoursOfOperations, category, phoneNo, website, starRating, delivery, ageRestricted,totalSales, noOfOrders, college, clubId)
VALUES (4, 'Target', 4, '$', 0, '7:00am-12:00am', 'clothing', '+1-792-924-2440x97391', 'wagner.com', 4, 1, 0, 9315, 318, 'Northwestern', NULL),
INSERT INTO store (storeId, name, locationId, priceRange, noOfDiscounts,hoursOfOperations, category, phoneNo, website, starRating, delivery, ageRestricted,totalSales, noOfOrders, college, clubId)
VALUES (5, 'Panera', 4, '$$', 0, '12:00pm-9:00pm', 'convenience', '(370)217-8988x052', 'butler.com', 1, 0, 1, 16473, 312, 'Northwestern', NULL);
INSERT INTO club (clubId, name, college, storeId, numberOfUsers)
VALUES (1, 'Trivia Club', 'UCBerkeley', NULL, 0),
INSERT INTO club (clubId, name, college, storeId, numberOfUsers)
VALUES (2, 'Badminton Club', 'UMiami', NULL, 0),
INSERT INTO club (clubId, name, college, storeId, numberOfUsers)
VALUES (3, 'Badminton Club', 'Northeastern', NULL, 0),
INSERT INTO club (clubId, name, college, storeId, numberOfUsers)
VALUES (4, 'Society of Women in Tech', 'Northwestern', NULL, 0),
INSERT INTO club (clubId, name, college, storeId, numberOfUsers)
VALUES (5, 'Film Club', 'Fordham', NULL, 0);
INSERT INTO discount (discountId, storeId, code, percentOff, item, startDate, endDate, ageRestricted, minPurchase, bdayDiscount)
VALUES (1, 4, 'REDEEMCODE', 1, 'furniature', '2025-04-14', '2025-06-01', 1, 89, 0),
INSERT INTO discount (discountId, storeId, code, percentOff, item, startDate, endDate, ageRestricted, minPurchase, bdayDiscount)
VALUES (2, 1, 'BUYBUYBUY', 64, 'clothing', '2025-02-18', '2025-06-01', 0, 10, 1),
INSERT INTO discount (discountId, storeId, code, percentOff, item, startDate, endDate, ageRestricted, minPurchase, bdayDiscount)
VALUES (3, 1, 'BUYBUYBUY', 81, 'produce', '2025-02-18', '2025-05-05', 1, 9, 0),
INSERT INTO discount (discountId, storeId, code, percentOff, item, startDate, endDate, ageRestricted, minPurchase, bdayDiscount)
VALUES (4, 1, 'BUYBUYBUY', 32, 'coffee', '2025-02-18', '2025-06-01', 0, 28, 1),
INSERT INTO discount (discountId, storeId, code, percentOff, item, startDate, endDate, ageRestricted, minPurchase, bdayDiscount)
VALUES (5, 4, 'REDEEMCODE', 38, 'furniature', '2025-04-14', '2025-05-05', 0, 94, 0),
INSERT INTO discount (discountId, storeId, code, percentOff, item, startDate, endDate, ageRestricted, minPurchase, bdayDiscount)
VALUES (6, 4, 'SPRINGSALE', 23, 'books', '2025-02-18', '2025-06-01', 0, 39, 1),
INSERT INTO discount (discountId, storeId, code, percentOff, item, startDate, endDate, ageRestricted, minPurchase, bdayDiscount)
VALUES (7, 5, 'BIGSALE', 93, 'produce', '2025-03-20', '2025-05-10', 1, 58, 1),
INSERT INTO discount (discountId, storeId, code, percentOff, item, startDate, endDate, ageRestricted, minPurchase, bdayDiscount)
VALUES (8, 4, 'SPRINGSALE', 58, 'clothing', '2025-02-18', '2025-05-05', 1, 74, 1),
INSERT INTO discount (discountId, storeId, code, percentOff, item, startDate, endDate, ageRestricted, minPurchase, bdayDiscount)
VALUES (9, 5, 'BUYBUYBUY', 74, 'clothing', '2025-04-14', '2025-06-01', 1, 12, 1),
INSERT INTO discount (discountId, storeId, code, percentOff, item, startDate, endDate, ageRestricted, minPurchase, bdayDiscount)
VALUES (10, 3, 'BIGSALE', 33, 'produce', '2025-03-30', '2025-05-05', 0, 52, 1);
INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate,  age, discountsUsed, clubId) VALUES ('MarkMorris26', 'Mark', 'Morris', '%W6a6(Jt', 'UMiami', 'MarkMorris26@UMiami.edu', '+1-634-239-1219', '2000-04-15', 25, 4),
INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate,  age, discountsUsed, clubId) VALUES ('JeremiahDavis164', 'Jeremiah', 'Davis', '*7)OOr!8', 'Northeastern', 'JeremiahDavis164@Northeastern.edu', '001-285-733-2132', '2003-05-10', 21, 3),
INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate,  age, discountsUsed, clubId) VALUES ('MadelineWeber92', 'Madeline', 'Weber', 'r%1ddfOt', 'Northwestern', 'MadelineWeber92@Northwestern.edu', '+1-915-343-8905x01750', '2002-06-01', 26, 2),
INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate,  age, discountsUsed, clubId) VALUES ('CoreyReyes197', 'Corey', 'Reyes', '8$n2WtTf', 'UMiami', 'CoreyReyes197@UMiami.edu', '727-577-3140x14463', '2003-05-10', 25, 3),
INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate,  age, discountsUsed, clubId) VALUES ('AbigailStanton186', 'Abigail', 'Stanton', '0F_4yEQv', 'UMiami', 'AbigailStanton186@UMiami.edu', '371-940-0129', '2002-06-01', 30, 3),
INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate,  age, discountsUsed, clubId) VALUES ('TammyAnderson146', 'Tammy', 'Anderson', '^d8A!aFf', 'Northwestern', 'TammyAnderson146@Northwestern.edu', '251-841-2029', '2005-11-11', 24, 5),
INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate,  age, discountsUsed, clubId) VALUES ('JackZamora155', 'Jack', 'Zamora', '^h01XeyF', 'UMiami', 'JackZamora155@UMiami.edu', '+1-647-435-6716x66361', '2000-04-15', 30, 5),
INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate,  age, discountsUsed, clubId) VALUES ('TamaraMoore103', 'Tamara', 'Moore', '$Mm5I8x6', 'Northeastern', 'TamaraMoore103@Northeastern.edu', '+1-446-876-7561', '2000-04-15', 24, 3),
INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate,  age, discountsUsed, clubId) VALUES ('MichelleYoung20', 'Michelle', 'Young', '(&*1D*ps', 'Northeastern', 'MichelleYoung20@Northeastern.edu', '200.284.3989', '2003-05-10', 30, 3),
INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate,  age, discountsUsed, clubId) VALUES ('MicheleKelly94', 'Michele', 'Kelly', '$m0Mo4FF', 'Northwestern', 'MicheleKelly94@Northwestern.edu', '(308)443-3158', '2002-06-01', 20, 5);
INSERT INTO discount_used (username, discountId)
VALUES ('MicheleKelly94', 9),
INSERT INTO discount_used (username, discountId)
VALUES ('JackZamora155', 5),
INSERT INTO discount_used (username, discountId)
VALUES ('MarkMorris26', 2),
INSERT INTO discount_used (username, discountId)
VALUES ('CoreyReyes197', 6),
INSERT INTO discount_used (username, discountId)
VALUES ('TammyAnderson146', 2),
INSERT INTO discount_used (username, discountId)
VALUES ('MadelineWeber92', 3),
INSERT INTO discount_used (username, discountId)
VALUES ('CoreyReyes197', 2),
INSERT INTO discount_used (username, discountId)
VALUES ('JackZamora155', 1),
INSERT INTO discount_used (username, discountId)
VALUES ('MarkMorris26', 4),
INSERT INTO discount_used (username, discountId)
VALUES ('TammyAnderson146', 3);
INSERT INTO admin (username, firstName, lastName, password, email, phoneNo,  supportUser, supportClub, supportStore)
VALUES('KatherineZhang47', 'Katherine', 'Zhang', '#s2qQLSs', 'KatherineZhang47@gmail.com', '+1-259-648-8472x1808', 'JeremiahDavis164', 5, 1),
INSERT INTO admin (username, firstName, lastName, password, email, phoneNo,  supportUser, supportClub, supportStore)
VALUES('NicoleGonzalez86', 'Nicole', 'Gonzalez', '@h1sQ7ec', 'NicoleGonzalez86@gmail.com', '618-670-7080x0235', 'TamaraMoore103', 4, 2);
