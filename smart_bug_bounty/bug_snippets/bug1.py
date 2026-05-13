# Bug Bounty Challenge - Case 1
# This function is intended to return the last N items
# of a given list using Python slicing.
# The developer made a mistake in the index calculation.

def get_last_n_items(items, n):
    # Bug: Incorrect offset calculation
    # Using len(items) - n + 1 skips the correct starting point
    if n <= 0:
        return []
    return items[len(items) - n + 1:]

# Example usage for debugging:
my_list = [10, 20, 30, 40, 50]
# Expected result for n=3 is [30, 40, 50]
# Actual result is [40, 50]
print(f"Result: {get_last_n_items(my_list, 3)}")
