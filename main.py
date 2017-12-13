import sys
sys.path.insert(0,'algorithms')
sys.path.insert(0,'bin')


from greedy import greedy
from dsatur import DSatur
from country import country
from backtracking import backtracking
from bktrk import bktrk
from visualisation import visualisation

costScheme1 = [12, 26, 27, 30, 37, 39, 41]
costScheme2 = [19, 20, 21, 23, 36, 37, 38]
costScheme3 = [16, 17, 31, 33, 36, 56, 57]
costScheme4 = [3,  34, 36, 39, 41, 43, 58]

UA = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
# USA = country("United States of America", "csv-borders/USACompleteDataset.csv")
# CN = country("China", "csv-borders/ChinaCompleteDataset.csv")
# RU = country("Russia", "csv-borders/NewRussiaCompleteDataset.csv")
# test = country("testland", "csv-borders/testGraph.csv")

bktrk(UA, 4)

# greedy(test, "degree")
# greedy(USA, "alphabetical")
# DSatur(CN)
# greedy(RU, "alphabetical", True)
# RU.getLowestCost(costScheme1)
# RU.getLowestCost(costScheme2)
# RU.getLowestCost(costScheme3)
# RU.getLowestCost(costScheme4)
# UA1 = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
# UA2 = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
# UA3 = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
#
# greedy(UA1, "degree")
# greedy(UA2, "alphabetical")
# DSatur(UA3)
#
# visualisation.distribution([UA1, UA2])

# backtracking(test, 3)
# visualisation.distribution([test])
