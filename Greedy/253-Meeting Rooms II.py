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