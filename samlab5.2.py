import numpy as np

# Transition probability matrix
P = np.array([[0.9, 0.1],
              [0.2, 0.8]])

# Calculate the probability after two purchases
P2 = np.dot(P, P)

# Extract the probability of purchasing Coke after two purchases
coke_probability = P2[1, 0]  # Transition from Pepsi to Coke

print("The probability of purchasing Coke after two purchases from now is:", coke_probability)
