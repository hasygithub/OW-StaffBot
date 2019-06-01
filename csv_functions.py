import pandas as pd

def add_row_to_projects(client,
                        project_name,
                        vert_horiz,
                        partner_name,
                        type_of_work_1,
                        type_of_work_2,
                        level_required,
                        office_preference,
                        start_date,
                        duration,
                        attachment,
                        contact_email):

    df = pd.read_csv('projects.csv')

    row = [client,
           project_name,
           vert_horiz,
           partner_name,
           type_of_work_1,
           type_of_work_2,
           level_required,
           office_preference,
           start_date,
           duration,
           attachment,
           contact_email]

    df_row = pd.DataFrame(data=[row], columns=df.columns)
    df_complete = df.append(df_row)
    df_complete.to_csv('projects.csv', index=False)


def add_row_to_resources(consultant_name,
                         vertical,
                         horizontal,
                         interest_1,
                         interest_2,
                         level,
                         office,
                         start_date,
                         attachments,
                         email_link,
                         contact_email,
                         tm_email):

    df = pd.read_csv('resources.csv')

    row = [consultant_name,
                         '{}-{}'.format(vertical, horizontal),
                         interest_1,
                         interest_2,
                         level,
                         office,
                         start_date,
                         attachments,
                         email_link,
                         contact_email,
                         tm_email]

    df_row = pd.DataFrame(data=[row], columns=df.columns)
    df_complete = df.append(df_row)
    df_complete.to_csv('resources.csv', index=False)