from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello world! </p>"


@app.route("/novarota")
def novarota():
    return "<h2>Esta é uma nova rota</h2>"


@app.route("/outranovarota/<int:valor>")
def outranovarota(valor):
    return f"<h2>O valor informado foi {valor}</h2>"


@app.route("/api", methods=["GET", "POST"])
def api():
    if request.method == "POST":
        return request.get_json()
    else:
        return "requisição GET"


