from .base import BasePolicy

class FixedSmallPolicy(BasePolicy):
    def decide(self, *args, **kwargs):
        return 'small'
