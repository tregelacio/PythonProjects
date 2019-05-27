import heap

nums = [120, 21, 534, 32, 744, 6, 420, 24, 69, 242]
print(heapq.nlargest(4, nums))
print(heapq.nsmallest(4, nums))
print(heapq.nsmallest(0, nums))
print(heapq.nsmallest(10, nums))
heap = list(nums)
heapq.heapify(heap)
heap
heapq.heappop(heap)
heapq.heappop(heap)
heapq.heappop(heap)
heapq.heappop(heap)
