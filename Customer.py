import random
import numpy as N

# Assumptions based on Chevys Fresh Mex data
MAX_WAITING_TIME_MEAN = 35
MAX_WAITING_TIME_STD = 25

MAX_EATING_TIME_MEAN = 50
MAX_EATING_TIME_STD = 20


class Customer(object):
    """ Returns a customer object"""
    def __init__(self):       
        self.maxWaitingTime = N.random.normal(MAX_WAITING_TIME_MEAN, MAX_WAITING_TIME_STD)
        self.maxEatingTime = N.random.normal(MAX_EATING_TIME_MEAN, MAX_EATING_TIME_STD)
        self.waitingTime  = 0
        self.eatingTime = 0
        self.table = None

    def finishedEating(self):
        return self.eatingTime >= self.maxEatingTime

    def abandonedLine(self):
        return self.waitingTime >= self.maxWaitingTime
    
    def timeUpdate(self):
        if self.table == None:
            self.waitingTime += 1
        else:
            self.eatingTime += 1

    def setTable(self, table):
        self.table = table