from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepag.html')


@app.route('/<name>')
def nomeia(name):
    return render_template('index.html', content=name, lista=['John', 'Jorge', 'Richard'])


if __name__ == '__main__':
    app.run(debug=True)
