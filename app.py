from flask import Flask, render_template, request

import config
from moduls.mail import send_mail

app = Flask(__name__, static_folder="static")


@app.route('/', methods=['POST', 'GET'])
def index():
    btn_value = 'SEND TO ME'
    msg = ''
    context = {'msg': msg, 'btn_value': btn_value}

    if request.method == 'POST':
        title = request.form['title']
        mail = request.form['mail']
        text = request.form['text']
        sent = request.form['sent']

        if sent == "OK" and not all([title, mail, text]):
            msg = ''
            btn_value = 'SEND TO ME'
            context = {'msg': msg, 'btn_value': btn_value}
            return render_template('index.html', context=context)

        if not all([title, mail, text]):
            msg = 'Please enter all fields'
            btn_value = 'TRY AGAIN'
            context = {'msg': msg, 'btn_value': btn_value}
            return render_template('index.html', context=context, scroll='scroll')

        if sent == 'TRY AGAIN' or 'SEND TO ME':
            msg = 'Your message sent'
            btn_value = 'OK'
            context = {'msg': msg, 'btn_value': btn_value}
            send_mail(to_email=config.mail,
                      subject=title, message=text, from_email=mail)
            return render_template('index.html', context=context, scroll='scroll')

    return render_template('index.html', context=context)


@app.route('/biography')
def biography():
    return render_template('biography.html')


if __name__ == '__main__':
    app.run(debug=True)
