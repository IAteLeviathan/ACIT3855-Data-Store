import connexion
from connexion import NoContent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from dentist_booking import Dentist_Appointment
from doctor_booking import Doctor_Appointment
import datetime
from pykafka import KafkaClient
import pykafka
import yaml as yaml
import json
from threading import Thread
from flask_cors import CORS, cross_origin

with open('app_conf.yaml', 'r') as f:
    app_conf = yaml.safe_load(f.read())

DB_ENGINE = create_engine('mysql+pymysql://' 
+ app_conf['datastore']['user'] 
+ ":" + app_conf['datastore']['password'] + "@" 
+ app_conf['datastore']['hostname'] + ":" 
+ app_conf['datastore']['port'] + '/' + app_conf['datastore']['db'])
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

def dentistbooking(reading):
    session = DB_SESSION()

    dea = Dentist_Appointment(reading['first_name'],
                       reading['last_name'],
                       reading['date'],
                       reading['reason'])

    session.add(dea)

    session.commit()
    session.close()
    return NoContent, 200

def doctorbooking(reading):
    session = DB_SESSION()

    doa = Doctor_Appointment(reading['first_name'],
                       reading['last_name'],
                       reading['date'],
                       reading['reason'])

    session.add(doa)

    session.commit()
    session.close()
    return 200

def get_doctor_appointment(startDate, endDate):
    results_list = []

    session = DB_SESSION()

    results = session.query(Doctor_Appointment).all()
    
    for result in results:
        datetime1 = datetime.datetime.strptime(startDate, '%Y-%m-%dT%H:%M:%S')
        datetime2 = datetime.datetime.strptime(endDate, '%Y-%m-%dT%H:%M:%S')
        print(result.to_dict())
        if datetime1 <= result.to_dict()['date_created'] <= datetime2:
            results_list.append(result.to_dict())
            print(result.to_dict())

    session.close()

    return results_list, 200

def get_dentist_appointment(startDate, endDate):
    results_list = []

    session = DB_SESSION()

    results = session.query(Dentist_Appointment).all()

    for result in results:
        datetime1 = datetime.datetime.strptime(startDate, '%Y-%m-%dT%H:%M:%S')
        datetime2 = datetime.datetime.strptime(endDate, '%Y-%m-%dT%H:%M:%S')
        print(result.to_dict())
        if datetime1 <= result.to_dict()['date_created'] <= datetime2:
            results_list.append(result.to_dict())
            print(result.to_dict())

    session.close()

    return results_list, 200

def process_messages():
    with open ('kafka_config.yaml', 'r') as f:
        kafka = yaml.safe_load(f.read())

    client = KafkaClient(hosts='{0}:{1}'.format(kafka['kafka']['kafka-server'], kafka['kafka']['kafka-port']))
    topic = client.topics['{0}'.format(kafka['kafka']['topic'])]
    consumer = topic.get_simple_consumer()

    for msg in consumer:
        msg_str = msg.value.decode('utf-8')
        msg = json.loads(msg_str)
        if msg['type'] == 'Doctor':
            reading = msg['payload']
            doctorbooking(reading)
        elif msg['type'] == 'Dentist':
            reading = msg['payload']
            dentistbooking(reading)

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yaml")
CORS(app.app)
app.app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == "__main__":
    t1 = Thread(target=process_messages)
    t1.setDaemon(True)
    t1.start()
    app.run(port=8090)