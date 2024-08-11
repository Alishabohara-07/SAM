import numpy as np

def kolmogorov_smirnov_test(data, alpha=0.05):
    n = len(data)
    data_sorted = np.sort(data)
    R = np.arange(1, n + 1)
    D_plus = np.max((R - 1) / n - data_sorted)
    D_minus = np.max(data_sorted - R / n)
    D = np.max([D_plus, D_minus])
    Da = np.sqrt(-np.log(alpha / 2) / (2 * n))
    reject = D > Da
    return D, Da, reject

# Example usage:
data = np.random.uniform(size=100)
D, Da, reject = kolmogorov_smirnov_test(data)

print(f"Kolmogorov-Smirnov statistic: {D}")
print(f"Critical value: {Da}")
print(f"Reject null hypothesis: {reject}")
