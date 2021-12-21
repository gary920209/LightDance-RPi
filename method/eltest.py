from .baseMethod import BaseMethod


# Eltest
class Eltest(BaseMethod):
    def method(self, payload=None):
        response = self.socket.send(["eltest", payload["id"], payload["brightness"]])
        return response
