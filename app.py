from flask import Flask
import pendulum

app = Flask(__name__)

@app.route("/")
def index():
    return "Sveiki atvykę"

@app.route("/skaiciavimai/")
def skaiciavimai():
    return "<h1>Skaičiavimų puslapis</h1>"


if __name__ == "__main__":
    app.run(debug=True)