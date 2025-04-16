import numpy as np


def pmx(individual, partner):
    """
    Partially mapped crossover (PMX)

    Returns
    -------
    child : Individual
    """
    size = len(individual.genes)
    child = [-1] * size
    a, b = sorted(np.random.choice(range(size), size=2, replace=False))

    # Copy segment from self to child
    for i in range(a, b):
        child[i] = individual.genes[i]

    # Create mapping for the other parent
    mapping = {value: index for index, value in enumerate(child) if value != -1}

    # Fill in the rest from other
    for i in range(size):
        if i < a or i >= b:
            value = partner.genes[i]
            while value in mapping:
                value = partner.genes[mapping[value]]
            child[i] = value
            mapping[value] = i
    return individual.__class__(child)


def blended(individual, partner, alpha=0.5):
    """
    Blend Crossover (BLX-alpha)

    Parameters
    ----------
    partner : Individual
        The other parent individual.
    alpha : float
        The blending parameter that controls the range of crossover.

    Returns
    -------
    child : Individual
        The offspring produced by crossover.
    """
    child = np.zeros_like(individual.genes)
    for i in range(len(individual.genes)):
        X_min = min(individual.genes[i], partner.genes[i])
        X_max = max(individual.genes[i], partner.genes[i])
        delta = X_max - X_min
        child[i] = np.random.uniform(X_min - alpha * delta, X_max + alpha * delta)
    return individual.__class__(child)
