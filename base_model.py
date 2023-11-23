#!/usr/bin/python3
"""
This module defines keeps track of my day to activities
"""
from file_storage import FileStorage
from datetime import date, datetime
import sys
class Task:
    """
    """

    def __init__(self, session = '', task ='',):
        """
        """
        self.session = session
        self.day = datetime.now().strftime("%A")
        self.task = task
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.time = datetime.now().strftime("%H:%M:%S")
 

    def to_dict(self):
        """
        Converting an instance object to a dictionary
        """
        dict_object = {}
        dict_object["Session"] = self.session
        dict_object["Day"] = self.day
        dict_object["Task"] = self.task
        dict_object["Date"] = self.date
        dict_object["Time"] = self.time
        return dict_object
if __name__ == '__main__':
    task = Task(sys.argv[1], sys.argv[2] )
    # converting the object to a dictionary
    task.to_dict()
    # Saving the state of the object 
    FileStorage.save(task.to_dict())
