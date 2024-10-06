class welcome_customer:
    def __init__(self):
        print('\n')
        print('Choose an option to proceed : \n    1.To See Menu\n    2.To See Table Details \n    3.To Place An Order For A Table\n    4.To Register A New Customer\n    5.To Manage Inventory\n    6.To View Inventory Info\n    7.To Generate Bill\n    8.To Quit')
        while True:

            try:
                a = int(input("Enter What You Want To Do : "))
            except TypeError:
                print('Input Error')
            print(a)
            try:
                if a == 1:
                    menu()
                elif a == 2:
                    table_details()
                elif a == 3:
                    table_no = input('Enter Table Number : ')
                    print('\n')
                    customer_name = input('Enter Customer Name : ')
                    print('\n')
                    order_date = input('Enter Order Date : ')
                    print('\n')
                    dish_name = input('Enter The Name Of Dish : ')
                    table_order(table_no, customer_name, order_date, dish_name)
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
                elif a == 7:
                    table_no = input("Enter Table Number to generate bill: ")
                    customer_name = input("Enter Customer Name: ")
                    billing(table_no, customer_name)
                else:
                    print("Your Have Entered Wrong Input")
                print('\nPress 9 To Enter Menu\n')
                if a == 9:
                   print('    1.To See Menu\n    2.To See Table Details\n    3.To Place An Order For A Table\n    4.To Register A New Customer\n    5.To Manage Inventory\n    6.To View Inventory Info\n    7.To Generate Bill\n    8.To Quit')
            except:
                print('ERROR')
            if a == 8:
                import time
                print('-------------- Thanks For Using The Restaurant Management System! --------------')
                time.sleep(5)
                exit()


class restaurant_inventory:
    def add_inventory(self, dishname, quantity):
        with open('RESTRAUNT-MANAGEMENT-SYSTEM/Dishes in inventory.txt', 'a') as inv_file:
            inv_file.write(f'Dish Name --------> {dishname} and its quantity is {quantity} \n')
        with open('RESTRAUNT-MANAGEMENT-SYSTEM/Dishes Available.txt', 'a') as available_dishes:
            available_dishes.write(f'{dishname}\n')

    def show_inventory(self):
        with open('RESTRAUNT-MANAGEMENT-SYSTEM/Dishes in inventory.txt', 'r') as inven:
            info = inven.read()
            print(info)

class menu:
    def __init__(self):
        with open('RESTRAUNT-MANAGEMENT-SYSTEM/Dishes Available.txt', 'r') as mn:
            available_dishes = mn.read()
        print(f'The Available Dishes are : \n\n{available_dishes}')

class table_order:
    def __init__(self, table_no, customer_name, order_date, ordered_dish):
        with open(f'RESTRAUNT-MANAGEMENT-SYSTEM/Table_{table_no}_Order_Record.txt', 'a') as table_record:
            table_record.write(f'{customer_name} at Table {table_no} ordered {ordered_dish} on {order_date}.\n')

class table_details:
    def __init__(self):
        table_no = input("Enter the Table Number to view orders: ")
        try:
            with open(f'RESTRAUNT-MANAGEMENT-SYSTEM/Table_{table_no}_Order_Record.txt', 'r') as table_rec:
                orders = table_rec.read()
                print(f"Orders for Table {table_no}:\n{orders}")
        except FileNotFoundError:
            print(f"No orders found for Table {table_no}.")

class billing:
    def __init__(self, table_no, customer_name):
        try:
            # Retrieve the order details for the table
            with open(f'RESTRAUNT-MANAGEMENT-SYSTEM/Table_{table_no}_Order_Record.txt', 'r') as table_rec:
                orders = table_rec.read()
                print(f"\n--- Bill for Table {table_no} ---")
                print(f"Customer Name: {customer_name}")
                print(f"Orders:\n{orders}")
                
                # Here you can add a function to calculate the total cost of the dishes if pricing is available
                total_cost = self.calculate_total_cost(orders)
                print(f"Total Cost: ${total_cost}")
                
                # Save the bill for future reference
                with open(f'RESTRAUNT-MANAGEMENT-SYSTEM/Bill_for_Table_{table_no}.txt', 'w') as bill_file:
                    bill_file.write(f"Customer Name: {customer_name}\n")
                    bill_file.write(f"Table Number: {table_no}\n")
                    bill_file.write(f"Orders:\n{orders}\n")
                    bill_file.write(f"Total Cost: ${total_cost}\n")
                    
                print("\n--- Thank you for dining with us! Your bill has been generated. ---")
        except FileNotFoundError:
            print(f"No orders found for Table {table_no}.")

    def calculate_total_cost(self, orders):
        # Assuming a simple pricing mechanism for demo purposes
        dish_prices = {
            'Pasta': 12.99,
            'Pizza': 15.99,
            'Salad': 8.99,
            'Burger': 10.99,
            'Soda': 2.50
        }
        total_cost = 0
        for order in orders.split('\n'):
            for dish, price in dish_prices.items():
                if dish in order:
                    total_cost += price
        return total_cost


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
