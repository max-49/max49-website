window.onload = function() {
  changeFrameInfo();
};

function changeFrameInfo() {
  document.getElementById("channel-title").innerHTML = "server-info";
  document.getElementById("server-info").style.display = "block";
  document.getElementById("round-9-writeups").style.display = "none";
  document.getElementById("round-10-writeups").style.display = "none";
  document.getElementById("round-11-writeups").style.display = "none";
  document.getElementById("round-12-writeups").style.display = "none";
  document.getElementById("round-13-writeups").style.display = "none";
  document.getElementById("round-14-writeups").style.display = "none";
}

function changeFrame9() {
  document.getElementById("channel-title").innerHTML = "<a href=\"/round-9-writeups.html\" target=\"_blank\" style=\"color: white;\">round-9-writeups</a>";
  document.getElementById("server-info").style.display = "none";
  document.getElementById("round-9-writeups").style.display = "block";
  document.getElementById("round-10-writeups").style.display = "none";
  document.getElementById("round-11-writeups").style.display = "none";
  document.getElementById("round-12-writeups").style.display = "none";
  document.getElementById("round-13-writeups").style.display = "none";
  document.getElementById("round-14-writeups").style.display = "none";
}

function changeFrame10() {
  document.getElementById("channel-title").innerHTML = "<a href=\"/round-10-writeups.html\" target=\"_blank\" style=\"color: white;\">round-10-writeups</a>";
  document.getElementById("server-info").style.display = "none";
  document.getElementById("round-9-writeups").style.display = "none";
  document.getElementById("round-10-writeups").style.display = "block";
  document.getElementById("round-11-writeups").style.display = "none";
  document.getElementById("round-12-writeups").style.display = "none";
  document.getElementById("round-13-writeups").style.display = "none";
  document.getElementById("round-14-writeups").style.display = "none";
}

function changeFrame11() {
  document.getElementById("channel-title").innerHTML = "<a href=\"/round-11-writeups.html\" target=\"_blank\" style=\"color: white;\">round-11-writeups</a>";
  document.getElementById("server-info").style.display = "none";
  document.getElementById("round-9-writeups").style.display = "none";
  document.getElementById("round-10-writeups").style.display = "none";
  document.getElementById("round-11-writeups").style.display = "block";
  document.getElementById("round-12-writeups").style.display = "none";
  document.getElementById("round-13-writeups").style.display = "none";
  document.getElementById("round-14-writeups").style.display = "none";
}

function changeFrame12() {
  document.getElementById("channel-title").innerHTML = "<a href=\"/round-12-writeups.html\" target=\"_blank\" style=\"color: white;\">round-12-writeups</a>";
  document.getElementById("server-info").style.display = "none";
  document.getElementById("round-9-writeups").style.display = "none";
  document.getElementById("round-10-writeups").style.display = "none";
  document.getElementById("round-11-writeups").style.display = "none";
  document.getElementById("round-12-writeups").style.display = "block";
  document.getElementById("round-13-writeups").style.display = "none";
  document.getElementById("round-14-writeups").style.display = "none";
}

function changeFrame13() {
  document.getElementById("channel-title").innerHTML = "<a href=\"/round-13-writeups.html\" target=\"_blank\" style=\"color: white;\">round-13-writeups</a>";
  document.getElementById("server-info").style.display = "none";
  document.getElementById("round-9-writeups").style.display = "none";
  document.getElementById("round-10-writeups").style.display = "none";
  document.getElementById("round-11-writeups").style.display = "none";
  document.getElementById("round-12-writeups").style.display = "none";
  document.getElementById("round-13-writeups").style.display = "block";
  document.getElementById("round-14-writeups").style.display = "none";
}

function changeFrame13() {
  document.getElementById("channel-title").innerHTML = "<a href=\"/round-14-writeups.html\" target=\"_blank\" style=\"color: white;\">round-13-writeups</a>";
  document.getElementById("server-info").style.display = "none";
  document.getElementById("round-9-writeups").style.display = "none";
  document.getElementById("round-10-writeups").style.display = "none";
  document.getElementById("round-11-writeups").style.display = "none";
  document.getElementById("round-12-writeups").style.display = "none";
  document.getElementById("round-13-writeups").style.display = "none";
  document.getElementById("round-14-writeups").style.display = "block";
}