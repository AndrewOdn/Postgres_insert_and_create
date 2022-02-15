import requests
from pprint import pprint
import json
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
class Sql_execute:
    def insert(tab,*data):
        try:
            val = ' VALUES (%s'
            for i in range(1, len(data)):
                val = val + ',%s'
            val = val + ')'
            connection = psycopg2.connect(user="postgres",
                                          # пароль, который указали при установке PostgreSQL
                                          password="admin",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="planes")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            # Курсор для выполнения операций с базой данных
            cursor = connection.cursor()
            connection.commit()
            cursor.execute("INSERT into "+tab+val,(data))
            connection.commit()
        except (Exception, Error) as error:
            asd = 0
        finally:
            if connection:
                cursor.close()
                connection.close()
url='http://api.currencylayer.com/live?access_key=9d7e137207a064104c5a4010abcae9cd'
r = requests.get(url)
try:
    b = json.loads(r.text)
    usdrub = b['quotes']['USDRUB']
    usdeur = b['quotes']['USDEUR']
    eurrub = float(usdrub)/float(usdeur)
    time = b['timestamp']
    
except Exception as ess:
    print(ess)