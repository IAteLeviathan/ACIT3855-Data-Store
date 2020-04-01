import sqlite3

conn = sqlite3.connect('readings.sqlite')

c = conn.cursor()

c.execute('''
          DROP TABLE doctor_appointment
          ''')

c.execute('''
          DROP TABLE dentist_appointment
          ''')
          
conn.commit()
conn.close()