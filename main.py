import os
from flask import Flask, send_file, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

import pandas as pd

from csv_functions import add_row_to_projects

UPLOAD_FOLDER = 'templates'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(requester_name+'.pdf')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #return redirect(url_for('uploaded_file', filename=filename))

    add_row_to_projects(requester_name, '{}-{}'.format(vertical, horizontal), level, office, interest_1, interest_2, start_date, duration, '')

    return 'project submitted :D'
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



@app.route('/hello/')
@app.route('/hello/<name>')
def template_test(name=None):
    return render_template('hello.html', name=name)

@app.route('/send_email/')
def send_email(name=None):
    return render_template('send_email.html', name=name)

@app.route('/download_pdf/<partner_name>')
def downloadFile(partner_name=None):
    path = "templates/{partner_name}.pdf".format(partner_name=partner_name)
    return send_file(path, as_attachment=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file_upload', methods=['GET', 'POST'])
def upload_file(name=None):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('file_upload.html', name=name)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)




