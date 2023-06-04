$(document).ready(function () {
    // Функция аутентификации
    function registration() {
        var nickname = $('#nickname').val();
        var email = $('#email').val();
        var password = $('#password').val();
        var url = 'http://158.160.51.82:30/api/v1/registration/';

	if (nickname.length < 3) {
            alert('Никнейм должен содержать не менее 3 символов.');
            return;
        }

        if (!/[A-Z]/.test(password) || !/[!@#$%^&*]/.test(password) || password.length < 8) {
            alert('Пароль должен содержать не менее 8 символов, хотя бы одну заглавную букву, один специальный символ (!@#$%^&*).');
            return;
        }

        if (!validateEmail(email)) {
            alert('Пожалуйста, введите корректный адрес электронной почты. \nПример: example@example.com');

            return;
        }

        var data = {
            'nickname': nickname,
            'email': email,
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
                $('#register-btn').show();

                redirectToMainPage();
            })
            .catch(error => {
                console.error('Error:', error);

            });
    }

	
    function validateEmail(email) {
        var re = /\S+@\S+\.\S+/;
        return re.test(email);
    }

    // Функция для перенаправления на страницу после аутентификации
    function redirectToMainPage() {
        window.location.href = 'http://158.160.51.82:30/login/'

    }

    // Обработчик события клика на кнопке входа
    $('#register-btn').click(function (event) {
        event.preventDefault();
        registration(); // Вызываем функцию аутентификации
    });

    $('#myForm').submit(function(event) {
        event.preventDefault(); // Предотвращаем отправку формы
        registration(); // Вызываем функцию аутентификации
    });
});
