import numpy as np
import pandas as pd
from distfit import distfit


def test(x):
    model = Test()
    model.testing(x)
    model.plot()

    return model


class Test:
    def testing(self, x):
        self.dist = distfit()
        self.dist.fit_transform(x)

        self.summary = self.dist.summary

    def plot(self):
        self.dist.plot()

