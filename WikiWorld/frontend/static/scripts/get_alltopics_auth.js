$(document).ready(function () {
    $.ajax({
        url: "http://158.160.51.82:30/api/v1/topics/",
        type: "GET",
        dataType: "json",
        success: function (data) {
            var users = data;
            for (var i = 0; i < users.length; i++) {


                var cont4 = `<img class="topic_img" src="data:image/svg+xml;base64,${data[i].image}" width="50px" height="50px">`
                var cont3 = `<a href="http://158.160.51.82:30/articles_topic_auth/${users[i].id}/" class="topic-main">${users[i].name}</a>`;
                var cont2 = '<div class="topic">' + cont3 + cont4 + '</div>'

                var cont1 = '<div class="container234">' + cont2  +'</div>'


                $('#forma1').append(cont1);
            }
        },
        error: function (error) {
            console.log(error);
        }
    });
});
