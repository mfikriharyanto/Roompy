const allRoom = document.getElementById('all-room')
const roomForm = document.getElementById('room-form')
const name = document.getElementById('id_name')
const description = document.getElementById('id_description')
const topic = document.getElementById('id_topic')
const alertBox = document.getElementById('alert-box')

$.ajax ({
  type: 'GET',
  url: '../api/rooms/',
  success: function(response){
  
      response.forEach(element => {
        allRoom.innerHTML += `
        <div class="card mt-4">
          <h5 class="card-header">${element.name}</h5>
          <div class="card-body">
            <p class="card-text">${element.description}</p>
            <a href="https://google.com/" class="btn btn-dark stretched-link">Go to Room</a>
          </div>
        </div>
        `
      });
  },
  error: function(error){
      console.log(error)
  }
})

roomForm.addEventListener('submit', e=>{
  e.preventDefault()

  $.ajax({
    type:'POST',
    url: '../api/rooms/create-room/',
    data: {
      'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
      'name': $('#id_name').val(),
      'description': $('#id_description').val(),
      'topic': $('#id_topic').val(),
    },
    success: function(response) {
      roomCard = `
      <div class="card mt-4">
        <h5 class="card-header">${response.name}</h5>
        <div class="card-body">
          <p class="card-text">${response.description}</p>
          <a href="https://google.com/" class="btn btn-dark stretched-link">Go to Room</a>
        </div>
      </div>
      `;
      $("#all-room").prepend(
        roomCard
      )
      $('#createRoomModal').modal('hide')
      alert('success', 'New room created!')
      roomForm.reset()
    },
    error: function(error){
      alert('danger', 'Oopsie! something went wrong')
    }
  })
})