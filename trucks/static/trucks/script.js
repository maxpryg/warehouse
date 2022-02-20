// Example starter JavaScript for disabling form submissions if there are invalid fields
/*
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          console.log('Preventing form submission');
          event.preventDefault();
          event.stopPropagation();
        } else {console.log('Form is OK')}
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();
*/

/*We use jQuery to loop through each table rows to check if there are any
text values that matches the value of the input field. The toggle() method
hides the row (display:none) that does not match the search. We use the
toLowerCase() DOM method to convert the text to lower case, which makes the
search case insensitive */
$(document).ready(function(){
  $("#search").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".table tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
