from environment.rectangle import Rectangle
from sq_oracle import SQOracle

from copy import deepcopy
import random
import warnings


class RectangleAlgo:
    def __init__(self, epsilon, minimum, maximum, delta, max_iter=100000, random_state=None) -> None:
        assert delta > 0
        self._epsilon = epsilon
        self._min = minimum
        self._max = maximum
        self._delta = delta
        self._max_iter = max_iter

        self._count_queries = None

        random.seed(random_state)

        x_points = None
        while x_points is None or x_points[0] == x_points[1]:
            x_points = sorted([random.uniform(self._min, self._max),
                               random.uniform(self._min, self._max)])
        y_points = None
        while y_points is None or y_points[0] == y_points[1]:
            y_points = sorted([random.uniform(self._min, self._max),
                               random.uniform(self._min, self._max)])
        self._predictor = [[x_points[0], y_points[0]],
                           [x_points[1], y_points[1]]]

    def _valid(self, temp_predictor):
        if temp_predictor[0][0] < self._min or temp_predictor[0][1] < self._min or temp_predictor[1][0] < self._min or temp_predictor[1][1] < self._min:
            return False
        elif temp_predictor[0][0] > self._max or temp_predictor[0][1] > self._max or temp_predictor[1][0] > self._max or temp_predictor[1][1] > self._max:
            return False
        elif temp_predictor[0][0] >= temp_predictor[1][0] or temp_predictor[0][1] >= temp_predictor[1][1]:
            return False
        else:
            return True

    def fit(self, sq_oracle):
        self._sq_oracle = sq_oracle
        self._count_queries = 0

        nu = float("inf")
        count = 0
        while abs(1 - nu) > self._epsilon:
            if count > self._max_iter:
                warnings.warn(
                    "WARNING: Did not converge. Maximum iteration reached.")
                break
            count += 1
            change = random.sample(
                list(self._frange(self._min, self._max, (self._max-self._min)*self._delta)), 1)[0]

            temp_predictor = deepcopy(self._predictor)
            if random.random() < 0.5:
                if random.random() < 0.5:
                    temp_predictor[0][0] += change
                else:
                    temp_predictor[0][1] += change
            else:
                if random.random() < 0.5:
                    temp_predictor[1][0] += change
                else:
                    temp_predictor[1][1] += change

            if not self._valid(temp_predictor):
                continue

            temp_nu = sq_oracle.query(temp_predictor)
            self._count_queries += 1

            if abs(1-temp_nu) < abs(1-nu):
                nu = temp_nu
                self._predictor = temp_predictor

    def _frange(self, start, stop, step):
        while start < stop:
            yield start
            start += step


if __name__ == "__main__":
    algo = RectangleAlgo(0.1, -10, 10, 1, 0.1, random_state=42)
    orc = SQOracle(Rectangle(eta=0.05, minimum=-10, maximum=10,
                   random_state=42), 10000, 0.01, random_state=42)
    algo.fit(orc)

    print(algo._predictor)
    print(algo._count_queries)
