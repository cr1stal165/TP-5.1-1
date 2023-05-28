$(document).ready(function() {
    // Функция аутентификации
    function add_article() {
        var date = '';
        var title = $('#title').val();
        var description = $('#description').val();
        var topic_id = $('#selecttheme_field').val();
        var id = localStorage.getItem('id');
        var token = localStorage.getItem('token');
        var url = '/api/v1/articles/';

        var data = {
            'date': date,
            'title': title,
            'description': description,
            'image': null,
            'user': id,
            'topic': topic_id

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

    // Обработчик события отправки формы
    $('#addForm').submit(function(event) {
        event.preventDefault(); // Предотвращаем отправку формы
        add_article(); // Вызываем функцию аутентификации
    });
});
