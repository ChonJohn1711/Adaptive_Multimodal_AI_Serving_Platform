from .base import BasePolicy

class ShortestQueuePolicy(BasePolicy):
    def decide(self, *args, **kwargs):
        return 'shortest_queue'
