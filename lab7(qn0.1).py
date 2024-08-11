import numpy as np
from math import erf, sqrt, pi

def normal_cdf(z):
    """
    Compute the cumulative distribution function of the standard normal distribution.
    This function approximates the CDF using the error function.
    """
    return 0.5 * (1 + erf(z / sqrt(2)))

def autocorrelation_test(data, i, m, alpha=0.05):
    """
    Perform an autocorrelation test on the given data.

    Parameters:
    - data (array-like): The sequence of numbers
    - i (int): The starting index (1-based index)
    - m (int): The lag
    - alpha (float, optional): The significance level (default: 0.05)

    Returns:
    - rho (float): The autocorrelation coefficient
    - sigma_rho (float): The standard error of the autocorrelation coefficient
    - z_score (float): The z-score of the autocorrelation coefficient
    - p_value (float): The p-value of the test
    - reject_null (bool): Whether to reject the null hypothesis of independence
    """
    N = len(data)
    M = int((N - i) / m) - 1  # Number of pairs to be considered

    # Compute the autocorrelation coefficient
    rho = 0
    for k in range(M + 1):
        rho += data[i + k * m] * data[i + (k + 1) * m]
    
    # Normalize and subtract 0.25
    rho = (rho / (M + 1)) - 0.25

    # Compute the standard error
    sigma_rho = sqrt((13 * M + 7) / (12 * M * (M + 1)))
    
    # Compute the z-score
    z_score = rho / sigma_rho
    
    # Compute the p-value manually
    p_value = 2 * (1 - normal_cdf(abs(z_score)))
    
    # Determine whether to reject the null hypothesis
    reject_null = p_value < alpha
    
    return rho, sigma_rho, z_score, p_value, reject_null

# Example usage:
data = np.array([0.12, 0.01, 0.23, 0.28, 0.89, 0.31, 0.64, 0.28, 0.83, 0.93,
                  0.99, 0.15, 0.33, 0.35, 0.91, 0.41, 0.60, 0.27, 0.75, 0.88,
                  0.68, 0.49, 0.05, 0.43, 0.95, 0.58, 0.19, 0.36, 0.69, 0.87])
i = 3  # Starting index (1-based)
m = 5  # Lag

# Adjust index for 0-based indexing in Python
i -= 1

rho, sigma_rho, z_score, p_value, reject_null = autocorrelation_test(data, i, m)
print(f"Autocorrelation coefficient (rho): {rho:.4f}")
print(f"Standard error of rho (sigma_rho): {sigma_rho:.4f}")
print(f"Z-score: {z_score:.4f}")
print(f"P-value: {p_value:.4f}")
print(f"Reject null hypothesis of independence: {reject_null}")
