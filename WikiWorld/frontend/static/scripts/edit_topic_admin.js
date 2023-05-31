$(document).ready(function() {

    var path = window.location.pathname;
    var parts = path.split('/');
    var art_id = parts[parts.length - 2];
    // Функция аутентификации
    function add_article() {

        var name = $('#topic_id').val();

        var token = localStorage.getItem('token');
        var url = `http://158.160.51.82:30/api/v1/topics/update/${art_id}/`;

        var data = {
            'name': name
        };

        fetch(url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + token
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {

            $('#admintheme-button').show();

            redirectToMainPage();
        })
        .catch(error => {
            console.error('Error:', error);

        });
    }

    function redirectToMainPage() {

        window.location.href = 'http://158.160.51.82:30/admin_thematics/';

    }

    // Обработчик события клика на кнопке входа
    $('#admintheme-button').click(function(event) {
        event.preventDefault(); // Предотвращаем отправку формы
        add_article(); // Вызываем функцию аутентификации
    });

});
