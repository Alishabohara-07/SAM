import math

def poisson_distribution(x, lamda):
  """
  Calculates the probability of x events in a Poisson distribution.

  Args:
    x: The number of events.
    lamda: The average number of events.

  Returns:
    The probability of x events.
  """
  return (math.exp(-lamda) * (lamda**x)) / math.factorial(x)

# Set the average number of events (lamda)
lamda = 12

# Calculate the probability for each value of x
for x in range(16):
  probability = poisson_distribution(x, lamda)
  print(f"x = {x}, Probability: {probability:.4f}")
