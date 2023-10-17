import yaml
from sqlalchemy import inspect
from sqlalchemy import create_engine
import data_extraction 
import data_cleaning
import pandas as pd

class DatabaseConnector:

    def __init__(self,yamlfile):
        self.yamlfile = yamlfile

    def read_db_creds(self):
        with open (self.yamlfile, 'r') as f:
            yamldict = yaml.load(f, Loader=yaml.FullLoader)
        return yamldict
    
    def init_db_engine(self,initialised_credentials):
        engine = create_engine(f"postgresql+psycopg2://{initialised_credentials['USER']}:{initialised_credentials['PASSWORD']}@{initialised_credentials['HOST']}:{initialised_credentials['PORT']}/{initialised_credentials['DATABASE']}")
        engine.execution_options(isolation_level='AUTOCOMMIT').connect()
        return engine
    
    def list_db_tables(self,initialised_engine):
        inspector = inspect(initialised_engine)
        for table_name in inspector.get_table_names():
            print("Table: %s" % table_name)
            for column in inspector.get_columns(table_name):
                print("Column: %s" % column['name'])

    def upload_to_db(self,dataframe,table_name,engine):
        with engine.connect() as connection:
            dataframe.to_sql(table_name,connection,index=False, method=None,if_exists='replace')

'''
The following block of code gets the credentials of the AWS database stored in the cloud and extracts the user data table, cleans the data and then uploads it into our sales data database in PostgreSQL. 
'''

main_instance = DatabaseConnector('db_creds.yaml')
rds_database_credentials = main_instance.read_db_creds()
rds_database_engine = main_instance.init_db_engine(rds_database_credentials)
#main_instance.list_db_tables(rds_database_engine)
extract = data_extraction.DataExtractor()
#user_df = extract.read_rds_table('legacy_users',rds_database_engine)
clean_data = data_cleaning.DataCleaning()
#clean_user_df = clean_data.clean_user_data(user_df)


#card_df = extract.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')
#clean_card_df = clean_data.clean_card_data(card_df)

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "x-api-key" : 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
url = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
number_of_stores = extract.list_number_of_stores(url,header)
#Number Of Stores =  200

stores_data = extract.retrieve_stores_data("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}",header)

'''The following block of code adds the cleaned user and card dataframes to our SQL sales_data database.'''

#my_sql_instance = DatabaseConnector('mysql_creds.yaml')
#my_sql_instance_dict = my_sql_instance.read_db_creds()
#my_sql_instance_engine = my_sql_instance.init_db_engine(my_sql_instance_dict)
#my_sql_instance.upload_to_db(clean_user_df,'dim_users',my_sql_instance_engine)
#my_sql_instance.upload_to_db(clean_card_df,'dim_card_details',my_sql_instance_engine)




