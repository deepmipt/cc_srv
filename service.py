from nameko.rpc import rpc
from model_provider import Agent


class ChitChat(object):

    name = 'chitchat'

    a = Agent()

    @rpc
    def predict(self, phrase=None, session=0):
        with self.a['graph'].as_default():
            answer = self.a['agent'].send(phrase)
            print("Session {}: {}".format(session, answer))
            return answer

    @rpc
    def init_session(self, session=0):
        print("Session {} initialized".format(session))

