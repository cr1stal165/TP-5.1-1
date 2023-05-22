$(document).ready(function () {
    var path = window.location.pathname;
    var parts = path.split('/');
    var id = parts[parts.length - 2];
    var url = `http://127.0.0.1:8000/api/v1/topics/${id}/`;
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            $('#topic-1').text(JSON.stringify(response['name']).replace(/"/g, ''));

            var secondUrl = '/api/v1/articles/';

            $.ajax({
                url: secondUrl,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    for (var i = 0; i < data.length; i++) {
                        if (id === data[i].topic.toString()) {

                            var topic = data[i];

                            var cont3 = `<a href="/article_page/${topic.id}/" class="topic-main">${topic.title}</a>`;
                            var cont5 = '<p class="topic-text">' + topic.description + '</p>'
                            var cont2 = '<div class="topic">' + cont3 + cont5 + '</div>';
                            var cont1 = '<div class="container234">' + cont2 + '</div>';

                            $('#main-cont').append(cont1);

                        }
                    }
                },
                error: function (secondError) {
                    console.log(secondError);
                }
            });
        },
        error: function (error) {
            console.log(error);
        }
    });

});