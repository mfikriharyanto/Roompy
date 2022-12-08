$.ajax({
  type: "GET",
  url: "../api/users/top-users",
  success: async function (response) {
    $.each(response, function(index, value) {
      user =
      `<tr id=${value.id}>
        <th scope="row">${index+1}</th>
        <td><a href="${value.id}" class="text-dark font-weight-bold btn p-0">${value.username}</a></td>
        <td>${value.total_follower_user}</td>
        <td>${value.total_following_user}</td>
      </tr>`;
      $("#top_users").append(user);
    });
    $.each(response, function(index, value) {
      $.ajax({
        type: "GET",
        url: `../api/users/${value.id}/flag-follow`,
        success: function (response) {
          if (response.is_followed) {
            is_followed = `<td class="unfollow"><button type="button" class="btn btn-secondary">Unfollow</button></td>`;
            $(`#${value.id}`).append(is_followed);
          } else {
            is_followed = `<td class="follow"><button type="button" class="btn btn-primary">Follow</button></td>`;
            $(`#${value.id}`).append(is_followed);
          }
        }
      });
    });
  }
});