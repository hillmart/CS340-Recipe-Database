/*
    SETUP
*/
// MySQL
var db = require('./db-connector')

// Express
var express = require('express');   // We are using the express library for the web server
var app     = express();            // We need to instantiate an express object to interact with the server in our code
PORT        = 8656;                 // Set a port number at the top so it's easy to change in the future
app.use(express.json())
app.use(express.urlencoded({extended: true}))

// Handlebars
const { engine } = require('express-handlebars');
var exphbs = require('express-handlebars');     // Import express-handlebars
app.engine('.hbs', exphbs({extname: ".hbs"}));  // Create an instance of the handlebars engine to process templates
app.set('view engine', '.hbs');                 // Tell express to use the handlebars engine whenever it encounters an *.hbs file.

// Make public directory (CSS, etc,.) available to client (user's browser)
app.use(express.static('public'));


/*
    ROUTES
*/
app.get('/', function(req, res)
{  
    // Define the SQL queries needed to populate data on the page
    let get_users = `SELECT user_ID, email, restriction_ID, 
                        FROM artists;`;
    let get_restrictions = `SELECT COLUMN_TYPE
                                FROM information_schema.COLUMNS
                                WHERE TABLE_NAME = 'dietaryRestrictions'
                                AND COLUMN_NAME = 'name';`               
    //let get_genres = "SELECT * FROM genres;";

    db.pool.query(get_users, function(error, users_rows, fields) {    
        //db.pool.query(get_genres, function(error, genres_rows, fields) {
            db.pool.query(get_restrictions, function(error, restrictions, fields) {

                // Make a mapping from genre_id to genre_name
                // let genremap = {};
                // genres_rows.map(genre => {
                //     let id = parseInt(genre.genre_id, 10);
                //     genremap[id] = genre.genre_name;
                // });

                // Replace the genre_id foreign keys with the actual genres from the category table
                // artists_rows = artists_rows.map(artists => {
                //     return Object.assign(artists, {primary_genre: genremap[artists.primary_genre]});
                // });

                // Parse instrument enum values
                // enum_string = instrument_enums[0].COLUMN_TYPE
                // instrument_selections =enum_string.substring(6, enum_string.length - 2).split('\',\'')

                // Finally, use the data to render the HTML page
                res.render('users', {users: users_rows, restictions: restrictions});
            })
        //})
    })
});

// Called when user adds an artist
app.post('/add_new_user', function(req, res){
    // Capture the incoming data and parse it back to a JS object
    let form_input = req.body;

    // Do input checking
    let user_restriction = parseInt(form_input['input-restriction']);
    if (isNaN(user_restriction))
    {
        user_restriction = 'NULL';
    }

    // Create the query and run it on the database
    insert_user = `INSERT INTO users (email, restriction) 
                        VALUES (?, ?, ?, ?, ?, ?)`;
    parameters = [form_input['input-email'], user_restriction]
    db.pool.query(insert_user, parameters, function(error, rows, fields){

        // Check to see if there was an error
        if (error) {

            // Log the error to the terminal so we know what went wrong, and send the visitor an HTTP response 400 indicating it was a bad request.
            console.log(error)
            res.sendStatus(400);
        }

        // If there was no error, we redirect back to our root route, which automatically runs the SELECT * FROM bsg_people and
        // presents it on the screen
        else
        {
            res.redirect('/');
        }
    })
})

// Called when the user adds a genre
app.post('/add_new_genre', function(req, res){
    
    // Capture the incoming data and parse it back to a JS object
    let form_input = req.body;

    // Create the query and run it on the database
    insert_genre = `INSERT INTO genres (genre_name) VALUES (?);`;
    db.pool.query(insert_genre, [form_input['input-genre_name']], function(error, rows, fields){

        // Check to see if there was an error
        if (error) {

            // Log the error to the terminal so we know what went wrong, and send the visitor an HTTP response 400 indicating it was a bad request.
            console.log(error)
            res.sendStatus(400);
        }
        // If there was no error, we redirect back to our root route, which automatically runs the SELECT * FROM bsg_people and
        // presents it on the screen
        else
        {
            console.log(rows);
            res.redirect('/');
        }
    })
})

// Called when the user clicks "see albums"
app.get('/albums/:artist_id', function(req, res){
    
    // Capture the incoming data and parse it back to a JS object
    // This is an example of NOT using prepared statements. In practice,
    // we should have mysql package sanitize inputs using ? slot filing (see other queries in this file)
    let artist_id = req.params['artist_id']
    const get_artist = `SELECT *
                            FROM artists
                            WHERE artists.artist_id = ${artist_id};`;
    const get_albums = `SELECT album_id, album_name, DATE_FORMAT(release_date, '%b %e, %Y') as release_date
                            FROM albums 
                            WHERE albums.artist_id = ${artist_id};`;

    // Create the query and run it on the database
    db.pool.query(get_artist, function(error, artist_row, fields){
        db.pool.query(get_albums, function(error, album_rows, fields){

            // Check to see if there was an error
            if (error) {
    
                // Log the error to the terminal so we know what went wrong, and send the visitor an HTTP response 400 indicating it was a bad request.
                console.log(error)
                res.sendStatus(400);
            }
            // If there was no error, we redirect back to our root route, which automatically runs the SELECT * FROM bsg_people and
            // presents it on the screen
            else
            {

                // Finally, use the data to render the HTML page
                res.render('albums', {artist: artist_row, albums: album_rows});
            }
        })
    })
})

// Called when the user adds an album
app.post('/add_new_album/:artist_id', function(req, res){
    
    // Capture the incoming data and parse it back to a JS object
    let artist_id = req.params['artist_id']
    let form_input = req.body;

    // Create the query and run it on the database
    insert_genre = `INSERT INTO albums (artist_id, album_name, release_date) VALUES (?, ?, ?);`;
    db.pool.query(insert_genre, [artist_id, form_input['input-album_name'], form_input['input-release_date']], function(error, rows, fields){

        // Check to see if there was an error
        if (error) {
            // Log the error to the terminal so we know what went wrong, and send the visitor an HTTP response 400 indicating it was a bad request.
            console.log(error)
            res.sendStatus(400);
        }

        // If there was no error, we redirect back to the page to reload the table
        else
        {
            res.redirect(`/albums/${artist_id}`);
        }
    })
})


/*
    LISTENER
*/
app.listen(PORT, function(){            // This is the basic syntax for what is called the 'listener' which receives incoming requests on the specified PORT.
    console.log('Express started on http://localhost:' + PORT + '; press Ctrl-C to terminate.')
});