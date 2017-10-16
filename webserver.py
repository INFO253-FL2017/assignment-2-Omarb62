"""
webserver.py

File that is the central location of code for your webserver.
"""
import requests
import os
from flask import Flask, request, render_template

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def hello_world():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"
    # return render_template("index.html", post1=url_for("post1")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about', methods=['GET'])
def about():
	return render_template("about.html")

@app.route('/contact', methods=['GET'])
def contact():
	return render_template("contact.html")

@app.route('/blog/8-experiments-in-motivation', methods=['GET'])
def get_post1():
	return render_template("post1.html")

@app.route('/blog/a-mindful-shift-of-focus', methods=['GET'])
def get_post2():
	return render_template("post2.html")

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction', methods=['GET'])
def get_post3():
	return render_template("post3.html")

@app.route('/blog/training-to-be-a-good-writer', methods=['GET'])
def get_post4():
	return render_template("post4.html")

@app.route('/blog/what-productivity-systems-wont-solve', methods=['GET'])
def get_post5():
	return render_template("post5.html")

@app.route('/contact', methods=['POST'])
def send_email():
	message = request.form.get("message")
	name = request.form.get("name")
	subject = request.form.get("subject")
	notifications = []

	data = {
		'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],
		'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
		'subject': subject,
		'text': message,
	}
	auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

	r = requests.post(
		'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),
		auth=auth,
		data=data)

	if r.status_code == requests.codes.ok:
		notifications.append("Hi " + name + ", your message has been sent.")
	else:
		notifications.append("Hi " + name + ", your message was not sent. Please try again later")

	return render_template("contact.html", notifications=notifications)
