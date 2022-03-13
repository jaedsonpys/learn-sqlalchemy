from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

# create engine
engine = create_engine('sqlite:///test.db')
Base = declarative_base()

# make a session with database
Session = sessionmaker(bind=engine)
session = Session()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# make all tables
Base.metadata.create_all(engine)

# add new object to database in "users" table
user = Users(name='Jaedson', age=15)
session.add(user)

# add a more objects
user2 = Users(name='Pedro', age=23)
user3 = Users(name='João', age=40)

session.add_all([user2, user3])
session.commit()

all_users = session.query(Users).all()
one_user = session.query(Users).get(2)

print('First User:')
print(one_user.name)
print(one_user.age)

print('\nAll Users:')
for row in all_users:
    print(f'ID: {row.id}')
    print(f'Name: {row.name}')
    print(f'Age: {row.age}')


# using filter
result = session.query(Users).filter('age > 18')
print(result.name)
