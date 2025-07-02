import numpy as np
from optimize_algorithm import ABC

def cost_function(x):
    ideal_total = 120_000_000
    total = np.sum(x)
    penalty = max(0, total - ideal_total)**2
    underfund_penalty = 0
    if x[0] < 10_000_000:
        underfund_penalty += (10_000_000 - x[0])**2
    return total + 0.1 * penalty + 0.05 * underfund_penalty

# Limit every position
bounds = [
    (5_000_000, 20_000_000),     # Marketing
    (10_000_000, 50_000_000),    # Operasional
    (50_000_000, 100_000_000),   # Salary
    (1_000_000, 10_000_000),     # Maintenance
    (0, 10_000_000)              # Other
]

abc = ABC(func=cost_function, dim=5, bounds=bounds, iterations=10)
abc.optimize()

# Result
print("Best Allocation (ABC):")
for i, val in enumerate(abc.best_position):
    print(f"Pos {i+1}: Rp{val:,.0f}")
print("\nTotal expenses:", np.sum(abc.best_position))
print("Fitness (the smaller the better):", abc.best_fitness)

abc.plot_convergence()