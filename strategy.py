from abc import abstractmethod, ABC
class Strategy(ABC):
    @abstractmethod
    def search(self, data):
        pass

class BinarySearch(Strategy):
    def search(self, data):
        print('Searching binarly ...')
        return data[0]
class LinearSearch(Strategy):
    def search(self, data):
        print('Searching linearly ...')
        return data[0]
    
class Context:
    def __init__(self, strategy):
        self._strategy = strategy
    def set_strategy(self, strategy):
        self._strategy = strategy
    def search(self, data):
        return self._strategy.search(data)
    
data = [6, 7, 3, 9, 10]

context = Context(BinarySearch())
print(context.search(data))

context.set_strategy(LinearSearch())
print(context.search(data))
