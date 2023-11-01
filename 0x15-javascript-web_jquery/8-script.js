
$(document).ready(function() {
    // Make a GET request to the specified URL
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
      // Extract the list of movies from the response data
      let  movies = data.results;
  
      // Select the UL with ID "list_movies"
      let  list = $("#list_movies");
  
      // Loop through the movies and add each title to the list
      for (let i = 0; i < movies.length; i++) {
        let title = movies[i].title;
        list.append("<li>" + title + "</li>");
      }
    });
  });
  