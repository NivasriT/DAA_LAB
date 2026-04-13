print("NIVASRI T | 24BAD081")
# Fractional Knapsack using Greedy Approach
# Task 1: Create Item Class
class Item:
    def __init__(self, item_id, value, weight):
        self.item_id = item_id
        self.value = value
        self.weight = weight
        self.ratio = value / weight   # Profit/Weight ratio

# Task 2 & 3: Greedy Selection
def fractional_knapsack(items, capacity):

    # Sort items in descending order of ratio
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_profit = 0
    remaining_capacity = capacity

    print("\nItem Selection Summary:")
    print("ID\tWeight Taken\tValue Added\tRemaining Capacity")
    print("-------")

    for item in items:
        if remaining_capacity == 0:
            break

        # If whole item can be taken
        if item.weight <= remaining_capacity:
            weight_taken = item.weight
            value_added = item.value

        # Take fraction of item
        else:
            weight_taken = remaining_capacity
            value_added = item.ratio * weight_taken

        total_profit += value_added
        remaining_capacity -= weight_taken

        print(f"{item.item_id}\t{weight_taken}\t\t{round(value_added,2)}\t\t{remaining_capacity}")

    print("--------")
    print("Maximum Profit =", round(total_profit, 2))

# Main Program
items = [
    Item(1, 60, 10),
    Item(2, 100, 20),
    Item(3, 120, 30)
]

capacity = 50

fractional_knapsack(items, capacity)
