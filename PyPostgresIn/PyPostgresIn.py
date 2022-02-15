import datetime
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
def sql_insert(connection, tab,data):
    num_data = []
    for i in range(0, len(data)):
        num_data.append(data[i][2])
    try:
        val = ' VALUES (%s'
        for i in range(1, len(num_data)):
            val = val + ',%s'
        val = val + ')'
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor.execute("INSERT into "+tab+val,(num_data))
        connection.commit()
    except (Exception, Error) as error:
        if str.find(str(error),'отношение '+tab+' не существует'):
            create_table(connection, tab, data)
            sql_insert(connection, tab, data)
        else:
            print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
def create_table(connection, tab, data):
    name_data = []
    type_data = []
    s =''
    for i in range(0, len(data)):
        name_data.append(data[i][0])
        type_data.append(data[i][1])
        s = s + str(data[i][0]) +' '+ str(data[i][1]) + ', '
    s = '(' + s[:len(s)-2] + ');'
    try:
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE "+tab+ s)
        connection.commit()
    except (Exception, Error) as error:
        print(error)
def name(x, l):
    s = ([n for n in l if id(l[n]) == id(x)])
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
def get_all(l, *data):
    a = []
    for i in range(0, len(data)):
        a.append((name(data[i], l), name_type(data[i]), data[i]))
    return a
#main.sql_insert(connection, table_name, main.get_all(locals(), New_date, New_str, New_int, New_bool))
#Выгразука даты в таблицу
#Пока поддерживаются только типы int, bool, date, str, float!
#sql_insert(connection, table_name, get_all(New_date, New_str, New_int, New_bool))
