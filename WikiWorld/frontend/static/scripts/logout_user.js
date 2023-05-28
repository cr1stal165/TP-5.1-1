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


                $('#logoutBtn').show();

                redirectToMainPage();
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    function redirectToMainPage() {

        window.location.href = 'http://127.0.0.1:8000';

    }

    $('#button_save_exit').click(function (event) {
        event.preventDefault();
        logout();
    });

    $('#myForm').submit(function (event) {
        event.preventDefault();
        logout();
    });
});
