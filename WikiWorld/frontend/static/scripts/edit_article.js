$(document).ready(function() {

    var path = window.location.pathname;
    var parts = path.split('/');
    var art_id = parts[parts.length - 2];
    // Функция аутентификации
    function add_article() {
        var date = '';
        var title = $('#title').val();
        var description = $('#description').val();
        var topic_id = $('#selecttheme_field').val();
        var id = localStorage.getItem('id');
        var token = localStorage.getItem('token');
        var url = `/api/v1/articles/${art_id}/`;

        var data = {
            'title': title,
            'description': description,
            'user': id,
            'topic': topic_id

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

            $('#button-save-article-edit').show();

            redirectToMainPage();
        })
        .catch(error => {
            console.error('Error:', error);

        });
    }

    function redirectToMainPage() {

        window.location.href = '/profile/';

    }

    // Обработчик события клика на кнопке входа
    $('#button-save-article-edit').click(function(event) {
        event.preventDefault(); // Предотвращаем отправку формы
        add_article(); // Вызываем функцию аутентификации
    });

});
