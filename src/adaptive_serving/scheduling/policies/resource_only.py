from .base import BasePolicy

class ResourceOnlyPolicy(BasePolicy):
    def decide(self, *args, **kwargs):
        return 'resource_only'
