from flask import Flask, render_template, request, url_for
from pyfladesk import init_gui
import subprocess as sp

app = Flask(__name__)

wdm_fields = ['fm', 'bvt', 'tracker', 'issue']


@app.route("/")
def home():
    return render_template('home.html', rt='hm')


@app.route('/exec-adb')
def command_exec():
    return render_template('exec-adb.html')


@app.route('/exec-adb', methods=['POST'])
def my_form_post_process():
    text = request.form['text']
    otp = sp.run(text, capture_output=True)
    return render_template('exec-adb.html', data=otp.stdout.decode())


@app.route('/manage_wd')
def manage_work_data():
    return render_template('manage_wd.html', fields=wdm_fields)
# from routes import *


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(init_gui(app, width=900, height=550,
                     window_title='Desktop Utility App'), debug=True)
