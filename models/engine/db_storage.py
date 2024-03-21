#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class represents a database storage using SQL"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes the SQL database storage"""
        # Get enviromental variables
        user = os.getenv("HBNB_MYSQL_USER")
        pword = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        # Link to connect to mysql database
        DATABASE_URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            user, pword, host, db_name
        )
        # Create engine
        self.__engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        # Check env
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method used to return all models in database"""
        # Empty Object Storage
        objects = {}
        # Allowed classes
        allowed_classes = (User, State, City, Amenity, Place, Review)
        # Check if class is not None
        if cls is None:
            for class_type in allowed_classes:
                query = self.__session.query(class_type)
                for obj in query.all():
                    obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj
            # Return filtered objects
            return objects

        query = self.__session.query(cls)
        for obj in query.all():
            obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objects[obj_key] = obj
        # Return objects
        return objects

    def delete(self, obj=None):
        """Method used to remove an object from database"""
        if obj is not None:
            self.__session.query(type(obj)).\
                filter(type(obj).id == obj.id).delete(
                synchronize_session=False
            )

    def new(self, obj):
        """Method used to add a new object to database"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as error:
                self.__session.rollback()
                raise error

    def save(self):
        """Commit session to database"""
        self.__session.commit()

    def reload(self):
        """Method used to load data from database"""
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        self.__session = scoped_session(SessionFactory)()

    def close(self):
        """Method used to close database"""
        self.__session.close()
