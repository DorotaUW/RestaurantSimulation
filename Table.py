
class Table(object):
    """Returns a table object"""
    
    def __init__(self, maxCustomerCount):
        self.maxCustomerCount = maxCustomerCount
        self.party = None 

    def __repr__(self):
        peopleCount = ' ' if self.party == None else ':(id '+ str(self.party.id) + ': C '+ str(self.party.peopleCount) + ')'
        return str(self.maxCustomerCount) + peopleCount

    def setParty(self, party):
        self.party = party