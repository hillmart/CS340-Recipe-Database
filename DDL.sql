-- Query to create the 6 tables below.
-- DROP TABLE userRecipes, recipeIngredients, users, recipes, ingredients, dietaryRestrictions;
-- DROP TABLE ingredientsInRecipes;

CREATE OR REPLACE TABLE dietaryRestrictions(
    restrictionId int(11) NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    PRIMARY KEY (restrictionId)
);

CREATE OR REPLACE TABLE ingredients(
    ingredientId int(11) NOT NULL AUTO_INCREMENT,
    price int(11) NOT NULL,
    name varchar(255) NOT NULL,
    PRIMARY KEY (ingredientId)
);

CREATE OR REPLACE TABLE users(
    userId int(11) NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL,
    restrictionID int(11),
    PRIMARY KEY (userId),
    FOREIGN KEY (restrictionID) REFERENCES dietaryRestrictions(restrictionId)
);

CREATE OR REPLACE TABLE recipes(
    recipeId int(11) NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    servings int(11) NOT NULL,
    restrictionID int(11),
    PRIMARY KEY (recipeId),
    FOREIGN KEY (restrictionID) REFERENCES dietaryRestrictions(restrictionId)
);

CREATE OR REPLACE TABLE userRecipes(
  userID int(11) NOT NULL,
  recipeID int(11) NOT NULL,
  dateAdded DATE NOT NULL,
  PRIMARY KEY (userID, recipeID),
  FOREIGN KEY (userID) REFERENCES users(userId),
  FOREIGN KEY (recipeID) REFERENCES recipes(recipeId)
);

CREATE OR REPLACE TABLE recipeIngredients(
  ingredientID int(11) NOT NULL,
  recipeID int(11) NOT NULL,
  quantity int(11) NOT NULL,
  units varchar(255) NOT NULL,
  PRIMARY KEY (ingredientID, recipeID),
  FOREIGN KEY (ingredientID) REFERENCES ingredients(ingredientId),
  FOREIGN KEY (recipeID) REFERENCES recipes(recipeId)
);

-- Queries to insert data
INSERT INTO dietaryRestrictions (name) 
VALUES 
('Vegetarian'),
('Gluten-free'),
('Vegan');

INSERT INTO users (email, restrictionID) 
VALUES 
('john.doe@example.com', (SELECT restrictionId from dietaryRestrictions where name = 'Vegetarian')),
('jane.smith@example.com', (SELECT restrictionId from dietaryRestrictions where name = 'Gluten-free')),
('mark.jones@example.com', (SELECT restrictionId from dietaryRestrictions where name = 'Vegan')),
('emma.taylor@example.com', (SELECT restrictionId from dietaryRestrictions where name = 'Vegetarian')),
('will.brown@example.com', (SELECT restrictionId from dietaryRestrictions where name = 'Gluten-free'));

INSERT INTO recipes (name, servings, restrictionID) 
VALUES 
('Tomato Soup', 4, (SELECT restrictionId from dietaryRestrictions where name = 'Vegetarian')),
('Grilled Chicken', 2, NULL),
('Vegan Tacos', 4, (SELECT restrictionId from dietaryRestrictions where name = 'Vegan')),
('Gluten-free Pasta', 4, (SELECT restrictionId from dietaryRestrictions where name = 'Gluten-free')),
('Garden Salad', 2, (SELECT restrictionId from dietaryRestrictions where name = 'Vegetarian'));

INSERT INTO ingredients (price, name) 
VALUES 
(1, 'Tomatoes'),
(2, 'Chicken'),
(1, 'Lettuce'),
(3, 'Vegan Cheese'),
(1, 'Gluten-free Noodles');

INSERT INTO userRecipes (userID, recipeID, dateAdded) 
VALUES 
((SELECT userId from users where email = 'john.doe@example.com'),
 (SELECT recipeId from recipes where name = 'Tomato Soup'),
 '2023-04-01'),
((SELECT userId  from users where email = 'jane.smith@example.com'),
 (SELECT recipeId from recipes where name = 'Vegan Tacos'),
 '2023-04-05'),
((SELECT userId  from users where email = 'jane.smith@example.com'),
 (SELECT recipeId from recipes where name = 'Grilled Chicken'),
 '2023-04-05'),
((SELECT userId  from users where email = 'mark.jones@example.com'),
 (SELECT recipeId from recipes where name = 'Vegan Tacos'),
 '2023-04-10'),
((SELECT userId  from users where email = 'emma.taylor@example.com'),
 (SELECT recipeId from recipes where name = 'Gluten-free Pasta'),
 '2023-04-15'),
((SELECT userId  from users where email = 'will.brown@example.com'),
 (SELECT recipeId from recipes where name = 'Garden Salad'),
 '2023-04-20');

INSERT INTO recipeIngredients (ingredientID, recipeID, quantity, units) 
VALUES 
((SELECT ingredientID from ingredients where name = 'Tomatoes'),
 (SELECT recipeId from recipes where name = 'Tomato Soup'),
 4,
 'cups'),

 ((SELECT ingredientID from ingredients where name = 'Lettuce'),
  (SELECT recipeId from recipes where name = 'Tomato Soup'),
  2,
  'cups'),

 ((SELECT ingredientID from ingredients where name = 'Chicken'),
  (SELECT recipeId from recipes where name = 'Grilled Chicken'),
  1,
  'pounds'),

 ((SELECT ingredientID from ingredients where name = 'Vegan Cheese'),
  (SELECT recipeId from recipes where name = 'Vegan Tacos'),
  1,
  'packages'),
 ((SELECT ingredientID from ingredients where name = 'Gluten-free Noodles'),
  (SELECT recipeId from recipes where name = 'Gluten-free Pasta'),
  1,
  'packages'),

 ((SELECT ingredientID from ingredients where name = 'Lettuce'),
  (SELECT recipeId from recipes where name = 'Garden Salad'),
  4,
  'cups'),

 ((SELECT ingredientID from ingredients where name = 'Tomatoes'),
  (SELECT recipeId from recipes where name = 'Garden Salad'),
  2,
  'cups');

-- Test queries.
select * from users;
select * from recipes;
select * from ingredients;
select * from dietaryRestrictions;
select * from userRecipes;
select * from recipeIngredients;
