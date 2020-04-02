def kClosest(self, points, K):
    dist = lambda i: points[i][0]**2 + points[i][1]**2

    def findKthSmallest(nums, start, end, kth):
	    # kth is zero based
        left, right = start, end
        mid = (left + right)//2
        pivot = dist(mid)

        while left <= right:
            while left <= right and dist(left) < pivot:
                left += 1
            while left <= right and dist(right) > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        if kth <= right:
            return findKthSmallest(nums, start, right, kth)
        elif kth >= left:
            return findKthSmallest(nums, left, end, kth)
        else:
            return nums[:kth+1]

    return findKthSmallest(points, 0, len(points) - 1, K-1)