import numpy as np
from collections import Counter

def poker_hand_test(sequence, hand_size=5):
    # Count the frequency of each poker hand
    hand_counts = Counter(tuple(sorted(sequence[i:i + hand_size])) for i in range(len(sequence) - hand_size + 1))
    
    return hand_counts

def chi_square_test(observed, expected):
    """ Perform a Chi-Square test given observed and expected frequencies """
    chi2 = sum((observed.get(k, 0) - expected.get(k, 0)) ** 2 / expected.get(k, 1) for k in set(observed) | set(expected))
    dof = len(expected) - 1
    return chi2, dof

# Example usage
np.random.seed(0)  # For reproducibility

# Generate a random sequence of numbers (cards), e.g., values from 1 to 13 (like poker cards)
sequence = np.random.randint(1, 14, size=1000)  # 1000 cards

# Define expected hand frequencies (for simplicity, assume uniform distribution)
expected_frequencies = {
    (1, 1, 1, 1, 1): 100,  # Example: For a hand with 5 of a kind
    (1, 1, 1, 1, 2): 150,  # Example: For a hand with 4 of a kind
    # Add other expected hand patterns and frequencies here
}

# Perform the poker hand test
hand_counts = poker_hand_test(sequence)
print("Observed Hand Counts:", hand_counts)

# Perform Chi-Square Test
chi2, dof = chi_square_test(hand_counts, expected_frequencies)
print("Chi-Square Statistic:", chi2)
print("Degrees of Freedom:", dof)

# Interpretation
alpha = 0.05
from scipy.stats import chi2 as chi2_dist
p_value = 1 - chi2_dist.cdf(chi2, dof)

if p_value < alpha:
    print("Reject the null hypothesis - The sequence is not random.")
else:
    print("Fail to reject the null hypothesis - The sequence appears to be random.")
s
