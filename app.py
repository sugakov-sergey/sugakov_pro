from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

from flask import url_for

app = Flask(__name__, static_folder="static")


def send_mail(to_email, subject, message, from_email, server='mailbe05.hoster.by'):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(message)
    server = smtplib.SMTP(server, 587)
    server.set_debuglevel(1)
    server.login(to_email, 'Independence01')  # user & password
    server.send_message(msg)
    server.quit()
    print('successfully sent the mail.')


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
            send_mail(to_email='me@sugakov.pro',
                      subject=title, message=text, from_email=mail)
            return render_template('index.html', context=context, scroll='scroll')



    return render_template('index.html', context=context)



@app.route('/biography')
def biography():
    return render_template('biography.html')


if __name__ == '__main__':
    app.run(debug=True)
