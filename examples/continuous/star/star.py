
import numpy as np
import matplotlib.pyplot as plt

from pyga import Individual, blended, gaussian


class Star(Individual):

    _crossover_method = staticmethod(blended)
    _mutate_method = staticmethod(gaussian)

    target_shape = None 

    def __init__(self, genes):
        super().__init__(genes)

    @classmethod
    def set_target_shape(cls, points):
        if cls.target_shape is not None:
            raise AttributeError("Target shape already set")
        cls.target_shape = points

    def evaluate_fitness(self):
        if Star.target_shape is None:
            raise ValueError("Target shape not set")
        individual_points = np.array(self.genes).reshape(-1, 2)
        target_points = np.array(Star.target_shape).reshape(-1, 2)
        distances = np.linalg.norm(individual_points - target_points, axis=1)
        mean_distance = np.mean(distances)
        self._fitness = 1 / (1 + mean_distance)  # Lower distance → higher fitness

    def plot(self, ax):
        points = np.array(self.genes).reshape(-1, 2)
        x = np.append(points[:, 0], points[0, 0])
        y = np.append(points[:, 1], points[0, 1])
        ax.plot(x, y, 'b-o')
        ax.set_aspect('equal')
        ax.axis('off')
