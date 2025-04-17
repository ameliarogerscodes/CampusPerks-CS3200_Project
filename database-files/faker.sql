USE campusPerks_db;
<<<<<<< HEAD

-- 1. Locations
INSERT INTO location (streetAddress, city, state, country, zipCode) VALUES
  ('199 High St',    'Chicago',       'New York',    'USA', '90210'),
  ('14 Baker St',    'Chicago',       'Illinois',    'USA', '11111'),
  ('14 Baker St',    'San Francisco', 'California',  'USA', '90210'),
  ('14 Baker St',    'New York',      'New York',    'USA', '11111'),
  ('199 High St',    'Miami',         'Florida',     'USA', '11111');

-- 2. Colleges
INSERT INTO college (collegeName, location, noOfStores, noOfUsers, domain) VALUES
  ('UMiami',        'Miami',       0, 0, 'UMiami.edu'),
  ('Fordham',       'New York',    0, 0, 'Fordham.edu'),
  ('Northeastern',  'Boston',      0, 0, 'Northeastern.edu'),
  ('Northwestern',  'Evanston',    0, 0, 'Northwestern.edu'),
  ('UCBerkeley',    'Berkeley',    0, 0, 'UCBerkeley.edu');

-- 3. Clubs
INSERT INTO club (name, college, numberOfUsers) VALUES
  ('Phi Delta Theta',          'Northeastern', 0),
  ('Society of Women in Tech', 'Northwestern', 0),
  ('Society of Women in Tech', 'Fordham',      0),
  ('Film Club',                'UMiami',       0),
  ('Society of Women in Tech', 'UCBerkeley',   0);

-- 4. Stores
INSERT INTO store (
    name, locationStreet, locationCity, locationState, locationCountry,
    priceRange, noOfDiscounts, hoursOfOperations, category, phoneNo,
    website, starRating, delivery, ageRestricted, totalSales, noOfOrders, college
) VALUES
  ('Star Market',   '14 Baker St',    'San Francisco', 'California', 'USA',
     '$', 0, '11:00am-11:00pm', 'grocery', '206-941-7227x291',
     'UCBerkeley.com', 4.0, TRUE,  FALSE, 10567.00, 378, 'Northeastern'),
  ('Aroma Joe''s',  '14 Baker St',    'New York',      'New York',    'USA',
     '$', 0, '7:00am-12:00am',  'grocery', '(310)937-5303',
     'UCBerkeley.com', 2.0, TRUE,  TRUE,  19279.00, 411, 'Fordham'),
  ('Aroma Joe''s',  '199 High St',    'Miami',         'Florida',     'USA',
     '$$$', 0, '10:00am-5:00pm',  'convenience', '659.313.2532',
     'UCBerkeley.com', 1.0, TRUE,  FALSE, 14257.00, 132, 'UMiami'),
  ('Target',        '14 Baker St',    'Chicago',       'Illinois',    'USA',
     '$$$', 0, '12:00pm-9:00pm',  'grocery', '744.778.8272',
     'UCBerkeley.com', 2.0, FALSE, TRUE,  938.00,   143, 'Northeastern'),
  ('Wollastons',    '14 Baker St',    'San Francisco', 'California',  'USA',
     '$', 0, '11:00am-11:00pm', 'convenience', '983-918-4580x57676',
     'UCBerkeley.com', 2.0, FALSE, TRUE,  16196.00,   0, 'UCBerkeley');

