-- Query to create the 6 tables below.
-- DROP TABLE userRecipes, ingredientsInRecipes, users, recipes, ingredients, dietaryRestrictions;

CREATE TABLE dietaryRestrictions(
    restrictionID int(11) NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    PRIMARY KEY (restrictionID)
);

CREATE TABLE ingredients(
    ingredientID int(11) NOT NULL AUTO_INCREMENT,
    price int(11) NOT NULL,
    name varchar(255) NOT NULL,
    PRIMARY KEY (ingredientID)
);

CREATE TABLE users(
    userID int(11) NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL,
    restrictionID int(11) NOT NULL,
    PRIMARY KEY (userID),
    FOREIGN KEY (restrictionID) REFERENCES dietaryRestrictions(restrictionID)
);

CREATE TABLE recipes(
    recipeID int(11) NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    servings int(11) NOT NULL,
    restrictionID int(11) NOT NULL,
    PRIMARY KEY (recipeID),
    FOREIGN KEY (restrictionID) REFERENCES dietaryRestrictions(restrictionID)
);

CREATE TABLE userRecipes(
  userID int(11) NOT NULL,
  recipeID int(11) NOT NULL,
  dateAdded DATE NOT NULL,
  PRIMARY KEY (userID, recipeID),
  FOREIGN KEY (userID) REFERENCES users(userID),
  FOREIGN KEY (recipeID) REFERENCES recipes(recipeID)
);

CREATE TABLE ingredientsInRecipes(
  ingredientID int(11) NOT NULL,
  recipeID int(11) NOT NULL,
  quantity int(11) NOT NULL,
  units varchar(255) NOT NULL,
  PRIMARY KEY (ingredientID, recipeID),
  FOREIGN KEY (ingredientID) REFERENCES ingredients(ingredientID),
  FOREIGN KEY (recipeID) REFERENCES recipes(recipeID)
);

-- Test that the tables were created.
DESCRIBE users;
DESCRIBE recipes;
DESCRIBE ingredients;
DESCRIBE dietaryRestrictions;
DESCRIBE userRecipes;
DESCRIBE ingredientsInRecipes;


