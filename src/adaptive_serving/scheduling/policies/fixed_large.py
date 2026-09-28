from .base import BasePolicy

class FixedLargePolicy(BasePolicy):
    def decide(self, *args, **kwargs):
        return 'large'
