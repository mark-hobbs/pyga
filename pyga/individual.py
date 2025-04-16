import numpy as np


class Individual:

    _crossover_method = None
    _mutate_method = None

    def __init__(self, genes):
        self.genes = genes
        self._fitness = None

    def evaluate_fitness(self):
        """
        This method should be implemented in subclasses to evaluate fitness.
        """
        raise NotImplementedError

    def fitness(self):
        """
        Returns the fitness of the individual. Computes fitness if it has not
        been computed yet.
        """
        if self._fitness is None:
            self.evaluate_fitness()
        return self._fitness

    def crossover(self, partner):
        """
        Crossover: combine the genetic material of two parent individuals
        to create offspring

        Returns
        -------
        child
        """
        if self._crossover_method is None:
            raise NotImplementedError("Crossover method not defined.")
        return self._crossover_method(self, partner)

    def mutate(self, mutation_probability):
        """
        Mutation: introduce small variations in the genetic material,
        preventing premature convergence and maintaining diversity
        in the population.
        """
        if self._mutate_method is None:
            raise NotImplementedError("Mutation method not defined.")
        return self._mutate_method(self, mutation_probability)
