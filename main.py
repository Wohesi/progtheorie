import sys
sys.path.insert(0,'algorithms')
sys.path.insert(0,'bin')

from greedy import greedy
from dsatur import DSatur
from country import country
from backtracking import backtracking
from visualisation import visualisation

import networkx as nx


costScheme1 = [12, 26, 27, 30, 37, 39, 41]
costScheme2 = [19, 20, 21, 23, 36, 37, 38]
costScheme3 = [16, 17, 31, 33, 36, 56, 57]
costScheme4 = [3,  34, 36, 39, 41, 43, 58]

UA = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
USA = country("United States of America", "csv-borders/USACompleteDataset.csv")
CN = country("China", "csv-borders/ChinaCompleteDataset.csv")
RU = country("Russia", "csv-borders/NewRussiaCompleteDataset.csv")

# greedy(UA, "degree")
# greedy(USA, "alphabetical")
# DSatur(CN)
# DSatur(RU)

<<<<<<< Updated upstream
# RU.getLowestCost(costScheme1)
=======
print(nx.get_node_attributes(RU.cg, 'freq'))
visualisation.basicInformation(RU)
RU.getLowestCost(costScheme1)
>>>>>>> Stashed changes
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

backtracking(USA, 4)
