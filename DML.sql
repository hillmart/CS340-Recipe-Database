-- Need to replace the following in a query with actual values for use:
--   userID, 
--   emailInput,
--   restrictionIDInput,
--   recipeID,
--   nameInput,
--   servingsInput,
--   ingredientID,
--   quantity,
--   units 

-- get all dietary restrictions to populate the Restrictions dropdown
SELECT id, name FROM dietaryRestrictions

-- get all ingredients to populate the Ingredients dropdown
SELECT id, name FROM ingredients

-- get all users and their dietary restrictions
SELECT users.id, email, dietaryRestrictions.name AS restriction 
FROM users 
INNER JOIN dietaryRestrictions ON users.restrictionID = dietaryRestrictions.id

-- get a single user's data
SELECT id, email, restrictionID FROM users WHERE id = :userID

-- get all users' data to populate a dropdown for associating with a recipe
SELECT id, email FROM users

-- get all recipes to populate a dropdown for associating with users
SELECT id, name FROM recipes

-- get all recipes and their dietary restrictions
SELECT recipes.id, recipes.name, dietaryRestrictions.name AS restriction 
FROM recipes 
INNER JOIN dietaryRestrictions ON recipes.restrictionID = dietaryRestrictions.id

-- add a new user
INSERT INTO users (email, restrictionID) VALUES (:emailInput, :restrictionIDInput)

-- associate a user with a recipe
INSERT INTO userRecipes (userID, recipeID, dateAdded) VALUES (:userID, :recipeID, :dateAdded)

-- update a user's data
UPDATE users SET email = :emailInput, restrictionID = :restrictionIDInput WHERE id = :userID

-- delete a user
DELETE FROM users WHERE id = :userID

-- get a single recipe's data
SELECT id, name, servings, restrictionID FROM recipes WHERE id = :recipeID

-- add a new recipe
INSERT INTO recipes (name, servings, restrictionID) VALUES (:nameInput, :servingsInput, :restrictionIDInput)

-- update a recipe's data
UPDATE recipes SET name = :nameInput, servings = :servingsInput, restrictionID = :restrictionIDInput WHERE id = :recipeID

-- delete a recipe
DELETE FROM recipes WHERE id = :recipeID

-- get all ingredients in a recipe
SELECT ingredientsInRecipes.ingredientID, ingredientsInRecipes.quantity, ingredientsInRecipes.units, ingredients.name
FROM ingredientsInRecipes 
INNER JOIN ingredients ON ingredientsInRecipes.ingredientID = ingredients.id 
WHERE ingredientsInRecipes.recipeID = :recipeID

-- add an ingredient to a recipe
INSERT INTO ingredientsInRecipes (ingredientID, recipeID, quantity, units) VALUES (:ingredientID, :recipeID, :quantity, :units)

-- update an ingredient in a recipe
UPDATE ingredientsInRecipes SET quantity = :quantity, units = :units WHERE ingredientID = :ingredientID AND recipeID = :recipeID

-- delete an ingredient from a recipe
DELETE FROM ingredientsInRecipes WHERE ingredientID = :ingredientID AND recipeID = :recipeID

-- dis-associate a recipe from a user
DELETE FROM userRecipes WHERE userID = :userID AND recipeID = :recipeID
