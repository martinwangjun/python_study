#!/usr/bin/python
# -*- coding: utf-8 -*-

# Connect to Mysql with mysql.connector
# 1. Install mysql.connector with 'pip install mysql-connector==2.1.4'. If you
# just use 'pip install mysql-connector', you will fail.
# 2. Please use utf-8 in MySQL to avoid funny codes.

import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'port': 3306,
    'database': 'python',
    'charset': 'utf8'
}

try:
    conn = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print('connect fails!{}'.format(err))

cursor = conn.cursor()

try:
    sql = 'SELECT f_name_chn AS name, f_user_code AS code FROM t_users'
    cursor.execute(sql)
    for code, name in cursor:
        print(code, name)
except mysql.connector.Error as err:
    print('connect fails!{}'.format(err))
finally:
    cursor.close()
    conn.close()
