import pandas as pd
import tabula
import requests
import boto3

class DataExtractor:

    '''
    This class is used for extraction of our data from different sources.

    Attributes:
        N/A
    '''
    
    def read_rds_table(self,table_name,engine):
        '''
        This function extracts a SQL database table to a pandas dataframe.

        Parameters:
            table_name (str)
            engine (sqlalchemy.engine.base.Engine)

        Returns:
        -------
        Dataframe (pandas.core.frame.DataFrame)
        '''
        df = pd.read_sql_table(table_name,engine,index_col='index')
        return df
    
    def retrieve_pdf_data(self,link):
        '''
        This function extracts a data from a pdf to a pandas database, also saving the data in a csv file locally.

        Parameters:
            link (str)

        Returns:
        -------
        Dataframe (pandas.core.frame.DataFrame)
        '''
        tabula.convert_into(link,"output.csv",output_format="csv",pages='all')
        df = pd.read_csv("output.csv")
        return df
    
    def list_number_of_stores(self,api_endpoint,header):
        '''
        This function prints the number of stores in our database using API get method.

        Parameters:
            api_endpoint (str)
            header (dict)

        Returns:
        -------
        None
        '''
        response = requests.get(api_endpoint, headers=header)
        res = response.json()
        print(res)
    
    def retrieve_stores_data(self,api_endpoint,header):
        '''
        This function using API get method returns pandas dataframe.

        Parameters:
            api_endpoint (str)
            header (dict)

        Returns:
        -------
        Dataframe (pandas.core.frame.DataFrame)
        '''
        results = []
        for store_number in range(0,100):
            res = requests.get(api_endpoint.format(store_number),headers=header)
            if res.status_code == 200:
                results.append(res.json())
            else: 
                print("Request to {} failed.".format(store_number))
        df = pd.DataFrame.from_dict(results)
        df=df.set_index('index')
        return df
    
    def extract_from_s3(self,bucket,filename,localfilename):
        '''
        This function downloads file from an s3 bucket using AWS and converts it into a pandas dataframe, also saves the file locally.

        Parameters:
            bucket (str)
            filename (str)
            localfilename (str)

        Returns:
        -------
        Dataframe (pandas.core.frame.DataFrame)
        '''
        s3 = boto3.resource('s3')
        s3.Bucket(bucket).download_file(filename,localfilename)
        if '.json' in filename:
            df = pd.read_json(localfilename)
        else:
            df = pd.read_csv(localfilename,index_col=0)
        return df
        

        

