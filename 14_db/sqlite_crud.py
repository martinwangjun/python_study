#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('sqlite.db')

cursor = conn.cursor()
sql = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name VARCHAR(20)
    )
    '''
cursor.execute(sql)
sql = '''
    INSERT INTO users (name) VALUES(?)
    '''
cursor.execute(sql, ('张飞',))
cursor.close()
conn.commit()
conn.close()

