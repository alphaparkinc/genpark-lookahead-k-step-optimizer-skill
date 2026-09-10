class LookaheadOptimizer:
    """
    Lookahead Optimizer: k steps forward, 1 step back.
    Zhang et al. (2019).
    """
    def __init__(self, k=5, alpha=0.5):
        self.k = k
        self.alpha = alpha
        self.step_count = 0
        self.slow_weights = {}

    def init_param(self, param_id, initial_weight):
        self.slow_weights[param_id] = initial_weight

    def step(self, fast_weight, param_id=0):
        if param_id not in self.slow_weights:
            self.slow_weights[param_id] = fast_weight

        self.step_count += 1
        if self.step_count % self.k == 0:
            slow = self.slow_weights[param_id]
            slow = slow + self.alpha * (fast_weight - slow)
            self.slow_weights[param_id] = slow
            return slow
        return fast_weight
