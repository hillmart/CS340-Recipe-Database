-- Queries to insert data
INSERT INTO dietaryRestrictions (name) 
VALUES 
('Vegetarian'),
('Gluten-free'),
('Vegan');

INSERT INTO users (email, restrictionID) 
VALUES 
('john.doe@example.com', (SELECT id from dietaryRestrictions where name = 'Vegetarian')),
('jane.smith@example.com', (SELECT id from dietaryRestrictions where name = 'Gluten-free')),
('mark.jones@example.com', (SELECT id from dietaryRestrictions where name = 'Vegan')),
('emma.taylor@example.com', (SELECT id from dietaryRestrictions where name = 'Vegetarian')),
('will.brown@example.com', (SELECT id from dietaryRestrictions where name = 'Gluten-free'));

INSERT INTO recipes (name, servings, restrictionID) 
VALUES 
('Tomato Soup', '4', (SELECT id from dietaryRestrictions where name = 'Vegetarian')),
('Grilled Chicken', '2', NULL),
('Vegan Tacos', '4', (SELECT id from dietaryRestrictions where name = 'Vegan')),
('Gluten-free Pasta', '4', (SELECT id from dietaryRestrictions where name = 'Gluten-free')),
('Garden Salad', '2', (SELECT id from dietaryRestrictions where name = 'Vegetarian'));

INSERT INTO ingredients (price, name) 
VALUES 
('1', 'Tomatoes'),
('2', 'Chicken'),
('1', 'Lettuce'),
('3', 'Vegan Cheese'),
('1', 'Gluten-free Noodles');

INSERT INTO userRecipes (userID, recipeID, dateAdded) 
VALUES 
((SELECT id from users where email = 'john.doe@example.com'),
 (SELECT id from recipes where name = 'Tomato Soup'),
 '2023-04-01'),
((SELECT id from users where email = 'jane.smith@example.com'),
 (SELECT id from recipes where name = 'Grilled Chicken'),
 '2023-04-05'),
((SELECT id from users where email = 'mark.jones@example.com'),
 (SELECT id from recipes where name = 'Vegan Tacos'),
 '2023-04-10'),
((SELECT id from users where email = 'emma.taylor@example.com'),
 (SELECT id from recipes where name = 'Gluten-free Pasta'),
 '2023-04-15'),
((SELECT id from users where email = 'will.brown@example.com'),
 (SELECT id from recipes where name = 'Garden Salad'),
 '2023-04-20');

INSERT INTO ingredientsInRecipes (ingredientID, recipeID, quantity, units) 
VALUES 
('1', '1', '1', 'lbs'),
('1', '2', '3', 'tomatoes'),
('1', '3', '1', 'lbs');

-- Test queries.
select * from users;
select * from recipes;
select * from ingredients;
select * from dietaryRestrictions;
select * from userRecipes;
select * from ingredientsInRecipes;
