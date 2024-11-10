import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

TEST_VALS = {
    2: 0.0278,  # 1/36
    3: 0.0556,  # 2/36
    4: 0.0833,  # 3/36
    5: 0.1111,  # 4/36
    6: 0.1389,  # 5/36
    7: 0.1667,  # 6/36
    8: 0.1389,  # 5/36
    9: 0.1111,  # 4/36
    10: 0.0833, # 3/36
    11: 0.0556, # 2/36
    12: 0.0278  # 1/36
}


def roll_dices():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return (dice1, dice2, dice1 + dice2)


def roll_dices_n_times(n):
    res = {}
    for _ in range(n):
        _, _, total = roll_dices()
        if total not in res:
            res[total] = 0
        res[total] += 1
    for key, value in res.items():
        res[key] = value / n
    return {key: res[key] for key in sorted(res.keys())}


def plot_simulations(simulations, test_vals):
    rows = 4
    cols = 3
    fig, axs = plt.subplots(rows, cols, figsize=(15, 10))

    for i, num in enumerate(range(2, 13)):
        x = []
        y_sim = []
        y_test = []
        for simulation, result in simulations.items():
            x.append(simulation)
            y_sim.append(result[num])
            y_test.append(test_vals[num])

        axs[i // cols, i % cols].plot(x, y_sim, label='Simulation')
        axs[i // cols, i % cols].plot(x, y_test, label='Test')
        axs[i // cols, i % cols].set_xlabel('Number of simulations')
        axs[i // cols, i % cols].set_ylabel(f'Probability of sum {num}')
        axs[i // cols, i % cols].legend()
        axs[i // cols, i % cols].yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))

    plt.tight_layout()
    plt.subplots_adjust(wspace=0.3, hspace=0.4)
    plt.show()


def main():
    test_nums = [100, 1000, 10000, 100000, 1000000, 10000000]
    simulations = {}
    for num in test_nums:
        simulations[num] = roll_dices_n_times(num)
        print(f"{simulations[num]}")

    plot_simulations(simulations, TEST_VALS)


if __name__ == "__main__":
    main()
