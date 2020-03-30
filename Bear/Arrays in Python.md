# Arrays in Python 
* Arrays VS Lists
	* Similarities:
		* Both are used for storing data
		* Both are mutable
		* Both can be indexed and iterated through
		* Both can be sliced
	* Differences
		* Mainly because Lists could store different data types, while arrays are only store the same data type.
		* Lists can’t be divided, but arrays can.
* There are many package to operate arrays, like numpy, array.
* Array Package Operation
	* array(data type, value list)
		* Create an array with data type like: ‘i’: unsigned int, etc. 
	* append()
		* This function is used to**add the value** mentioned in its arguments at the **end** of the array.
	* insert(I, x)
		* This function is used to**add the value at the position**specified in its argument.
	* pop(x)
		* This function**removes the element at the position** mentioned in its argument, and returns it.
	* remove(x)
		* This function is used to**remove the first occurrence** of the value mentioned in its arguments.
	* index(x)
		* This function returns the**index of the first occurrence** of value mentioned in arguments.
	* reverse()
		* This function**reverses** the array.
	* typecode
		* This function **returns the data type** by which array is initialised.
	* itemsize
		* This function returns **size** in bytes of a **single array element.**
	* buffer_info()
		* Returns a tuple representing the**address in which array is stored and number of elements** in it.
	* count(x)
		* This function **counts the number of occurrences**of argument mentioned in array.
	* extend(arr)
		* This function**appends a whole array** mentioned in its arguments to the specified array.
	* fromlist(list)
		* This function is used to**append a list** mentioned in its argument **to end of array**.
	* tolist()
		* This function is used to **transform an array into a list**.


#Leetcode/structure