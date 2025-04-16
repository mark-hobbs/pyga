
from pyga import Individual, blended, gaussian


class Design(Individual):

    _crossover_method = staticmethod(blended)
    _mutate_method = staticmethod(gaussian)

    posterior = None

    def __init__(self, genes):
        super().__init__(genes)

    @classmethod
    def set_posterior(cls, posterior):
        if cls.posterior is not None:
            raise AttributeError("Posterior already set")
        cls.posterior = posterior

    def evaluate_fitness(self):
        self._fitness = self.posterior.evaluate(self.genes)

    def plot(self, ax):
        """
        Plot an individual design
        """
        ax.scatter(self.genes[0], self.genes[1], color='black')