from smtplib import SMTPSenderRefused

from flask import Flask, render_template, request

import config
from moduls.mail import send_mail

app = Flask(__name__, static_folder="static")
application = app  # для работы на хостинге


@app.errorhandler(404)
def page_not_found(e):
    # в функцию `render_template()` передаем HTML-станицу с собственным
    # дизайном, а так же явно устанавливаем статус 404
    return render_template('404.html'), 404


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
            try:
                send_mail(to_email=config.mail,
                          subject=title, message=text, from_email=mail)
            except SMTPSenderRefused:
                msg = 'Invalid email'
                btn_value = 'TRY AGAIN'
                context = {'msg': msg, 'btn_value': btn_value}
                return render_template('index.html', context=context, scroll='scroll')
            except Exception:
                msg = 'Sorry, something wrong!'
                btn_value = 'TRY AGAIN'
                context = {'msg': msg, 'btn_value': btn_value}
                return render_template('index.html', context=context, scroll='scroll')

            return render_template('index.html', context=context, scroll='scroll')

    return render_template('index.html', context=context)


@app.route('/biography')
def biography():
    return render_template('biography.html')


if __name__ == '__main__':
    app.run(debug=True)
