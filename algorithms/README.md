# Algorithms 

Here you'll find three kinds of algorithms. 
----
## Greedy algorithm. 

> In practice, the GREEDY algorithm produces feasible solutions quite quickly;
> however, these solutions can often be quite poor in terms of the number of colours
> that the algorithm requires compared to the chromatic number
_A Guide to Graph Colouring - Algorithms and Applications, page 30 - by R.M.R. Lewis _ 

The greedy algorithm contains four types of sorting. 
* Alphabetical:   This can be done on either ascending or descending. 
* Degree:         This can be done on either the highest degree of a node, or smallest degree of a node.

## Dsatur algorithm.

> for the DSATUR algorithm the choice of which vertex to colour next 
> is decided heuristically based on the characteristics of the current
> partial colouring of the graph. This choice is based primarily on the saturation
> degree of the vertices, defined as follows.

_A Guide to Graph Colouring - Algorithms and Applications, page 39 - by R.M.R. Lewis _ 

The DSatur algorthim is a recursive algorithm. It bases the ordering of a list on the amount of 
coloured neighbors a node has. This puts them recursively into a priority queue. 

## Backtracking algorithm

> In essence backtracking algorithms work by systematically building up partial 
> solutionsinto complete solutions. However, during this construction process as soon as
> evidence is gained telling us that there is no way of completing the current partial
> solution to gain an optimal solution, the algorithm backtracks in order to try to find
> suitable ways of adjusting the current partial solution

Despite this algorithm's incompleteness, there is a fundation based on psudocode inside the 
python file. 

