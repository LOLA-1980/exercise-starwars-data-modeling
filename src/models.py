import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    password = Column(String(32))

class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    population = Column(Integer)

class FavoritePlanets(Base):
    __tablename__= 'favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets_id_relationship = relationship(Planets)

class Characters(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    height = Column(Integer)
    mass = Column(Integer)

class FavoriteCharacters(Base):
    __tablename__= 'favorite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters_id_relationship = relationship(Characters)

class Starships(Base):
    __tablename__='starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    model = Column(Integer)
    lenght = Column(Integer)

class FavoriteStarships(Base):
    __tablename__= 'favorite_starships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships_id_relationship = relationship(Starships)



class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
