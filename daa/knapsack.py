def knapsack(W, wt, val, n):
    # Create a 2D array to store the maximum value for each subproblem
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table K[][] in a bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Store the result of the Knapsack
    res = K[n][W]
    print(f"The maximum value that can be put in the knapsack is {res}")

    # Find which items are included in the knapsack
    w = W
    items_included = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        # Either the result comes from the top (K[i-1][w]) or from (val[i-1] + K[i-1][w-wt[i-1]]) as in Knapsack table. If it comes from the latter one, it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:
            # This item is included
            items_included.append(i - 1)

            # Since this weight is included, its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]

    print("Items included in the knapsack (0-indexed):")
    for i in items_included:
        print(f"Item {i}: Value = {val[i]}, Weight = {wt[i]}")


# User input for number of items
n = int(input("Enter the number of items: "))

# Lists to store weights and values of items
val = []
wt = []

print("Enter the value and weight of each item:")
for _ in range(n):
    v, w = map(int, input().split())
    val.append(v)
    wt.append(w)

# User input for the capacity of the knapsack
W = int(input("Enter the capacity of the knapsack: "))

# Compute and print the maximum value that can be put in the knapsack
knapsack(W, wt, val, n)
