-- sample users
INSERT INTO users (firstName, middleName, lastName, mobile, email, passwordHash, lastLogin, intro, profile, totalPosts) VALUES
('Amelia', 'Ann', 'Rogers', '123-456-7890', 'amelia@example.com', 'secret1', NOW(), 'Student', 'Student at Northeastern.', 0),
('Charlie', 'Brian', 'Smith', '838-238-2343', 'charlie@example.com', 'secret2', NOW(), 'Student', 'Student at Northeastern', 0),
('Andrew', NULL, 'Burke', '345-678-9012', 'andrew@example.com', 'secret3', NOW(), 'HVAC', 'Provides HVAC services', 0),
('Timmy', 'Chris', 'Chalamet', '456-789-0123', 'timmy@example.com', 'secret4', NOW(), 'Actor', 'Dune', 0),
('Belle', NULL, 'Field', '567-890-1234', 'belle@example.com', 'secret5', NOW(), 'Cook', 'Home chef', 0),
('Lindsey', 'Jane', 'Barbella', '678-901-2345', 'lindsey@example.com', 'secret6', NOW(), 'Biologist', 'Travels', 0);

-- sample tags
INSERT INTO tags (title, metaTitle, slug, content) VALUES
('Memes', 'funny', 'silly', 'Edited photos and videos'),
('Finance', 'AI advancements', 'ai', 'Finance and AI'),
('Football', 'Sports Insider', 'teams', 'football plays'),
('Coding', 'Computer Science', 'cs', 'CS and technology topics.');

-- sample categories
INSERT INTO categories (title, metaTitle, slug, content) VALUES
('Entertainment', 'Pop culture', 'entertainment', 'movies, tv, and radio'),
('Technology', 'tech and innovation', 'technology', 'exploring new coding solutions and ai advancements'),
('Sports', 'sports news', 'sports', 'updates on major sports');


-- sample blog posts //used AI generation for sample text, did not use for SQL clauses
INSERT INTO posts (authorId, title, metaTitle, slug, summary, published, createdAt, updatedAt, publishedAt, content) VALUES
(1, 'The Future of AI in Finance', 'AI transforming the financial world', 'ai-finance', 'Exploring AI in financial markets.', 1, NOW(), NOW(), NOW(), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
(2, 'Why Football Strategies Matter', 'Game-winning plays analyzed', 'football-strategies', 'Breaking down winning football strategies.', 1, NOW(), NOW(), NOW(), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
(3, 'How to Maintain Your HVAC System', 'Tips for HVAC longevity', 'hvac-maintenance', 'Essential HVAC maintenance tips.', 1, NOW(), NOW(), NOW(), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
(4, 'Breaking Down the Dune Movie', 'Timothée Chalamet shines', 'dune-review', 'A deep dive into the latest Dune movie.', 1, NOW(), NOW(), NOW(), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
(5, 'The Rise of Home Cooking Trends', 'Why cooking at home is booming', 'home-cooking', 'How people are embracing home-cooked meals.', 1, NOW(), NOW(), NOW(), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
(6, 'Top 10 Coding Mistakes Beginners Make', 'Common errors in coding', 'coding-mistakes', 'Avoid these common programming pitfalls.', 1, NOW(), NOW(), NOW(), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.');


INSERT INTO post_tags (postId, tagId) VALUES
(1, 2), (1, 4),
(2, 3), (2, 1),
(3, 1), (3, 3),
(4, 1), (4, 2),
(5, 1), (5, 3),
(6, 2), (6, 4);


INSERT INTO post_categories (postId, categoryId) VALUES
(1, 2),
(2, 3),
(3, 2),
(4, 1),
(5, 1),
(6, 2);

-- sample comments //used AI generation for sample text, did not use for SQL clauses
INSERT INTO post_comments (postId, title, published, createdAt, publishedAt, content) VALUES
(1, 'AI in finance is amazing!', 1, NOW(), NOW(), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
(2, 'Football is the best sport!', 1, NOW(), NOW(), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
(4, 'Dune was visually stunning!', 1, NOW(), NOW(), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
(6, 'I have made every mistake on this list.', 1, NOW(), NOW(), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.');


