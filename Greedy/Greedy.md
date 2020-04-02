# Greedy

## 253. Meeting Rooms II

```
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
```

### Solution 1. Priority Queues(Greedy)

* Sort by their start time
* To find if the room is available or not, using min-heap and add the first meeting's ending time to the heap. So only compare the top of the heap to see if free or not.

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        free = []
        
        intervals.sort(key = lambda x : x[0])
        heapq.heappush(free, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if free[0] <= intervals[i][0]:
                #Meaning there a free room
                heapq.heappop(free)
            heapq.heappush(free, intervals[i][1])
        
        return len(free)
```

* Complexity:

  * Time
    $$
    O(NlogN)
    $$
    Sorting: Takes O(NlogN) time

    For min-heap: worst O(NlogN)

  * Space
    $$
    O(N)
    $$

### Solution 2. Chronological Ordering

* Separate out the start times and the end times, Sort them separately.
* Consider two points: start_point, end_point. If sp > ep, some room is free. Else, the number of the room will be added.

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        count = 0
        
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        
        start_point = 0
        end_point = 0
        
        while start_point < len(intervals):
            if starts[start_point] >= ends[end_point]:
                count -= 1
                end_point += 1
            start_point += 1
            count += 1
        return count 
```

