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
UAgreedyAlphabetical = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
UAgreedyDegree = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
UADSatur = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
UAbacktracking = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")

# Ukraine Algorithms:
greedy(UAgreedyAlphabetical, "alphabetical", True)
greedy(UAgreedyDegree, "degree")
DSatur(UADSatur)
backtracking(UAbacktracking, 4)

# Ukraine Distribution Graph:
visualisation.distribution([UAgreedyAlphabetical, UAgreedyDegree, UADSatur, UAbacktracking])

# Ukraine Basic Information:
visualisation.basicInformation(UAgreedyAlphabetical)
visualisation.basicInformation(UAgreedyDegree)
visualisation.basicInformation(UADSatur)
visualisation.basicInformation(UAbacktracking)

# Ukraine Graph Visualisations:
visualisation.visualisation(UAgreedyAlphabetical)
# visualisation.visualisation(UAgreedyDegree)
# visualisation.visualisation(UADSatur)
# visualisation.visualisation(UAbacktracking)

# Ukraine costscheme
UADSatur.getLowestCost(costScheme1)
UADSatur.getLowestCost(costScheme2)
UADSatur.getLowestCost(costScheme3)
UADSatur.getLowestCost(costScheme4)


# # ----- COUNTRY = United States of America -----
# USA = country("USA", "csv-borders/USACompleteDataset.csv")
# # USA Algorithm Parameters
# USAgreedyAlphabetical = country("USA", "csv-borders/USACompleteDataset.csv")
# USAgreedyDegree = country("USA", "csv-borders/USACompleteDataset.csv")
# USADSatur = country("USA", "csv-borders/USACompleteDataset.csv")
# USAbacktracking = country("USA", "csv-borders/USACompleteDataset.csv")
#
# # USA Algorithms:
# greedy(USAgreedyAlphabetical, "alphabetical", True)
# greedy(USAgreedyDegree, "degree")
# DSatur(USADSatur)
# backtracking(USAbacktracking, 4)
#
# # USA Distribution Graph:
# visualisation.distribution([USAgreedyAlphabetical, USAgreedyDegree, USADSatur, USAbacktracking])
#
# # USA Basic Information:
# visualisation.basicInformation(USAgreedyAlphabetical)
# visualisation.basicInformation(USAgreedyDegree)
# visualisation.basicInformation(USADSatur)
# visualisation.basicInformation(USAbacktracking)
#
# # USA Graph Visualisations:
# visualisation.visualisation(USAgreedyAlphabetical)
# # visualisation.visualisation(USAgreedyDegree)
# # visualisation.visualisation(USADSatur)
# # visualisation.visualisation(USAbacktracking)
#
# # USA costscheme
# USAgreedyAlphabetical.getLowestCost(costScheme1)
# USAgreedyAlphabetical.getLowestCost(costScheme2)
# USAgreedyAlphabetical.getLowestCost(costScheme3)
# USAgreedyAlphabetical.getLowestCost(costScheme4)



# # ----- COUNTRY = CHINA -----
# CN = country("China", "csv-borders/ChinaCompleteDataset.csv")
# # China Algorithm Parameters
# CNgreedyAlphabetical = country("China", "csv-borders/ChinaCompleteDataset.csv")
# CNgreedyDegree = country("China", "csv-borders/ChinaCompleteDataset.csv")
# CNDSatur = country("China", "csv-borders/ChinaCompleteDataset.csv")
# CNbacktracking = country("China", "csv-borders/ChinaCompleteDataset.csv")
#
# # China Algorithms:
# greedy(CNgreedyAlphabetical, "alphabetical", True)
# greedy(CNgreedyDegree, "degree")
# DSatur(CNDSatur)
# backtracking(CNbacktracking, 4)
#
# # China Distribution Graph:
# visualisation.distribution([CNgreedyAlphabetical, CNgreedyDegree, CNDSatur, CNbacktracking])
#
# # China Basic Information:
# visualisation.basicInformation(CNgreedyAlphabetical)
# visualisation.basicInformation(CNgreedyDegree)
# visualisation.basicInformation(CNDSatur)
# visualisation.basicInformation(CNbacktracking)
#
# # China Graph Visualisations:
# visualisation.visualisation(CNgreedyAlphabetical)
# # visualisation.visualisation(CNgreedyDegree)
# # visualisation.visualisation(CNDSatur)
# # visualisation.visualisation(CNbacktracking)
#
# # China Costschemes
# CNDSatur.getLowestCost(costScheme1)
# CNDSatur.getLowestCost(costScheme2)
# CNDSatur.getLowestCost(costScheme3)
# CNDSatur.getLowestCost(costScheme4)



# # ----- COUNTRY = RUSSIA -----
# RU = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
# # Russia Algorithm Parameters
# RUgreedyAlphabetical = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
# RUgreedyDegree = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
# RUDSatur = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
# RUbacktracking = country("Russia", "csv-borders/RussiaCompleteDataset.csv")
#
# # Russia Algorithms:
# greedy(RUgreedyAlphabetical, "alphabetical", True)
# greedy(RUgreedyDegree, "degree")
# DSatur(RUDSatur)
# backtracking(RUbacktracking, 4)
#
# # Russia Distribution Graph:
# visualisation.distribution([RUgreedyAlphabetical, RUgreedyDegree, RUDSatur, RUbacktracking])
#
# # Russia Basic Information:
# visualisation.basicInformation(RUgreedyAlphabetical)
# visualisation.basicInformation(RUgreedyDegree)
# visualisation.basicInformation(RUDSatur)
# visualisation.basicInformation(RUbacktracking)
#
# # Russia Graph Visualisations:
# visualisation.visualisation(RUgreedyAlphabetical)
# # visualisation.visualisation(RUgreedyDegree)
# # visualisation.visualisation(RUDSatur)
# # visualisation.visualisation(RUbacktracking)
#
# # Russia costscheme
# RUDSatur.getLowestCost(costScheme1)
# RUDSatur.getLowestCost(costScheme2)
# RUDSatur.getLowestCost(costScheme3)
# RUDSatur.getLowestCost(costScheme4)
