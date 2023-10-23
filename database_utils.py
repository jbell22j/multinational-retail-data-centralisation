import yaml
from sqlalchemy import inspect
from sqlalchemy import create_engine
import data_extraction 
import data_cleaning

class DatabaseConnector:
    '''
    This class is used to connect to SQL to upload data.

    Attributes:
        yamlfile (str) : yaml file containing credentials to connect to SQL.
    '''

    def __init__(self,yamlfile):
        '''
        See help(DatabaseConnector) for accurate signature.
        '''
        self.yamlfile = yamlfile

    def read_db_creds(self):
        '''
        This function is returns a dictionary from the yaml credentials file.

        Parameters:
        
        None

        Returns:
        -------
        yamldict (dict) 
        '''
        with open (self.yamlfile, 'r') as f:
            yamldict = yaml.load(f, Loader=yaml.FullLoader)
        return yamldict
    
    def init_db_engine(self,initialised_credentials):
        '''
        This function initialises an engine to connect to databases.

        Parameters:
            initialised_credentials (dict) : dictionary contained credentials to allow for database connection.

        Returns:
        -------
        engine (sqlalchemy.engine.base.Engine)
        '''
        engine = create_engine(f"postgresql+psycopg2://{initialised_credentials['USER']}:{initialised_credentials['PASSWORD']}@{initialised_credentials['HOST']}:{initialised_credentials['PORT']}/{initialised_credentials['DATABASE']}")
        engine.execution_options(isolation_level='AUTOCOMMIT').connect()
        return engine
    
    def list_db_tables(self,initialised_engine):
        '''
        This function prints a list of the tables and column names in a database.

        Parameters:
            engine (sqlalchemy.engine.base.Engine)

        Returns:
        -------
        None
        '''
        inspector = inspect(initialised_engine)
        for table_name in inspector.get_table_names():
            print("Table: %s" % table_name)
            for column in inspector.get_columns(table_name):
                print("Column: %s" % column['name'])

    def upload_to_db(self,dataframe,table_name,engine):
        '''
        This function uploads a dataframe to our chosen database.

        Parameters:
            dataframe (pandas.core.frame.DataFrame) 
            table_name (str) : the desired table name of this dataframe when uploaded to the database.
            engine (sqlalchemy.engine.base.Engine)

        Returns:
        -------
        None
        '''
        with engine.connect() as connection:
            dataframe.to_sql(table_name,connection,index=False, method=None,if_exists='replace')


if __name__ == "__main__":

    '''
    The following code uses all methods from our classes to extract, clean and upload all required dataframes
    to our SQL database.
    '''

    main_instance = DatabaseConnector('db_creds.yaml')
    rds_database_credentials = main_instance.read_db_creds()
    rds_database_engine = main_instance.init_db_engine(rds_database_credentials)
    main_instance.list_db_tables(rds_database_engine)

    extract = data_extraction.DataExtractor()
    clean_data = data_cleaning.DataCleaning()

    user_df = extract.read_rds_table('legacy_users',rds_database_engine)
    clean_user_df = clean_data.clean_user_data(user_df)


    orders_df = extract.read_rds_table('orders_table',rds_database_engine)
    clean_orders_data = clean_data.clean_orders_data(orders_df)

    card_df = extract.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')
    clean_card_df = clean_data.clean_card_data(card_df)

    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "x-api-key" : 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
    url = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
    number_of_stores = extract.list_number_of_stores(url,header)

    stores_data = extract.retrieve_stores_data("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{}",header)
    clean_stores_data = clean_data.clean_store_data(stores_data)

    products_data = extract.extract_from_s3('data-handling-public','products.csv','local_products.csv')
    products_data_main = clean_data.convert_product_weights(products_data)
    clean_products_data = clean_data.clean_products_data(products_data_main)

    date_details_data = extract.extract_from_s3('data-handling-public','date_details.json','local_date_details.json')
    clean_date_data = clean_data.clean_date_data(date_details_data)

    my_sql_instance = DatabaseConnector('mysql_creds.yaml')
    my_sql_instance_dict = my_sql_instance.read_db_creds()
    my_sql_instance_engine = my_sql_instance.init_db_engine(my_sql_instance_dict)
    my_sql_instance.upload_to_db(clean_user_df,'dim_users',my_sql_instance_engine)
    my_sql_instance.upload_to_db(clean_card_df,'dim_card_details',my_sql_instance_engine)
    my_sql_instance.upload_to_db(clean_stores_data,'dim_store_details',my_sql_instance_engine)
    my_sql_instance.upload_to_db(clean_products_data,'dim_products',my_sql_instance_engine)
    my_sql_instance.upload_to_db(clean_orders_data,'orders_table',my_sql_instance_engine)
    my_sql_instance.upload_to_db(clean_date_data,'dim_date_times',my_sql_instance_engine)