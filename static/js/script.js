// script.js

console.log("js/script.js has been loaded!");

function validation() {
	var name = document.forms["myContact"]["name"].value;
	var subject = document.forms["myContact"]["subject"].value;
	var message = document.forms["myContact"]["message"].value;

	var msg = "";
	if (name.length === 0) {
		msg = msg.concat("name, ");
		console.log(msg)
	}
	if (subject.length === 0) {
		msg = msg + "subject, ";
	}
	if (message.length === 0) {
		msg = msg + "message, ";
	}
	if (msg.length != 0) {
		msg = msg.slice(0, -2);
		// alert("The following fields still need to be filled: " + msg);
		document.getElementById("top").innerHTML = "The following fields still need to be filled: " + msg;
		// e.preventDefault();
		return false;
	}
	return true;
}