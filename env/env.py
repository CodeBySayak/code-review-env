class CodeReviewEnv:
    def __init__(self, task):
        self.task = task

    def reset(self):
        self.state = self.task.get_problem()
        return self.state

    def step(self, action):
        reward, done, info = self.task.evaluate(action)
        return self.state, reward, done, info