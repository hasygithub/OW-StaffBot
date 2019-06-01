import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def match_and_email(test_email):

    projects = pd.read_csv('projects.csv')
    resources = pd.read_csv('resources.csv')

    cross_join = projects.assign(foo=1).merge(resources.assign(foo=1), on='foo').drop('foo', 1)
    cross_join.loc[(cross_join.level_required == cross_join.level) &
                   ((cross_join.type_of_work_1 == cross_join.interest_1) |
                    (cross_join.type_of_work_1 == cross_join.interest_2) |
                    (cross_join.type_of_work_2 == cross_join.interest_1) |
                    (cross_join.type_of_work_2 == cross_join.interest_2)), 'match'] = 1

    for i in range(0, len(cross_join)):
        if cross_join.loc[i, 'match'] == 1.0:
            #TODO Change these back to the emails
            # partner_email = cross_join.loc[i, 'partner_name']
            # consultant_email = cross_join.loc[i, 'consultant_name']
            partner_email = 'kei.nishimuragasparian@gmail.com'
            consultant_email = 'kei.nishimura-gasparian@oliverwyman.com'
            partner_name = cross_join.loc[i, 'partner_name']
            consultant_name = cross_join.loc[i, 'consultant_name']


            project = cross_join.loc[i, 'type_of_work_1']
            print("It's a match for " + partner_name + " and " + consultant_name + " for " + project)

            # consultant email
            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Project Radar'
            msg['From'] = 'staff.bot.ow@gmail.com'
            msg['To'] = consultant_email

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.ehlo()
            #TODO make a better email address
            #TODO host server
            server.login('staff.bot.ow@gmail.com', 'Pyspark4lyfe22')
            server.sendmail('Project Radar', [test_email,consultant_email], "Hi " + consultant_name + ",\n" \
            "It's a match for " + partner_name + " and " + consultant_name + " for " + project + "." \
            + " Please use this email chain as a form of communication and visit XX for further information." \
            + "\n" + "From,\n" + "Staffbot")
            server.quit()

            # partner email
            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Staffing Radar'
            msg['From'] = 'staff.bot.ow@gmail.com'
            msg['To'] = partner_email

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.ehlo()
            #TODO make a better email address
            #TODO host server
            server.login('staff.bot.ow@gmail.com', 'Pyspark4lyfe22')
            server.sendmail('Project Radar', [test_email,partner_email], "Hi " + partner_name + ",\n" \
            "It's a match for " + partner_name + " and " + consultant_name + " for " + project + "." \
            + " Please use this email chain as a form of communication and visit XX for further information")
            server.quit()


        else:
            print("not a match")

    pass