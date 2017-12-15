schemeCustom = [5, 8, 13, 20, 25, 32, 38]
count = [4, 2, 3, 5]


def customCostPercentage(x,z):
    ''' Calculates the cost of the given cost scheme.
        And reduces the price by 10 percent every time a
        Frequency type is used.
    Args:
        costScheme (list) : a list of integers'''
    if z == 0:
        return 0
    else:
        return (x + customCostPercentage(x-0.90,z-1))


def customCostOneDollar(x,z):
    ''' Calculates the cost of the given cost scheme.
        And reduces the price by 1 Dollar a
        Frequency type is used.
    Args:
        costScheme (list) : a list of integers'''
    if z == 0:
        return 0
    else:
        return (x + customCostOneDollar(x-1,z-1))


def advancedCostScheme(strategyType):

     cheapCost=[strategyType(j[0],j[1]) for j in list(zip(schemeCustom,count))]

     if strategyType == customCostOneDollar:
         print ("Costs by making the price every iteration 1 Dollar cheaper: "
                + str(cheapCost))

     if strategyType == customCostPercentage:
         print ("Costs by making the price every iteration 10 percent cheaper: "
         + str(cheapCost))

     return


advancedCostScheme(customCostPercentage)
advancedCostScheme(customCostOneDollar)
