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

# test = country("testland", "csv-borders/testGraph.csv")


# ----- COUNTRY = UKRAINE -----
UA = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
# Ukraine Algorithm Parameters
UAgreedyDegree = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
UAgreedyAlphabetical = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
UADsatur = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
UAbacktracking = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")

# Ukraine Algorithms:
greedy(UAgreedyDegree, "degree")
greedy(UAgreedyAlphabetical, "alphabetical", True)
DSatur(UADsatur)
backtracking(UAbacktracking, 4)

# Ukraine visualisation:
visualisation.distribution([UAgreedyDegree, UAgreedyAlphabetica, UADsatur, UAbacktracking])
visualisation.basicInformation(UA)

# Ukraine costscheme
UA.getLowestCost(costScheme1)
UA.getLowestCost(costScheme2)
UA.getLowestCost(costScheme3)
UA.getLowestCost(costScheme4)


# ----- COUNTRY = RUSSIA -----
RU = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
# Russia Algorithm Parameters
RUgreedyDegree = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
RUgreedyAlphabetical = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
RUDsatur = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
RUbacktracking = country("Russia", "csv-borders/RussiaCompleteDataset.csv")

# Russia Algorithms:
greedy(RUgreedyDegree, "degree")
greedy(RUgreedyAlphabetical, "alphabetical", True)
DSatur(RUDsatur)
backtracking(RUbacktracking, 4)

# Russia visualisation:
visualisation.distribution([RUgreedyDegree, RUgreedyAlphabetica, RUDsatur, RUbacktracking])
visualisation.basicInformation(RU)

# Russia costscheme
RU.getLowestCost(costScheme1)
RU.getLowestCost(costScheme2)
RU.getLowestCost(costScheme3)
RU.getLowestCost(costScheme4)


# ----- COUNTRY = United States of America -----
USA = country("USA", "csv-borders/USACompleteDataset.csv")
# Russia Algorithm Parameters
USAgreedyDegree = country("USA", "csv-borders/USACompleteDataset.csv")
USAgreedyAlphabetical = country("USA", "csv-borders/RussiaCompleteDataset.csv")
USADsatur = country("USA", "csv-borders/USACompleteDataset.csv")
USAbacktracking = country("USA", "csv-borders/USACompleteDataset.csv")

# Russia Algorithms:
greedy(USAgreedyDegree, "degree")
greedy(USAgreedyAlphabetical, "alphabetical", True)
DSatur(USADsatur)
backtracking(USAbacktracking, 4)

# Russia visualisation:
visualisation.distribution([USAgreedyDegree, USAgreedyAlphabetica, USADsatur, USAbacktracking])
visualisation.basicInformation(RU)

# Russia costscheme
USA.getLowestCost(costScheme1)
USA.getLowestCost(costScheme2)
USA.getLowestCost(costScheme3)
USA.getLowestCost(costScheme4)



# ----- COUNTRY = CHINA -----
CN = country("China", "csv-borders/ChinaCompleteDataset.csv")
# Russia Algorithm Parameters
CNgreedyDegree = country("China", "csv-borders/ChinaCompleteDataset.csv")
CNgreedyAlphabetical = country("China", "csv-borders/ChinaCompleteDataset.csv")
CNDsatur = country("China", "csv-borders/ChinaCompleteDataset.csv")
CNbacktracking = country("China", "csv-borders/ChinaCompleteDataset.csv")

# Russia Algorithms:
greedy(CNgreedyDegree, "degree")
greedy(CNgreedyAlphabetical, "alphabetical", True)
DSatur(CNDsatur)
backtracking(CNbacktracking, 4)

# Russia visualisation:
visualisation.distribution([CNgreedyDegree, CNgreedyAlphabetica, CNDsatur, CNbacktracking])
visualisation.basicInformation(CN)

# Russia costscheme
CN.getLowestCost(costScheme1)
CN.getLowestCost(costScheme2)
CN.getLowestCost(costScheme3)
CN.getLowestCost(costScheme4)
