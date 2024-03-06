import random

populations = ['A', 'B', 'C', 'D']
# weights = [10, 500, 15, 100]
cum_weights = (100, 2, 150, 10)

choices = random.choices(populations, cum_weights=cum_weights, k=5)
print(choices)