# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(name):
    return name['name']


def get_total_cash(customers):
    return customers['admin']['total_cash']


def add_or_remove_cash(customers ,amount):
    customers['admin']['total_cash'] += amount

    return customers['admin']['total_cash']


def get_pets_sold(lst):
    return lst['admin']['pets_sold']


def increase_pets_sold(lst, pets_sold):
    lst['admin']['pets_sold'] += pets_sold
    
    return lst['admin']['pets_sold']


def get_stock_count(lst):
    stock = 0 + len(lst['pets'])
    return stock


# def get_pets_by_breed(pets_list, breed):
#     x = []
#     for pet in pets_list:
       ????????????