function send() {
  const input = document.getElementById("msg");
  const body = document.getElementById("chat-body");

  body.innerHTML += `<div>${input.value}</div>`;
  body.innerHTML += `<div class="bot">Mình sẽ hỗ trợ bạn sớm 😊</div>`;
  input.value = "";
}

