class AbstractHandler(object):
    def __init__(self, nxt):
        self._nxt = nxt

    def handle(self, request):
        handled = self.processRequest(request)
        if not handled:
            self._nxt.handle(request)

    def processRequest(self, request):
        raise NotImplementedError


class FirstHandler(AbstractHandler):
    def processRequest(self, request):
        if type(request) == int:
            print(f'First Handler handled the request "{request}"!')
            return True

class SecondHandler(AbstractHandler):
    def processRequest(self, request):
        if type(request) == str:
            print(f'Second Handler handled the request "{request}"!')
            return True

class ThirdHandler(AbstractHandler):
    def processRequest(self, request):
        if type(request) is bool:
            print(f'Third Handler handled the request "{request}"!')
        return True

class DefaultHandler(AbstractHandler):
    def processRequest(self, request):
        print(f'No handlers handled the request "{request}"!')
        return True

class User:
    def __init__(self):
        initial = None
        self.handler = FirstHandler(SecondHandler(ThirdHandler(DefaultHandler(initial))))
    def agent(self, user_request):
        for request in user_request:
            self.handler.handle(request)

data = [1, 'r', '123', True, {1, 2, 3}, False]
user = User()
user.agent(data)