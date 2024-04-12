from flask import Flask
app= Flask(__name__)


@app.route("/")
def hello():
    return "hello world"

@app.route("/moeeed")
def moeeed():
    return "my name is moeed!"
app.run(debug=True)