document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    var searchTitle = document.getElementById('searchTitle').value;

    fetch('/searchRecipes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({title: searchTitle})
    })
    .then(response => response.json())
    .then(data => {
        let tableBody = document.querySelector('#browse table tbody');
        tableBody.innerHTML = ''; // Clear the current list of recipes
        for (let recipe of data) {
            let row = document.createElement('tr');
            row.innerHTML = `<td><a href="#">Edit</a></td><td><a href="#">Delete</a></td><td align="right">${recipe.recipeID}</td><td>${recipe.name}</td><td align="right">${recipe.servings}</td><td align="right">${recipe.restrictionID}</td>`;
            tableBody.appendChild(row);
        }
    });
});
