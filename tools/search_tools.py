from datetime import datetime

def get_todays_date():
    return datetime.now().strftime("%Y-%m-%d")