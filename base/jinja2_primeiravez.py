from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/<nome>')
def user(nome):
    return f"Hello, {nome}!"


@app.route("/admin")
def admin():
    return redirect(url_for("user", nome="Admin"))


if __name__ == '__main__':
    app.run(debug=True)
