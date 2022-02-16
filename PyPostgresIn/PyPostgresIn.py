import datetime
import sys
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def sql_insert(connection, tab, data):
    """Метод для вставки данных в таблицу

            Input:
                psycopg2.connect(...), table_name, PyPostgresIn.get_all(locals(),data)
            - psycopg2.connect(...) - установка соединения с бд postgres 7.4+

            - table_name - название таблицы куда вставлять или какую создавать

            - locals() - можно заменить на globals() или самому сгенерировать словарь, главное во избежание ошибок - не передавать в словаре лишние переменные

            - data - переменные, расставленные в порядке соответственно столбцам. В первый столбец - первая переменная и тд

            Raises
            ------
            Exception Table_Not_Exist
                Если таблица отсутствует, то выполняется метод create_table, а следом sql_insert
            Exception
                При иной ошибке, вывод ошибки в консоль
    """
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
        cursor.execute("INSERT into " + tab + val, (num_data))
        connection.commit()
    except (Exception, Error) as error:
        if str.find(str(error), 'отношение "' + tab.lower() + '" не существует') != -1:
            create_table(connection, tab, data)
            sql_insert(connection, tab, data)
        else:
            print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()


def create_table(connection, tab, data):
    """Метод для создания таблицы

        Создание таблицы в которой названиями и типами столбов являются названия и типы переменных соответственно

        Note:
            Доступные типы переменных int, str, float, datetime, bool

            Названия переменных обязаны следовать нормам названий столбцов в postgres

        Raises
        ------
            Exception
                При ошибке, вывод ошибки в консоль
    """
    name_data = []
    type_data = []
    s = ''
    for i in range(0, len(data)):
        name_data.append(data[i][0])
        type_data.append(data[i][1])
        s = s + str(data[i][0]) + ' ' + str(data[i][1]) + ', '
    s = '(' + s[:len(s) - 2] + ');'
    try:
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor.execute("CREATE TABLE " + tab + s)
        connection.commit()
    except (Exception, Error) as error:
        print(error)
        sys.exit()
    finally:
        if connection:
            cursor.close()


def name(x, l):
    """Метод для получение имени переменной

        Получение названий переменных по их значениям в local()

        Note:
            Чтобы избежать ошибок, рекомендуется передавать local(), только с нужными переменными

            Названия переменных обязаны следовать нормам названий столбцов в postgres
        Raises
        ------
    """
    s = ([n for n in l if id(l[n]) == id(x)])
    l.pop(s[0], s)
    return s[0]


def name_type(x):
    """Метод для конвертации названий типов питона в типы postgres

        Note:
            Доступные типы переменных питона

            int, str, float, datetime, bool
        Raises
        ------
    """
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
    """Метод обработки данных для метода sql_insert

            Создание tuple из названий, типов и значений переменных

            Note:
                Доступные типы переменных int, str, float, datetime, bool

                Названия переменных обязаны следовать нормам названий столбцов в postgres

            Raises
            ------
    """
    a = []
    for i in range(0, len(data)):
        a.append((name(data[i], l), name_type(data[i]), data[i]))
    return a
# main.sql_insert(connection, table_name, main.get_all(locals(), New_date, New_str, New_int, New_bool))
# Выгразука даты в таблицу
# Пока поддерживаются только типы int, bool, date, str, float!
# sql_insert(connection, table_name, get_all(New_date, New_str, New_int, New_bool))
