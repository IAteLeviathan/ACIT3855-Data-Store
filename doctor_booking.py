from sqlalchemy import Column, Integer, String, DateTime
from base import Base
import datetime


class Doctor_Appointment(Base):
    """ Doctor Appointment """

    __tablename__ = "doctor_appointment"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    date = Column(String(100), nullable=False)
    reason = Column(String(250), nullable=False)
    date_created = Column(DateTime, nullable=False)

    def __init__(self, first_name, last_name, date, reason):
        """ Initializes a doctor appointment """
        self.first_name = first_name
        self.last_name = last_name
        self.date = date
        self.reason = reason
        self.date_created = datetime.datetime.now()

    def to_dict(self):
        """ Dictionary Representation of a doctor appointment """
        dict = {}
        dict['id'] = self.id
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        dict['date'] = self.date
        dict['reason'] = self.reason
        dict['date_created'] = self.date_created

        return dict
