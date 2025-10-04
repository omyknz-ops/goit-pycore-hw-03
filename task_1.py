from datetime import datetime 


def get_days_from_today(date_string): # data_string in "YYYY-MM-DD" format

    given_date = datetime.strptime(date_string, "%Y-%m-%d").date() # Convert string to date
    today = datetime.today().date() #Get today's date

    delta = today - given_date #Calculate the difference
    return delta.days #Return the difference in days 
print (get_days_from_today("2026-10-06")) # checning the function