from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer,ForeignKey, String, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.orm import relationship, backref,relation



engine = create_engine('postgresql://postgres:root@localhost:5432/dps2')

Base = declarative_base()

class Addresses(Base):
    __tablename__ = 'addresses'
    address_id = Column(Integer, primary_key=True)
    street_address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code=Column(String)
    
    
##    def __repr__(self):
##        return "<Addresses(streetaddress='{}', city='{}', state='{}', zipcode='{}')>"\
##                .format(self.streetaddress, self.city, self.state, self.zipcode)
    
class PeopleMaster(Base):
    __tablename__ = 'people_master'
    person_id = Column(Integer, primary_key=True)
    person_name = Column(String)
    person_DOB = Column(Date)
    active_phone_number = Column(String)
    
##    def __repr__(self):
##        return "<PeopleMaster(name='{}', dob='{}', phone='{)'>"\
##                .format(self.name, self.dob, self.phone)

class PeopleAddress(Base):
    __tablename__ = 'people_address'
    address_id = Column(Integer, primary_key=True)
    person_id = Column(Integer)
    p = relationship('PeopleMaster', foreign_keys=[person_id],primaryjoin='PeopleMaster.person_id == PeopleAddress.person_id')

    start_date = Column(Date)
    end_date = Column(Date)
    
    
##    def __repr__(self):
##        return "<PeopleAddress(startdate={}, enddate={})>"\
##                .format(self.startdate, self.enddate)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


addresses = Addresses(
    streetaddress='Deep Learning',
    city='Ian Goodfellow',
    state='Andhra Pradesh',
    zipcode='456677'
)

people_master = PeopleMaster(
    name='Deep Learning',
    dob=datetime(2016, 11, 18),
    phone='9627889278',
)

people_address = PeopleAddress(
    
    startdate= datetime(2019, 11, 18),
    enddate=datetime(2020, 11, 18)
    )

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


s=Session()
s.add(people_address)
s.add(people_master)
s.add(addresses)
s.commit()

