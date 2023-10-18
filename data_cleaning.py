import numpy as np
import pandas as pd
from datetime import datetime

class DataCleaning():
    
    def clean_user_data(self,dataframe):
        df = dataframe.dropna(how = 'any')
        df['date_of_birth'] = df['date_of_birth'].values.astype(str)
        df['join_date'] = df['join_date'].values.astype(str)
        df['date_of_birth'] = pd.to_datetime(df['join_date'],format='mixed',errors='coerce')
        df['join_date'] = pd.to_datetime(df['join_date'],format='mixed',errors='coerce')
        df = df.drop_duplicates()
        df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        df['email_address'] = df['email_address'].str.lower()
        df['country_code'] = df['country_code'].str.upper()
        df['address'] = df['address'].str.title()
        df['first_name'] = df['last_name'].str.title()
        df = df[~df['phone_number'].str.contains('X')]
        df = df[~df['phone_number'].str.contains('.')]
        df = df.dropna(how = 'any')
        return df
    
    def clean_card_data(self,dataframe):
        df = dataframe.dropna(how = 'any')
        df = df.drop_duplicates()
        df[df['card_number'].filter(like='0123456789')]
        df['date_payment_confirmed'] = pd.to_datetime(df['date_payment_confirmed'],format='mixed',errors='coerce')
        df = df.dropna(how = 'any')
        return df
    
    def clean_store_data(self,dataframe):
        df = dataframe.dropna(thresh = 7)
        df = df.drop(['lat'],axis=1)
        df = df.drop_duplicates()
        df['address']=df['address'].str.title()
        df['continent']=df['continent'].str.title()
        df['country_code'] = df['country_code'].str.upper()
        df['opening_date'] = df['opening_date'].values.astype(str)
        df['opening_date'] = pd.to_datetime(df['opening_date'],format='mixed',errors='coerce')
        df = df[df['country_code'].str.len() == 2]
        return df
    
    def convert_product_weights(self,products_dataframe):
        units = {'g': 0.001, 'ml':0.001, 'kg': 1}
        df = products_dataframe.copy()
        df['numbers'] = df['weight'].str.extract('^([-\d\.,\s]+)').astype(float)
        print(df['numbers'])
        df['unit'] = df['weight'].str.extract(f'({"|".join(units)})', expand=False)
        df['map'] = df['unit'].map(units).fillna(1)
        df['weight'] = df['numbers'].mul(df['map'])
        products_dataframe['weight'] = df['weight']
        return products_dataframe
    
    def clean_products_data(self,products_dataframe):
        df = products_dataframe.dropna(how = 'any')
        df.EAN=df.EAN.apply(lambda x: x if len(x)== 13 else np.nan)
        df['date_added'] = pd.to_datetime(df['date_added'],format='mixed',errors='coerce')
        df['product_name']=df['product_name'].str.title()
        df['removed']=df['removed'].str.replace('Still_avaliable','Available')
        df = df.dropna(how = 'any')
        return df
    
    def clean_orders_data(self,orders_dataframe):
        df = orders_dataframe.copy()
        df = df.drop(['level_0'],axis=1)
        df = df.drop(['1'],axis=1)
        df = df.drop(['first_name'],axis=1)
        df = df.drop(['last_name'],axis=1)
        return df
    
    def clean_date_data(self,date_dataframe):
        df = date_dataframe.copy()
        df = df.dropna(how = 'any')
        df['time_period']=df['time_period'].str.replace('_',' ')
        return df