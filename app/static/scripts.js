function togglePass() {
  var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function newPass() {
  document.getElementById("form").style.display="block";
  document.getElementById("button").style.display="block";
}

function closePass() {
  document.getElementById("form").style.display="none";
  document.getElementById("button").style.display="none";
}

function togglePassUser(id) {
  var x = document.getElementById(id);
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}