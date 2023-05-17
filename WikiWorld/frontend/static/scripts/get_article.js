

$(document).ready(function () {
    var path = window.location.pathname;
// Разбивка пути по символу '/'
    var parts = path.split('/');
// Получение id из нужной позиции
    var id = parts[parts.length - 2];
    var url = `http://127.0.0.1:8000/api/v1/article/${id}/`;
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            var user = response['user'];
            $('#art').text(JSON.stringify(response['title']).replace(/"/g, ''));
            $('#main-text').text(JSON.stringify(response['description']).replace(/"/g, ''));

            var url2 = `http://127.0.0.1:8000/api/v1/user/${user}/`; // Используем значение user во втором URL-адресе
            $.ajax({
                url: url2,
                type: 'GET',
                dataType: 'json',
                success: function (response) {
                    $('#author').text(JSON.stringify(response['nickname']).replace(/"/g, ''));
                },
                error: function (error) {
                    console.log(error);
                }
            });
        },
        error: function (error) {
            console.log(error);
        }
    });

});
