# GracefulLabeling

The aim of this project is to be able to play with the idea of graceful labelings of perfect binary trees
to find patterns that could lead to algorithms or rulesets to systematically generate a graceful perfect binary tree
of any size.

This project implements many algorithms such as converting a sorted array to a balanced binary tree and implementing
Heap's algorithm, which generates all possible permutations for a set of numbers.

We define gracefully labeled graph as a graph whose nodes
have unique values 0 through n and whose edges also have unique values. 
Nodes are assigned the values, and the values of the edges are calculated by subtracting
the values of the nodes adjacent to the edge, and taking the absolute value of the difference

For example, the tree

                     6
 
           5
 
                     4
 
 3
 
                     2
 
           1
 
                     0

 is not a graceful labeling because the edge that connects 1 and 3, and the edge that connects 3 and 5, have
 the values |3-1| = 2, and |3-5| = 2 respectively. Since they are both 2, this is not a graceful labeling.

 An example of a tree that is gracefully labeled is

                     4
 
           3
 
                     5
 
 0
 
                     1
 
           6
 
                     2

 since the edge that connects 0 and 6 has value |0-6| = 6, the one with 0 and 3 is |0-3| = 3,
 the one with 3 and 4 is |3-4| = 1, the one with 3 and 5 is |3-5| = 2, the one with 6 and 1 is |6-1| = 5,
 and the one with |6-2| = 4. Since these are all different, this graph is gracefully labeled. 
