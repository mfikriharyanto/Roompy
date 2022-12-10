$(document).ready(function() {
  $.ajax({
    type: "GET",
    url: "../api/topics",
    success: async function (response) {
      $.each(response, function(index, value) {
        user =
        `<tr id=${value.id}>
          <th scope="row">${index+1}</th>
          <td><a href="${value.id}" class="text-dark font-weight-bold btn p-0">${value.username}</a></td>
        </tr>`;
        $("#all_topic").append(user);
      });
      $.each(response, function(index, value) {
        $.ajax({
          type: "GET",
          url: `../api/topics/${value.id}/follow`,
          success: function (response) {
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            if (response.is_followed) {
              is_followed = `<td><button type="button" id="unfollow-${value.id}" class="btn btn-secondary">Unfollow</button></td>`;
              $(`#${value.id}`).append(is_followed);
              $(`#unfollow-${value.id}`).click(function() {
                $.ajax({
                  type: "POST",
                  headers:{
                    "X-CSRFToken": csrftoken
                  },
                  url: `../api/users/${value.id}/unfollow`,
                  success: function (response) {
                    alert(response.message);
                    location.reload();
                  },
                  error: function(response) {
                    if (response.status == 403) {
                      alert("You're not logged in. You must login to unfollow user.");
                    } else {
                      var err = JSON.parse(response.responseText);
                      alert(err.message);
                    }
                  }
                });
              });
            } else {
              is_followed = `<td><button type="button" id="follow-${value.id}" class="btn btn-primary">Follow</button></td>`;
              $(`#${value.id}`).append(is_followed);
              $(`#follow-${value.id}`).click(function() {
                $.ajax({
                  type: "POST",
                  headers:{
                    "X-CSRFToken": csrftoken
                  },
                  url: `../api/users/${value.id}/follow`,
                  success: function (response) {
                    alert(response.message);
                    location.reload();
                  },
                  error: function(response) {
                    if (response.status == 403) {
                      alert("You're not logged in. You must login to follow user.");
                    } else {
                      var err = JSON.parse(response.responseText);
                      alert(err.message);
                    }
                  }
                });
              });
            }
          }
        });
      });
    },
    error: function() {
      alert("Failed to get top users. Please try again later.")
      location.reload()
    }
  });
});