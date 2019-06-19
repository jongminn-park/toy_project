from datetime import datetime, timedelta

def get_local_time(dt):
    s_year = int(dt[:4])
    s_month = int(dt[5:7])
    s_day = int(dt[8:10])
    s_hour = int(dt[11:13])
    s_minute = int(dt[14:16])
    result = datetime(s_year, s_month, s_day, s_hour, s_minute)
    
    return result
    
def get_latest_time(s_time, d_hours, d_minutes):
    return s_time - timedelta(hours=d_hours, minutes=d_minutes)

def print_route_guide(data):
    summary = data["route"]["trafast"][0]["summary"]
    points = data["route"]["trafast"][0]["guide"]
    title = data["event_title"]
    event_start_time = get_local_time(data["event_start_time"])
    hour , sec = divmod(int(summary["duration"]/1000),3600)
    minute, sec = divmod(sec, 60)
    latest_time = get_latest_time(event_start_time, hour, minute)
    origin = data["origin"]
    dest = data["dest"]

    print("경로 안내")
    for p in points:
       print( p["instructions"])   
    print('\n')
    print("summary")
    print("next event : ", title)
    print("current location : ", origin)
    print("destination : ", dest)
    print("event_start_time : ", event_start_time )
    print("duration : %dh %dm %ds"%(hour, minute, sec))
    print("latest time : ", latest_time)
