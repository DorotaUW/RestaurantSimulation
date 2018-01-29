from Table import Table
from Party import Party

import numpy as N
import random


class Restaurant(object):

    def __init__(self, tableDefinition):
                
        self.eatingParties = []
        self.waitingParties = []
        self.abandonedParties = []
        self.satisfiedParties = []

        #create tablelist based on the tableDefinition
        self.tableList = []
        for i in xrange(0, len(tableDefinition)):
            tableCount = tableDefinition[i][0]
            for table in xrange(0, tableCount):
                tableCustomerCount = tableDefinition[i][1]
                self.tableList.append(Table(tableCustomerCount))

    
    def getEmptyTable(self, party):        
        for table in self.tableList:
            if(table.party == None and party.peopleCount <= table.maxCustomerCount):
                return table   
        return None 
 
    def getRandomEmptyTable(self, party):
        table = random.choice(self.tableList)                 
        if(table.party == None and party.peopleCount <= table.maxCustomerCount):
            return table
        return None                                  

    def sitPartyBlockingFIFO(self):       
        if len(self.waitingParties) > 0:
            party = self.waitingParties[0]
            table = self.getEmptyTable(party)
            if table != None: 
                self.bindPartyWithTable(party, table)
                return
    
    def sitPartySmallestAvailTable(self):         
        # iterate though each party in the list of parties                                     
        for party in self.waitingParties:               
                       
            # see if there's an empty table where size >= peopleCount
            table = self.getEmptyTable(party)

            # if the table exists
            if table != None:
                self.bindPartyWithTable(party, table)
                return 

    def sitPartySmallestPossibleTable(self):        
        for party in self.waitingParties:                     
            table = self.getBestMatchEmptyTable(party)
            if table != None: 
                self.bindPartyWithTable(party, table)
                return       
                            
    def getBestMatchEmptyTable(self, party):    
        bestMatchTableSeats = None
        for table in self.tableList:
            if table.maxCustomerCount >= party.peopleCount:
                bestMatchTableSeats = table.maxCustomerCount 
                break
                                       
        for table in self.tableList:
            if(table.party == None and table.maxCustomerCount == bestMatchTableSeats):
                return table   
        return None                 

    def sitPartyRandomly(self):        
        for party in self.waitingParties:                     
            table = self.getRandomEmptyTable(party)
            if table != None: 
                self.bindPartyWithTable(party, table)
                return

    def bindPartyWithTable(self, party, table):
        # sets the table's party data attribute to the current party 
        table.setParty(party)
        # sets the party's Table data attribute to the empty table
        # obtained from tableList
        party.setTable(table)
        # update eatingParties and waitingParties
        self.eatingParties.append(party)
        self.waitingParties.remove(party)
                

    def timeUpdate(self):
        for eatingParty in self.eatingParties:        
            eatingParty.timeUpdate()
            if eatingParty.finishedEating():
                self.satisfiedParties.append(eatingParty)
                self.eatingParties.remove(eatingParty)                        
                eatingParty.table.setParty(None)
                eatingParty.setTable(None)
         
        self.sittingMethod(self)
                          
        for waitingParty in self.waitingParties:
            waitingParty.timeUpdate()
            if waitingParty.abandonedLine():
                self.abandonedParties.append(waitingParty)       
                self.waitingParties.remove(waitingParty)   

