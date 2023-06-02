$(document).ready(function() {
    // Функция аутентификации
    function edit_profile() {
        var username;
        var temp = $('#nicknameinput-editprofile').val();
        if (temp === '' || temp === ' '){
            username = localStorage.getItem('nickname');
        } else {
            username = $('#nicknameinput-editprofile').val();
        }
        var password = $('#passwordnameinput-editprofile').val();
        var token = localStorage.getItem('token');
        var url = 'http://158.160.51.82:30/api/v1/updatepassword/';

        var data = {
            'nickname': username,
            'password': password
        };

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + token
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {

            $('#button-save-profile-edit').show();

            redirectToMainPage();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Пароль совпадает с предыдущим');
        });
    }

    // Функция для перенаправления на страницу после аутентификации
    function redirectToMainPage() {

        window.location.href = 'http://158.160.51.82:30/profile/';

    }

    // Обработчик события клика на кнопке входа
    $('#button-save-profile-edit').click(function(event) {
        event.preventDefault(); // Предотвращаем отправку формы
        edit_profile(); // Вызываем функцию аутентификации
    });

    // Обработчик события отправки формы
    $('#editForm').submit(function(event) {
        event.preventDefault(); // Предотвращаем отправку формы
        edit_profile(); // Вызываем функцию аутентификации
    });
});
