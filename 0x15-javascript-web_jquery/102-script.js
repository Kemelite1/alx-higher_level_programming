
$(document).ready(function() {
    // Attach a click event handler to the "Translate" button
    $("#btn_translate").click(function() {
      // Get the language code from the input field
      let languageCode = $("#language_code").val();
  
      // Make a GET request to the hello API service with the language code
      $.get("https://www.fourtonfish.com/hellosalut/hello/", { lang: languageCode }, function(data) {
        // Extract the translation of "Hello" from the response
        let translation = data.hello;
  
        // Display the translation in the HTML tag with ID "hello"
        $("#hello").text(translation);
      });
    });
  });
  