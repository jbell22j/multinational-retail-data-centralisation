import pandas as pd


class DataCleaning():
     
     '''
    This class is used for cleaning of our dataframes.

    Attributes:
        N/A
     '''
    
    
     def clean_user_data(self,dataframe):
        '''
        This function is to clean the data from the user dataframe.
        Cleaning includes :
            - Checking formatting errors in datetime columns.
            - Dropping null values.
            - Dropping duplicate columns except for the first occurence.
            - Checking email address formatting.
            - Checking country code and user uuid are the correct length.
            - Removing any invalid non-numerical characters from phone number.
            - Correcting capitalisation issues.

        Parameters:
            dataframe (pandas.core.frame.DataFrame)

        Returns:
        -------
        New dataframe following the data cleaning process. (pandas.core.frame.DataFrame)
        '''
        df = dataframe.dropna(how = 'any')
        df['date_of_birth'] = df['date_of_birth'].values.astype(str)
        df['join_date'] = df['join_date'].values.astype(str)
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'],format='mixed',errors='ignore')
        df['join_date'] = pd.to_datetime(df['join_date'],format='mixed',errors='ignore')
        df = df.drop_duplicates()
        df['email_address'] = df['email_address'].str.lower()
        df['country_code'] = df['country_code'].str.upper()
        df['address'] = df['address'].str.title()
        df['first_name'] = df['first_name'].str.title()
        df['last_name'] = df['last_name'].str.title()
        df['country_code'] = df.country_code.str.replace('GGB', 'GB')
        df = df[df['user_uuid'].str.len() == 36]
        df = df[df['country_code'].str.len() == 2]
        df = df[df['email_address'].str.contains('@')]
        df['phone_number'] = df.phone_number.str.replace('\.', '')
        df['phone_number'] = df.phone_number.str.replace('x', '')
        df['phone_number'] = df.phone_number.str.replace('X', '')
        df = df.dropna(how = 'any')
        return df
    
     def clean_card_data(self,dataframe):
        '''
        This function is to clean the data from the card dataframe.
        Cleaning includes :
            - Checking formatting errors in datetime columns.
            - Dropping null values.
            - Dropping duplicate columns except for the first occurence.
            - Checking expiry date and card number are the correct length.

        Parameters:
            dataframe (pandas.core.frame.DataFrame)

        Returns:
        -------
        New dataframe following the data cleaning process. (pandas.core.frame.DataFrame)
        '''
        df = dataframe.dropna(how = 'any')
        df = df.drop_duplicates(subset=['card_number'])
        df['card_number'] = df.card_number.str.replace('?', '')
        df['date_payment_confirmed'] = pd.to_datetime(df['date_payment_confirmed'], format='mixed',errors='ignore')
        df = df[df['expiry_date'].astype(str).str.len() < 6]
        df = df[df['card_number'].astype(str).str.isnumeric()]
        df = df[df['card_number'].astype(str).str.len() < 20]
        return df
    
     def clean_store_data(self,dataframe):
        '''
        This function is to clean the data from the store dataframe.
        Cleaning includes :
            - Checking formatting errors in datetime columns.
            - Dropping null values.
            - Dropping duplicate columns except for the first occurence.
            - Checking email address formatting.
            - Checking country code is the correct length.
            - Removing any invalid non-numerical characters from staff numbers column.
            - Correcting capitalisation issues.

        Parameters:
            dataframe (pandas.core.frame.DataFrame)

        Returns:
        -------
        New dataframe following the data cleaning process. (pandas.core.frame.DataFrame)
        '''
        df = dataframe.dropna(thresh = 7)
        df = df.drop_duplicates()
        df['address']=df['address'].str.title()
        df['continent']=df['continent'].str.title()
        df['country_code'] = df['country_code'].str.upper()
        df['opening_date'] = df['opening_date'].values.astype(str)
        df['staff_numbers'] = pd.to_numeric(df.staff_numbers.str.replace('[^\d.]', ''), errors='coerce')
        df['opening_date'] = pd.to_datetime(df['opening_date'],format='mixed',errors='coerce')
        df = df[df['country_code'].str.len() == 2]
        return df
    
     def convert_product_weights(self,products_dataframe):
        '''
        This function is to convert the weights from the products dataframe all into kg.

        Parameters:
            dataframe (pandas.core.frame.DataFrame)

        Returns:
        -------
        New dataframe following the weight column conversion process. (pandas.core.frame.DataFrame)
        '''
        units = {'g': 0.001, 'ml':0.001, 'kg': 1}
        df = products_dataframe.copy()
        df['numbers'] = df['weight'].str.extract('^([-\d\.,\s]+)').astype(float)
        df['unit'] = df['weight'].str.extract(f'({"|".join(units)})', expand=False)
        df['map'] = df['unit'].map(units).fillna(1)
        df['weight'] = df['numbers'].mul(df['map'])
        products_dataframe['weight'] = df['weight']
        return products_dataframe
    
     def clean_products_data(self,products_dataframe):
        '''
        This function is to clean the data from the products dataframe.
        Cleaning includes :
            - Checking formatting errors in datetime columns.
            - Dropping null values.
            - Dropping duplicate columns except for the first occurence.
            - Checking EAN and uuid are the correct length.
            - Removing any invalid non-numerical characters from phone number.
            - Correcting capitalisation and spelling errors.

        Parameters:
            dataframe (pandas.core.frame.DataFrame)

        Returns:
        -------
        New dataframe following the data cleaning process. (pandas.core.frame.DataFrame)
        '''
        df = products_dataframe.copy()
        df = df.dropna(how = 'any')
        df = df[df.EAN.astype(str).apply(lambda x: len(x) > 5 )]
        df['date_added'] = pd.to_datetime(df['date_added'],format='mixed',errors='ignore')
        df['product_name']=df['product_name'].str.title()
        df['removed']=df['removed'].str.replace('Still_avaliable','Available')
        df = df[df['uuid'].astype(str).str.len() == 36]
        df = df.dropna(how = 'any')
        return df
    
     def clean_orders_data(self,orders_dataframe):
        '''
        This function is to clean the data from the orders dataframe.
        Cleaning includes :
            - Dropping unnecessary columns.
            - Dropping null values.
            - Dropping duplicate columns except for the first occurence.
            - Checking date_uuid and user uuid are the correct length.
            - Checking product quantity column only contains numerical values.

        Parameters:
            dataframe (pandas.core.frame.DataFrame)

        Returns:
        -------
        New dataframe following the data cleaning process. (pandas.core.frame.DataFrame)
        '''
        df = orders_dataframe.copy()
        df = df.drop(['level_0'],axis=1)
        df = df.drop(['1'],axis=1)
        df = df.drop(['first_name'],axis=1)
        df = df.drop(['last_name'],axis=1)
        df = df.drop_duplicates()
        df = df.dropna()
        df = df[df.product_quantity.astype(str).str.isnumeric()]
        df = df[df['date_uuid'].str.len() == 36]
        df = df[df['user_uuid'].str.len() == 36]
        return df
    
     def clean_date_data(self,date_dataframe):
        '''
        This function is to clean the data from the orders dataframe.
        Cleaning includes :
            - Dropping null values.
            - Checking date_uuid and year columns are the correct length.

        Parameters:
            dataframe (pandas.core.frame.DataFrame)

        Returns:
        -------
        New dataframe following the data cleaning process. (pandas.core.frame.DataFrame)
        '''
        df = date_dataframe.copy()
        df = df.dropna(how = 'any')
        df = df[df['year'].str.len() == 4]
        df['time_period']=df['time_period'].str.replace('_',' ')
        df = df[df['date_uuid'].str.len() == 36]
        return df