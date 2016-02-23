from flask import Flask
from flask import render_template
from flask import request

app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello World again."

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/signup", methods=['POST'])
def sign_up():
    form_data = request.form
    print form_data['name']
    return "All OK"

app.run(debug=True)
