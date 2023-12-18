from environment.rectangle import Rectangle
from sq_oracle import SQOracle
from algo import RectangleAlgo

import json
from tqdm import tqdm


def vary_epsilon(epsilons):
    eta = 0.05
    tau = 0.1
    for epsilon in epsilons:
        query_counts = {}
        for delta_inv in tqdm(range(10, 21)):
            query_counts[str(delta_inv)] = []

            for seed in tqdm(range(150)):
                algo = RectangleAlgo(
                    epsilon=epsilon,
                    minimum=-100,
                    maximum=100,
                    delta=1/delta_inv,
                    random_state=seed
                )
                orc = SQOracle(
                    rectangle=Rectangle(
                        ratio=0.5,
                        eta=eta,
                        minimum=-100,
                        maximum=100,
                        random_state=seed
                    ),
                    n_points=100000,
                    tau=tau,
                    random_state=seed
                )

                algo.fit(orc)

                query_counts[str(delta_inv)].append(algo._count_queries)

        with open(f"results_epsilon_{epsilon}.json", "w") as f:
            json.dump(query_counts, f, indent=4)


def vary_tau(taus):
    epsilon = 0.05
    eta = 0.05
    for tau in taus:
        query_counts = {}
        for delta_inv in tqdm(range(10, 21)):
            query_counts[str(delta_inv)] = []

            for seed in tqdm(range(150)):
                algo = RectangleAlgo(
                    epsilon=epsilon,
                    minimum=-100,
                    maximum=100,
                    delta=1/delta_inv,
                    random_state=seed
                )
                orc = SQOracle(
                    rectangle=Rectangle(
                        ratio=0.5,
                        eta=eta,
                        minimum=-100,
                        maximum=100,
                        random_state=seed
                    ),
                    n_points=100000,
                    tau=tau,
                    random_state=seed
                )

                algo.fit(orc)

                query_counts[str(delta_inv)].append(algo._count_queries)

        with open(f"results_tau_{tau}.json", "w") as f:
            json.dump(query_counts, f, indent=4)


def vary_eta(etas):
    epsilon = 0.05
    tau = 0.1
    for eta in etas:
        query_counts = {}
        for delta_inv in tqdm(range(10, 21)):
            query_counts[str(delta_inv)] = []

            for seed in tqdm(range(150)):
                algo = RectangleAlgo(
                    epsilon=epsilon,
                    minimum=-100,
                    maximum=100,
                    delta=1/delta_inv,
                    random_state=seed
                )
                orc = SQOracle(
                    rectangle=Rectangle(
                        ratio=0.5,
                        eta=eta,
                        minimum=-100,
                        maximum=100,
                        random_state=seed
                    ),
                    n_points=100000,
                    tau=tau,
                    random_state=seed
                )

                algo.fit(orc)

                query_counts[str(delta_inv)].append(algo._count_queries)

        with open(f"results_eta_{eta}.json", "w") as f:
            json.dump(query_counts, f, indent=4)


if __name__ == "__main__":
    vary_epsilon([0.05, 0.1, 0.01])
    vary_tau([0.1, 0, 0.2])
    vary_eta([0.05, 0.1, 0])
