# LeetCode

## Divide And Conquer

* Divide: Break the problem into smaller sub-problems. Takes a recursive approach to divide until no sub-problem is further divisible.
* Conquer: The sub-problems are considered solved on their own.
* Merge: Recursively combines the sub-problems until they formulate a solution of the original problem.

## Dynamic Programming(Pending)

* Similar to divide and conquer. But these sub-problems are not solved independently, these sub-problems are remembered and used for similar or overlapping sub-problems.
* Before solving the in-hand sub-problem, the algorithm will try to examine the results of the previously solved sub-problems. Combine the solutions to achieve the best solution.
* General Solution
  * Characterize the structure of an optimal solution.
  * Recursively define the value of an optimal solution.
  * Compute the value of an optimal solution, typically in a bottom-up fashion.
  * Construct an optimal solution from computed information.
* Optimal Substructure

## Greedy(Pending)

* Find a localized optimum solution, may lead to globally optimized solutions.

* Because the problem is an optimization, greedy algorithm use a priority queue.

## Back Tracking

### Three types of problems

#### Decision Problem

* Search for a feasible solution

```python
def solve(node, path):
    path += [node]
    if node:
        return path if path else None
    
    for element in node:
        ans = solve(element, path)
        if ans is not None:
            return ans
    return None
```

#### Optimization Problem

* Search for the best solution

```python
best = -float("inf")
def find_best(node, path):
    path += [node]
    if node:
        if path satisfy:
            best = max(best, node)
        return
    
    for element in node:
        find_best(element, path)
```

#### Enumeration Problem

* Find all feasible solutions

```python
ans = []

def find_all(node, path):
    path += node
    if node:
        if path satisfy:
            ans += path
        return
    
    for element in node:
        find_all(element, path)

```

Reference: [BackTracking](http://summerisgreen.com/blog/2017-07-07-2017-07-07-算法技巧-backtracking.html)

## Sort Algorithm

### Overview

* In-place && Not-in-place: whether require any extra space or not.
* Stable && Not Stable: whether change the sequence of similar content in which they appear.

* Sort Algorithms

  * Selection Sort 

    * For the entire list, find the smallest element, put in the first position.

  * Insertion Sort 

    * A sub-list is maintained sorted.
    * Search sequentially and unsorted items are moved and inserted into the sub-list.
    * To be short, just find element one by one, put into the right position.

  * Bubble Sort 

    * Compared each pair of adjacent elements, swap them if they are not in order.

  * Shell Sort 

    * Based on Insertion Sort, avoid large shift.

    * Depend different gap value, combine the elements into a sorted list. Change gap.

    * Based on Knuth's Formula, h is interval with initial value 1.
      $$
      \frac{3^k-1}{2}\  No\ greater\ than [N/3]
      $$

    $$
    O(N^{\frac{3}{2}})
    $$

    * Based on the original Shell, 
      $$
      \frac{N}{2^k}
      $$

      $$
      O(N^2)
      $$

  * Quick Sort 

    * Split array into two arrays. One has the elements smaller than the pivot. The other has the elements greater than the pivot.
    * Has two points, the lower point, the higher point.
    * While left smaller than pivot, move right. While right greater than pivot, move left.
    * Else swap the two elements.
    * When left meet right, put the pivot in this position.

  * Merge Sort 

    * Based on Divide and Conquer Technique.
    * Divide into two groups until undivided.
    * Sort each group, merge them one by one.

  * Heap Sort 

    * Based on Binary Heap data structure, which the parent is greater or smaller than children nodes.
    * Build Max Heap. Then the root should contain max element. Swap with the last element.
    * Heapify the max heap excluding the last element. Repeat this step.

  * Radix Sort 

    * If the elements are in range from 1 to n^2, use Radix Sort.
    * Do digit by digit sort starting from least significant digit to most significant digit.

  * Bucket Sort 

    * Set up an array of empty buckets.
    * Scatter: put each element in bucket.
    * Sort and merge.

### Complexity

#### Time Complexity



#### Space Complexity





## Data Structure

### Overview



### Stack 



### Queue



### Linked List



### Binary Search Trees



### Balanced Binary Search Trees



### Hashing 



### Priority Queues(Heaps)