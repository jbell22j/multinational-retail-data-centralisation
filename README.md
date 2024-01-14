# multinational-retail-data-centralisation

## Table of Contents

- [Project Brief](#brief)
- [Project Dependencies](#depend)
- [Tools Utilised](#tools)
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

<a id="structure"></a>
## File Structure

The project consists of three main classes:
* `DataCleaning` in `data_cleaning.py` - contains methods for cleaning individual pandas dataframes.

<img width="427" alt="image" src="https://github.com/jbell22j/multinational-retail-data-centralisation/assets/141024595/ee4cb94e-e1aa-40ad-9431-a162db6e1810">

* `DataExtractor` in `data_extraction.py` - contains methods to extract data from various sources.

<img width="424" alt="image" src="https://github.com/jbell22j/multinational-retail-data-centralisation/assets/141024595/d37c04b5-b1b2-47eb-906f-4f8bf3ec7f5e">

* `DatabaseConnector` in `database_utils.py` - contains methods to connect and upload to SQL databases.
Together these contain the functions to create a database in SQL.

The sql_files folder contains the SQL queries used to query and alter the retail sales database. `total_staff_per_country.sql` is an example of a querying SQL file and `altering_dim_store_details_column_datatypes.sql` is an example of an SQL file that alters the SQL database.
