from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        persona = request.form['username']
        session['username1'] = persona
        return redirect(url_for('user'))
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username1', None)
    return redirect(url_for('index'))


@app.route('/user')
def user():
    if 'username1' in session:
        u = session['username1']
        return render_template('user.html', username=u)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
