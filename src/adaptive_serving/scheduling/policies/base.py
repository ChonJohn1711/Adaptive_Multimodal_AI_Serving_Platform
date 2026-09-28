class BasePolicy:
    def decide(self, *args, **kwargs):
        raise NotImplementedError