-- 5. Discounts
INSERT INTO discount (
    storeId, code, percentOff, item, startDate, endDate,
    ageRestricted, minPurchase, bdayDiscount
) VALUES
  (2, 'BIGSALE',     21.00, 'books',     '2025-03-20', '2025-05-05', FALSE, 30.00, TRUE),
  (5, 'BUYBUYBUY',   70.00, 'furniture', '2025-03-20', '2025-05-10', TRUE,  71.00, FALSE),
  (5, 'BUYBUYBUY',   23.00, 'coffee',    '2025-03-30', '2025-04-15', TRUE,  22.00, FALSE),
  (4, 'SPRINGSALE',  64.00, 'furniture', '2025-03-30', '2025-05-05', TRUE,  11.00, TRUE),
  (3, 'BIGSALE',     70.00, 'produce',   '2025-03-30', '2025-04-15', TRUE,  81.00, FALSE),
  (1, 'REDEEMCODE',  63.00, 'coffee',    '2025-04-14', '2025-04-15', TRUE,  98.00, FALSE),
  (1, 'BIGSALE',     54.00, 'books',     '2025-02-18', '2025-05-10', TRUE,  12.00, FALSE),
  (2, 'SPRINGSALE',  22.00, 'produce',   '2025-03-20', '2025-06-01', TRUE,  31.00, TRUE),
  (2, 'SALECODE',    72.00, 'furniture', '2025-03-30', '2025-04-15', TRUE,  52.00, FALSE),
  (5, 'REDEEMCODE',  39.00, 'books',     '2025-04-14', '2025-06-01', FALSE, 41.00, TRUE);

-- 6. Users
INSERT INTO user (
    username, firstName, lastName, password, college, email,
    phoneNo, birthdate, age, discountsUsed
) VALUES
  ('DarrellBryant59',    'Darrell', 'Bryant',  'j^1mLTFx', 'UMiami',      'DarrellBryant59@UMiami.edu',   '+1-668-274-0345x635',  '2003-05-10', 30, 5),
  ('JoshuaGomez141',     'Joshua',  'Gomez',   '@85ZCnM^', 'Fordham',     'JoshuaGomez141@Fordham.edu',    '(332)499-6459',         '2001-05-05', 19, 5),
  ('JeffreySims164',     'Jeffrey', 'Sims',    '#@!9B+Nc', 'Fordham',     'JeffreySims164@Fordham.edu',    '001-895-562-2539',      '2000-04-15', 25, 4),
  ('TimothySweeney192',  'Timothy', 'Sweeney', 'Q3^0A$pK', 'Fordham',     'TimothySweeney192@Fordham.edu', '+1-647-717-9419x3044',  '2003-05-10', 23, 3),
  ('AustinWarren83',     'Austin',  'Warren',  ')3ebGJb*', 'Fordham',     'AustinWarren83@Fordham.edu',    '001-829-448-7075x08446','2003-05-10', 29, 3),
  ('JonathanYork86',     'Jonathan','York',    '@E*g9Eid', 'UCBerkeley', 'JonathanYork86@UCBerkeley.edu', '736.687.6018x49308',    '2000-04-15', 18, 2),
  ('MichaelHensley123',  'Michael', 'Hensley', 'G&+R7Kj%', 'UMiami',      'MichaelHensley123@UMiami.edu',  '(628)850-9885x976',     '2002-06-01', 25, 3),
  ('ErinMitchell118',    'Erin',    'Mitchell','4Z&R8Qze', 'UMiami',      'ErinMitchell118@UMiami.edu',    '001-317-967-1695x27664','2000-04-15', 19, 4),
  ('JasonHolt143',       'Jason',   'Holt',    't&#@4hBy', 'UCBerkeley', 'JasonHolt143@UCBerkeley.edu',   '(839)861-2384',         '2002-06-01', 25, 3),
  ('HannahNorris131',    'Hannah',  'Norris',  'v!5W*bCD', 'Fordham',     'HannahNorris131@Fordham.edu',    '788-746-9849x89793',    '2000-04-15', 29, 3);

-- 7. Discount usage
INSERT INTO discount_used (username, discountId) VALUES
  ('JoshuaGomez141', 5),
  ('JoshuaGomez141', 1),
  ('HannahNorris131', 4),
  ('MichaelHensley123', 1),
  ('ErinMitchell118', 3),
  ('TimothySweeney192', 8),
  ('DarrellBryant59', 9),
  ('HannahNorris131', 4),
  ('TimothySweeney192', 9),
  ('MichaelHensley123', 2);

