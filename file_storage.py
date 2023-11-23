#!/usr/bin/python3
"""
"""
import json
class FileStorage:
    """
    """

    def __init__(self):
        """
        """

        print("i Store the task")

    @staticmethod
    def save(self):
        """
        save the contain of the object in a json file
        """
        item = []
        item.append(self)
        with open("dimka.json", "w") as file:
            json.dump(item, file, indent = 2)

