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
    if (!token) {
        // Show Bootstrap modal with error message
        $('#myModal').modal('show');
        return;
    }

    // Redirect to the authenticated main page
    window.location.href = '/profile/?token=' + token + '/?user=' + id;
}


var nickname = $('#nickname').val();
var password = $('#password').val();
authenticate('cr1stal165' , '123' )
redirectToMainPage()