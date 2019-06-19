import my_gps
import requests
import c_meal_service
import c_weather_service
import c_routing_service


data = my_gps.get_geolocation(using_wifiInfo=True)
lat = str(data['location']['lat'])
lng = str(data['location']['lng'])
geolo = lat+','+lng
host = "http://192.168.55.46:8000"
headers = {'geolocation' : geolo}

user_id = input("please type your id : ")
while True:
    headers["myauth"] =  user_id
    with requests.get(host+"/my-auth", headers=headers) as resp:
        if resp.status_code != 200:
           user_id = input("please type your id again : ")
        else:
            break
while True:
    command = input('command :')

    if command == "다음 일정":
        resource = "/schedule-svc/next-schedule"

        with requests.get(host+resource, headers=headers) as resp:
            result = resp.json()
        if "answer" in result:
            print("다음 일정이 없습니다.")
        else:
            c_routing_service.print_route_guide(result)
    elif command in ["식사 추천", "육류 추천", "면류 추천", "밥류 추천"]:
        resource = "/meal-svc/recommendation"

        with requests.get(host+resource, headers=headers) as resp:
            menus = resp.json()['menus']
        c_meal_service.print_menus_by_label(menus, command)

    elif command == "일기예보":
        resource = "/weather-svc/forecast"

        with requests.get(host+resource, headers=headers) as resp:
            result = resp.json()
        c_weather_service.print_forecast(result)
    elif command == "현재 날씨":
        resource = "/weather-svc/current-weather"


        with requests.get(host+resource, headers=headers) as resp:
            result = resp.json()
        c_weather_service.print_current_weather(result)
    else:
        print("지원하지 않는 명령어입니다.")


    print('\n')

