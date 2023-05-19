const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');

const app = express();
app.use(bodyParser.json());

// MySQL connection
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'recipes' 
});

// Connect to database
db.connect((err) => {
    if(err) throw err;
    console.log('MySQL connected...');
});

// Search route
app.post('/searchRecipes', (req, res) => {
    let searchTitle = '%' + req.body.title + '%';
    let restrictionId = req.body.restrictionId;
    let sql = 'SELECT * FROM recipes WHERE name LIKE ? AND restrictionId = ?';
    db.query(sql, [searchTitle, restrictionId], (err, result) => {
        if (err) throw err;
        res.json(result);
    });
});

app.use(bodyParser.json());

// Start server
app.listen(3000, () => console.log('Server started on port 3000'));
