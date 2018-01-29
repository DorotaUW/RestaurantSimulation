from Restaurant import Restaurant
from Party import Party
import Visualization as V


import random
import time
import numpy as N
import matplotlib.pyplot as plt

# Assumptions based on Chevys Fresh Mex data
MIN_PEOPLE_COUNT = 1
MAX_PEOPLE_COUNT = 6



class RestaurantSimulation(object):

    def __init__(self):
        return        


    def simulateOnce(self, tableDefinition):
        restaurant = Restaurant(tableDefinition)
        restaurant.sittingMethod = self.sittingMethod
        id = 1
        timer = 0
        while(timer < 180):
            #randomly add new party
            # this simulates rush hours of the getting a new party every minute 
            if random.random() < 1:              
                peopleCount = self.getRandomPartyCount()
                party = Party(peopleCount, id)
                id += 1                     
                restaurant.waitingParties.append(party)
            timer += 1
            
            # Please uncomment for animation of the simulation 
            #V.plotRestaurant(restaurant)
            restaurant.timeUpdate()
                       
        return restaurant
    
    def getRandomPartyCount(self):   
        # Assumptions based on Chevys Fresh Mex dinner time data
        partyProbability = random.random()
        if(partyProbability < 0.53):
            peopleCount = 2 
        elif(partyProbability < 0.74):
            peopleCount = 3
        elif(partyProbability < 0.89):
            peopleCount = 4
        elif(partyProbability < 0.93):
            peopleCount = 5
        else:
            peopleCount = 6  
        return peopleCount

    def simulateMultiple(self, tableDefinition):             
        totalServedCustomers = []
        
        for i in xrange(0,20):          
            restaurant = self.simulateOnce(tableDefinition)
            #self.printRestaurant(restaurant)
            servedCustomers = 0
            for party in restaurant.satisfiedParties:
                servedCustomers += party.peopleCount
                           
            for party in restaurant.eatingParties:
                servedCustomers += party.peopleCount                 

            totalServedCustomers.append(servedCustomers)
        
        meanCustomerServed = N.mean(totalServedCustomers)
        stdCustomerServed = N.std(totalServedCustomers)
        return meanCustomerServed, stdCustomerServed
        
    def simulateTables(self):
        customers = []
        twoTopTables = []
        for twoTops in range(0,52,2):
            fourTops = 25 - (twoTops/2)
            tableDefinition = [[twoTops, 2],[fourTops, 4],[3,6]]
            tableSortedDefinition = sorted(tableDefinition, key = lambda l:l[1])       
            statistics = self.simulateMultiple(tableSortedDefinition)
            twoTopTables.append(twoTops)
            customers.append(statistics[0])           
        return twoTopTables, customers

    def simulate(self):
        self.sittingMethod = Restaurant.sitPartyBlockingFIFO
        setupData = self.simulateTables()
        self.plotCustomerData(setupData[0], setupData[1], 1,"data1.png","BlockingFIFO")
        self.plotCustomerData(setupData[0], setupData[1], 10, "All data.png", "BlockingFIFO")

        self.sittingMethod = Restaurant.sitPartySmallestAvailTable
        setupData = self.simulateTables()
        self.plotCustomerData(setupData[0], setupData[1], 2, "data2.png", "SmallestAvailableTable")
        self.plotCustomerData(setupData[0], setupData[1], 10, "All data.png", "SmallestAvailableTable")

        self.sittingMethod = Restaurant.sitPartyRandomly
        setupData = self.simulateTables()
        self.plotCustomerData(setupData[0], setupData[1], 3, "data3.png", "RandomMatchingTable")
        self.plotCustomerData(setupData[0], setupData[1], 10,"All data.png", "RandomMatchingTable")

        self.sittingMethod = Restaurant.sitPartySmallestPossibleTable
        setupData = self.simulateTables()
        self.plotCustomerData(setupData[0], setupData[1], 4,"data4.png","SmallestPossibleTable")
        self.plotCustomerData(setupData[0], setupData[1], 10, "All data.png", "SmallestPossibleTable")

        # for recording
        #self.sittingMethod = Restaurant.sitPartyRandomly
        #setupData = self.simulateMultiple([[5,2],[8,4],[2,6]])


    def plotCustomerData(self, twoTopTables, customers, figureNumber, name, plotLabel):

        plt.figure(figureNumber)
        plt.plot(twoTopTables, customers, label=plotLabel)       
        plt.xlabel('Two-Top Tables')
        plt.ylabel('Served Customers')
        plt.title('Restaurant Simulation')
       
        plt.legend(loc='lower center')
        plt.savefig(name, dpi=300)
        plt.pause(0.01)


    def addToLine(self):
        return True
    
    def printRestaurant(self, restaurant):
        print ('Tables:    ', restaurant.tableList)
        print ('Eating:    ', restaurant.eatingParties)            
        print ('Waiting:   ', restaurant.waitingParties)                  
        print ('Abandoned: ', restaurant.abandonedParties)
        print ('Satisfied: ', restaurant.satisfiedParties)



simulation = RestaurantSimulation()
simulation.simulate()
