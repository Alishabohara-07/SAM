import random

def monte_carlo_pi(n):
  """
  Estimates the value of PI using Monte Carlo Simulation.

  Args:
    n: The number of random points to generate.

  Returns:
    The estimated value of PI.
  """
  inside_circle = 0

  for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
      inside_circle += 1

  return 4 * (inside_circle / n)

# Set the number of random points to generate
n = 100000

# Estimate the value of PI
pi_estimate = monte_carlo_pi(n)

print(f"Estimated value of PI: {pi_estimate:.4f}")
