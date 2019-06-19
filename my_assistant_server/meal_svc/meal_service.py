from bs4 import BeautifulSoup
import requests
import sys, os
sys.path.append("..")
from my_assistant.settings import BASE_DIR
import json

file_path = os.path.join(BASE_DIR, 'meal_svc/html_files/re')

MEAT = ["고기", "까스", "육", "돈", "닭", "함바그", "함박", "치킨", "스테이크"]
RICE = ["밥", "라이스"]
NOODLES = ["면", "국수", "우동", "소바"]


class Menu(dict):
    def __init__(self, data):
        super().__init__(data)


def classify_food(menu_main):
    global MEAT, RICE, NOODLES
    for item in RICE:
        if item in menu_main:
            return "rice"
    for item in NOODLES:
        if item in menu_main:
            return "noodles"
    for item in MEAT:
        if item in menu_main:
            return "meat"


def parsing_data(url):
    global file_path
   # resp = requests.get(url)
   # soup = BeautifulSoup(resp.text, 'html.parser')
    with open(file_path+str(url), 'rt') as f:
        soup = BeautifulSoup(f, 'html.parser')
    result = []

    # get location where menu served
    location = soup.h4.get_text()
    targets = soup.find_all("div", {"class": "in-box"})

    for target in targets:
        # get time when menu served
        time = target.h4.get_text()
        if time == "공통찬":
            break
        menus = target.find_all('li')
        
        for each_menu in menus:
            # menu's name
            items = each_menu.img["alt"].replace(',','').split(' ')
            if items:
                if items[0] == "[학생]" or items[0] == "[교직원]":
                    items.pop(0)
                store = items.pop(0)
                if store == "[The":
                    store = store + " " + items.pop(0)
                main_dish = items[0]
                label = classify_food(main_dish)
                if label == None:
                    for i in range(1,len(items)):
                        label = classify_food(items[i])
                        if label != None:
                            break
                name = ", ".join(items)
                price = each_menu.find("p", {"class": "price"}).get_text()
                tmp = [
                        ('name', name),
                        ('location', location),
                        ('price', price),
                        ('time',time),
                        ('store_name', store),
                        ('label', label)]
                
                result.append(Menu(tmp))

    return result


def print_menu(menu):
    print("name : ", menu["name"])
    print("location : ", menu["location"])
    print("store_name : ", menu["store_name"])
    print("time : ", menu["time"])
    print("type : ", menu["label"])
    print("price : ", menu["price"])


def get_all_menus():
    menus = []
    for i in range(2,9):
       if i ==6 or i == 7:
           continue
       menus.extend(parsing_data(i))
    result = {"menus": menus}
    return result

if __name__ == "__main__":
    url = "http://www.hanyang.ac.kr/web/www/re"
    for i in range(2,9):
        if i == 6 or i == 7:
            continue
        menus = parsing_data(i)

        for menu in menus:
            print_menu(menu)
            print()
        print('\n\n')
