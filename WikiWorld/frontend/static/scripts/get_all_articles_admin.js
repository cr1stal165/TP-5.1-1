$(document).ready(function () {
    var url = 'http://127.0.0.1:8000/api/v1/articles/';
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            for (var i = 0; i < response.length; i++) {

                var cont2 = `<a class="article_title">${response[i].title}</a>`;
                var cont3 = `<p class="article_description">${response[i].description}</p>`;
                var but1 = '<form id="form_delete_article">' + `<button data-id="${response[i].id}" value="${response[i].id}" class="deletebutton-profile"><img class="deletebutton-profile-svg" src="/static/img/delete.svg"></button>` + '</form>';
                var but2 = '<form id="form_edit_article">' + `<button class="editbutton-profile"><a href="/admin_edit_article/${response[i].id}/"><img class="editbutton-profile-svg" src="/static/img/pencil.svg"></a></button>` + '</form>';
                var cont1 = '<div class="my-article">' + cont2 + cont3 + but1 + but2 + '</div>' + '<br>';
                $('#scrollable-div').append(cont1);

            }
        },
        error: function (error) {
            console.log(error);
        }
    });
});