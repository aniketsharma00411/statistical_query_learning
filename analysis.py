import json
import matplotlib.pyplot as plt
import numpy as np


def load_files():
    with open("results_epsilon_0.01.json", "r") as f:
        epsilon001 = json.load(f)
    with open("results_epsilon_0.05.json", "r") as f:
        epsilon005 = json.load(f)
    with open("results_epsilon_0.1.json", "r") as f:
        epsilon01 = json.load(f)
    with open("results_tau_0.json", "r") as f:
        tau0 = json.load(f)
    with open("results_tau_0.1.json", "r") as f:
        tau01 = json.load(f)
    with open("results_tau_0.2.json", "r") as f:
        tau02 = json.load(f)
    with open("results_eta_0.json", "r") as f:
        eta0 = json.load(f)
    with open("results_eta_0.05.json", "r") as f:
        eta005 = json.load(f)
    with open("results_eta_0.1.json", "r") as f:
        eta01 = json.load(f)

    return epsilon001, epsilon005, epsilon01, tau0, tau01, tau02, eta0, eta005, eta01


if __name__ == "__main__":
    epsilon001, epsilon005, epsilon01, tau0, tau01, tau02, eta0, eta005, eta01 = load_files()

    estimate = []
    epsilon001_mean = []
    epsilon001_ci = []
    epsilon005_mean = []
    epsilon005_ci = []
    epsilon01_mean = []
    epsilon01_ci = []
    tau0_mean = []
    tau0_ci = []
    tau01_mean = []
    tau01_ci = []
    tau02_mean = []
    tau02_ci = []
    eta0_mean = []
    eta0_ci = []
    eta005_mean = []
    eta005_ci = []
    eta01_mean = []
    eta01_ci = []
    for delta_inv in range(10, 21):
        estimate.append((1-((1/delta_inv)**2))/(2*((1/delta_inv)**4)))

        epsilon001_mean.append(np.mean(epsilon001[str(delta_inv)]))
        epsilon001_ci.append(
            1.96 * np.std(epsilon001[str(delta_inv)])/np.sqrt(len(epsilon001[str(delta_inv)])))
        epsilon005_mean.append(np.mean(epsilon005[str(delta_inv)]))
        epsilon005_ci.append(
            1.96 * np.std(epsilon005[str(delta_inv)])/np.sqrt(len(epsilon005[str(delta_inv)])))
        epsilon01_mean.append(np.mean(epsilon01[str(delta_inv)]))
        epsilon01_ci.append(
            1.96 * np.std(epsilon01[str(delta_inv)])/np.sqrt(len(epsilon01[str(delta_inv)])))
        tau0_mean.append(np.mean(tau0[str(delta_inv)]))
        tau0_ci.append(
            1.96 * np.std(tau0[str(delta_inv)])/np.sqrt(len(tau0[str(delta_inv)])))
        tau01_mean.append(np.mean(tau01[str(delta_inv)]))
        tau01_ci.append(
            1.96 * np.std(tau01[str(delta_inv)])/np.sqrt(len(tau01[str(delta_inv)])))
        tau02_mean.append(np.mean(tau02[str(delta_inv)]))
        tau02_ci.append(
            1.96 * np.std(tau02[str(delta_inv)])/np.sqrt(len(tau02[str(delta_inv)])))
        eta0_mean.append(np.mean(eta0[str(delta_inv)]))
        eta0_ci.append(
            1.96 * np.std(eta0[str(delta_inv)])/np.sqrt(len(eta0[str(delta_inv)])))
        eta005_mean.append(np.mean(eta005[str(delta_inv)]))
        eta005_ci.append(
            1.96 * np.std(eta005[str(delta_inv)])/np.sqrt(len(eta005[str(delta_inv)])))
        eta01_mean.append(np.mean(eta01[str(delta_inv)]))
        eta01_ci.append(
            1.96 * np.std(eta01[str(delta_inv)])/np.sqrt(len(eta01[str(delta_inv)])))

    epsilon001_mean = np.array(epsilon001_mean)
    epsilon001_ci = np.array(epsilon001_ci)
    epsilon005_mean = np.array(epsilon005_mean)
    epsilon005_ci = np.array(epsilon005_ci)
    epsilon01_mean = np.array(epsilon01_mean)
    epsilon01_ci = np.array(epsilon01_ci)
    tau0_mean = np.array(tau0_mean)
    tau0_ci = np.array(tau0_ci)
    tau01_mean = np.array(tau01_mean)
    tau01_ci = np.array(tau01_ci)
    tau02_mean = np.array(tau02_mean)
    tau02_ci = np.array(tau02_ci)
    eta0_mean = np.array(eta0_mean)
    eta0_ci = np.array(eta0_ci)
    eta005_mean = np.array(eta005_mean)
    eta005_ci = np.array(eta005_ci)
    eta01_mean = np.array(eta01_mean)
    eta01_ci = np.array(eta01_ci)

    # plt.plot(range(10, 21), estimate)
    plt.plot(range(10, 21), epsilon001_mean,
             color="r", label="$\\epsilon=0.01$")
    plt.fill_between(range(10, 21), (epsilon001_mean-epsilon001_ci),
                     (epsilon001_mean+epsilon001_ci), color="r", alpha=.1)
    plt.plot(range(10, 21), epsilon005_mean,
             color="c", label="$\\epsilon=0.05$")
    plt.fill_between(range(10, 21), (epsilon005_mean-epsilon005_ci),
                     (epsilon005_mean+epsilon005_ci), color="c", alpha=.1)
    plt.plot(range(10, 21), epsilon01_mean, color="m", label="$\\epsilon=0.1$")
    plt.fill_between(range(10, 21), (epsilon01_mean-epsilon01_ci),
                     (epsilon01_mean+epsilon01_ci), color="m", alpha=.1)
    plt.xlabel("$\\delta^{-1}$")
    plt.ylabel("No. of statistical queries used")
    plt.xlim((10, 20))
    # plt.ylim((0, 250))
    plt.xticks(
        range(10, 21),
        ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    )
    plt.legend()

    plt.savefig("epsilon.png")
    plt.clf()

    plt.plot(range(10, 21), tau0_mean, color="r", label="$\\tau=0$")
    plt.fill_between(range(10, 21), (tau0_mean-tau0_ci),
                     (tau0_mean+tau0_ci), color="r", alpha=.1)
    plt.plot(range(10, 21), tau01_mean, color="c", label="$\\tau=0.1$")
    plt.fill_between(range(10, 21), (tau01_mean-tau01_ci),
                     (tau01_mean+tau01_ci), color="c", alpha=.1)
    plt.plot(range(10, 21), tau02_mean, color="m", label="$\\tau=0.2$")
    plt.fill_between(range(10, 21), (tau02_mean-tau02_ci),
                     (tau02_mean+tau02_ci), color="m", alpha=.1)
    plt.xlabel("$\\delta^{-1}$")
    plt.ylabel("No. of statistical queries used")
    plt.xlim((10, 20))
    # plt.ylim((0, 250))
    plt.xticks(
        range(10, 21),
        ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    )
    plt.legend()

    plt.savefig("tau.png")
    plt.clf()

    plt.plot(range(10, 21), eta0_mean, color="r", label="$\\eta=0$")
    plt.fill_between(range(10, 21), (eta0_mean-eta0_ci),
                     (eta0_mean+eta0_ci), color="r", alpha=.1)
    plt.plot(range(10, 21), eta005_mean, color="c", label="$\\eta=0.05$")
    plt.fill_between(range(10, 21), (eta005_mean-eta005_ci),
                     (eta005_mean+eta005_ci), color="c", alpha=.1)
    plt.plot(range(10, 21), eta01_mean, color="m", label="$\\eta=0.1$")
    plt.fill_between(range(10, 21), (eta01_mean-eta01_ci),
                     (eta01_mean+eta01_ci), color="m", alpha=.1)
    plt.xlabel("$\\delta^{-1}$")
    plt.ylabel("No. of statistical queries used")
    plt.xlim((10, 20))
    # plt.ylim((0, 250))
    plt.xticks(
        range(10, 21),
        ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    )
    plt.legend()

    plt.savefig("eta.png")
    plt.clf()
