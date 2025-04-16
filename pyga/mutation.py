import numpy as np


def swap(individual, mutation_probability):
    """
    Mutation: Swap mutation

    Returns
    -------
    Modifies individual.genes in place
    """
    if np.random.rand() < mutation_probability:
        idx1, idx2 = np.random.randint(0, len(individual.genes), 2)
        individual.genes[idx1], individual.genes[idx2] = (
            individual.genes[idx2],
            individual.genes[idx1],
        )
