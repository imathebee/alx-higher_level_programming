#!/usr/bin/python3
"""
    Replaces all attributes of the Student instance
    based on a provided JSON representation.

    Args:
        json (dict): A dictionary containing attribute
        names as keys and their corresponding values.

    Note:
        This method updates the attributes of the Student
        instance using the provided JSON representation.
        The keys of the dictionary should match the public
        attribute names of the Student instance.

    Example:
        json = {
            "first_name": "John",
            "last_name": "Doe",
            "age": 25
        }
        student.reload_from_json(json)

    """


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
