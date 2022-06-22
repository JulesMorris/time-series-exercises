import os
import requests
import pandas as pd

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_store_data_from_api():    
    #extract multiple pages while loop
    #base 
    domain = 'https://python.zgulde.net'

    #where url is leading
    endpoint = '/api/v1/stores'

    #create empty list

    stores = []

    while True:
        #create url variable
        url = domain + endpoint
        #get url
        response = requests.get(url)
        #create a dict from response
        data = response.json()
        #use print response
        print(f'\rGetting page {data["payload"]["page"]} of {data["payload"]["max_page"]}: {url}', end = '')
        #add each page to empty list
        stores.extend(data['payload']['stores'])
        #update endpoint to cycle through pages
        endpoint = data['payload']['next_page']
        #once there are no empty pages, break
        if endpoint is None:
            break

    return stores

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_store_data_from_api2():
    response = requests.get('https://api.data.codeup.com/api/v1/stores')
    data = response.json()
    stores = pd.DataFrame(data['payload']['stores'])
    stores = pd.DataFrame(stores)
    return stores

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_items_data_from_api():
    #extract multiple pages while loop

    #base 
    domain = 'https://python.zgulde.net'

    #where url is leading
    endpoint = '/api/v1/items'

    #create empty list

    items = []

    while True:
        #create url variable
        url = domain + endpoint
        #get url
        response = requests.get(url)
        #create a dict from response
        data = response.json()
        #use print response
        print(f'\rGetting page {data["payload"]["page"]} of {data["payload"]["max_page"]}: {url}', end = '')
        #add each page to empty list
        items.extend(data['payload']['items'])
        #update endpoint to cycle through pages
        endpoint = data['payload']['next_page']
        #once there are no empty pages, break
        if endpoint is None:
            break

    return items

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_items_data_from_api2():
    domain = 'https://api.data.codeup.com'
    endpoint = '/api/v1/items'
    items = []
    while True:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        print(f'\rGetting page {data["payload"]["page"]} of {data["payload"]["max_page"]}: {url}', end='')
        items.extend(data['payload']['items'])
        endpoint = data['payload']['next_page']
        if endpoint is None:
            break
    items = pd.DataFrame(items)
    return items    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_sales_data_from_api():
    #base 
    domain = 'https://python.zgulde.net'

    #where url is leading
    endpoint = '/api/v1/sales'

    #create empty list

    sales = []

    while True:
        #create url variable
        url = domain + endpoint
        #get url
        response = requests.get(url)
        #create a dict from response
        data = response.json()
        #use print response
        print(f'\rGetting page {data["payload"]["page"]} of {data["payload"]["max_page"]}: {url}', end = '')
        #add each page to empty list
        sales.extend(data['payload']['sales'])
        #update endpoint to cycle through pages
        endpoint = data['payload']['next_page']
        #once there are no empty pages, break
        if endpoint is None:
            break

    return sales


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_stores_data():
    if os.path.exists('stores.csv'):
        return pd.read_csv('stores.csv')
    df = get_store_data_from_api()
    df.to_csv('stores.csv', index = False)
    return df

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    

def get_items_data():
    if os.path.exists('items.csv'):
        return pd.read_csv('items.csv')
    df = get_items_data_from_api()
    df.to_csv('items.csv', index = False)
    return df
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_sales_data():
    if os.path.exists('sales.csv'):
        return pd.read_csv('sales.csv')
    df = get_sales_data_from_api()
    df.to_csv('sales.csv', index = False)
    return df

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_store_item_demand_data():
    sales = get_sales_data()
    stores = get_stores_data()
    items = get_items_data()

    sales = sales.rename(columns = {'store': 'store_id', 'item': 'item_id'})
    df = pd.merge(sales, stores, how = 'left', on = 'store_id')
    df = pd.merge(df, items, how = 'left', on = 'item_id')

    return df
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_opsd_data():
    if os.path.exists('opsd.csv'):
        return pd.read_csv('opsd.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    df.to_csv('opsd.csv', index = False)
    return df