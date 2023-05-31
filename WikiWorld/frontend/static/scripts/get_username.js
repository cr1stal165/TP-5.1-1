$(document).ready(function () {
    const name = localStorage.getItem('id');

    var url = `http://158.160.51.82:30/api/v1/user/${name}/`;

    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            $('#author').text(JSON.stringify(response['nickname']).replace(/"/g, ''));
            $('#author_email').text(JSON.stringify(response['email']).replace(/"/g, ''));
        },
        error: function (error) {
            console.log(error);
        }
    });
});


