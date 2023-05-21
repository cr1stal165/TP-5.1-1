$(document).ready(function () {
    const name = localStorage.getItem('id');
    var url = `http://127.0.0.1:8000/api/v1/user/${name}/`;

    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            $('#loginname').text(JSON.stringify(response['nickname']).replace(/"/g, ''));

        },
        error: function (error) {
            console.log(error);
        }
    });
});


