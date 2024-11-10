import random

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    items_needed = {}
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    for item_name, item_properties in sorted_items:
        div = budget // item_properties["cost"]
        if div > 0:
            items_needed[item_name] = div
        budget %= item_properties["cost"]
    return items_needed


def dp_algorithm(budget):
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    items_list = list(items.items())

    for i in range(1, len(items) + 1):
        _, item_properties = items_list[i - 1]
        for j in range(1, budget + 1):
            if j < item_properties["cost"]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_properties["cost"]] + item_properties["calories"])

    items_needed = {}
    i, j = len(items), budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            items_needed[items_list[i - 1][0]] = items_needed.get(items_list[i - 1][0], 0) + 1
            j -= items_list[i - 1][1]["cost"]
        i -= 1

    return items_needed


def main():
    test_vals = sorted([random.randint(10, 200) for _ in range(5)])

    for budget in test_vals:
        print(f"\nBudget: {budget}")
        print("Greedy Algorithm:")
        print(greedy_algorithm(budget))
        print("Dynamic Programming:")
        print(dp_algorithm(budget))


if __name__ == "__main__":
    main()