from flask import Flask

app = Flask(_name_)

@app.route("/")
def index():
  return "Olá, <b>tudo bem<b>?"
