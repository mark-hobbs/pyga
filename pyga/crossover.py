import numpy as np


def pmx(individual, partner):
    """
    Partially mapped crossover (PMX)

    Returns
    -------
    child
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
