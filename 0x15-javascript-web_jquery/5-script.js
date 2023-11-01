
$(document).ready(function() {
    // Attach a click event handler to the div with ID "add_item"
    $("#add_item").click(function() {
      // Create a new <li> element
      var newItem = $("<li>Item</li>");
      
      // Add the new element to UL.my_list
      $("ul.my_list").append(newItem);
    });
  });
  