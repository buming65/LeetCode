# 731 My Calendar II
* Problem
	* If the three calendars have the same overlap, then it’s triple booking.
* Solution
	* For the new calendar, see if there is an overlap in overlaps, if there is, it means triple booking.
	* Also find the overlap between the new calendar with other calendars, if there is overlap, means double booking. And if there is another overlap, then triple booking.
```
class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True
```
#Leetcode/problems/Orderedmap 