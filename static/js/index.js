const roomName = JSON.parse(document.getElementById("room-name").textContent);
const userName = JSON.parse(document.getElementById("username").textContent);
const form = document.getElementById("messageform");

const chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/chatroom/" + roomName + "/"
);

chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  if (data.message) {
    let chatBox = document.querySelector(".chatbox");

    let message = `<div class="messages bg-white rounded mx-2 my-2"><h5 class="text-start p-2 text-warning">${data.username}</h5><p class="text-dark m-2">${data.message}</p><p class="float-end">today</p></div>`;
    chatBox.innerHTML += message;
  } else {
    alert("message is empty");
  }
};

chatSocket.onclose = function (e) {
  console.error("Chat socket closed unexpectedly");
};

form.addEventListener("submit", function (e) {
  e.preventDefault();
  const messageInput = document.querySelector("#chatmessage");
  const message = messageInput.value;

  chatSocket.send(
    JSON.stringify({
      'message': message,
      'username': userName,
      'room': roomName
    })
  );
  messageInput.value = " ";
  return false;
});