/*
*   artists validation
*/
// Called prior to submitting request to server-side JS. Prevent users from leaving both first name and last name AND stage name empty.
function validateArtistForm() {
    let input = document.forms["add-artist-form"];
    // console.log(input['input-first_name'].value)
    // console.log(input['input-last_name'].value)
    if ((input['input-first_name'].value == "" || input['input-last_name'].value == "") && input['input-stage_name'].value == "") {
      alert("Either first name and last name OR stage name must be provided");
      return false;
    }
}

/*
*   genres validation
*/
// Called prior to submitting request to server-side JS. Prevent users from submitting a genre that is already in the list.
function validateGenreForm() {
    new_genre = document.forms["add-genre-form"]['input-genre_name'].value;
    // console.log(new_genre)
    for (var option of document.getElementById("input-primary_genre").options) {
        console.log(option.text)
        if (new_genre == option.text) {
            alert("\"" + new_genre + "\" is already included as a genre");
            return false;
        }
    };
}