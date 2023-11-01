
$(document).ready(function() {
    // Make a GET request to the specified URL with the lang parameter set to "fr" (French)
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
      // Extract the translation of "hello" from the response data
      let translation = data.hello;
  
      // Display the translation in the HTML tag with ID "hello"
      $("#hello").text(translation);
    });
  });
  