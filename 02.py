from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///test2.db', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class People(Base):
    __tablename__ = 'peoples'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('peoples.id'))
    brand = Column(String)
    model = Column(String)

    peoples = relationship('People', back_populates='cars')


People.cars = relationship('Car', back_populates='peoples')
Base.metadata.create_all(engine)

p1 = People(name='Jaedson', age=15)
session.add(p1)
session.commit()

c1 = Car(brand='Porsche', model='911', people_id=1)
c2 = Car(brand='Audi', model='TT', people_id=1)

session.add_all([c1, c2])
session.commit()

result = session.query(People).all()

for row in result:
    print(f'Name: {row.name}')
    print(f'Cars:')
    for car in row.cars:
        print(f'    Brand: {car.brand}')
        print(f'    Model: {car.model}')
