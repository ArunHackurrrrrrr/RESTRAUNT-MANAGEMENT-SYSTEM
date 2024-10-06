class welcome_customer:
    def __init__(self):
        print('\n')
        print('Choose an option to proceed : \n    1.To See Menu\n    2.To See Order Records \n    3.To Place An Order\n    4.To Register A New Customer\n    5.To Manage Inventory\n    6.To View Inventory Info\n    7.To Quit')
        while True:

            try:
                a= int(input("Enter What You Want To Do : "))
            except TypeError:
                print('Input Error')
            print(a)
            try:
                if a == 1:
                    menu()
                elif a == 2:
                    order_record()
                elif a == 3:
                    customer_name = input('Enter Customer Name : ')
                    print('\n')
                    order_date = input('Enter Order Date : ')
                    print('\n')
                    dish_name = input('Enter The Name Of Dish : ')
                    order(customer_name, order_date, dish_name)
                elif a == 4:
                    access = customer_profile()
                    access.create_profile()
                elif a == 5:
                    dish_name = input('Enter the name of the dish to add : ')
                    print('\n')
                    quantity = input('Enter The Quantity : ')
                    access = restaurant_inventory()
                    access.add_inventory(dish_name, quantity)
                elif a == 6:
                    access = restaurant_inventory()
                    access.show_inventory()
                else:
                    print("Your Have Entered Wrong Input")
                print('\nPress 8 To Enter Menu\n')
                if a == 8:
                   print('    1.To See Menu\n    2.To See Order Records \n    3.To Place An Order\n    4.To Register A New Customer\n    5.To Manage Inventory\n    6.To View Inventory Info\n    7.To Quit')
            except:
                print('ERROR')
            if a == 7:
                import time
                print('-------------- Thanks For Using The Restaurant Management System! --------------')
                time.sleep(5)
                exit()


class restaurant_inventory:
    def add_inventory(self, dishname, quantity):
        with open('Content/Dishes/Dishes in inventory.txt', 'a') as inv_file:
            inv_file.write(f'Dish Name --------> {dishname} and its quantity is {quantity} \n')
        with open('Content/Dishes/Dishes Available.txt', 'a') as available_dishes:
            available_dishes.write(f'{dishname}\n')

    def show_inventory(self):
        with open('Content/Dishes/Dishes in inventory.txt', 'r') as inven:
            info = inven.read()
            print(info)

class menu:
    def __init__(self):
        with open('Content/Dishes/Dishes Available.txt', 'r') as mn:
            available_dishes = mn.read()
        print(f'The Available Dishes are : \n\n{available_dishes}')

class order:
    def __init__(self, customer_name, order_date, ordered_dish):
        with open('Content/orders/Order Record.txt', 'a') as order_record:
            order_record.write(f'{customer_name} ordered {ordered_dish} on {order_date}.\n')

class order_record:
    def __init__(self):
        with open('Content/orders/Order Record.txt', 'r') as order_rec:
            orders = order_rec.read()
            print(orders)

class customer_profile:
    def create_profile(self):
        print("To Create Customer Profile, Fill The Details Below : \n")
        print("Your Information : \n")
        customer_name = input('Enter Customer Name : ')
        print('\n')
        address = input('Enter Address (House no./Street/Area/City): ')
        print('\n')
        pincode = input('Enter Pincode : ')
        print('\n')
        print('Contact Details : \n')
        phone = input('Enter Phone Number : ')
        print('\n')
        email = input('Enter Email Address : ')
        print('\n')
        
        with open(f'Content/customer_profiles/{customer_name}_details.txt', 'w') as profile:
            profile.write(f'Name ----> {customer_name}\nAddress ----> {address}, Pincode ----> {pincode}\nContact ----> {phone}, Email ----> {email}')


# Entry point for the program
start = input('-------------------- Welcome To Restaurant Management System -------------------- \n \n Press M For Menu : ')
if start == 'M':
    welcome_customer()
else:
    print('Input Error')
    import time
    time.sleep(3)
MemoryError
