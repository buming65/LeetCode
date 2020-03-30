# Heap Sort
* Heap
	* A special tree-based data structure, the tree is  a complete binary tree.
	* Max-Heap:
		* The parent node mush greater than the child node.
	* Min-Heap:
		* The parent node mush smaller than the child node.
* Time Consuming:
	* Ave O(n log n)
	* Build heap is O(n)
	* Heapify is O(logn)
* Use Max-Heap.
* Maintain the heap property
```
MAX_HEAPIFY(A,i)
l = LEFT(i)
r = RIGHT(i)
if l <= A.heap-size and A[l] > A[i]
    largest = l
else 
    largest = i
if r <= A.heap-size and A[r] > A[largest]
    largest = r
if largest not equal i
    exchange A[i] with A[largest]
    MAX_HEAPIFY(A,largest)
```
* Build Max Heap
```
A.heap-size = A.length 
for i = A.length/2 to 1
    MAX_HEAPIFY(A,i) 
```
![](Heap%20Sort/3E201C9B-5571-446C-96E3-0B5DA1FC17A3.png)
* HEAPSORT Algorithm 
```
Build-Max-Heap(A)
for i = A.length to 2
    exchange A[1] with A[i]
    A.heap-size = A.heap-size - 1
    Max-Heapify(A,1) 
```
![](Heap%20Sort/E9CF2CA9-E408-4E3C-9FD9-218089E8E1AF.png)
* Python Implement 
```
# Python program for implementation of heap Sort 

# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
	largest = i # Initialize largest as root 
	l = 2 * i + 1	 # left = 2*i + 1 
	r = 2 * i + 2	 # right = 2*i + 2 

	# See if left child of root exists and is 
	# greater than root 
	if l < n and arr[i] < arr[l]: 
		largest = l 

	# See if right child of root exists and is 
	# greater than root 
	if r < n and arr[largest] < arr[r]: 
		largest = r 

	# Change root, if needed 
	if largest != i: 
		arr[i],arr[largest] = arr[largest],arr[i] # swap 

		# Heapify the root. 
		heapify(arr, n, largest) 

# The main function to sort an array of given size 
def heapSort(arr): 
	n = len(arr) 

	# Build a maxheap. 
	for i in range(n, -1, -1): 
		heapify(arr, n, i) 

	# One by one extract elements 
	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i] # swap 
		heapify(arr, i, 0) 

# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
	print ("%d" %arr[i]) 
```
#Leetcode/algorithm/sort