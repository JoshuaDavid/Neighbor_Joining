# Neighbor Joining

## Description

Takes a distance matrix and a list of names and returns a tree

## Example

**distance\_matrix.txt**  
     , A, B, C, D, E, F  
    A, 0, 5, 4, 7, 6, 8   
    B, 5, 0, 7,10, 9,11   
    C, 4, 7, 0, 7, 6, 8   
    D, 7,10, 7, 0, 5, 9   
    E, 6, 9, 6, 5, 0, 8   
    F, 8,11, 8, 9, 8, 0   

**$ python numpy_nj distance\_matrix.txt**  
    ┬─┬─── D  
    │ └─ E  
    └─┬───── F  
      └─┬─── C  
        └┬ A  
         └──────── B  

## Properties

* The order in which the distances are given in the matrix will not affect the shape of the tree that is returned. (*tested*)
* If the input is well formed, summing the distances from two leaves to the nearest connecting node will give the same distance as the distance between those leaves in the original distance matrix.

## Running Time

The algorithm currently runs in O( N^3 ) time (empirically, O( N^2.8 ) or so)

