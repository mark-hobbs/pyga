
from pyga import Individual


class Design(Individual):

    def __init__(self, genes, posterior):
        super().__init__(genes)
        self.posterior = posterior

    def evaluate_fitness(self):
        self._fitness = self.posterior.evaluate(self.genes)

    def crossover(self, partner):
        return Design(super().crossover(partner), self.posterior)
        
    def mutate(self, mutation_probability):
        super().mutate(mutation_probability)

    def plot(self, ax):
        """
        Plot an individual design
        """
        ax.scatter(self.genes[0], self.genes[1], color='black')