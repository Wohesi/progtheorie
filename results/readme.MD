# Results & Experimentation

This folder contains various images of the results of our algorithms. 


## Amount of frequencies

|                | Greedy Alphabetical | Greedy Degree | DSatur | Backtracking |
|----------------| :------------------:|:-------------:|:------:|-------------:|
| **Ukraine**    |        5            |        5      |   **4**   |     **4***       |
| **USA**        |        5            |        6      |   **4**   |     **4***       |
| **China**      |        5            |        5      |   **4**    |     **4***       |
| **Russia**     |        5            |        6      |   **4**    |     **4***       |
|                | * *Backtracking uses a fixed amount of frequencies *



## Balance ( Coefficient of variation)

|                | Greedy Alphabetical | Greedy Degree | DSatur | Backtracking
|----------------| :------------------:|:-------------:|:------:|-------------:|
| **Ukraine**    |        0.58         |      0.566    |  0.346 |     **0.327**       |
| **USA**        |        0.469        |      0.661    |  0.437 |     **0.358**       |
| **China**      |        0.564        |      0.654    |  0.405 |     **0.264**       |
| **Russia**     |       0.494         |      0.671    |  0.561 |     TBD       |
*Note: Backtracking yields different results each time you run it. Results could thus vary



## Results of Ukraine
| **Ukraine**   | Greedy Alphabetical | Greedy Degree | DSatur | Backtracking
|---------------| :------------------:|:-------------:|:------:|------------:|
| Cost Scheme 1 |    542              |   548         | 542    |  560
| Cost Scheme 2 |    523              |   535         | **506**    |  510
| Cost Scheme 3 |    568              |   557         | 548    |  549
| Cost Scheme 4 |    577              |   577         | 598    |  629


### Images of frequecy distrubtution
![distribution](https://github.com/Wohesi/progtheorie/blob/master/results/ukraine_freq.png)

#### Example map
![map](https://github.com/Wohesi/progtheorie/blob/master/results/ukraine_freq_DS.png)


## Results of Unites States of America
|**USA**        | Greedy Alphabetical  | Greedy Degree    | DSatur  | Backtracking
|---------------| :-------------------:|:----------------:|:-------:|------------:|
| Cost Scheme 1 |    1936              |   1103           | 1050    | 1085
| Cost Scheme 2 |    1779              |   1036           | **967**     | 983
| Cost Scheme 3 |    1949              |   1118           | 1044    | 1099
| Cost Scheme 4 |    2177              |   1214           | 1179    | 1234


### Images of frequecy distrubtution
![distribution](https://github.com/Wohesi/progtheorie/blob/master/results/usa_freq.png)

#### Example map
![map](https://github.com/Wohesi/progtheorie/blob/master/results/usa_freq_GD.png)


## Results of China
| **China**     | Greedy Alphabetical | Greedy Degree | DSatur | Backtracking
|---------------| :------------------:|:-------------:|:------:|------------:|
| Cost Scheme 1 |    721              |   696         | 710    |  750
| Cost Scheme 2 |    698              |   681         | **665**    |  676
| Cost Scheme 3 |    748              |   728         | 709    |  759
| Cost Scheme 4 |    767              |  729          | 781    |  858


### Images of frequecy distrubtution
![distribution](https://github.com/Wohesi/progtheorie/blob/master/results/china_freq.png)

#### Example map
![map](https://github.com/Wohesi/progtheorie/blob/master/results/china_freq_BT.png)


## Results of Russia
| **Russia**    | Greedy Alphabetical | Greedy Degree | DSatur | Backtracking
|---------------|:-------------------:|:-------------:|:------:|------------:|
| Cost Scheme 1 |    1936             |   1943        | 1915   |
| Cost Scheme 2 |    1779             |   1873        | **1756**   |
| Cost Scheme 3 |    1949             |   2010        | 1901   |
| Cost Scheme 4 |    2177             |   2078        | 2159   |


### Images of frequency distribution
![distribution](https://github.com/Wohesi/progtheorie/blob/master/results/russia_freq.png)

![map](https://github.com/Wohesi/progtheorie/blob/master/results/russia_freq_GA.png)

### Explanation
Cost scheme 2 seems to be the cheapest scheme overall. 
DSatur is best at minimising the amount of frequencies used (apart from backtracking).
DSatur seems to give the most evenly distributed results.
