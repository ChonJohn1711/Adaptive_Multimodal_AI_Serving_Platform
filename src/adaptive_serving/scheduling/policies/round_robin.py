from .base import BasePolicy

class RoundRobinPolicy(BasePolicy):
    def decide(self, *args, **kwargs):
        return 'round_robin'
