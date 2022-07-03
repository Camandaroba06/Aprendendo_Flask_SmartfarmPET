from distutils.log import info
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.permanent_session_lifetime = timedelta(minutes=1)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        persona = request.form['username']
        session['username1'] = persona
        flash("Você logou com Sucesso! {}".format(persona), "info")
        return redirect(url_for('user'))
    else:
        return render_template('login.html')


@app.route('/user')
def user():
    if 'username1' in session:
        u = session['username1']
        return render_template('user.html', username=u)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if 'username1' in session:
        u = session['username1']
        flash("You were logged out!! {}".format(u), "info")
        session.pop('username1', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
