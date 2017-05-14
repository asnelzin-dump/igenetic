import random


class Solution:
    DELTA = 2.7
    SIGMA = 14000

    L = 500
    l = 100
    P = 50000
    E = 2 * (10**7)

    LB = [1, 30, 2.4, 45, 2.4, 45, 1, 30, 1, 30]
    UB = [5, 65, 3.1, 60, 3.1, 60, 5, 65, 5, 65]

    def __init__(self, solution):
        self._fitness = -1
        self._solution = solution

    def __getitem__(self, index):
        return self._solution[index]

    def __iter__(self):
        return self._solution.__iter__()

    @property
    def size(self):
        return len(self._solution)

    @classmethod
    def generate_random(cls):
        numbers = []

        for low, up in zip(cls.LB, cls.UB):
            numbers.append(random.uniform(low, up))

        return Solution(numbers)

    def _volume(self):
        return self.l*sum(map(lambda x: x[0]*x[1], zip(self._solution[::2], self._solution[1::2])))

    def _delta(self):
        coeff = (self.P * (self.l**3)) / self.E
        return coeff * (244 / (self._solution[0] * (self._solution[1] ** 3)) +
                        148 / (self._solution[2] * (self._solution[3] ** 3)) +
                        76 / (self._solution[4] * (self._solution[5] ** 3)) +
                        28 / (self._solution[6] * (self._solution[7] ** 3)) +
                        4 / (self._solution[8] * (self._solution[9] ** 3)))

    def _sigmas(self):
        return [(6*self.P*self.l) / (self._solution[8] * (self._solution[9] ** 2)),
                (6*self.P*2*self.l) / (self._solution[6] * (self._solution[7] ** 2)),
                (6*self.P*3*self.l) / (self._solution[4] * (self._solution[5] ** 2)),
                (6*self.P*4*self.l) / (self._solution[2] * (self._solution[3] ** 2)),
                (6*self.P*5*self.l) / (self._solution[0] * (self._solution[1] ** 2))]

    def fitness(self):
        if self._fitness == -1:
            if (self._delta() > self.DELTA) or \
                    any(sigma > self.SIGMA for sigma in self._sigmas()):
                self._fitness = 0
            else:
                self._fitness = 1 / self._volume()
        return self._fitness

    def crossover(self, parent):
        child = [None] * parent.size

        start = int(random.random() * parent.size)
        end = int(random.random() * parent.size)

        if start > end:
            start, end = end, start

        child[start:end] = parent[start:end]

        for idx, number in enumerate(self._solution):
            if child[idx] is None:
                child[idx] = number

        return Solution(child)

    def mutate(self):
        if random.random() < 0.05:
            random_index = int(random.random() * self.size)
            low = self.LB[random_index]
            up = self.UB[random_index]
            self._solution[random_index] = random.uniform(low, up)