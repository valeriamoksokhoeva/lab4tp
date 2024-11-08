class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.low > self.high:
            raise StopIteration
        self.low += 1
        return self.low - 1
    
counter = Counter(3, 10)

for i in range(4):
    print(next(counter))