import math
from datetime import datetime
# from openpyxl import Workbook
from threading import Thread
from psycopg2 import *
from pickle import dump
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)
# KEY = b'R7OwvbqM-LJ7i3PifwBCRl1pYJMTYZHPghtB9OR-wRA='


def db_connect():

    connection = connect(user=os.environ.get('USER', str),
                         password=os.environ.get('PASSWORD', str),
                         host=os.environ.get('HOST', str),
                         port=os.environ.get('PORT', int),
                         database=os.environ.get('DATABASE_NAME', str))

    return connection


# def encrypt(list):

#     print('key :', Fernet.generate_key())
#     f = Fernet(KEY)
#     for key, value in list.items():
#         print(value)
#         list[key] = f.encrypt(value.encode())

#     return list


def add_many(con, query, datalist):

    cursor = con.cursor()
    cursor.executemany(query, datalist)
    con.commit()


def add(con, query, data):

    try:
        cursor = con.cursor()
        cursor.execute(query, data)
        con.commit()
    except:
        raise


# def create():
#     list = {
#         'count': """ SELECT count(id) FROM attendance """,
#         'exist': """ SELECT * FROM attendance WHERE pin=%s and date_event =%s  ORDER BY id DESC LIMIT 1"""
#     }

#     list = encrypt(list)

#     with open('script.config', 'wb') as config:

#         dump(list, config)


# def load():
#     list = {
#         'count': """ SELECT count(id) FROM attendance """,
#         'exist': """ SELECT * FROM attendance WHERE pin=%s and date_event =%s  ORDER BY id DESC LIMIT 1"""
#     }

#     list = encrypt(list)

#     with open('script.config', 'wb') as config:

#         dump(list, config)

# def get_last(con):
#     query = """ SELECT * FROM attendance ORDER BY id DESC LIMIT 1"""
#     cursor = con.cursor()
#     cursor.execute(query)
#     data = cursor.fetchone()
#     con.commit()
#     return data


def progress(c, t, bar):
    frac = c/t
    fill = round(frac * bar)
    d = '] (Done)' if frac == 1 else ']'
    print('- [{:>3.0%}]'.format(frac), '[', '=' *
          fill + '_' * (bar - fill), d, '\r', end='')  # [{:>7.2%}]


def exists(con, data):

    query = """ SELECT * FROM attendance WHERE pin=%s and date_event =%s  ORDER BY id DESC LIMIT 1"""
    cursor = con.cursor()
    cursor.execute(query, data)
    data = cursor.fetchone()
    con.commit()
    return data != None


def count_attendance(con):

    # query = """ SELECT count(id) FROM attendance """
    query = """ SELECT count(*) FROM attendance where date_event <= (select max(date_event) from attendance)"""
    cursor = con.cursor()
    cursor.execute(query)
    data = cursor.fetchone()
    con.commit()
    return data


def seconds_to_time(seconds_since_2000):

    sec = seconds_since_2000 % 60
    # print('second : ', sec)

    seconds_since_2000 = math.floor(seconds_since_2000 / 60)
    minute = seconds_since_2000 % 60
    # print('minute : ', minute)

    seconds_since_2000 = math.floor(seconds_since_2000 / 60)
    hour = seconds_since_2000 % 24
    # print('hour : ', hour)

    seconds_since_2000 = math.floor(seconds_since_2000 / 24)
    day = (seconds_since_2000 % 31) + 1
    # print('day : ', day)

    seconds_since_2000 = math.floor(seconds_since_2000 / 31)
    month = (seconds_since_2000 % 12) + 1
    # print('month : ', month)

    seconds_since_2000 = math.floor(seconds_since_2000 / 12)
    year = seconds_since_2000 + 2000
    # print('year : ', year)

    date_time_str = f'{year}-{month}-{day} {hour}:{minute}:{sec}'

    return datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')


def save_data(con, data, n):
    # book = Workbook()
    # sheet = book.active
    # datalist = ()

    query = """INSERT INTO attendance(
                card_no, 
                pin, 
                verified, 
                door_id, 
                event_type, 
                status, 
                date_event
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s);"""
    n = n-50 if n > 50 else 0

    # data_length = len(data.decode().split('\r\n'))

    table = enumerate(data.decode().split('\r\n')[n:])

    length = len(data.decode().split('\r\n')[n:])
    for index, line in table:
        data_fields = line.split(',')

        #print(f'index = {index}', end='', flush=True)
        # print(f'index = {index}', " => data_length ! ", data_length, " => n = ",
        #       n, "=> B = ", before, " data_length  - n =", len(data.decode().split('\r\n')[n:]))
        # row = index + 1
        if n <= 0:
            n += 1
            pass
            # sheet["A1"] = data_fields[0]
            # sheet["B1"] = data_fields[1]
            # sheet["C1"] = data_fields[2]
            # sheet["D1"] = data_fields[3]
            # sheet["E1"] = data_fields[4]
            # sheet["F1"] = data_fields[5]
            # sheet["G1"] = data_fields[6]
        else:

            if not data_fields is None and len(data_fields) > 6:
                #     print(f'index = {index}', " => n = ",
                #           n, " => data_length = ", data_length, "=> free lines =", free)
                # print('data_fields : ', data_fields)
                #print(data_fields[0], data_fields[1])

                # sheet[f"A{row}"] = data_fields[0]
                # sheet[f"B{row}"] = data_fields[1]
                # sheet[f"C{row}"] = data_fields[2]
                # sheet[f"D{row}"] = data_fields[3]
                # sheet[f"E{row}"] = data_fields[4]
                data_fields[5] = 'in' if int(
                    data_fields[5]) == 1 else 'out'  # in or out
                # sheet[f"F{row}"] = data_fields[5]
                data_fields[6] = seconds_to_time(int(data_fields[6]))
                # sheet[f"G{row}"] = data_fields[6]

                row = (data_fields[0], data_fields[1], data_fields[2],
                       data_fields[3], data_fields[4], data_fields[5],
                       data_fields[6])

                # print('data_fields : ', data_fields)

                # datalist += (row,)
                is_exist = exists(con, (row[1], row[6]))
                # print('is_exist : ', is_exist)
                if not is_exist:

                    add(con, query, row)
            # else:
            #     print("len(data_fields) : ", len(
            #         data_fields), "Data : ", data_fields)

        progress(index, length - 1, 70)
        # i += 1
        # if i > 15:
        #     break
    # book.save(filename="device_data.xlsx")
    # add_many(connection, query, datalist)
