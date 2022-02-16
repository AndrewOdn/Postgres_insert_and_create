<h1>PyPostgresIn</h1>

This library is  needed to **quickly start** working with **Postgres** in python. The library provides the ability to skip creating **SQL queries** and simply load data into an existing table, or create table and load data into it while saving **data types**, all in one **line** of code

<h2>Prerequirements</h2>

- Python >= **3.6**
- PostgreSQL server >= **7.4**
- PostgreSQL client library >= **9.1**
<h2>Installation</h2>

```
pip install -i https://test.pypi.org/simple/ PyPostgresIn==0.0.31
```
```
pip install -r requirements.txt
```
<h2>Examples</h2>
This is a short example showing how to use PyPostgresIn

```
import datetime
import psycopg2
from PyPostgresIn import PyPostgresIn  # import lib

connection = psycopg2.connect(user="postgres",  # just use your connection info
                              password="admin",
                              host="127.0.0.1",
                              port="5432",
                              database="planes")
# IMPORTANT!! If table not exist, then the names of the variables will become the names of the columns 
# (WARNING:Don't forget to name variables correctly) and they will receive the types of the variables
# (Supported types: float as float8, str as text, int as int8, datetime as timestamp, bool as bool) 
table_name = 'Falcon_8'
icao24 = 17356
time_position = datetime.datetime.now()
on_ground = False
origin_country = 'Russia'
velocity = 1234.56

PyPostgresIn.sql_insert(connection, table_name,  # Your connection and table_name variables
                        PyPostgresIn.get_all(locals(),
                                             # Any dictionary that containing the current scope's and name of 
                                             # variables like global() WARNING!! Make sure that there are no extra 
                                             # variables in the dictionary with the same values as the transferred variables 
                                             icao24, origin_country, time_position, on_ground,
                                             velocity))  # Any count of your variables to table


```
<h3>Release not stable and constantly updated, follow to get the latest releases
<h3>https://github.com/AndrewOdn/PyPostgresIn
<h3>https://test.pypi.org/project/PyPostgresIn/
