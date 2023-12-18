from environment.rectangle import Rectangle

import random


class SQOracle:
    def __init__(self, rectangle, n_points, tau=0.1, random_state=None) -> None:
        self._rectangle = rectangle
        self._n_points = n_points
        self._tau = tau

        random.seed(random_state)

        self._points, self._labels = self._rectangle.generate(self._n_points)

        assert len(self._points) == self._n_points and len(
            self._labels) == self._n_points

    def _predict(self, predictor, point):
        if point[0] < predictor[0][0] or point[0] > predictor[1][0]:
            return -1
        elif point[1] < predictor[0][1] or point[1] > predictor[1][1]:
            return -1
        else:
            return 1

    def statistical_query(self, point, true_label, predictor):
        return 1 if true_label == self._predict(predictor, point) else -1

    def query(self, predictor):
        sq_outputs = [self.statistical_query(
            self._points[i], self._labels[i], predictor) for i in range(self._n_points)]

        expectation = sum(sq_outputs)/len(sq_outputs)

        return random.uniform(expectation-self._tau, expectation+self._tau)


if __name__ == "__main__":
    orc = SQOracle(Rectangle(minimum=-10, maximum=10), 100)
