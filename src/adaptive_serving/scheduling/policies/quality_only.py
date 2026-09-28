from .base import BasePolicy

class QualityOnlyPolicy(BasePolicy):
    def decide(self, *args, **kwargs):
        return 'quality_only'
