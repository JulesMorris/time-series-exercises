
import pandas as pd

def prep_store(df):
    #remove last 13 characters of sale_date
    df.sale_date = df.sale_date.apply(lambda date: date[:-13])
    
    #convert sale_date to datetime format
    df.sale_date = pd.to_datetime(df.sale_date, format = '%a, %d %b %Y')
    
    #set sale_date as index, sort index
    df = df.set_index('sale_date').sort_index()
    
    #rename sale_amount to quantity
    df = df.rename(columns = {'sale_amount': 'quantity'})
    
    #add month column
    df['month'] = df.index.month
    
    #add day of week column
    df['weekday'] = df.index.day_name()
    
    #add sales_total column
    df['sales_total'] = df.quantity * df.item_price
    
    return df


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def prep_opsd(df):
    #remove '+' and make all columns lowercase
    df.columns = [column.replace('+','_').lower() for column in df]
    
    #convert date column to  datetime format
    df.date = pd.to_datetime(df.date, format = '%Y %m %d')
    
    #set date as index, sort index
    df = df.set_index('date').sort_index()
    
    #create month column
    df['month'] = df.index.month
    
    #create year column
    df['year'] = df.index.year

    #fill null values w/ 0
    df = df.fillna(0)
    
    #add values of wind and solar together to get wind_solar
    df['wind_solar'] = df.wind + df.solar
    
    return df