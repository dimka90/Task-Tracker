#!/usr/bin/python3
"""
This module defines keeps track of my day to activities
"""
from file_storage import FileStorage
import datetime
import sys
class Task:
    """
    """

    def __init__(self, period = '', time = '', task = ''):
        """
        """
        self.period = period
        self.time = time
        self.task = task
        print("This is the base class")


task = Task("morning","1:30", "coding" )
print(task.period)
Save = FileStorage()
