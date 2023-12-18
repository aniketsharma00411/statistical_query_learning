import random
import sys


class Rectangle:
    def __init__(self, ratio=0.5, eta=0.1, minimum=None, maximum=None, random_state=None) -> None:
        """
        ratio: Ratio of positive points. The number of positive points will be n*ratio where n is the total number of points.
        eta: Noise factor
        minimum: Minimum value any point can take. If None it will take -sys.maxsize
        (An integer giving the maximum value a variable of type Py_ssize_t can take. It's usually 2**31 - 1 on a 32-bit platform and 2**63 - 1 on a 64-bit platform.
        [https://docs.python.org/3/library/sys.html#sys.maxsize])
        maximum: Maximum value any point can take. If None it will take sys.maxsize
        random_state: Seed for random number generator
        """

        assert ratio > 0 and ratio < 1
        assert eta >= 0 and eta <= 1
        self._ratio = ratio
        self._eta = eta
        self._min = minimum if minimum is not None else -sys.maxsize
        self._max = maximum if maximum is not None else sys.maxsize

        random.seed(random_state)

        x_points = None
        while x_points is None or x_points[0] == x_points[1]:
            x_points = sorted([random.uniform(self._min, self._max),
                               random.uniform(self._min, self._max)])
        y_points = None
        while y_points is None or y_points[0] == y_points[1]:
            y_points = sorted([random.uniform(self._min, self._max),
                               random.uniform(self._min, self._max)])
        self.target_rectangle = (
            (x_points[0], y_points[0]), (x_points[1], y_points[1]))

    def generate(self, n_points):
        self._n_points = int(n_points)

        points = []
        for _ in range(int(self._n_points*self._ratio)):
            point = (random.uniform(self.target_rectangle[0][0], self.target_rectangle[1][0]), random.uniform(
                self.target_rectangle[0][1], self.target_rectangle[1][1]))

            points.append((point, 1))

        for _ in range(self._n_points - int(self._n_points*self._ratio)):
            if random.random() < 0.5:
                if random.random() < 0.5:
                    point = (random.uniform(self._min, self.target_rectangle[0][0]), random.uniform(
                        self._min, self.target_rectangle[0][1]))
                else:
                    point = (random.uniform(self._min, self.target_rectangle[0][0]), random.uniform(
                        self.target_rectangle[1][1], self._max))
            else:
                if random.random() < 0.5:
                    point = (random.uniform(self.target_rectangle[1][0], self._max), random.uniform(
                        self._min, self.target_rectangle[0][1]))
                else:
                    point = (random.uniform(self.target_rectangle[1][0], self._max), random.uniform(
                        self.target_rectangle[1][1], self._max))

            points.append((point, -1))

        assert len(points) == self._n_points

        random.shuffle(points)

        X = []
        label = []
        for i in range(self._n_points):
            X.append(points[i][0])
            if random.random() < self._eta:
                label.append(1 if points[i][1] == -1 else -1)
            else:
                label.append(points[i][1])

        assert len(X) == self._n_points and len(label) == self._n_points

        return X, label


if __name__ == "__main__":
    rectangle = Rectangle(minimum=-10, maximum=10)

    print(rectangle.generate(100))
    print(rectangle.target_rectangle)
