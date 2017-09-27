from nameko.extensions import DependencyProvider
import tensorflow as tf
import os
from nmt.interface import Agents


class Agent(DependencyProvider):
    def __init__(self):
        self.graph = tf.get_default_graph()
        model_path = os.environ.get("CHITCHAT_MODEL")
        self.agent = Agents(model_path)

    def get_dependency(self, worker_ctx):
        return {
            'agent': self.agent,
            'graph': self.graph
        }
