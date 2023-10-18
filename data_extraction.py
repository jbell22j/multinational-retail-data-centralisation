import pandas as pd
import tabula
import requests
import json
import boto3

class DataExtractor:
    
    def read_rds_table(self,table_name,engine):
        df = pd.read_sql_table(table_name,engine,index_col='index')
        return df
    
    def retrieve_pdf_data(self,link):
        tabula.convert_into(link,"output.csv",output_format="csv",pages='all')
        df = pd.read_csv("output.csv")
        return df
    
    def list_number_of_stores(self,api_endpoint,header):
        response = requests.get(api_endpoint, headers=header)
        res = response.json()
        return res
    
    def retrieve_stores_data(self,api_endpoint,header):
        results = []
        for store_number in range(0,451):
            res = requests.get(api_endpoint.format(store_number),headers=header)
            if res.status_code == 200:
                results.append(res.json())
            else: 
                print("Request to {} failed.".format(store_number))
        df = pd.DataFrame.from_dict(results)
        df=df.set_index('index')
        return df
    
    def extract_from_s3(self):
        s3 = boto3.resource('s3')
        s3.Bucket('data-handling-public').download_file('date_details.json','my_local_json.json')
        df = pd.read_json('my_local_json.json')
        return df
        

        
