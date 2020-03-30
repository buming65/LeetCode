# Insertion Sort 
* Good for sorting a small number of elements.
```
for j = 2 to A.length 
    key = A[j]
    i = j - 1
    while i > 0 and A[i] > key
        A[i+1] = A[i]
        i = i - 1 
    A[i+1] = key
```
![](Insertion%20Sort/AC8FE1F6-8300-45D8-873A-0A37E02A1812.png)
* Time Consuming:
	* Best: O(n), when they are sorted.
	* Worst: O(n*n), when they are reverse order.
* Python Implement 
```
# Python program for implementation of Insertion Sort 

# Function to do insertion sort 
def insertionSort(arr): 

	# Traverse through 1 to len(arr) 
	for i in range(1, len(arr)): 

		key = arr[i] 

		# Move elements of arr[0..i-1], that are 
		# greater than key, to one position ahead 
		# of their current position 
		j = i-1
		while j >= 0 and key < arr[j] : 
				arr[j + 1] = arr[j] 
				j -= 1
		arr[j + 1] = key 


# Driver code to test above 
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
	print ("% d" % arr[i]) 
```
#Leetcode/algorithm/sort