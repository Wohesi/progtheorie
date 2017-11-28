import sys
sys.path.insert(0,'algorithms')

# from algorithms import greedy
# from algorithms import DSatur
from greedy import greedy
from dsatur import DSatur
from country import country
'''
def main(String dataSetName, String algorithmName, ):
    if

UA1  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
# USA1  = country("United States of America", "csv-borders/USACompleteDataset.csv")
# RU1  = country("Russia", "csv-borders/NewRussiaCompleteDataset.csv")
# CN1  = country("China", "csv-borders/ChinaCompleteDataset.csv")

greedy(UA1.cg, "degree")
# greedy(USA1.cg, "degree")
# greedy(RU1.cg, "degree")
# greedy(CN1.cg, "degree")

# UA2  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
USA2  = country("United States of America", "csv-borders/USACompleteDataset.csv")
# RU2  = country("Russia", "csv-borders/NewRussiaCompleteDataset.csv")
# CN2  = country("China", "csv-borders/ChinaCompleteDataset.csv")

# greedy(UA2.cg, "degree", True)
greedy(USA2.cg, "degree", True)
# greedy(RU2.cg, "degree", True)
# greedy(CN2.cg, "degree", True)

# UA3  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
# USA3  = country("United States of America", "csv-borders/USACompleteDataset.csv")
RU3  = country("Russia", "csv-borders/NewRussiaCompleteDataset.csv")
# CN3  = country("China", "csv-borders/ChinaCompleteDataset.csv")

# greedy(UA3.cg, "alphabetical")
# greedy(USA3.cg, "alphabetical")
greedy(RU3.cg, "alphabetical")
# greedy(CN3.cg, "alphabetical")

# UA4  = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
# USA4  = country("United States of America", "csv-borders/USACompleteDataset.csv")
# RU4  = country("Russia", "csv-borders/NewRussiaCompleteDataset.csv")
CN4  = country("China", "csv-borders/ChinaCompleteDataset.csv")

# greedy(UA4.cg, "alphabetical", True)
# greedy(USA4.cg, "alphabetical", True)
# greedy(RU4.cg, "alphabetical", True)
greedy(CN4.cg, "alphabetical", True)

UA1.distribution()
USA2.distribution()
RU3.distribution()
CN4.distribution()
'''

UA = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
DSatur(UA.cg)
USA = country("USA", "csv-borders/USACompleteDataset.csv")
DSatur(USA.cg)
RU  = country("Russia", "csv-borders/NewRussiaCompleteDataset.csv")
DSatur(RU.cg)
CN = country("China", "csv-borders/ChinaCompleteDataset.csv")
DSatur(CN.cg)

UA.distribution()
USA.distribution()
RU.distribution()
CN.distribution()

# UA.visualisation()
# USA.visualisation()
# RU.visualisation()
# CN.visualisation()