-- 8. Admins
INSERT INTO admin (
    username, firstName, lastName, password, email, phoneNo,
    supportUser, supportClub, supportStore
) VALUES
  ('MichelleGreen177','Michelle','Green','iA)69QMj','MichelleGreen177@gmail.com','(766)968-0632x7115', TRUE, FALSE, FALSE),
  ('DebbieLee17',    'Debbie',  'Lee',  'X*c9Q#x*', 'DebbieLee17@gmail.com',    TRUE, TRUE,  FALSE);
=======
INSERT INTO location (locationId, streetAddress, city, state, country, zipcode)
VALUES
(1, '15 Fruit St', 'San Francisco', 'Massachusetts', 'USA', '02110'),
(2, '15 Fruit St', 'San Francisco', 'Illinois', 'USA', '02110'),
(3, '15 Fruit St', 'New York', 'New York', 'USA', '11111'),
(4, '12 Summit Pl', 'Miami', 'California', 'USA', '77777'),
(5, '15 Fruit St', 'Boston', 'California', 'USA', '01950');
INSERT INTO college (collegeName, locationId, noOfStores, noOfUsers, domain)
VALUES
('Northwestern', 4, 0, 0, '@Northwestern.edu'),
('Northeastern', 5, 0, 0, '@Northeastern.edu'),
('UCBerkeley', 3, 0, 0, '@UCBerkeley.edu'),
('Fordham', 1, 0, 0, '@Fordham.edu'),
('UMiami', 1, 0, 0, '@UMiami.edu');
INSERT INTO store (storeId, name, locationId, priceRange, noOfDiscounts, hoursOfOperations, category, phoneNo, website, starRating, delivery, ageRestricted, totalSales, noOfOrders, college, clubId)
VALUES
(1, 'Wollastons', 5, '$$$', 0, '10:00am-5:00pm', 'clothing', '882.664.0395', 'parker.biz', 1, 0, 0, 13277, 47, 'UCBerkeley', NULL),
(2, 'Aroma Joes', 1, '$$$', 0, '11:00am-11:00pm', 'convenience', '8047451749', 'alexander-alvarez.info', 1, 0, 0, 3207, 81, 'UMiami', NULL),
(3, 'Star Market', 2, '$', 0, '10:00am-5:00pm', 'grocery', '+1-583-771-3698', 'sandoval-anderson.com', 3, 1, 0, 5003, 248, 'Northeastern', NULL),
(4, 'Panera', 5, '$$', 0, '12:00pm-9:00pm', 'grocery', '001-234-255-9391x3831', 'taylor-bailey.com', 4, 1, 1, 18902, 444, 'UMiami', NULL),
(5, 'Wollastons', 2, '$$$', 0, '7:00am-12:00am', 'clothing', '412-860-3707x648', 'perez.com', 4, 0, 0, 18453, 219, 'Northeastern', NULL);
INSERT INTO club (clubId, name, college, storeId, numberOfUsers)
VALUES
(1, 'Film Club', 'UCBerkeley', NULL, 0),
(2, 'Badminton Club', 'Northeastern', NULL, 0),
(3, 'Society of Women in Tech', 'Fordham', NULL, 0),
(4, 'Trivia Club', 'UMiami', NULL, 0),
(5, 'Phi Delta Theta', 'Northwestern', NULL, 0);
INSERT INTO discount (discountId, storeId, code, percentOff, item, startDate, endDate, ageRestricted, minPurchase, bdayDiscount)
VALUES
(1, 4, 'REDEEMCODE', 87, 'produce', '2025-04-14', '2025-04-15', 1, 94, 0),
(2, 4, 'SPRINGSALE', 8, 'books', '2025-03-20', '2025-05-05', 1, 13, 0),
(3, 4, 'SALECODE', 32, 'books', '2025-03-30', '2025-05-10', 0, 65, 0),
(4, 3, 'REDEEMCODE', 22, 'coffee', '2025-03-30', '2025-06-01', 1, 84, 1),
(5, 5, 'REDEEMCODE', 88, 'produce', '2025-04-14', '2025-05-05', 1, 23, 1),
(6, 1, 'SPRINGSALE', 22, 'books', '2025-04-14', '2025-04-15', 1, 34, 0),
(7, 3, 'SALECODE', 27, 'furniature', '2025-03-30', '2025-05-10', 0, 50, 1),
(8, 1, 'REDEEMCODE', 10, 'coffee', '2025-02-18', '2025-04-15', 0, 50, 0),
(9, 1, 'BUYBUYBUY', 25, 'clothing', '2025-04-14', '2025-05-05', 1, 21, 1),
(10, 5, 'BUYBUYBUY', 43, 'books', '2025-02-18', '2025-05-05', 1, 28, 1);
INSERT INTO user (username, firstName, lastName, password, college, email, phoneNo, birthdate, age, discountsUsed, clubId)
VALUES
('MeaganGay64', 'Meagan', 'Gay', '&3Nsh((l', 'UCBerkeley', 'MeaganGay64@UCBerkeley.edu', '616-542-6069', '1999-09-12', 23, 0, 5),
('KarenWalker95', 'Karen', 'Walker', 'PV+Qi7Bs', 'Fordham', 'KarenWalker95@Fordham.edu', '462-220-1324x2396', '1999-09-12', 21, 0, 3),
('KellyRobles135', 'Kelly', 'Robles', '_6Iv$Q6P', 'UMiami', 'KellyRobles135@UMiami.edu', '001-631-760-2178x0850', '2002-06-01', 19, 1, 4),
('ArielAyala34', 'Ariel', 'Ayala', 'Tg__4zBm', 'UMiami', 'ArielAyala34@UMiami.edu', '+1-994-640-8526x686', '2003-05-10', 30, 4, 2),
('PaulJohnson36', 'Paul', 'Johnson', 'N@U3Yuz)', 'UMiami', 'PaulJohnson36@UMiami.edu', '767-240-1769x5113', '2005-11-11', 19, 0, 2),
('LoganJones71', 'Logan', 'Jones', '*V0XeRCf', 'Northwestern', 'LoganJones71@Northwestern.edu', '382-746-8596', '2002-06-01', 19, 1, 5),
('TaylorContreras86', 'Taylor', 'Contreras', '$cS4Bya1', 'Northwestern', 'TaylorContreras86@Northwestern.edu', '2267857394', '2001-05-05', 18, 3, 2),
('SheliaArmstrong94', 'Shelia', 'Armstrong', '^a9VBb4t', 'UMiami', 'SheliaArmstrong94@UMiami.edu', '822-893-9440', '2001-05-05', 30, 5, 5),
('TammyHowell76', 'Tammy', 'Howell', 'E)uN65Nf', 'UCBerkeley', 'TammyHowell76@UCBerkeley.edu', '3115198345', '2003-05-10', 21, 2, 3),
('FrankMorton31', 'Frank', 'Morton', 'Q_1!BgOf', 'UMiami', 'FrankMorton31@UMiami.edu', '001-634-425-4856', '2005-11-11', 30, 0, 5);
INSERT INTO discount_used (username, discountId)
VALUES
('FrankMorton31', 3),
('SheliaArmstrong94', 4),
('LoganJones71', 7),
('TaylorContreras86', 3),
('MeaganGay64', 3),
('PaulJohnson36', 7),
('KellyRobles135', 9),
('FrankMorton31', 2),
('TammyHowell76', 5),
('FrankMorton31', 4);
INSERT INTO admin (username, firstName, lastName, password, email, phoneNo, supportUser, supportClub, supportStore)
VALUES
('ValerieMolina53', 'Valerie', 'Molina', 'RO@C4Exa', 'ValerieMolina53@gmail.com', '718-870-6829x0832', 'KellyRobles135', 5, 4),
('DavidZavala56', 'David', 'Zavala', 'B&5&6Qte', 'DavidZavala56@gmail.com', '+1-345-708-5215x714', 'LoganJones71', 3, 2);
>>>>>>> bd51fe0369dcdeda42cbdacac098b25074b5208a
