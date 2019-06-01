from flask import Flask
from flask import send_file

import pandas as pd
from csv_functions import add_row_to_projects, add_row_to_resources
from match import match_and_email
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

@app.route('/request_form')
def request_form():
    return render_template('request_form.html')

@app.route('/auto_email')
def auto_email():
    match_and_email()

    return 'Email sent!'

@app.route('/resource_form')
def resource_form():
    return render_template('resource_form.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    requester_name = request.form['requester_name']
    vertical = request.form['vertical']

    horizontal = request.form['horizontal']
    level = request.form['level']
    office = request.form['office']
    interest_1 = request.form['interest_1']
    interest_2 = request.form['interest_2']

    start_date = request.form['start_date']
    duration = request.form['duration']

    add_row_to_projects(requester_name, '{}-{}'.format(vertical, horizontal), level, office, interest_1, interest_2, start_date, duration, '')

    return 'project submitted :D'
    # your code
    # return a response


@app.route('/handle_data_resources', methods=['POST'])
def handle_data_resources():
    consultant_name = request.form['consultant_name']
    vertical = request.form['vertical']
    horizontal = request.form['horizontal']

    level = request.form['level']
    office = request.form['office']
    interest_1 = request.form['interest_1']
    interest_2 = request.form['interest_2']

    start_date = request.form['start_date']
    TM = request.form['TM']

    add_row_to_resources(consultant_name, vertical, horizontal, interest_1, interest_2, level, office, start_date, '', '', '', TM)

    return 'resource submitted :D'
    # your code
    # return a response


@app.route('/projects_clean')
def projects_clean():
    df = pd.read_csv('projects.csv')
    return render_template('projects_clean.html',
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



@app.route('/resources_clean')
def resources_clean():
    df = pd.read_csv('resources.csv')
    return render_template('resources_clean.html',
                           num=len(list(df['consultant_name'])),
                           consultant_name=list(df['consultant_name']),
                           vertical=list(df['vertical']),
                           horizontal=list(df['horizontal']),
                           interest_1=list(df['interest_1']),
                           interest_2=list(df['interest_2']),
                           level=list(df['level']),
                           office=list(df['office']),
                           start_date=list(df['start_date']),
                           attachments=list(df['attachments']),
                           email_link=list(df['email_link']),
                           contact_email=list(df['contact_email']),
                           tm_email=list(df['tm_email']),
                           )


@app.route('/hello/')
@app.route('/hello/<name>')
def template_test(name=None):
    return render_template('hello.html', name=name)

@app.route('/send_email/')
def send_email(name=None):
    return render_template('send_email.html', name=name)

@app.route('/download_pdf')
def downloadFile():
    path = "templates/20190414_2302_0_1_neural_net_iterations.pdf"
    return send_file(path, as_attachment=True)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404



