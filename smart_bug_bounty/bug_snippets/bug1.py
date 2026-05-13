# BUG BOUNTY CASE #1
# Language: Python
# Intended: Return the last N items of a list.
# Current issue: Logic error in slicing index calculation.

def get_last_n_items(items, n):
    """
    Returns the last n elements from the input list.
    """
    if not items or n <= 0:
        return []
    # The +1 below is the intentional bug causing an off-by-one error
    return items[len(items) - n + 1:]

# Testing the function
sample_list = [10, 20, 30, 40, 50]
result = get_last_n_items(sample_list, 3)
print(f"Result for n=3: {result}") 
