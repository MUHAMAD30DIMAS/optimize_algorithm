# Optimize Algorithm: PSO & ABC

A Python package for solving optimization problems using two heuristic algorithms:  
**Particle Swarm Optimization (PSO)** and **Artificial Bee Colony (ABC)**.

---

## Features

- Simple implementation of PSO and ABC
- Modular and reusable codebase
- Easy to extend for other optimization problems
- Rastrigin function as demo test case

## Installation

```bash
pip install optimize-algorithm
```
### Usage

Particle Swarm Optimization (PSO):
```
from optimize_algorithm import PSO

#Define your objective function
def rastrigin(x):
    return 10*len(x) + sum([xi**2 - 10 * np.cos(2 * np.pi * xi) for xi in x])

pso = PSO(objective_func=rastrigin, n_particles=30, n_iterations=100, dim=2)
best_pos, best_score = pso.optimize()
print("Best position:", best_pos)
print("Best score:", best_score)

```
Artificial Bee Colony (ABC):
```
from optimize_algorithm import ABC

abc = ABC(objective_func=rastrigin, n_bees=30, n_iterations=100, dim=2)
best_pos, best_score = abc.optimize()
print("Best position:", best_pos)
print("Best score:", best_score)
```
### Documentation
- How PSO Works

- How ABC Works

### Contributing
Pull requests are welcome! Please see CONTRIBUTING.md.

### License
MIT


