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
    
    
    def __repr__(self):
        return "<Book(street_address='{}', city='{}', state={}, zip_code={})>"\
                .format(self.street_address, self.city, self.state, self.zip_code)           
    
class PeopleMaster(Base):
    __tablename__ = 'people_master'
    person_id = Column(Integer, primary_key=True)
    person_name = Column(String)
    person_DOB = Column(Date)
    active_phone_number = Column(String)
    
    def __repr__(self):
        return "<Book(person_name='{}', person_DOB='{}', active_phone_number={})>"\
                .format(self.person_name, self.person_DOB, self.active_phone_number)

class PeopleAddress(Base):
    __tablename__ = 'people_address'
    address_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("people_master.person_id"))
    person = relationship("PeopleMaster", backref="people_address")

    start_date = Column(Date)
    end_date = Column(Date)
    
    def __repr__(self):
        return "<Book(start_date='{}', end_date='{}')>"\
                .format(self.start_date, self.end_date)
              

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


addresses = Addresses(
    street_address='Deep Learning',
    city='Ian Goodfellow',
    state='Andhra Pradesh',
    zip_code='456677'
)

people_master = PeopleMaster(
    person_name='Deep Learning',
    person_DOB=datetime(2016, 11, 18),

    active_phone_number='9627889278',
)

people_address = PeopleAddress(
    person_id=person,
    start_date= datetime(2019, 11, 18),
    end_date=datetime(2020, 11, 18)
    )

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


s=Session()
##s.add(people_address)
##s.add(people_master)
##s.add(addresses)
##s.commit()
res=s.query(PeopleMaster) \
    .join(PeopleAddress) \
    .filter(ContactDetails.address.ilike('%glendale%')) \
    .all()

