import numpy as np
from optimize_algorithm import PSO

def cost_function(x):
    ideal_total = 120_000_000
    total = np.sum(x)
    penalty = max(0, total - ideal_total)**2

    # Penalti jika marketing kurang dari 10 juta
    underfund_penalty = 0
    if x[0] < 10_000_000:
        underfund_penalty += (10_000_000 - x[0])**2

    return total + 0.1 * penalty + 0.05 * underfund_penalty

# Pos pengeluaran: [Marketing, Operasional, Gaji, Maintenance, Lain-lain]
bounds = [
    (5_000_000, 20_000_000),     # Marketing
    (10_000_000, 50_000_000),    # Operasional
    (50_000_000, 100_000_000),   # Gaji
    (1_000_000, 10_000_000),     # Maintenance
    (0, 10_000_000)              # Lain-lain
]

pso = PSO(func=cost_function, dim=5, bounds=bounds, iterations=100)

pso.optimize()

print("Best Allocation:")
for i, val in enumerate(pso.gbest_position):
    print(f"Pos {i+1}: Rp{val:,.0f}")

print("\nTotal Pengeluaran:", np.sum(pso.gbest_position))
print("Fitness (Semakin kecil semakin baik):", pso.gbest_value)

pso.plot_convergence()