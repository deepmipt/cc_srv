from nameko.rpc import rpc
from model_provider import Agent


class ChitChat(object):

    name = 'chitchat'

    a = Agent()

    @rpc
    def predict(self, phrase=None):
        with self.a['graph'].as_default():
            answer = self.a['agent'].send(phrase)
            print(answer)
            return answer
