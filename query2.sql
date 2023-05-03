-- Queries to insert data
INSERT INTO users (userID, email, restrictionID) 
VALUES 
('1', 'user1@gmail.com', '1'),
('2', 'user2@gmail.com', '2'),
('3', 'user3@gmail.com', '3');

INSERT INTO recipes (recipeID, name, servings, restrictionID) 
VALUES 
('1', 'Pasta', '4', '1'),
('2', 'Pizza', '2', '2'),
('3', 'Salad', '3', '1');

INSERT INTO ingredients (ingredientID, price, name) 
VALUES 
('1', '10', 'cheese'),
('2', '1', 'tomatoes'),
('3', '5', 'dough');

INSERT INTO dietaryRestrictions (restrictionID, name) 
VALUES 
('1', 'gluten-free'),
('2', 'vegetarian'),
('3', 'keto');

INSERT INTO userRecipes (userID, recipeID, dateAdded) 
VALUES 
('1', '1', '2023-05-02'),
('1', '2', '2023-05-03'),
('2', '1', '2023-05-04');

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
