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
    }
});