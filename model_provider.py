from nameko.extensions import DependencyProvider
import tensorflow as tf
import os
import nmt.interface as bot


class Agent(DependencyProvider):
    def __init__(self):
        self.graph = tf.get_default_graph()
        model_path = os.environ.get("CHITCHAT_MODEL")
        bot.init(model_path)
        self.agent = bot

    def get_dependency(self, worker_ctx):
        return {
            'agent': self.agent,
            'graph': self.graph
        }
