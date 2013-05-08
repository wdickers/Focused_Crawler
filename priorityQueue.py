import heapq
class PriorityQueue:
    def __init__(self,seedList):
        if seedList is not None:
            self.queue = seedList
            heapq.heapify(self.queue)
        else:
            self.queue = []

    def pop(self):
        return heapq.heappop(self.queue)

    def push(self,element):
        heapq.heappush(self.queue,element)

    def isempty(self):
        if len(self.queue)> 0:
            return False
        else:
            return True
