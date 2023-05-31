$(document).ready(function () {
    $(document).on('click', '.deletebutton-profile', function (event) {
        event.preventDefault();
        var id = $(this).data('id');
        delete_article(id);
    });

    function delete_article(id) {
        var token = localStorage.getItem('token');
        var url = `http://158.160.51.82:30/api/v1/topics/delete/${id}/`;

        fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + token
            }
        })
            .then(response => response.json())
            .then(data => {
                redirectToMainPage();
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    function redirectToMainPage() {
        alert('Тематика успешно удалена');
        window.location.href = 'http://158.160.51.82:30/admin_main/';
    }
});