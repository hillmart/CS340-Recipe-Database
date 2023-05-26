from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

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

        # if request.form.get("Edit_User"):
        #     userID = request.form["userID"]
        #     email = request.form["email"]
        #     restrictionID = request.form["restrictionID"]

        #     if restrictionID == "null":
        #         restrictionID = None

        #     query = "UPDATE users SET email=%s, restrictionID = %s WHERE userID = %s"
        #     cur = mysql.connection.cursor()
        #     cur.execute(query, (email, restrictionID, userID))
        #     mysql.connection.commit()

        return redirect("/users")

@app.route("/edit_user/<int:id>", methods=["POST"])
def edit_user(id):
    if request.method == "POST":
        if request.form.get("Edit_User"):
            email = request.form["email"]
            restrictionID = request.form["restrictionID"]

            if restrictionID == "null":
                restrictionID = None

            query = "UPDATE users SET email = %s, restrictionID = %s WHERE userID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (email, restrictionID, id))
            mysql.connection.commit()

        return redirect("/users")

@app.route("/delete_user/<int:id>")
def delete_user(id):
    query = "DELETE FROM users WHERE userID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/users")

@app.route('/recipes')
def recipes():
    # Establish a connection to the database
    cur = mysql.connection.cursor()

    # Execute a query to fetch user data from the database
    cur.execute("SELECT * FROM recipes")
    recipes = cur.fetchall()

    # Render the .j2 template and pass the user data as a variable
    return render_template('recipes.j2', recipes=recipes)
  
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

@app.route('/userRecipes')
def userRecipes():
    # Establish a connection to the database
    cur = mysql.connection.cursor()

    # Execute a query to fetch user data from the database
    cur.execute("SELECT * FROM userRecipes")
    ur = cur.fetchall()

    # Render the .j2 template and pass the user data as a variable
    return render_template('userRecipes.j2', userRecipes=ur)

# Listener
if __name__ == "__main__":

    port = int(os.environ.get('PORT', 56305))
    #Start the app on port 56305, it will be different once hosted
    app.run(debug=True, port=56305, host='0.0.0.0')
    
    
