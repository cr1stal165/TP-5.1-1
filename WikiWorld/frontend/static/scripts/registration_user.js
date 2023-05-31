$(document).ready(function () {
    $('#register-btn').click(function () {
        var nickname = $('#nickname').val();
        var email = $('#email').val();
        var password = $('#password').val();
        var requestData = {
            'nickname': nickname,
            'email': email,
            'password': password
        };

        $.ajax({
            url: 'http://158.160.51.82:30/api/v1/registration/',
            type: 'POST',
            dataType: 'json',
            data: requestData,
            success: function (response) {
                // Обработка успешного ответа сервера после регистрации
                console.log(response);

            },
            complete: function (xmlHttp) {

                window.location.href = 'http://158.160.51.82:30/login/'
            },
            error: function (error) {
                // Обработка ошибки
                console.log(error);
            }
        });

    });
});