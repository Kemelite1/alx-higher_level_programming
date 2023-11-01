
$(document).ready(function() {
    // Make a GET request to the specified URL
    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
      // Extract the character name from the response data
      const characterName = data.name;
      
      // Display the character name in the HTML tag with ID "character"
      $("#character").text(characterName);
    });
  });