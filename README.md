# multinational-retail-data-centralisation

## Table of Contents

- [Project Brief](#brief)
- [Project Dependencies](#depend)
- [Tools Utilised](#tools)
- [Local Database Setup](#database)
- [Connecting to Local Database using pgAdmin](#connect)
- [File Structure](#structure)

<a id="brief"></a>
## Project Brief
You work for a multinational company that sells various goods across the globe. Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.
In an effort to become more data-driven, your organisation would like to make its sales data accessible from one centralised location. Your first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data. You will then query the database to get up-to-date metrics for the business. 🌎

The different data sources that need to be extracted from and collected together are:

* two tables of an SQL database hosted on AWS RDS
* one table stored as a .pdf file hosted on AWS S3
* one table stored as a .csv file hosted on AWS S3
* one table stored as a .json file hosted on AWD S3
* a series of JSON objects available via an API

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
### SQLAlchemy
[SQL Alchemy](https://www.sqlalchemy.org/) was used to connect to the local SQL and AWS databases in `database_utils.py`.

### pandas
[pandas](https://pandas.pydata.org/) is an open source data analysis and manipulation built ontop of Python.

### PyYAML
[PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation) was used to read the YAML files where the credentials for the databases are stored and load the contents into dictionaries.

### Tabula
[Tabula](https://tabula-py.readthedocs.io/en/latest/#) is a tool used to read tables from pdf files and convert them to a pandas dataframe or CSV/JSON/TSV file.

### Requests
[Requests](https://pypi.org/project/requests/) is used to make HTTPS GET requests to connect to API endpoints.

<a id="database"></a>
## Local Database Setup

A local Postgres database was set up to receive the cleaned data from the different sources. Postgres was installed globally using Homebrew:
`brew install postgresql@14`

The local database was created using the following command in the terminal:
`initdb -D db -U postgres -W`
where `db` is the directory containing the database files and postgres is the database username. The `-W` flag indicates that the database will be password protected and the user is prompted to enter the password upon running this command.

The database can be started using:
`postgres -D db`

<a id="connect"></a>
## Connecting to Local Database using pgAdmin

pgAdmin is used to connect to the local database. With pgAdmin installed and running, follow these steps to connect:

* On the main application page, click on 'Add New Server'.
* On the 'General' tab of the dialogue that appears, enter a name for the new server connection.
* On the 'Connection' tab, enter 'localhost' for the 'Host name/address', and enter the username and password specified when creating the database.
* Click 'Save' to save the server and connect to the database.

<a id="structure"></a>
## File Structure

The project consists of three main classes:
* `DataCleaning` in `data_cleaning.py` - contains methods for cleaning individual pandas dataframes.

<img width="576" alt="image" src="https://github.com/jbell22j/multinational-retail-data-centralisation/assets/141024595/f471753d-39be-416e-9ca4-32b27d5cd4b4">


* `DataExtractor` in `data_extraction.py` - contains methods to extract data from various sources.

<img width="424" alt="image" src="https://github.com/jbell22j/multinational-retail-data-centralisation/assets/141024595/d37c04b5-b1b2-47eb-906f-4f8bf3ec7f5e">

* `DatabaseConnector` in `database_utils.py` - contains methods to connect and upload to SQL databases.
Together these contain the functions to create a database in SQL.

<img width="512" alt="image" src="https://github.com/jbell22j/multinational-retail-data-centralisation/assets/141024595/7226458f-9c40-460f-ab97-dd5c2a20c762">

The sql_files folder contains the SQL queries used to query and alter the retail sales database. `total_staff_per_country.sql` is an example of a querying SQL file and `altering_dim_store_details_column_datatypes.sql` is an example of an SQL file that alters the SQL database.

<img width="395" alt="image" src="https://github.com/jbell22j/multinational-retail-data-centralisation/assets/141024595/dc3e9000-0b9f-4506-8f4c-02e8751a076d">
