from flask import Flask
from flask import render_template
from flask import request

import requests

app = Flask("MyApp")

@app.route("/")
def hello():
    return render_template("hello.html")
    #return "Hello World"

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())
    #return "Hello {0}!".format(name.title())

#@app.route("/<bye>/<name>")
#def bye(name,bye):
#    return render_template("hello.html", name=name.title(), bye=bye)
@app.route("/bye/<name>")
def bye(name):
    return "Goodbye {0}!".format(name.title())

@app.route("/goodbye/<name>/<time>")
def day(name,time):
    return render_template("hello.html", name=name.title(), time=time)

@app.route("/signup", methods=['POST'])
def sign_up():
    form_data=request.form
    print form_data['name']
    print form_data['email']

    name = form_data['name']
    email = form_data['email']

    requests.post(
        "https://api.mailgun.net/v3/YOUR OWN LINK THAT MAILGUN ASSIGNED",
        auth=("api", "YOUR OWM KEY"),
        #files=[("attachment", open("/Users/melis/Documents/cfg_example_screenshot.png"))],
        data={
            "from": "CFG Python Course<no_reply@cfgpython.com>",
            "to": name + " <" + email + ">",
            "subject": "Hello " +  name,
            "text": "Congratulations " + name + ", you just signed up!  You are truly awesome!"
            #"o:deliverytime": "Tue, 23 Feb 2016 01:34:10 -0000"
            #"html": "<html>HTML version of the body</html>"
            }
            )
    return render_template("hello.html", name=name.title())
    #return "All OK"

app.run(debug=True)
