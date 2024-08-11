import math

def autocorrelation_test(sequence, i, m, alpha=0.05):
    """
    Perform the autocorrelation test on the given sequence with lag m starting from index i.
    
    Parameters:
    sequence (list): The input sequence of numbers.
    i (int): The starting index (1-based index).
    m (int): The lag, or space between the numbers being tested.
    alpha (float): Significance level for the test (default is 0.05).
    
    Returns:
    dict: A dictionary containing the autocorrelation value, standard deviation, test statistic, 
          critical value, and the result of the hypothesis test.
    """
    # Convert 1-based index to 0-based index
    i -= 1
    N = len(sequence)
    
    # Calculate M
    M = (N - i - 1) // m
    
    # Extract the subsequence
    subsequence = [sequence[i + k * m] for k in range(M + 1)]
    
    # Compute autocorrelation
    autocorr_sum = sum(subsequence[k] * subsequence[k + 1] for k in range(M))
    autocorr = (autocorr_sum / (M + 1)) - 0.25
    
    # Compute standard deviation
    sigma = math.sqrt((13 * M + 7) / (12 * (M + 1)))
    
    # Compute the test statistic Z0
    Z0 = autocorr / sigma
    
    # Critical value for two-tailed test at alpha = 0.05
    critical_value = 1.96

    # Determine the result of the hypothesis test
    result = abs(Z0) < critical_value

    return {
        'Autocorrelation': autocorr,
        'Standard Deviation': sigma,
        'Test Statistic Z0': Z0,
        'Critical Value': critical_value,
        'Result': 'Cannot reject the hypothesis of independence' if result else 'Reject the hypothesis of independence'
    }

# Example usage
if __name__ == "__main__":
    sequence = [
        0.12, 0.01, 0.23, 0.28, 0.89, 0.31, 0.64, 0.28, 0.83, 0.93,
        0.99, 0.15, 0.33, 0.35, 0.91, 0.41, 0.60, 0.27, 0.75, 0.88,
        0.68, 0.49, 0.05, 0.43, 0.95, 0.58, 0.19, 0.36, 0.69, 0.87
    ]
    
    i = 3  # Starting index (1-based)
    m = 5  # Lag
    alpha = 0.05  # Significance level

    results = autocorrelation_test(sequence, i, m, alpha)
    
    # Print results
    for key, value in results.items():
        print(f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}")

