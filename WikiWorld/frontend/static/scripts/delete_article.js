$(document).ready(function() {

    function delete_article(id) {
        var token = localStorage.getItem('token');
        var url = `/api/v1/articles/delete/${id}/`;


        fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + token
            }

        })
        .then(response => response.json())
        .then(data => {
            $('#delete-button').show();
            redirectToMainPage();
        })
        .catch(error => {
            console.error('Error:', error);

        });
    }

    function redirectToMainPage() {
        alert('3');
        window.location.href = '/profile/';

    }

    // Обработчик события клика на кнопке входа
    $('#delete-button').click(function(event) {
        alert('1');
        event.preventDefault(); // Предотвращаем отправку формы
        var id = $(this).val(); // Получаем значение id статьи из нажатой кнопки
        console.log(id);
        delete_article(id);
    });

});
