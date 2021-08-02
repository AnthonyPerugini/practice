class PriortyQueue:
    import heapq

    def __init__(self, queue: list =[], maxsize=None):
        self.queue = queue
        self.heapq.heapify(self.queue)
        self.maxsize = maxsize
        

    def __repr__(self):
        return ' '.join([str(x) for x in self.queue])

    def is_empty(self):
        return len(self.queue) == 0

    def get_size(self):
        return len(self.queue)

    def add(self, value):
        self.push(value)
        
    def push(self, value):
        if self.maxsize is None or self.get_size() < self.maxsize:
            self.heapq.heappush(self.queue, value)
        else:
            print('cannot add more values!')

    def remove(self):
        self.pop()

    def pop(self):
        return self.heapq.heappop(self.queue)

    def nsmallest(self, size):
        return self.heapq.nsmallest(size, self.queue)



pq = PriortyQueue(maxsize=3)
print(pq.maxsize)
pq.add(3)
pq.add(4)
pq.add(10)
pq.add(15)
pq.add(3)
print(pq)


