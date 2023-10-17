#!/usr/bin/python3
'''Base Model'''
import json


class Base:
    '''Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''init method'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                json_file.write(Base.to_json_string(list_dictionaries))
