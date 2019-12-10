# Data-Structures-and-Algorithms - Code Challenge Three

# Array_Binary_Search

### Problem domain:
We have a sorted list of integers and a given value. We would like to know if the value is in the list. If it is, we would like to know at which index the value is located.

>inputs: ( [2, 4, 6, 8, 15, 16, 23, 40, 47] , 15 ) ---> output: 4   
### Challenge
Algorithm:
    1. Define a function that accepts two arguements(list, value)
    2. If value is not in the list, return -1
    3. Finds the middle of the list
    4. If the value is less than or greater than the input, the appropriate half will be taken (upper or lower half)
    5. Repeat binary search until value is found
    6. Return index of the value
### Approach & Efficiency
For this challenge I worked with Amy. We set out to write a simple function (d.r.y) that matched the algorithm we determined beforehand. It appears that this algorithm would be O(N) performance.
### Solution
![array_binary_search](../../assets/array_binary_search.jpeg)

## Other Challenges
### 1. Code Challenge One - [Array_Reverse](https://github.com/kochsj/python-data-structures-and-algorithms/challenges/array_reverse.py)<br>2. Code Challenge Two - [Array_Shift](https://github.com/kochsj/python-data-structures-and-algorithms/challenges/array_shift)<br>3. Code Challenge Three - [Array_Binary_Search](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/array_binary_search)