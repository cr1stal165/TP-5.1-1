$(document).ready(function () {
    function logout() {
        var url = 'http://127.0.0.1:8000/api/v1/logout/';

        var username = localStorage.getItem('nickname');
        var password = localStorage.getItem('password');
        var token = localStorage.getItem('token');
        var data = {
            'nickname': username,
            'password': password
        };

        fetch(url, {
            method: 'POST',
            headers: {
                'Authorization': 'Token ' + token
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                localStorage.removeItem('token');

                // Показываем кнопку для перенаправления на страницу после аутентификации
                $('#logoutBtn').show();

                redirectToMainPage();
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    // Функция для перенаправления на страницу после аутентификации
    function redirectToMainPage() {

        window.location.href = 'http://127.0.0.1:8000';

    }

    // Обработчик события клика на кнопке входа
    $('#logoutBtn').click(function (event) {
        event.preventDefault(); // Предотвращаем отправку формы
        logout(); // Вызываем функцию аутентификации
    });

    // Обработчик события отправки формы
    $('#myForm').submit(function (event) {
        event.preventDefault(); // Предотвращаем отправку формы
        logout(); // Вызываем функцию аутентификации
    });
});
