$(document).ready(function () {
    var url = 'http://127.0.0.1:8000/api/v1/articles/';

    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            var num = Math.floor(Math.random() * response.length);

            $('#main-text1').text(JSON.stringify(response[num]['description']).replace(/"/g, ''));
            $('#h-f').text(JSON.stringify(response[num]['title']).replace(/"/g, '')).attr('href', `http://127.0.0.1:8000/article_page/${response[num]['id']}/`);

            $('#main-text').text(JSON.stringify(response[response.length - 1]['description']).replace(/"/g, ''));
            $('#h-s').text(JSON.stringify(response[response.length - 1]['title']).replace(/"/g, '')).attr('href', `http://127.0.0.1:8000/article_page/${response[response.length - 1]['id']}/`);
        },
        error: function (error) {
            console.log(error);
        }
    });
});