# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(name):
    return name['name']


def get_total_cash(customers):
    return customers['admin']['total_cash']


def add_or_remove_cash(customers ,amount):
    customers['admin']['total_cash'] += amount

    return customers['admin']['total_cash']


def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']


def increase_pets_sold(pet_shop, pets_sold):
    pet_shop['admin']['pets_sold'] += pets_sold
    
    return pet_shop['admin']['pets_sold']


def get_stock_count(pet_shop):
    stock = 0 + len(pet_shop['pets'])
    return stock


def get_pets_by_breed(pet_shop, breed):
    list = []
    for pet in pet_shop['pets']:
        if breed in pet['breed']:
            list.append(pet)
    return list


def find_pet_by_name(pet_shop, name):
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            return pet


def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            pet_shop['pets'].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    if new_pet not in pet_shop['pets']:
        pet_shop['pets'].append(new_pet)


def get_customer_cash(customer):
        return customer['cash']

    
def remove_customer_cash(customer, cash):
    customer['cash'] -= cash


def get_customer_pet_count(customer):
    return len(customer['pets'])


def add_pet_to_customer(customer, pet):
    customer['pets'].append(pet)


def customer_can_afford_pet(customer, pet):
    return customer['cash'] >= pet['price']

    


def sell_pet_to_customer(pet_shop, pet, customer):
    if customer_can_afford_pet(customer, pet):
        remove_customer_cash(customer, pet['price'])
        remove_pet_by_name(pet_shop, pet)
        add_pet_to_customer(customer, pet)
        pet_shop['admin']['total_cash'] += pet['price']
        pet_shop['admin']['pets_sold'] += 1
        

