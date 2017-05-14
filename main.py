from solution import Solution
from igenetic.models import GA

# ga = GA(Solution, 150, 200, 10)
#
# best, graph_data = ga.optimize()
# print zip(*graph_data)[2]
# print best._solution
# print best._volume()
# print best._delta()


P = 50000
l = 100
sigma = 14000.0

answer = []

for i in xrange(5, 0, -1):
    bi = ((6*P*i*l) / (400 * sigma)) ** (1.0/3)
    hi = 20 * bi
    answer.append(bi)
    answer.append(hi)

sol = Solution(answer)

print sol._volume()
print sol._delta()
