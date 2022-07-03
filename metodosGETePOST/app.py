from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


# aqui eu seto os métodos possíveis de se utilizar GET e POST
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('user', usr=user))
    else:
        return render_template('login.html')


@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
