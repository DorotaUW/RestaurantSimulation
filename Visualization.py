
from Restaurant import Restaurant

import numpy as N
import matplotlib
import matplotlib.pyplot as plt


# for recording
#FIRST = 0
fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()

def plotRestaurant(restaurant, show=True):
       
    row = 60
    col = 60
    data = N.zeros((row, col, 3), dtype='f')
    shape = N.shape(data)
    frameColor = (1,1,0)
    data[0,:,:] = frameColor
    data[:,0,:] = frameColor
    data[-1,:,:] = frameColor
    data[:, -1, :] = frameColor
    #door
    data[-1,3:9,:] = (0.59, 0.29, 0.0)
    #green door
    data[0, 51:57,:] = (0,1,0)
    # red door
    data[0, 14:20, :] = (1,0,0)
    wallColor = (1,0,1)
    data[7: -1, 11 ,:] = wallColor 
    data[7: -1, 22 ,:] = wallColor
    data[7: -1, 48, :] = wallColor

    maxTablePosition = 48
    row = 10
    col = 24
    emptyTableColor = (1,1,1)
    for table in restaurant.tableList:
        if (table.party == None):
            customerColor = emptyTableColor
            occupiedSeats = 0
        else:
            customerColor = table.party.color
            occupiedSeats = table.party.peopleCount

        if (col + table.maxCustomerCount >= maxTablePosition):
            row += 2
            col = 24
        customerEnd = col + occupiedSeats
        tableEnd = col + table.maxCustomerCount
        
        data[row, col : customerEnd, :] = customerColor
        data[row, customerEnd : tableEnd, :] = emptyTableColor        
        col = tableEnd + 1
    
    waitingPartyRow = 10 
    waitingPartyCol = 2        
    # show a waiting line of customers
    showLine(restaurant.waitingParties, waitingPartyRow, waitingPartyCol, data)

    # show a abandoned line of customers
    abandonedPartyRow = 10
    abandonedPartyCol = 13
    showLine(restaurant.abandonedParties, abandonedPartyRow, abandonedPartyCol, data)
    
    #show a satisfied line of customers
    satisfiedPartyRow = 10
    satisfiedPartyCol = 50
    showLine(restaurant.satisfiedParties, satisfiedPartyRow, satisfiedPartyCol, data)
  
    font = {'family': 'serif',
        'color':  'white',
        'weight': 'normal',
        'size': 14,
        }
    plt.text(3,56, 'Waiting', fontdict=font)
    plt.text(13.5, 56, 'Abandoned',fontdict=font)
    plt.text(33, 56, 'Eating',fontdict=font)
    plt.text(51, 56, 'Satisfied',fontdict=font)

    plt.title("Restaurant Simulation")
    ax.imshow(data, interpolation='none', extent=[0, shape[0], 0, shape[1]], zorder=0)    
    ax.axis('off')
    plt.pause(0.5)
     

    #for recording
    #if FIRST == 0:
    #    plt.pause(2)
    #    global FIRST
    #    FIRST = 1


def showLine(line, row, col, data):
    for party in line:        
        if(row >= 55):
            return      
        data[row, col : col + party.peopleCount, :] = party.color
        row += 2

