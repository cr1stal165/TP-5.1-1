
$(document).ready(function () {
    var path = window.location.pathname;
    var parts = path.split('/');
    var id = parts[parts.length - 2];
    var url = `http://158.160.51.82:30/api/v1/article/${id}/`;
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            var user = response['user'];
            var lsd = btoa(JSON.stringify(response['image']).replace(/"/g, ''));
            $('#art').text(JSON.stringify(response['title']).replace(/"/g, ''));
            $('#main-text').text(JSON.stringify(response['description']).replace(/"/g, ''));
            $('#hid_id').val(JSON.stringify(response['id']).replace(/"/g, '')).text(JSON.stringify(response['id']).replace(/"/g, ''));
            $('#hid_id1').val(JSON.stringify(response['id']).replace(/"/g, '')).text(JSON.stringify(response['id']).replace(/"/g, ''));
            $('#hid_id2').val(JSON.stringify(response['id']).replace(/"/g, '')).text(JSON.stringify(response['id']).replace(/"/g, ''));
            $('#avatar').attr('src', 'data:image/png;base64,' + JSON.stringify(response['image']).replace(/"/g, ''));


            var url2 = `http://158.160.51.82:30/api/v1/user/${user}/`;
            $.ajax({
                url: url2,
                type: 'GET',
                dataType: 'json',
                success: function (response) {
                    $('#author').text(JSON.stringify(response['nickname']).replace(/"/g, ''));
                },
                error: function (error) {
                    console.log(error);
                }
            });
        },
        error: function (error) {
            console.log(error);
        }
    });

});
