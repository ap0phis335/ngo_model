const joinForm = document.getElementById("joinForm");

joinForm.addEventListener("submit", function(event) {
  event.preventDefault();

  alert("Registration Successful! Thank you for joining She Can Foundation.");

  joinForm.reset();
});