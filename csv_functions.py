import pandas as pd

def add_row_to_projects(partner_name,
                        practice,
                        level_required,
                        office_preference,
                        type_of_work_1,
                        type_of_work_2,
                        start_date,
                        duration,
                        attachment):

    df = pd.read_csv('projects.csv')

    row = [partner_name,
           practice,
           level_required,
           office_preference,
           type_of_work_1,
           type_of_work_2,
           start_date,
           duration,
           attachment]

    df_row = pd.DataFrame(data=[row], columns=df.columns)
    df_complete = df.append(df_row)
    df_complete.to_csv('projects.csv', index=False)