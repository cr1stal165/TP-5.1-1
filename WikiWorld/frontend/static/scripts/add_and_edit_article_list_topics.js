$(document).ready(function() {
  var url = 'http://127.0.0.1:8000/api/v1/topics/';

  $.ajax({
    url: url,
    type: 'GET',
    dataType: 'json',
    success: function(response) {
      for (var i = 0; i < response.length; i++) {

          $('#selecttheme_field').append(`<option value="${response[i].id}">${response[i].name}</option>`);
      }
    },
    error: function(error) {
      console.log(error);
    }
  });
});