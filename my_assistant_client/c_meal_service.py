
def print_menu(menu):
    print("name : ", menu["name"])
    print("location : ", menu["location"])
    print("store_name : ", menu["store_name"])
    print("time : ", menu["time"])
    print("label : ", menu["label"])
    print("price : ", menu["price"])
    print()
    
def print_menus_by_label(menus,command):
    if command == "식사 추천":
        for menu in menus:
             print_menu(menu)

    elif command == "육류 추천":
        for menu in menus:
            if menu["label"] == "meat":
                print_menu(menu)

    elif command == "면류 추천":
        for menu in menus:
            if menu["label"] == "noodles":
                print_menu(menu)

    elif command == "밥류 추천":
        for menu in menus:
            if menu["label"] == "rice":
                print_menu(menu)
