$.ajax({
    type: "GET",
    url: "../api/rooms/trending-rooms",
    success: function (response) {
        $.each(response, function(index, value) {
            room =
                `<tr id=${value.id}>
                <td>${value.name}</td>
                <td>${value.total_followers}</td>
                <td>${value.total_upvote}</td>
                <td>${value.total_downvote}</td>
              </tr>`;
            $("#trending_rooms").append(room);
        });
        $.each(response, function(index, value) {
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            follow_button = `<td><button type="button" id="follow-${value.id}" class="btn btn-primary">Follow</button></td>`;
            $(`#${value.id}`).append(follow_button);
            $(`#follow-${value.id}`).click(function() {
                $.ajax({
                    type: "POST",
                    headers:{
                        "X-CSRFToken": csrftoken
                    },
                    url: `../api/rooms/${value.id}/follow`,
                    success: function (response) {
                        console.log(response)
                        $(`#follow-${value.id}`).text("Followed")
                    }
                    ,
                    error: function(response) {
                        console.log(response)
                        if (response.status == 403) {
                            alert("You're not logged in. You must login to follow room.");
                        } else {
                            var err = JSON.parse(response.responseText);
                            alert("Gagal mengikuti room.");
                        }
                    }
                });
            });
        });
    },
    error: function(response) {
        if (response.status == 403) {
            alert("You're not logged in. You must login to follow room.");
        } else {
            var err = JSON.parse(response.responseText);
            alert("Gagal melihat trending room.");
        }
    }
});