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


def gaussian(individual, mutation_probability, sigma=0.1):
    """
    Gaussian Mutation

    Parameters
    ----------
    mutation_probability : float
        The probability of mutating each gene.
    sigma : float
        The standard deviation of the Gaussian distribution 
        used for mutation.

    Returns
    -------
    None
    """
    for i in range(len(individual.genes)):
        if np.random.rand() < mutation_probability:
            individual.genes[i] += np.random.normal(0, sigma)