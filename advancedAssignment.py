#ADVANCED SECTION
#a cost scheme that is variable in costs with
#the numbers of frequencies of a type placed.
from collections import Counter
from country import country
from backtracking import backtracking
import networkx as nx


def customCostPercentage(x,z):
    ''' Reduces the price by 10 percent every time a Frequency type is used.
    Args:
        x (integer) : integer with the frequency price'''
    if z == 0:
        return 0
    else:
        return (x + customCostPercentage(x*0.90,z-1))


def customCostOneDollar(x,z):
    '''
    reduces the price by 1 Dollar a Frequency type is used.
    Args:
        x (integer) : integer with the frequency price
    '''
    if z == 0:
        return 0
    else:
        return (x + customCostOneDollar(x-1,z-1))



def advancedCostScheme(country,costScheme,strat):
    '''
    Calculates the cost of the given cost scheme.
    Args:
        costScheme (list) : a list of integers
    '''

    count = Counter(nx.get_node_attributes(country.cg, 'freq').values())
    freqValues = list(count.values())


    strategyType = None

    if strat == "customCostPercentage":
            strategyType = customCostPercentage

    if strat == "customCostOneDollar":
            strategyType = customCostOneDollar

    # gives the the final price of the custom scheme
    #after the advanced calculations
    cheapCost=sum([strategyType(j[0],j[1]) for j in list(zip(costScheme,freqValues))])

    print("country name: " + country.countryName)
    print("algorithm type: " + country.algorithmType)
    print("lowest cost: " + str(cheapCost))
    print("")
    return cheapCost
