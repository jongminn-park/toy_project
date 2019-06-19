from datetime import datetime, timedelta

def datetime_from_utc_to_local(utc_date_time):
    offset = timedelta(hours=9)
    return utc_date_time + offset

def print_current_weather(data):
    utc_dt = datetime.utcfromtimestamp(int(data["dt"]))
    local_dt = datetime_from_utc_to_local(utc_dt)
    print("time : ",local_dt.strftime("%m-%d %H:%M"))
    print("weather description : ", data["weather"][0]["description"])
    print("temperature : %.2f\u2103 " %(float(data["main"]["temp"]) - 273.15))
    print("humidity : %d%%" % data["main"]["humidity"])
    if "rain" in data:
        print("rain volume : ", data["rain"])
    if "snow" in data:
        print("snow voulme : ", data["snow"])
    print()

def print_forecast(data):
    umb = False
    first_five = data["list"][:5]
    for each_data in first_five:
        if "rain" in each_data:
            umb = True
        print_current_weather(each_data)
    
    if umb:
        print("우산 챙겨야 함")
