import random


class Organism:
    def __init__(self):
        pass

    @staticmethod
    def generate_random():
        raise NotImplementedError()

    def fitness(self):
        raise NotImplementedError('You should implement fitness function in your subclass!')

    def crossover(self, organism):
        raise NotImplementedError('You should implement crossover function in your subclass!')

    def mutate(self):
        raise NotImplementedError('You should implement mutation function in your subclass!')


class Population:
    def __init__(self, population_size, elite_count):
        self.population_size = population_size
        self.elite_count = elite_count
        self._organisms = []

    @property
    def size(self):
        return len(self._organisms)

    def add(self, organism):
        self._organisms.append(organism)

    def get_fittest(self):
        return max(self._organisms, key=lambda x: x.fitness())

    def tournament_selection(self):
        tournament_population = Population(self.population_size, self.elite_count)
        for i in xrange(self.elite_count):
            tournament_population.add(random.choice(self._organisms))
        return tournament_population.get_fittest()

    def evolve(self):
        new_population = Population(self.population_size, self.elite_count)
        new_population.add(self.get_fittest())
        for i in xrange(self.size - 1):
            parent1 = self.tournament_selection()
            parent2 = self.tournament_selection()
            child = parent1.crossover(parent2)
            child.mutate()
            new_population.add(child)
        return new_population

    def generate_random_population(self, organism_class):
        for i in xrange(self.population_size):
            self.add(organism_class.generate_random())


class GA:
    def __init__(self, organism_class, population_size, generations, elite_count):
        self.organism_class = organism_class
        self.elite_count = elite_count
        self.generations = generations
        self.population_size = population_size

    def optimize(self):
        graph_data = []

        population = Population(self.population_size, self.elite_count)
        population.generate_random_population(self.organism_class)

        for iteration in xrange(self.generations):
            mean_fitness = sum(organism.fitness() for organism in population._organisms) / (population.size + 0.0)
            graph_data.append((iteration, population.get_fittest(), mean_fitness))
            population = population.evolve()

        return population.get_fittest(), graph_data
