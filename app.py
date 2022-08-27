from flask import Flask, render_template
from flask import url_for
app = Flask(__name__, static_folder="static")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/temp')
def temp():
    return render_template('temp.html')


@app.route('/biography')
def biography():
    return render_template('biography.html')


if __name__ == '__main__':
    app.run(debug=True)
