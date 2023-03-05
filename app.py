from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def search():
    return render_template("login.html")


@app.route('/regestration')
def reg():
    return render_template("reg.html")


if __name__ == '__main__':
    app.run()
