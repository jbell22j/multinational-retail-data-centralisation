# multinational-retail-data-centralisation

## Table of Contents

- [Project Brief](#brief)
- [Project Dependencies](#depend)
- [Tools Utilised](#tools)
- [Instructions](#instruct)
- [File Structure](#structure)

<a id="brief"></a>
## Project Brief
The project aim was to create a multinational retail sales database using data extracted from different locations including SQL, AWS (s3-bucket), pdf weblinks and API. Extracting the information using python functions to transform the data into pandas dataframes. Data cleaning functions to be implemented to clean each dataframe individually where necessary, including removing missing values or unnecessary columns, incorrectly inputted values to be fixed (length,invalid characters) and datetime data to be formatted correctly. Once cleaned the dataframes can be uploaded to SQL to create a database, datatypes can then be correctly formatted, further data cleaning where necessary in SQL as well as setting primary and foreign keys to create a star-based schema linking the dataframes to allow for analysis in SQL.

<a id="depend"></a>
## Project Dependencies

In order to run this project, the following modules need to be installed:

* `sqlalchemy`
* `pandas`
* `requests`
* `tabula-py`
* `PyYAML`

It's important to mention that the pipeline cannot function as it is without access to the AWS credentials or API key. However, modifications to API endpoints will allow the DatabaseConnector and DataExtractor classes to operate successfully with alternative data sources.

 <a id="tools"></a>
## Tools Utilised



 <a id="instruct"></a>
## Instructions

- The functions implemented can be used to replicate the retail sales database in your own SQL, or can be used to create your own database from pdf weblinks, files in s3-buckets using AWS, an API or SQL dataframes.

 <a id="structure"></a>
## File Structure

The files data_cleaning.py, data_extraction.py and database_utils.py contain the functions to create a database in your SQL. The sql_files folder contains the SQL queries used to query the retail sales database but could also provide insight to query your own database.
