$(document).ready(function () {

    function getImageBinaryData(imageFile) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onloadend = () => resolve(reader.result);
            reader.onerror = reject;
            reader.readAsArrayBuffer(imageFile);
        });
    }

    var path = window.location.pathname;
    var parts = path.split('/');
    var art_id = parts[parts.length - 2];

    function add_article() {
        var date = '';
        var title = $('#title').val();
        var description = $('#description').val();
        var topic_id = $('#selecttheme_field').val();
        var id = localStorage.getItem('id');
        var token = localStorage.getItem('token');
        var url = `http://158.160.51.82:30/api/v1/articles/${art_id}/`;

        var imageInput = document.getElementById('file_input');
        var imageFile = imageInput.files[0];

        getImageBinaryData(imageFile)
            .then(imageBinaryData => {
                var base64String = btoa(String.fromCharCode.apply(null, new Uint8Array(imageBinaryData)));
                var image = base64String;
                

                var data = {
                    'title': title,
                    'description': description,
                    'image': image,
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
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    function redirectToMainPage() {

        window.location.href = 'http://158.160.51.82:30/profile/';

    }

    // Обработчик события клика на кнопке входа
    $('#button-save-article-edit').click(function (event) {
        event.preventDefault(); // Предотвращаем отправку формы
        add_article(); // Вызываем функцию аутентификации
    });

    // // // Обработчик события отправки формы
    // $('#addForm').submit(function (event) {
    //     event.preventDefault(); // Предотвращаем отправку формы
    //     add_article(); // Вызываем функцию аутентификации
    // });
});
