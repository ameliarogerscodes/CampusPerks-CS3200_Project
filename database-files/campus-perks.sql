-- 1. Seed Locations
INSERT INTO location (
  locationId, streetAddress, city, state, country, zipCode
) VALUES
  (1, '360 huntington ave',    'boston', 'ma',  'usa', '02115'),
  (2, '881 commonwealth ave',  'boston', 'ma',  'usa', '02215');

-- 2. Seed Colleges
INSERT INTO college (
  collegeName, locationId, noOfStores, noOfUsers, domain
) VALUES
  ('northeastern university',  1, 0, 0, 'northeastern.edu'),
  ('boston university',        2, 0, 0, 'bu.edu');

-- 3. Seed Users (personas)
INSERT INTO user (
  username, firstName, lastName, password, college,
  email, phoneNo, birthdate, age, discountsUsed, clubId
) VALUES
  ('beth_smith',   'Beth',   'Smith',    'farmers123', 'northeastern university',
                   'beth@farmershorse.com', '617-555-0101', '1988-05-20',
                   36, 0, NULL),
  ('bharat_m',     'Bharat', 'Malipeddi','student123', 'northeastern university',
                   'bharat@neu.edu',       '617-555-0102', '2000-11-15',
                   23, 0, NULL),
  ('glen_howard',  'Glen',   'Howard',   'csclub456',  'northeastern university',
                   'glen@neu.edu',         '617-555-0103', '2002-03-10',
                   21, 0, NULL);

-- 4. Seed Clubs
INSERT INTO club (
  name, college, storeId, numberOfUsers
) VALUES
  ('cs club',        'northeastern university', NULL, 120),
  ('husky hackers',  'northeastern university', NULL,  85);

-- 5. Seed Stores
INSERT INTO store (
  name, locationId, priceRange, noOfDiscounts,
  hoursOfOperations, category, phoneNo,
  website, starRating, delivery, ageRestricted,
  totalSales, noOfOrders, college, clubId
) VALUES
  ('farmers horse coffee', 1, '$$', 0,
   '6am-8pm',   'cafe',   '617-373-2000',
    NULL,          NULL,   FALSE, FALSE,
    0.00,          0,      'northeastern university', NULL),
  ('bu bookstore',        2, '$$$', 0,
   '9am-7pm',   'books',  '617-353-2500',
    NULL,          NULL,   FALSE, FALSE,
    0.00,          0,      'boston university',       NULL);

-- 6. Seed Discounts
INSERT INTO discount (
  discountId, storeId, code, percentOff, item,
  startDate, endDate, ageRestricted, minPurchase, bdayDiscount
) VALUES
  (1, 1, 'COFFEE10',   10, 'any coffee drink',
     '2025-04-01', '2025-05-01', FALSE, NULL, FALSE),
  (2, 1, 'PASTRY15',   15, 'any pastry',
     '2025-04-01', '2025-04-30', FALSE, NULL, FALSE),
  (3, 2, 'TEXTBOOK5',   5, 'textbooks',
     '2025-04-01', '2025-06-01', FALSE, NULL, FALSE);

-- 7. Seed Admins
INSERT INTO admin (
  username, firstName, lastName, password, email, phoneNo,
  supportUser, supportClub, supportStore
) VALUES
  ('john_doe',    'John',   'Doe',   'admin123', 'john@campusperks.com',  '617-555-0301',
                   NULL,       NULL,        NULL),
  ('amanda_lee',  'Amanda', 'Lee',   'admin456', 'amanda@campusperks.com','617-555-0302',
                   NULL,       NULL,        NULL);


-- 9. Seed Discount Usage (bookmarks)
INSERT INTO discount_used (username, discountId) VALUES
  ('bharat_m',    1),
  ('bharat_m',    2),
  ('glen_howard', 1);

