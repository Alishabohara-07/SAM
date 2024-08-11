import random

def monte_carlo_area(n, a, b, c, d):
  """
  Estimates the area under the curve using Monte Carlo Simulation.

  Args:
    n: The number of random points to generate.
    a, b: The x-coordinates of the left and right endpoints of the curve.
    c, d: The y-coordinates of the left and right endpoints of the curve.

  Returns:
    The estimated area under the curve.
  """
  inside_curve = 0

  for i in range(n):
    x = random.uniform(a, b)
    y = random.uniform(0, 1)

    if y <= (d - c) * x / (b - a) + c:
      inside_curve += 1

  return (b - a) * (inside_curve / n)

# Set the number of random points to generate
n = 1000000

# Set the endpoints of the curve
a = 0
b = 1
c = 0
d = 1

# Estimate the area under the curve
area_estimate = monte_carlo_area(n, a, b, c, d)

print(f"Estimated area under the curve: {area_estimate:.4f}")
