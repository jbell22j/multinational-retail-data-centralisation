import pandas as pd
import tabula
import requests
import json

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
        return response
    
    def retrieve_stores_data(self,api_endpoint,header):
        results = {}
        for store in range(1,3):
            res = requests.get(api_endpoint.format(store),header)
            if res.status_code == 200:
                results.append(res.json())
            else: 
                print("Request to {} failed.".format(store))
        print(results)
        return results
        

        

