$(document).ready(function () {
    // Функция аутентификации
    function getImageBinaryData(imageFile) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onloadend = () => resolve(reader.result);
            reader.onerror = reject;
            reader.readAsArrayBuffer(imageFile);
        });
    }

    function add_article() {
        var topic = $('#topic_id').val();
        var token = localStorage.getItem('token');
        var url = 'http://158.160.51.82:30/api/v1/topics/add/';

        var imageInput = document.getElementById('file_input');
        var imageFile = imageInput.files[0];

        getImageBinaryData(imageFile)
            .then(imageBinaryData => {
                var base64String = btoa(String.fromCharCode.apply(null, new Uint8Array(imageBinaryData)));
                var image = base64String;
                

                var data = {
                    'name': topic,
                    'image': image,

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
                        $('#admintheme-button').show();
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

        window.location.href = 'http://158.160.51.82:30/admin_main/';

    }

    // Обработчик события клика на кнопке входа
    $('#admintheme-button').click(function (event) {
        event.preventDefault(); // Предотвращаем отправку формы
        add_article(); // Вызываем функцию аутентификации
    });

    // Обработчик события отправки формы
    $('#myForm').submit(function (event) {
        event.preventDefault(); // Предотвращаем отправку формы
        add_article(); // Вызываем функцию аутентификации
    });
});
