import datetime

def get_commission(date_str) -> float:

    #price standard
    price = 500
    high_season = "15%"
    less_season = "10%"

    # format
    format = '%Y/%m/%d'

    # convert from string format to datetime format
    datetimes = datetime.datetime.strptime(date_str, format)
    date = datetimes.date()
    
    # save specifq month
    specifq_month = date.month
    
    if specifq_month >= 6 and specifq_month <= 9:
        total = price * 0.15;
        #print("Comission is 15% :{0} in the month of".format(total), date.strftime("%B"))
        return high_season
    else:
        total = price * 0.10;
        #print("Comission is 10% :{0} in the month of".format(total), date.strftime("%B"))
        return less_season

get_commission("2021/07/15")
