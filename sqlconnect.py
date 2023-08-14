import sqlite3
from cleandata import *
 
# connecting to the database
# "sample.db" didn't exist when i wrote this code. sql will make this database for me
connection = sqlite3.connect("sample.db")
 
# cursor
crsr = connection.cursor()

#if 
# SQL command to create a table in the database
sql_command = """CREATE TABLE chemists (
id INTEGER PRIMARY KEY,
pagetitle TEXT,
tag VARCHAR(30),
gender CHAR(1),
joining DATE);"""
 
# execute the statement
crsr.execute(sql_command)


# SQL command to insert the data in the table
count = 0
for elem in pageTitles:
    sql_command = """INSERT INTO chemists VALUES (count, elem);"""
    crsr.execute(sql_command)
    count +=1

#save changes 
connection.commit()
# close the connection
connection.close()