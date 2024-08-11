def calculate_sample_mean(sample_data):
    return sum(sample_data) / len(sample_data)

def calculate_bias(sample_mean, population_mean):
    return sample_mean - population_mean

def main():
    # Sample data (example)
    sample_data = [10, 12, 23, 23, 16, 23, 21, 16]
    
    # Known population mean
    population_mean = 20
    
    # Calculate sample mean
    sample_mean = calculate_sample_mean(sample_data)
    
    # Calculate bias
    bias = calculate_bias(sample_mean, population_mean)
    
    # Output the results
    print(f"Sample Data: {sample_data}")
    print(f"Sample Mean (Point Estimation): {sample_mean}")
    print(f"Population Mean: {population_mean}")
    print(f"Bias: {bias}")

if __name__ == "__main__":
    main()
