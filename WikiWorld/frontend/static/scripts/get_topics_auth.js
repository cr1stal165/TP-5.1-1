$(document).ready(function() {
  var url = 'http://158.160.51.82:30/api/v1/topics/';

  $.ajax({
    url: url,
    type: 'GET',
    dataType: 'json',
    success: function(response) {
      $('#1').text(JSON.stringify(response[0]['name']).replace(/"/g, '')).attr('href', `http://158.160.51.82:30/articles_topic_auth/${response[0]['id']}/`);
      $('#2').text(JSON.stringify(response[1]['name']).replace(/"/g, '')).attr('href', `http://158.160.51.82:30/articles_topic_auth/${response[1]['id']}/`);
      $('#3').text(JSON.stringify(response[2]['name']).replace(/"/g, '')).attr('href', `http://158.160.51.82:30/articles_topic_auth/${response[2]['id']}/`);
      $('#4').text(JSON.stringify(response[3]['name']).replace(/"/g, '')).attr('href', `http://158.160.51.82:30/articles_topic_auth/${response[3]['id']}/`);

    },
    error: function(error) {
      console.log(error);
    }
  });
});