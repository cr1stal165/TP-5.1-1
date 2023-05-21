$(document).ready(function () {
    var path = window.location.pathname;
    var parts = path.split('/');
    var id = parts[parts.length - 2];
    var url = `http://127.0.0.1:8000/api/v1/topics/${id}/`;
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            $('#topic-1').text(JSON.stringify(response['name']).replace(/"/g, ''));

        },
        error: function (error) {
            console.log(error);
        }
    });

});