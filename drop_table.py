import mysql.connector

db_conn = mysql.connector.connect(
    host="ec2-54-184-96-229.us-west-2.compute.amazonaws.com", port="3306", user="user", password="password", database="events")
db_cursor = db_conn.cursor()

db_cursor.execute('''
          DROP TABLE doctor_appointment
          ''')

db_cursor.execute('''
          DROP TABLE dentist_appointment
          ''')
          
db_cursor.commit()
db_cursor.close()