import random

import numpy
from matplotlib import pyplot


class DataLoader:
    def get_input(self):
        x = []
        x.append([0, 1, 0, 0])
        x.append([0, 1, 0, 0])
        x.append([0, 1, 0, 0])
        x.append([0.5, 1, 1, 0])
        x.append([0.5, 1, 1, 0])
        x.append([0.5, 1, 1, 0])
        x.append([0.5, 0, 0, 0.5])
        x.append([0.5, 0, 0, 0.5])
        x.append([0.5, 0, 0, 0.5])
        x.append([1, 0, 0.8, 0])
        x.append([1, 0.32, 0.65, 0])
        x.append([1, 0.43, 0.87, 0])
        x.append([1, 0.51, 0.75, 0])
        x.append([1, 0.67, 0.75, 0.91])
        x.append([1, 0.89, 0.91, 0.99])
        x.append([1, 0.9, 0.77, 0.82])
        x.append([1, 0.8, 1, 0.91])

        # x.append([0, 1, 0, 0, -0.82, 0.91])
        # x.append([0, 1, 0, 0, -0.62, 0.83])
        # x.append([0, 1, 0, 0, -0.74, 0.21])
        # x.append([0.5, 1, 1, 0, -0.5, 0.1])
        # x.append([0.5, 1, 1, 0, -0.67, 0.47])
        # x.append([0.5, 1, 1, 0, -0.21, 0.68])
        # x.append([0.5, 0, 0, 0.5, 0.82, -0.91])
        # x.append([0.5, 0, 0, 0.5, 0.78, -0.77])
        # x.append([0.5, 0, 0, 0.5, 0.65, -0.91])
        # x.append([1, 0, 0.8, 0, 0.82, -0.41])
        # x.append([1, 0.32, 0.65, 0, 0.45, -0.34])
        # x.append([1, 0.43, 0.87, 0, 0.32, -0.15])
        # x.append([1, 0.51, 0.75, 0, 0.77, -0.1])
        # x.append([1, 0.67, 0.75, 0.91, 0.77, 0.89])
        # x.append([1, 0.89, 0.91, 0.99, 0.57, 0.79])
        # x.append([1, 0.9, 0.77, 0.82, 0.83, 0.92])
        # x.append([1, 0.8, 1, 0.91, 0.87, 0.85])
        return x

    # def get_train_input(self, n3=15):
    #     x = []
    #     g = []
    #     mu = 0.25
    #     for t in range(3):
    #         dr = 0.3 if t == 0 else 0
    #         dg = 0.3 if t == 1 else 0
    #         db = 0.3 if t == 2 else 0
    #         for i in range(n3):
    #             r = random.normalvariate(mu+dr, 0.05)
    #             g = random.normalvariate(mu+dg, 0.05)
    #             b = random.normalvariate(mu+db, 0.05)
    #             x.append([t/2, r, g, b])
    #     return x