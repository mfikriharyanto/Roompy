$.ajax({
  type: "GET",
  url: "../api/users/top-users",
  success: function (response) {
    $.each(response, function(index, value) {
      user =
      `<tr id=${value.id}>
        <td>${value.username}</td>
        <td>${value.total_follower_user}</td>
        <td>${value.total_following_user}</td>
      </tr>`;
      $("#top_users").append(user);
    });
  }
});