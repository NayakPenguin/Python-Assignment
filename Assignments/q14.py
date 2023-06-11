class PriorityQueue:
    def __init__(self):
        self.arr = []

    def insert(self, value):
        self.arr.append(value)
        self.arr.sort(reverse=True)

    def top(self): 
        return self.arr[0]


pq = PriorityQueue()
pq.insert(10)
print(pq.top())
pq.insert(42)
print(pq.top())
pq.insert(12)
print(pq.top())