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
        df = df.apply(lambda x: x.str.title() if x.dtype == "object" else x) 
        df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        df['email_address'] = df['email_address'].str.lower()
        df['country_code'] = df['country_code'].str.upper()
        df = df[~df['phone_number'].str.contains('X')]
        df = df[~df['phone_number'].str.contains('.')]
        df = df.dropna(how = 'any')
        return df
    
    def clean_card_data(self,dataframe):
        df = dataframe.dropna(how = 'any')
        df = df.drop_duplicates()
        df = df.apply(lambda x: x.str.title() if x.dtype == "object" else x) 
        df[df['card_number'].filter(like='0123456789')]
        df['date_payment_confirmed'] = pd.to_datetime(df['date_payment_confirmed'],format='mixed',errors='coerce')
        df = df.dropna(how = 'any')
        return df