from flask import Flask, render_template, json, redirect, flash
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)
app.secret_key = "1234567890" 

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_hillmart'
app.config['MYSQL_PASSWORD'] = '7778' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_hillmart'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)


# Routes
@app.route('/')
def home():

    return render_template("main.j2")

@app.route('/users', methods=["POST", "GET"])
def users():
    if request.method == "GET":
        # Establish a connection to the database
        cur = mysql.connection.cursor()

        # Execute a query to fetch user data from the database
        cur.execute("SELECT users.userID, email, users.restrictionID FROM users")
        users = cur.fetchall()

        # Execute a query to fetch dietary restrictions from the database
        cur.execute("SELECT restrictionID, name FROM dietaryRestrictions")
        dietary_restrictions = cur.fetchall()

        # Render the .j2 template and pass the user and dietary_restrictions data as variables
        return render_template('users.j2', users=users, dietaryRestrictions=dietary_restrictions)

    if request.method == "POST":
        if request.form.get("Add_User"):
            email = request.form["email"]
            restrictionID = request.form["restrictionID"]

            if restrictionID == "null":
                restrictionID = None

            query = "INSERT INTO users (email, restrictionID) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (email, restrictionID))
            mysql.connection.commit()

        return redirect("/users")

@app.route('/edit_user/<int:id>', methods=["POST","GET"])
def edit_user(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM users WHERE userID = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (id,))
        data = cur.fetchone()

        # mySQL query to grab planet id/name data for our dropdown
        query2 = "SELECT * FROM dietaryRestrictions"
        cur.execute(query2)
        restrictions_data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("editUsers.j2", data=data, restrictions_data=restrictions_data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button
        if request.form.get("Edit_User"):
            # grab user form inputs
            id = request.form["userID"]
            email = request.form["email"]
            restrictionID = request.form["restrictionID"]

            if restrictionID == "null":
                restrictionID = None

            query = "UPDATE users SET users.email = %s, users.restrictionID = %s WHERE users.userID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (email, restrictionID, id))
            mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/users")

@app.route("/delete_user/<int:id>")
def delete_user(id):
    query = "DELETE FROM users WHERE userID = '%s'"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/users")

@app.route('/recipes', methods=["POST", "GET"])
def recipes():
    if request.method == "GET":
        # Establish a connection to the database
        cur = mysql.connection.cursor()

        # Execute a query to fetch user data from the database
        cur.execute("SELECT * FROM recipes")
        recipes = cur.fetchall()

        # Execute a query to fetch dietary restrictions from the database
        cur.execute("SELECT restrictionID, name FROM dietaryRestrictions")
        dietary_restrictions = cur.fetchall()

        # Render the .j2 template and pass the user and dietary_restrictions data as variables
        return render_template('recipes.j2', recipes=recipes, dietaryRestrictions=dietary_restrictions)

    if request.method == "POST":
        if request.form.get("Add_Recipe"):
            name = request.form["name"]
            servings = request.form["servings"]
            restrictionID = request.form["restrictionID"]

            if restrictionID == "null":
                restrictionID = None

            query = "INSERT INTO recipes (name, servings, restrictionID) VALUES (%s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, servings, restrictionID))
            mysql.connection.commit()

        return redirect("/recipes")

@app.route('/edit_recipe/<int:id>', methods=["POST","GET"])
def edit_recipe(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM recipes WHERE recipeID = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (id,))
        data = cur.fetchone()

        # mySQL query to grab planet id/name data for our dropdown
        query2 = "SELECT * FROM dietaryRestrictions"
        cur.execute(query2)
        restrictions_data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("editRecipes.j2", data=data, restrictions_data=restrictions_data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button
        if request.form.get("Edit_Recipe"):
            # grab user form inputs
            id = request.form["recipeID"]
            name = request.form["name"]
            servings = request.form["servings"]
            restrictionID = request.form["restrictionID"]

            if restrictionID == "null":
                restrictionID = None

            query = "UPDATE recipes SET recipes.name = %s, recipes.servings = %s, recipes.restrictionID = %s WHERE recipes.recipeID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, servings, restrictionID, id))
            mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/recipes")

@app.route("/delete_recipe/<int:id>")
def delete_recipe(id):
    query = "DELETE FROM recipes WHERE recipeID = '%s'"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/recipes")

@app.route('/ingredients')
def ingredients():
    # Establish a connection to the database
    cur = mysql.connection.cursor()

    # Execute a query to fetch user data from the database
    cur.execute("SELECT * FROM ingredients")
    ingredients = cur.fetchall()

    # Render the .j2 template and pass the user data as a variable
    return render_template('ingredients.j2', ingredients=ingredients)

@app.route('/dietaryRestrictions')
def dietaryRestrictions():
    # Establish a connection to the database
    cur = mysql.connection.cursor()

    # Execute a query to fetch user data from the database
    cur.execute("SELECT * FROM dietaryRestrictions")
    dietaryRestrictions = cur.fetchall()

    # Render the .j2 template and pass the user data as a variable
    return render_template('dietaryRestrictions.j2', dietaryRestrictions=dietaryRestrictions)

@app.route('/recipeIngredients')
def recipeIngredients():
    # Establish a connection to the database
    cur = mysql.connection.cursor()

    # Execute a query to fetch user data from the database
    cur.execute("SELECT * FROM recipeIngredients")
    recipeIngredients = cur.fetchall()

    # Render the .j2 template and pass the user data as a variable
    return render_template('recipeIngredients.j2', recipeIngredients=recipeIngredients)

@app.route('/userRecipes', methods=["POST", "GET"])
def userRecipes():
    if request.method == "GET":
        # Establish a connection to the database
        cur = mysql.connection.cursor()

        # Execute a query to fetch user data from the database
        cur.execute("SELECT * FROM userRecipes")
        userRecipes = cur.fetchall()

        # Execute a query to fetch dietary restrictions from the database
        cur.execute("SELECT userID, email FROM users")
        users = cur.fetchall()

        cur.execute("SELECT recipeID, name FROM recipes")
        recipes = cur.fetchall()

        # Render the .j2 template and pass the user and dietary_restrictions data as variables
        return render_template('userRecipes.j2', userRecipes=userRecipes, users=users, recipes=recipes)

    if request.method == "POST":
        if request.form.get("Add_User_Recipe"):
            userID = request.form["userID"]
            recipeID = request.form["recipeID"]
            dateAdded = request.form["dateAdded"]
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM userRecipes WHERE userID = %s AND recipeID = %s", (userID, recipeID))
            preexisting = cur.fetchall()
            if preexisting:
                flash("Combination already exists.","error")
            else:
                query = "INSERT INTO userRecipes (userID, recipeID, dateAdded) VALUES (%s, %s, %s)"
                cur.execute(query, (userID, recipeID, dateAdded))
                mysql.connection.commit()

        return redirect("/userRecipes")

@app.route("/edit_user_recipe/<string:userIDs>", methods=["POST","GET"])
def edit_user_recipe(userIDs):
    userID, recipeID = userIDs.split(',')
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM userRecipes WHERE userID = %s AND recipeID = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (userID, recipeID,))
        data = cur.fetchone()

        # Execute a query to fetch dietary restrictions from the database
        cur.execute("SELECT userID, email FROM users")
        users = cur.fetchall()

        cur.execute("SELECT recipeID, name FROM recipes")
        recipes = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("editUserRecipes.j2", data=data, users=users, recipes=recipes)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button
        if request.form.get("Edit_User_Recipe"):
            # grab user form inputs
            newUserID = request.form["userID"]
            newRecipeID = request.form["recipeID"]
            dateAdded = request.form["dateAdded"]
            cur = mysql.connection.cursor()
            query = "DELETE FROM userRecipes WHERE userID = %s AND recipeID = %s;" 
            query2 = "INSERT INTO userRecipes (userID, recipeID, dateAdded) VALUES (%s, %s, %s)"
            cur.execute(query, (userID, recipeID))
            mysql.connection.commit()
            cur.execute(query2, (newUserID, newRecipeID, dateAdded))
            mysql.connection.commit()
            return redirect("/userRecipes")
            

@app.route("/delete_user_recipe/<string:userIDs>")
def delete_user_recipe(userIDs):
    userID, recipeID = userIDs.split(',')
    query = "DELETE FROM userRecipes WHERE userID = %s AND recipeID = %s"
    cur = mysql.connection.cursor()
    cur.execute(query, (userID, recipeID,))
    mysql.connection.commit()

    return redirect("/userRecipes")

# Listener
if __name__ == "__main__":

    port = int(os.environ.get('PORT', 56305))
    #Start the app on port 56305, it will be different once hosted
    app.run(debug=True, port=56305, host='0.0.0.0')
    
    
