import numpy as np
import scipy.stats as stats

def calculate_sample_mean(sample_data):
    return np.mean(sample_data)

def calculate_sample_std(sample_data):
    return np.std(sample_data, ddof=1)  # Using Bessel's correction

def calculate_standard_error(sample_std, sample_size):
    return sample_std / np.sqrt(sample_size)

def calculate_margin_of_error(standard_error, confidence_level, sample_size):
    if sample_size > 30:
        z_critical = stats.norm.ppf(1 - (1 - confidence_level) / 2)
        return z_critical * standard_error
    else:
        t_critical = stats.t.ppf(1 - (1 - confidence_level) / 2, df=sample_size-1)
        return t_critical * standard_error

def calculate_confidence_interval(sample_mean, margin_of_error):
    return (sample_mean - margin_of_error, sample_mean + margin_of_error)

def main():
    # Sample data (example)
    sample_data = [10, 12, 23, 23, 16, 23, 21, 16]
    
    # Known population mean (for reference, not used in calculation)
    population_mean = 20
    
    # Confidence level (e.g., 95%)
    confidence_level = 0.95
    
    # Calculate sample statistics
    sample_mean = calculate_sample_mean(sample_data)
    sample_std = calculate_sample_std(sample_data)
    sample_size = len(sample_data)
    standard_error = calculate_standard_error(sample_std, sample_size)
    
    # Calculate margin of error
    margin_of_error = calculate_margin_of_error(standard_error, confidence_level, sample_size)
    
    # Calculate confidence interval
    confidence_interval = calculate_confidence_interval(sample_mean, margin_of_error)
    
    # Output the results
    print(f"Sample Data: {sample_data}")
    print(f"Sample Mean: {sample_mean}")
    print(f"Population Mean: {population_mean}")
    print(f"Sample Standard Deviation: {sample_std}")
    print(f"Standard Error: {standard_error}")
    print(f"Confidence Level: {confidence_level * 100}%")
    print(f"Margin of Error: {margin_of_error}")
    print(f"Confidence Interval: {confidence_interval}")

if __name__ == "__main__":
    main()
