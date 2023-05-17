$(document).ready(function() {
  var url = 'http://127.0.0.1:8000/api/v1/topics/';

  $.ajax({
    url: url,
    type: 'GET',
    dataType: 'json',
    success: function(response) {
      $('#1').text(JSON.stringify(response[0]['name']).replace(/"/g, ''));
      $('#2').text(JSON.stringify(response[1]['name']).replace(/"/g, ''));
      $('#3').text(JSON.stringify(response[2]['name']).replace(/"/g, ''));
      $('#4').text(JSON.stringify(response[3]['name']).replace(/"/g, ''));

    },
    error: function(error) {
      console.log(error);
    }
  });
});