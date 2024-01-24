import datetime

def get_week_day():
    ## returns an integer between 1 (Monday) and 7 (Sunday)
    return (datetime.today().weekday()+1)
