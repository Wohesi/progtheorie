import sys
sys.path.insert(0,'algorithms')
sys.path.insert(0,'bin')

from greedy import greedy
from dsatur import DSatur
from country import country
from visualisation import visualisation

UA = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
USA = country("United States of America", "csv-borders/USACompleteDataset.csv")
CN = country("China", "csv-borders/ChinaCompleteDataset.csv")
RU = country("Russia", "csv-borders/NewRussiaCompleteDataset.csv")

greedy(UA, "degree")
greedy(USA, "alphabetical")
DSatur(CN)
DSatur(RU)

UA1 = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
UA2 = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")
UA3 = country("Ukraine", "csv-borders/UkraineCompleteDataset.csv")

greedy(UA1, "degree")
greedy(UA2, "alphabetical")
DSatur(UA3)

visualisation.distribution([UA1, UA2, UA3])
