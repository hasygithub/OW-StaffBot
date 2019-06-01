import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def match_and_email():

    projects = pd.read_csv('projects.csv')
    resources = pd.read_csv('resources.csv')

    cross_join = projects.assign(foo=1).merge(resources.assign(foo=1), on='foo').drop('foo', 1)
    cross_join.loc[(cross_join.level_required == cross_join.level) &
                   (cross_join.office_preference == cross_join.office), 'match'] = 1

    for i in range(0, len(cross_join)):
        if cross_join.loc[i, 'match'] == 1.0:
            #TODO Change these back to the emails
            # partner_email = cross_join.loc[i, 'partner_name']
            # consultant_email = cross_join.loc[i, 'consultant_name']
            partner_email = 'amyryush1115@gmail.com'
            consultant_email = 'amy.ryu@oliverwyman.com'
            partner_name = cross_join.loc[i, 'partner_name']
            consultant_name = cross_join.loc[i, 'consultant_name']


            project = cross_join.loc[i, 'type_of_work_1']
            print("It's a match for " + partner_name + " and " + consultant_name + " for " + project)

            # consultant email
            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Project Radar'
            msg['From'] = 'Staff.Bot@gmail.com'
            msg['To'] = consultant_email

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.ehlo()
            #TODO make a better email address
            #TODO host server
            server.login('StaffBotforOW@gmail.com', 'Staffbot123')
            server.sendmail('Project Radar', consultant_email, "Hi " + consultant_name + ",\n" \
            "It's a match for " + partner_name + " and " + consultant_name + " for " + project + "." \
            + " Please use this email chain as a form of communication and visit XX for further information")
            server.quit()

            # partner email
            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Staffing Radar'
            msg['From'] = 'Staff.Bot@gmail.com'
            msg['To'] = partner_email

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.ehlo()
            #TODO make a better email address
            #TODO host server
            server.login('StaffBotforOW@gmail.com', 'Staffbot123')
            server.sendmail('Project Radar', partner_email, "Hi " + partner_name + ",\n" \
            "It's a match for " + partner_name + " and " + consultant_name + " for " + project + "." \
            + " Please use this email chain as a form of communication and visit XX for further information")
            server.quit()


        else:
            print("not a match")

    pass