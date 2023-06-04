$(document).ready(function() {
    // Функция аутентификации
    function authenticate() {
        var username = $('#nickname').val();
        var password = $('#password').val();
        var url = 'http://158.160.51.82:30/api/v1/login/';

        var data = {
            'nickname': username,
            'password': password
        };

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            // Сохраняем токен безопасно (например, в локальное хранилище или cookie)
            localStorage.setItem('token', data[0].auth_token);
            localStorage.setItem('nickname', data[1].nickname);
            localStorage.setItem('is_superuser', data[3].is_superuser);
            localStorage.setItem('id', data[4].id);
            localStorage.setItem('password', data[5].password);
            // Показываем кнопку для перенаправления на страницу после аутентификации
            $('#loginBtn').show();

            redirectToMainPage();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Неверное имя или пароль');
        });
    }

    // Функция для перенаправления на страницу после аутентификации
    function redirectToMainPage() {
        var token = localStorage.getItem('token');
        var id = localStorage.getItem('id');
        var is_superuser = localStorage.getItem('is_superuser');
        if (!token) {
            // Показываем модальное окно Bootstrap с сообщением об ошибке
            $('#myModal').modal('show');
            return;
        }
        if (is_superuser === 'true') {
            window.location.href = 'http://158.160.51.82:30/admin_main/?token=' + token + '&user=' + id;
        } else {
            window.location.href = 'http://158.160.51.82:30/profile/?token=' + token + '&user=' + id;
        }
    }

    // Обработчик события клика на кнопке входа
    $('#loginBtn').click(function(event) {
        event.preventDefault(); // Предотвращаем отправку формы
        authenticate(); // Вызываем функцию аутентификации
    });

    // Обработчик события отправки формы
    $('#myForm').submit(function(event) {
        event.preventDefault(); // Предотвращаем отправку формы
        authenticate(); // Вызываем функцию аутентификации
    });
});
