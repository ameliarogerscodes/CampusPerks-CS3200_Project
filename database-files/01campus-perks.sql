USE campusPerks_db;

-- 1. Locations
INSERT INTO location (streetAddress, city, state, country, zipCode) VALUES
  ('199 High St',    'Chicago',       'Illinois',    'USA', '90210'),
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
     'UCBerkeley.com', 2.0, FALSE, TRUE,   938.00,   143, 'Northeastern'),
  ('Wollastons',    '14 Baker St',    'San Francisco', 'California',  'USA',
     '$', 0, '11:00am-11:00pm', 'convenience', '983-918-4580x57676',
     'UCBerkeley.com', 2.0, FALSE, TRUE,  16196.00,     0, 'UCBerkeley');

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
INSERT INTO `user` (
    username, firstName, lastName, password, college, email,
    phoneNo, birthdate, age, discountsUsed
) VALUES
  ('DarrellBryant59',   'Darrell', 'Bryant',  'j^1mLTFx', 'UMiami',      'DarrellBryant59@UMiami.edu',   '+1-668-274-0345',   '2003-05-10', 30, 5),
  ('JoshuaGomez141',    'Joshua',  'Gomez',   '@85ZCnM^', 'Fordham',     'JoshuaGomez141@Fordham.edu',    '(332)499-6459',     '2001-05-05', 19, 5),
  ('JeffreySims164',    'Jeffrey', 'Sims',    '#@!9B+Nc', 'Fordham',     'JeffreySims164@Fordham.edu',    '001-895-562-2539',  '2000-04-15', 25, 4),
  ('TimothySweeney192', 'Timothy', 'Sweeney', 'Q3^0A$pK', 'Fordham',     'TimothySweeney192@Fordham.edu', '+1-647-717-9419',   '2003-05-10', 23, 3),
  ('AustinWarren83',    'Austin',  'Warren',  ')3ebGJb*', 'Fordham',     'AustinWarren83@Fordham.edu',    '001-829-448-7075',  '2003-05-10', 29, 3),
  ('JonathanYork86',    'Jonathan','York',    '@E*g9Eid', 'UCBerkeley', 'JonathanYork86@UCBerkeley.edu','736.687.6018x49308','2000-04-15', 18, 2),
  ('MichaelHensley123', 'Michael', 'Hensley', 'G&+R7Kj%', 'UMiami',      'MichaelHensley123@UMiami.edu',  '(628)850-9885',     '2002-06-01', 25, 3),
  ('ErinMitchell118',   'Erin',    'Mitchell','4Z&R8Qze', 'UMiami',      'ErinMitchell118@UMiami.edu',    '001-317-967-1695',  '2000-04-15', 19, 4),
  ('JasonHolt143',      'Jason',   'Holt',    't&#@4hBy', 'UCBerkeley', 'JasonHolt143@UCBerkeley.edu',   '(839)861-2384',     '2002-06-01', 25, 3),
  ('HannahNorris131',   'Hannah',  'Norris',  'v!5W*bCD', 'Fordham',     'HannahNorris131@Fordham.edu',    '788-746-9849',      '2000-04-15', 29, 3);

-- 7. Discount usage
INSERT INTO discount_used (username, discountId) VALUES
  ('JoshuaGomez141',    5),
  ('JoshuaGomez141',    1),
  ('HannahNorris131',   4),
  ('MichaelHensley123', 1),
  ('ErinMitchell118',   3),
  ('TimothySweeney192', 8),
  ('DarrellBryant59',   9),
  ('TimothySweeney192', 9),
  ('MichaelHensley123', 2);

-- 8. Admins
INSERT INTO admin (
    username, firstName, lastName, password, email, phoneNo,
    supportUser, supportClub, supportStore
) VALUES
  ('MichelleGreen177','Michelle','Green','iA)69QMj','MichelleGreen177@gmail.com','(766)968-0632', TRUE, FALSE, FALSE),
  ('DebbieLee17',    'Debbie',  'Lee',  'X*c9Q#x*', 'DebbieLee17@gmail.com',    '(430)434-2285', TRUE, TRUE,  FALSE);
