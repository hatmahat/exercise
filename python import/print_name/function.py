def adds(num1, num2):
    return num1 + num2

class random:
    def __init__(self, seed):
        self._seed = seed

    def get_seed(self):
        return self._seed