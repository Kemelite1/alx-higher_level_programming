
$(document).ready(function() {
    // Attach a click event handler to the "Add item" div
    $("#add_item").click(function() {
      // Create a new <li> element and add it to the list
      let newItem = $("<li>Item</li>");
      $("ul.my_list").append(newItem);
    });
  
    // Attach a click event handler to the "Remove item" div
    $("#remove_item").click(function() {
      // Remove the last <li> element from the list
      $("ul.my_list li:last-child").remove();
    });
  
    // Attach a click event handler to the "Clear list" div
    $("#clear_list").click(function() {
      // Remove all <li> elements from the list
      $("ul.my_list").empty();
    });
  });
  