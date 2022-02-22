def menu():
    
    Main_Menu = '''
    [0] To exit app
    [1] To view couriers list
    [2] To add new couriers
    [3] To update/replace courier 
    [4] To Delet/Remove courier "\n" '''

    print(Main_Menu)


# add item - working but not for coffee - also first item not showing on line 1 
def add_courier(name):
    try:
        with open("database/couriers.txt", "a", newline="") as couriers:
            couriers.write(name + "\n")
    except Exception as error1:
        print("failed to execute courier", error1)

# add_courier("james")

# view menu - working
def view_courier():
    try:
        with open("database/couriers.txt", "r") as couriers:
            view_courier = couriers.readlines()
            item_num = 1
            for items in view_courier:
                print(f"{item_num}.", items.replace("\n", ""))
                item_num += 1
    except Exception as error1:
        print("failed to execute courier", error1)

# view_courier()


# update/replace with new product - working
def update_courier(old_courier, new_courier):
    old_courier = old_courier + "\n"
    try:
        with open("database/couriers.txt", "r") as couriers:
            view_courier = couriers.readlines()
            for names in view_courier:
                if names == old_courier:
                    item_num = view_courier.index(names)
                    view_courier[item_num] = new_courier + "\n"
                    try:
                        with open("database/couriers.txt", "w") as couriers:
                            couriers.writelines(view_courier)
                            view_courier
                    except Exception as error1:
                        print("failed to write to the file", error1)
    except Exception as error1:
        print("failed to execute courier", error1)

# old_courier = "Sandra"
# new_courier = "sammy"
# update_courier(old_courier, new_courier)

# delete item - working
def delete_courier(old_courier):
    old_courier = old_courier + "\n"
    try:
        with open("database/couriers.txt", "r") as couriers:
            view_courier = couriers.readlines()
            for names in view_courier:
                if names == old_courier:
                    item_num = view_courier.index(names)
                    del view_courier[item_num]
                    try:
                        with open("database/couriers.txt", "w") as couriers:
                            couriers.writelines(view_courier)
                            view_courier
                    except Exception as error1:
                        print("failed to write to the file", error1)
    except Exception as error1:
        print("failed to execute courier", error1)

# delete_courier("adam")

def get_courier_name(courier_id):
    courier_name = " "
    try:
        with open("database/couriers.txt", "r") as courier_file:
            courier_list = courier_file.readlines()
            item_num = 1
            for couriers in courier_list:
                if item_num == courier_id:
                    courier_name = couriers.replace("\n", "")
                # print(f"{item_num}.", products.replace("\n", ""))
                item_num += 1
    except Exception as error1:
        print("failed to execute courier", error1)
    return courier_name

# print(get_courier_name(4))
