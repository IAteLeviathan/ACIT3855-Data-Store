import mysql.connector

db_conn = mysql.connector.connect(
    host="ec2-54-184-96-229.us-west-2.compute.amazonaws.com", port="3306", user="user", password="password", database="events")
db_cursor = db_conn.cursor()

db_cursor.execute('''
          CREATE TABLE dentist_appointment
          (id INTEGER PRIMARY KEY ASC, 
           first_name VARCHAR(250) NOT NULL,
           last_name VARCHAR(250) NOT NULL,
           date VARCHAR(100) NOT NULL,
           reason VARCHAR(250) NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

db_cursor.execute('''
          CREATE TABLE doctor_appointment
          (id INTEGER PRIMARY KEY ASC, 
           first_name VARCHAR(250) NOT NULL,
           last_name VARCHAR(250) NOT NULL,
           date VARCHAR(100) NOT NULL,
           reason VARCHAR(250) NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

db_cursor.commit()
db_cursor.close()