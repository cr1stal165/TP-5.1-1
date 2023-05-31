$(document).ready(function () {
    function add_topic() {
        var url = 'http://158.160.51.82:30/api/v1/topics/add/';
        var topic = $('#topic_id').val();
        var token = localStorage.getItem('token');
        var data = {
            'name': topic,
            'image': null
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
    }

    function redirectToMainPage() {

        window.location.href = 'http://127.0.0.1:8000/admin_main/';

    }

    $('#admintheme-button').click(function (event) {
        event.preventDefault();
        add_topic();
    });

    $('#myForm').submit(function (event) {
        event.preventDefault();
        add_topic();
    });
});
