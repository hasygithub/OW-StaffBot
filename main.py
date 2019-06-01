from flask import Flask
import pandas as pd

from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/beach_requests/')
def beach_requests():
    df = pd.read_csv('beach_requests.csv')
    return render_template('hello.html',
                           num=len(list(df['request_id'])),
                           request_id=list(df['request_id']),
                           partner_name=list(df['partner_name']),
                           request_description=list(df['request_description']),
                           days_required=list(df['days_required']))



@app.route('/beach_resources/')
def beach_requests():
    df = pd.read_csv('beach_resources.csv')
    return render_template('hello.html',
                           num=len(list(df['request_id'])),
                           request_id=list(df['request_id']),
                           partner_name=list(df['partner_name']),
                           request_description=list(df['request_description']),
                           days_required=list(df['days_required']))


@app.route('/hello/')
@app.route('/hello/<name>')
def template_test(name=None):
    return render_template('hello.html', name=name)


