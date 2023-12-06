from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {'teste': '123', 'user2': 'password2'}


@app.route('/')
def login():
    return render_template('index.html')


@app.route('/dashboard', methods=['post'])
def dashboard():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return render_template('dashboard.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/cadastro')
def cadastro():
    return  render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)