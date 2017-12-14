<p align="center">
  <img src="https://i.imgur.com/Sgd3iqW.png" alt="radio russia" height="400" width="400" />
</p>

# Radio Russia

## Opdracht 1
Verzin een zenderinrichting voor de Oekraïne. Iedere provincie moet een zendertype hebben, geen enkele twee aangrenzende provincies mogen hetzelfde zendertype hebben. Verzin een zenderinrichting voor het hele land, en hoe minder zendertypes je gebruikt, hoe beter.

Doe hetzelfde voor China, de USA en uiteindelijk voor moedertje Rusland. Hoe minder zenderypes, hoe beter.

Probeer voor ieder land met ieder minimumaantal zendertypes te bepalen hoe een evenwichtige verdeling eruit zou zien, en kijk of een inrichting mogelijk is met zo'n verdeling.

## Opdracht 2

Er zijn vier mogelijke kostenschema's bekend geworden. Bekijk voor ieder land welk kostenschema de voordeligste inrichting oplevert.

Zendertype | Kosten 1 | Kosten 2 | Kosten 3 | Kosten 4
------|----|------|---|--
A | 12 | 19 | 16 | 3
B | 26 | 20 | 17 | 34
C | 27 | 21 | 31 | 36
D | 30 | 23 | 33 | 39
E | 37 | 36 | 36 | 41
F | 39 | 37 | 56 | 43
G | 41 | 38 | 57 | 58

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To run our algorithms the following packages are being used, and thus are required in order to run our algorithms.

```
Python 3
NetworkX
Matplotlib
pandas
numpy
```

## Running the tests

In order to run the algorithms various elements from the main.py file have to be commented or uncommented. 
Here we take Ukraine as an example. 

```
# ----- COUNTRY = UKRAINE -----
UA = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
Ukraine Algorithm Parameters
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
visualisation.visualisation(UAgreedyDegree)
visualisation.visualisation(UADSatur)
visualisation.visualisation(UAbacktracking)

# Ukraine costscheme
UADSatur.getLowestCost(costScheme1)
UADSatur.getLowestCost(costScheme2)
UADSatur.getLowestCost(costScheme3)
UADSatur.getLowestCost(costScheme4)
```
The example above shows every action that can be performed for the country of ukraine. 
To use a specific algorithm, the other algorithms can be commented as the following example where only
the DStatur algorithm will be run: 
```
# Ukraine Algorithms:
# greedy(UAgreedyAlphabetical, "alphabetical", True)
# greedy(UAgreedyDegree, "degree")
DSatur(UADSatur)
# backtracking(UAbacktracking, 4)
```

The same principle goes for all the other algorithms. 
Simply make sure that what is to be run should be uncommented and what should be ignored
should be commented.


### Results

To see the results of all the algorithms, check the readme of the results folder. Here various tables and
images can be seen showing and explaining the results. 


## Authors

* **Mathijs Parmentier** - *Initial work* - [MathijsPar](https://github.com/MathijsPar)
* **Iliass Allach** - *Initial work* - [iliassrifie](https://github.com/iliassrifie)
* **Wout Singerling** - *Initial work* - [Wohesi](https://github.com/Wohesi)

Zie ook de lijst met [contributors](https://github.com/Wohesi/progtheorie/graphs/contributors) voor de deelnemers van dit project. 


## Acknowledgments

A lof of inspiration has been drawn from the following book: 

*A Guide to Graph Colouring - Algorithms and Applications by R.M.R. Lewis*

This book allowed us to explore different types of algorithms and it's usage in graphcolouring problems. 
 


