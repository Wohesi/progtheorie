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


# # ----- COUNTRY = UKRAINE -----
# UA = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
# # Ukraine Algorithm Parameters
# UAgreedyAlphabetical = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
# UAgreedyDegree = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
# UADSatur = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
# UAbacktracking = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
#
# # Ukraine Algorithms:
# greedy(UAgreedyAlphabetical, "alphabetical", True)
# greedy(UAgreedyDegree, "degree")
# DSatur(UADSatur)
# backtracking(UAbacktracking, 4)
#
# # Ukraine visualisation:
# visualisation.distribution([UAgreedyAlphabetical, UAgreedyDegree, UADSatur, UAbacktracking])
# visualisation.basicInformation(UADSatur)
# visualisation.visualisation(UADSatur)
#
# # Ukraine costscheme
# UADSatur.getLowestCost(costScheme1)
# UADSatur.getLowestCost(costScheme2)
# UADSatur.getLowestCost(costScheme3)
# UADSatur.getLowestCost(costScheme4)


# # ----- COUNTRY = United States of America -----
# USA = country("USA", "csv-borders/USACompleteDataset.csv")
# # USA Algorithm Parameters
# USAgreedyAlphabetical = country("USA", "csv-borders/RussiaCompleteDataset.csv")
# USAgreedyDegree = country("USA", "csv-borders/USACompleteDataset.csv")
# USADsatur = country("USA", "csv-borders/USACompleteDataset.csv")
# USAbacktracking = country("USA", "csv-borders/USACompleteDataset.csv")
#
# # USA Algorithms:
# greedy(USAgreedyAlphabetical, "alphabetical", True)
# greedy(USAgreedyDegree, "degree")
# DSatur(USADsatur)
# backtracking(USAbacktracking, 4)
#
# # USA visualisation:
# visualisation.distribution([USAgreedyAlphabetical, USAgreedyDegree, USADsatur, USAbacktracking])
# visualisation.basicInformation(USADSatur)
# visualisation.visualisation(USADSatur)
#
# # USA costscheme
# USAgreedyAlphabetical.getLowestCost(costScheme1)
# USAgreedyAlphabetical.getLowestCost(costScheme2)
# USAgreedyAlphabetical.getLowestCost(costScheme3)
# USAgreedyAlphabetical.getLowestCost(costScheme4)



# ----- COUNTRY = CHINA -----
CN = country("China", "csv-borders/ChinaCompleteDataset.csv")
# China Algorithm Parameters
CNgreedyAlphabetical = country("China", "csv-borders/ChinaCompleteDataset.csv")
CNgreedyDegree = country("China", "csv-borders/ChinaCompleteDataset.csv")
CNDSatur = country("China", "csv-borders/ChinaCompleteDataset.csv")
CNbacktracking = country("China", "csv-borders/ChinaCompleteDataset.csv")

# China Algorithms:
greedy(CNgreedyAlphabetical, "alphabetical", True)
greedy(CNgreedyDegree, "degree")
DSatur(CNDSatur)
backtracking(CNbacktracking, 4)

# China visualisation:
visualisation.distribution([CNgreedyAlphabetical, CNgreedyDegree, CNDSatur, CNbacktracking])
visualisation.basicInformation(CNDSatur)
visualisation.visualisation(CNDSatur)

# China costscheme
CNDSatur.getLowestCost(costScheme1)
CNDSatur.getLowestCost(costScheme2)
CNDSatur.getLowestCost(costScheme3)
CNDSatur.getLowestCost(costScheme4)



# # ----- COUNTRY = RUSSIA -----
# RU = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
# # Russia Algorithm Parameters
# RUgreedyAlphabetical = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
# RUgreedyDegree = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
# RUDsatur = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
# RUbacktracking = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
#
# # Russia Algorithms:
# greedy(RUgreedyAlphabetical, "alphabetical", True)
# greedy(RUgreedyDegree, "degree")
# DSatur(RUDsatur)
# backtracking(RUbacktracking, 4)
#
# # Russia visualisation:
# visualisation.distribution([RUgreedyDegree, RUgreedyAlphabetical, RUDsatur, RUbacktracking])
# visualisation.basicInformation(RUDsatur)
# visualisation.visualisation(RUDsatur)
#
# # Russia costscheme
# RUDsatur.getLowestCost(costScheme1)
# RUDsatur.getLowestCost(costScheme2)
# RUDsatur.getLowestCost(costScheme3)
# RUDsatur.getLowestCost(costScheme4)
