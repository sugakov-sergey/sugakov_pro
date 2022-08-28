from flask import Flask, render_template, request, redirect
from flask import url_for

app = Flask(__name__, static_folder="static")


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        mail = request.form['mail']
        text = request.form['text']
        msg = 'Your message sent'
        context = {'msg': msg}
        return render_template('index.html', context=context, scroll='scroll')
    return render_template('index.html')

@app.route('/temp')
def temp():
    return render_template('temp.html')


@app.route('/biography')
def biography():
    return render_template('biography.html')


if __name__ == '__main__':
    app.run(debug=True)
