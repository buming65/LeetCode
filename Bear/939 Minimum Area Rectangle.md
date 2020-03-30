# 939 Minimum Area Rectangle
* Problem
	* Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.
	* If there isn’t any rectangle, return 0.
	* Example
```
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2 
```
* Solution
	* Map these points to hash table, keys are the x  coordinate, values are y coordinates. 
	* For each x, compare the values, to find the point with the same y coordinate. Then the area is the distance between x multiply the distance between y. 
	* Find the min area.
```
SOLUTION
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        dic = dict()
        for x, y in points:
            if x not in dic:
                dic.setdefault(x, [])
            dic[x].append(y)
        keys = list(key for key in dic.keys() if len(dic[key]) >= 2)
        # print(dic)
        minarea = sys.maxsize
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                y_list = [y for y in dic[keys[i]] if y in dic[keys[j]]]
                # print(y_list)
                y_list = sorted(y_list)
                # need to be sorted since the min minus is in the between numbers.
                # print(y_list)
                if len(y_list) >= 2:
                    min_temp = sys.maxsize
                    for k in range(0, len(y_list)):
                        # // -1 0 1 ...
                        min_temp = min(min_temp, abs(y_list[k] - y_list[k-1]))
                    # print(min_temp)
                    minarea = min(minarea, abs(keys[i] - keys[j]) * min_temp)
        return 0 if minarea == sys.maxsize else minarea
```
#Leetcode/problems/hashtable

