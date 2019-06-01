from flask import Flask
import pandas as pd

from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/projects/')
def projects():
    df = pd.read_csv('projects.csv')
    return render_template('projects.html',
                           num=len(list(df['partner_name'])),
                           partner_name=list(df['partner_name']),
                           practice=list(df['practice']),
                           level_required=list(df['level_required']),
                           office_preference=list(df['office_preference']),
                           type_of_work_1=list(df['type_of_work_1']),
                           type_of_work_2=list(df['type_of_work_2']),
                           start_date=list(df['start_date']),
                           duration=list(df['duration']),
                           attachment=list(df['attachment'])
                           )

@app.route('/resources/')
def resources():
    df = pd.read_csv('resources.csv')
    return render_template('resources.html',
                           num=len(list(df['consultant_name'])),
                           consultant_name=list(df['consultant_name']),
                           practice=list(df['practice']),
                           level=list(df['level']),
                           office=list(df['office']),
                           interest_1=list(df['interest_1']),
                           interest_2=list(df['interest_2']),
                           start_date=list(df['start_date']),
                           one_pager=list(df['one_pager'])
                           )

@app.route('/input_test')
def input_test():
    return render_template('input_test.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    return projectpath
    # your code
    # return a response



@app.route('/hello/')
@app.route('/hello/<name>')
def template_test(name=None):
    return render_template('hello.html', name=name)

@app.route('/send_email/')
def send_email(name=None):
    return render_template('send_email.html', name=name)


