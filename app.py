from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return "<h1>Student Application - Version 001</h1>"
test fail deployment
