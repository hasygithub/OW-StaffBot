import os
from flask import Flask, send_file, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

import pandas as pd

from csv_functions import add_row_to_projects, add_row_to_resources
from match import match_and_email

UPLOAD_FOLDER = 'files'
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
                           num=len(list(df['client'])),
                           client=list(df['client']),
                           project_name=list(df['project_name']),
                           vert_horiz=list(df['vert_horiz']),
                           partner_name=list(df['partner_name']),
                           type_of_work_1=list(df['type_of_work_1']),
                           type_of_work_2=list(df['type_of_work_2']),
                           level=list(df['level_required']),
                           office_preference=list(df['office_preference']),
                           start_date=list(df['start_date']),
                           duration=list(df['duration']),
                           attachment=list(df['attachment']),
                           contact_email=list(df['contact_email'])
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

    print ('test')

    client = request.form['client']
    project_name = request.form['project_name']
    vertical = request.form['vertical']
    horizontal = request.form['horizontal']
    partner_name = request.form['partner_name']
    type_of_work_1 = request.form['interest_1']
    type_of_work_2 = request.form['interest_2']
    level_required = request.form['level']
    office_preference = request.form['office']
    start_date = request.form['start_date']
    duration = request.form['duration']
    attachment = ''
    contact_email = request.form['contact_email']

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
        filename = secure_filename(project_name+'_proposal.pdf')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #return redirect(url_for('uploaded_file', filename=filename))

    add_row_to_projects(client,
                        project_name,
                        '{}-{}'.format(vertical, horizontal),
                        partner_name,
                        type_of_work_1,
                        type_of_work_2,
                        level_required,
                        office_preference,
                        start_date,
                        duration,
                        attachment,
                        contact_email)

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
        filename = secure_filename(consultant_name+'_resume.pdf')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #return redirect(url_for('uploaded_file', filename=filename))

    add_row_to_resources(consultant_name, vertical, horizontal, interest_1, interest_2, level, office, start_date, '', '', '', TM)

    return 'resource submitted :D'
    # your code
    # return a response


@app.route('/projects_clean')
def projects_clean():
    df = pd.read_csv('projects.csv')
    return render_template('projects_clean.html',
                           num=len(list(df['client'])),
                           client=list(df['client']),
                           project_name=list(df['project_name']),
                           vert_horiz=list(df['vert_horiz']),
                           partner_name=list(df['partner_name']),
                           type_of_work_1=list(df['type_of_work_1']),
                           type_of_work_2=list(df['type_of_work_2']),
                           level_required=list(df['level_required']),
                           office_preference=list(df['office_preference']),
                           start_date=list(df['start_date']),
                           duration=list(df['duration']),
                           attachment=list(df['attachment']),
                           contact_email=list(df['contact_email'])
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

@app.route('/download_proposal_pdf/<partner_name>')
def downloadproposalFile(partner_name=None):
    path = "files/{partner_name}_proposal.pdf".format(partner_name=partner_name)
    return send_file(path, as_attachment=True)

@app.route('/download_resume_pdf/<consultant_name>')
def downloadresumeFile(consultant_name=None):
    path = "files/{consultant_name}_resume.pdf".format(consultant_name=consultant_name)
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



@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404



