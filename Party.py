from Customer import Customer
import random
import numpy as N

class Party(object):
    """ Returns a party object"""
  
    def __init__(self, peopleCount, id):
        
        self.customerList = []
        self.table = None
        self.peopleCount = peopleCount
        self.id = id
        self.color = (random.random(),random.random(),random.random()) 

        for i in xrange(0, self.peopleCount):
            self.customerList.append(Customer())


    def finishedEating(self):
        for customer in self.customerList:
            if not customer.finishedEating():
                return False
        return True   
            

    def abandonedLine(self):
        for customer in self.customerList:
            if customer.abandonedLine():
                return True
        return False

    def timeUpdate(self):
        for customer in self.customerList:
            customer.timeUpdate()
        

    def setTable(self, table):
        for customer in self.customerList:
            customer.setTable(table)
        self.table = table

    def __repr__(self):
        return 'id '+ str(self.id) + ':' + 'C ' + str(self.peopleCount) 