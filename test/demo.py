import os

from generic_utils import Excel_Utils

import datetime

def get_the_news_posted_date(text):
    today = datetime.date.today()
    if str(text).__contains__("hour"):
        return today.strftime("%Y-%m-%d")
    elif str(text).__contains__("days"):
        digits = filter(str.isdigit, text)
        integer_str = int(''.join(digits))
        date_to_print = today - datetime.timedelta(days=integer_str)
        return date_to_print.strftime("%Y-%m-%d")


get_the_news_posted_date("1 hour")
