import requests
from pprint import pprint
import json
import datetime
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
class Sql_execute:
    def insert(tab,data):
        num_data = []
        for i in range(0, len(data)):
            num_data.append(data[i][2])
        try:
            val = ' VALUES (%s'
            for i in range(1, len(num_data)):
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
            cursor.execute("INSERT into "+tab+val,(num_data))
            connection.commit()
        except (Exception, Error) as error:
            if connection:
                cursor.close()
                connection.close()
            if str.find(str(error),'отношение '+tab+' не существует'):
                Sql_execute.create_table(tab, data)
                Sql_execute.insert(tab, data)
            else:
                print(error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    def create_table(tab, data):
        name_data = []
        type_data = []
        s =''
        for i in range(0, len(data)):
            name_data.append(data[i][0])
            type_data.append(data[i][1])
            s = s + str(data[i][0]) +' '+ str(data[i][1]) + ', '
        s = '(' + s[:len(s)-2] + ');'
        try:
            connection = psycopg2.connect(user="postgres",
                                          # пароль, который указали при установке PostgreSQL
                                          password="admin",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="planes")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            # Курсор для выполнения операций с базой данных
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE "+tab+ s)
            connection.commit()
        except (Exception, Error) as error:
            print(error)
        finally:
            if connection:
                cursor.close()
                connection.close()
class Var_input:
    def name(x, g=globals()):
        s = ([n for n in g if id(g[n]) == id(x)])
        return s[0]

    def name_type(x):
        if type(x) is int:
            return 'int8'
        elif type(x) is str:
            return 'text'
        elif type(x) is float:
            return 'float8'
        elif type(x) is datetime.datetime:
            return 'timestamp'
        elif type(x) is bool:
            return 'bool'

    def get_all(*data):
        a = []
        for i in range(0, len(data)):
            a.append((Var_input.name(data[i]), Var_input.name_type(data[i]), data[i]))
        return a

#Твоя дата которая летит в таблицу
New_int = 123
New_bool = False
New_str = 'Обезьяна!'
New_date = datetime.datetime.now()
#Название твоей таблицы
table_name ='rour_table_name'
#Выгразука даты в таблицу
#Пока поддерживаются только типы int, bool, date, str, float!
Sql_execute.insert(table_name,  Var_input.get_all(New_date, New_str, New_int, New_bool))
