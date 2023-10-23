
katz_deli = []

def line(customers):
    if len(customers) == 0:
        print("The line is currently empty.")
    else:
        customers_list = []
        i = 0 
        while i < len(customers):
            message = f'{i+1}. {customers[i]}'
            customers_list.append(message)
            i+=1
        print(f'The line is currently: {" ".join(customers_list)}')

def take_a_number(customers, name):
    customers.append(name)
    print(f'Welcome, {name}. You are number {customers.index(name)+1} in line.')

def now_serving(customer):
    if len(customer) > 0:
        name = customer.pop(0)
        print(f'Currently serving {name}.')
    else:
        print("There is nobody waiting to be served!")
