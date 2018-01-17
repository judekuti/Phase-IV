import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# start of configuration...declare a map
# ie this allows us to describe the db tables we will use and then define our own classes which will be mapped into those tables.
Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

# the User class defines a __repr__() method(optional though) to display nicely formatted User objects

    # def __repr__(self):
    #     return "<Restaurant(name='%s')>" % (self.name)

# create schema with User class
class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    # def __repr__(self):
    #     return "<MenuItem(name='%s', description ='%s', price='%s', course='%s')>" % (self.name, self.description, self.price, self.course)


# in memory-only SQLite database.. creates an instance of Engine
engine = create_engine('sqlite:///restaurantmenu.db')

# the
Base.metadata.create_all(engine)
