import sqlite3

conn = sqlite3.connect('readings.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE dentist_appointment
          (id INTEGER PRIMARY KEY ASC, 
           first_name VARCHAR(250) NOT NULL,
           last_name VARCHAR(250) NOT NULL,
           date VARCHAR(100) NOT NULL,
           reason VARCHAR(250) NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

c.execute('''
          CREATE TABLE doctor_appointment
          (id INTEGER PRIMARY KEY ASC, 
           first_name VARCHAR(250) NOT NULL,
           last_name VARCHAR(250) NOT NULL,
           date VARCHAR(100) NOT NULL,
           reason VARCHAR(250) NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

conn.commit()
conn.close()