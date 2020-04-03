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

### Selection Sort 

* For the entire list, find the smallest element, put in the first position.

### Insertion Sort 

* A sub-list is maintained sorted.
* Search sequentially and unsorted items are moved and inserted into the sub-list.
* To be short, just find element one by one, put into the right position.

### Bubble Sort 

* Compared each pair of adjacent elements, swap them if they are not in order.

### Shell Sort 

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

### Quick Sort 

* Split array into two arrays. One has the elements smaller than the pivot. The other has the elements greater than the pivot.
* Has two points, the lower point, the higher point.
* While left smaller than pivot, move right. While right greater than pivot, move left.
* Else swap the two elements.
* When left meet right, put the pivot in this position.

### Merge Sort 

* Based on Divide and Conquer Technique.
* Divide into two groups until undivided.
* Sort each group, merge them one by one.

### Heap Sort 

* Based on Binary Heap data structure, which the parent is greater or smaller than children nodes.
* Build Max Heap. Then the root should contain max element. Swap with the last element.
* Heapify the max heap excluding the last element. Repeat this step.

### Radix Sort 

* If the elements are in range from 1 to n^2, use Radix Sort.
* Do digit by digit sort starting from least significant digit to most significant digit.

### Bucket Sort 

* Set up an array of empty buckets.
* Scatter: put each element in bucket.
* Sort and merge.

### Complexity

#### Time Complexity



#### Space Complexity





## Data Structure

### Overview



### Stack (LIFO)

* A last-in, first-out policy which means the element deleted from the set is the one most recently inserted. 
  * S.top: indexes the most recently inserted element.
* Bottom: S[1]
* Top: S[S.top]. When S.top == 0, the stack is empty. It could be test by STACK-EMPTY. **Overflows** means top exceeds. **Underflows** means empty stack, cause error when pop.
* Operations, all these three operations are O(1) :
  * STACK-EMPTY(S)
  * PUSH(S, x)
  * POP(S)

### Queue (FIFO)

* A first-in, first-out policy which means the element deleted from the set is the one that has been in the set for the longest time. 
  * Head: The head of the line
  * Tail: The end of the line
* When head == tail, empty queue. If attempt to dequeue the queue, cause underflows. When head == tail + 1 or (head == 1 and tail == length), full queue. If attempt to enqueue, cause overflows.
* Operations:
  * ENQUEUE: Insert operation. 
  * DEQUEUE: Delete operation. 

### Linked List

* The objects are arranged in a linear order, provide a simple, flexible representation for dynamic sets.
* Linked List have several forms, it may be either singly or doubly, it may be sorted or not, and it may be circular or not.

#### Singly Linked List

* No prev compared to the doubly linked list.

#### Doubly Linked List

* Each element is an object with key, next and prev.
  * x.next points to its successor
  * x.prev points to its predecessor
* Head means the first element, tail means the last element.

#### Operations

* Search: Find the first element with key k. O(N)
* Insert: Given an element with specific key, insert into the from of the linked list. O(1)
* Delete: Delete specific key. Worst: O(N)
  * Could be simpler if ignore the boundary conditions at the head and tail of the list.(Sentinel)
  * x.prev.next = x.next
  * x.next.prev = x.prev

### Binary Trees

* A tree data structure in which each node has at most two children which are referred as left child and right child.
* There are many types of binary tree like balanced binary tree, perfect binary tree...

### Binary Search Trees

* A binary search tree is organized in a binary tree.

* Binary Search Tree property: Node in the left subtree is no bigger than the parent node. Nodes in the right subtree is no smaller than the parent node.

* Recursive Algorithms O(N):

  * Preorder: Parent, Left, Right
  * Inorder: Left, Parent, Right
  * Postorder: Left, Right, Parent

* Operations:

  * Search O(H) h is the height of the tree: Begin search at root and traces downward.

  * Minimum and Maximum O(H):

    * Minimum: Begin root, follow left child until meet NULL.
    * Maximum: Begin root, follow right child until meet NULL.

  * Successor and Predecessor O(H):

    * Successor: The node ahead of given node

      * If right subtree is nonempty, the successor is the leftmost of the right subtree

      * Else, the successor is the lowest ancestor of x whose left child is also an ancestor of x.

      * ![image-20200403144902583](README.assets/image-20200403144902583.png)

      * For node 13, it doesn't have right sub tree. So to find it successor, follow the path up, until the node have left child which is 15(6 also has left child but it's not in the path followed by 13)

      * ```python
        if x.right != NIL:
            return TREE-MINIMUM(x.right)
        y = x.parent
        while y != NIL and x == y.right:
            x = y
            y = y.parent
        return y
        ```

    * Predecessor: The node behind of given node(Same as successor)

  * Insert O(H)

    * Set trailing pointer y as the parent of x.

  * Delete O(H)

    * If no children, then simply remove it and modify its parent.
    * If just one children, then we set that child to the original position, modify its parent.
    * If has two children, find the successor(predecessor is also acceptable) to replace this node.

### Balanced Binary Search Trees

* Balance: each operation makes local adjustments. There're many types of Balanced BST. Such as AVL, Red-Black, 

#### AVL

* For each node, the depths of its subtrees differ by at most 1.

### Hashing 



### Priority Queues(Heaps)



## Search Algorithms

### 