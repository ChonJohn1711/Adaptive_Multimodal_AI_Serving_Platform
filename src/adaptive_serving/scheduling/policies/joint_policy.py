from .base import BasePolicy

class JointPolicy(BasePolicy):
    def decide(self, *args, **kwargs):
        return 'joint'
