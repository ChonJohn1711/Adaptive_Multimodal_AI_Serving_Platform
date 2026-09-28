class SchedulingEngine:
    def __init__(self) -> None:
        self.policy = None

    def select_policy(self, policy):
        self.policy = policy
