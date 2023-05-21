$(document).ready(function () {
    function authenticate(username, password) {
        const url = '/api/v1/login/';

        const data = {
            'nickname': username,
            'password': password
        };

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                // Store the token securely (e.g., in local storage or a cookie)
                localStorage.setItem('token', data[0].auth_token);
                localStorage.setItem('nickname', data[1].nickname);
                localStorage.setItem('is_superuser', data[3].is_superuser)
                localStorage.setItem('id', data[4].id)

                // Show the button for redirecting to the authenticated main page
                document.getElementById('loginBtn').style.display = 'block';
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    // Function to redirect to the authenticated main page
    function redirectToMainPage() {
        const token = localStorage.getItem('token');
        const id = localStorage.getItem('id');
        const is_superuser = localStorage.getItem('is_superuser');
        if (!token) {
            // Show Bootstrap modal with error message
            $('#myModal').modal('show');
            return;
        }
        if (is_superuser === 'true'){
            window.location.href = '/topics/';
        } else {
            window.location.href = '/profile/?token=' + token + '/?user=' + id;
        }
        // Redirect to the authenticated main page

    }

    // Event handler for clicking the login button

    var nickname = document.getElementById('nickname').value;
    var password = document.getElementById('password').value;

    authenticate('sergeyX', '1234');
    redirectToMainPage();

});
