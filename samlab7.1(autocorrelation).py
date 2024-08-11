import numpy as np

def autocorrelation_test(random_numbers, lag, start_index):
    N = len(random_numbers)
    M = (N - start_index - lag) // lag

    if M < 1:
        raise ValueError("M must be at least 1. Increase N or decrease the lag.")

    Pim = 0.0
    for k in range(M):
        Pim += random_numbers[start_index + k * lag] * random_numbers[start_index + (k + 1) * lag]
    Pim = Pim / M - 0.25

    sigma_im = np.sqrt((13 * M + 7) / (12 * (M + 1)))
    z0 = Pim / sigma_im
    
    return Pim, z0

def main():
    # Example list of random numbers
    random_numbers = [
        0.54, 0.73, 0.89, 0.28, 0.66, 0.37, 0.55, 0.61, 0.29, 0.14,
        0.58, 0.93, 0.75, 0.44, 0.22, 0.69, 0.35, 0.82, 0.10, 0.79
    ]
    
    try:
        lag = int(input("Enter the lag value for the autocorrelation test: "))
        start_index = int(input("Enter the start index for the autocorrelation test: "))

        if start_index < 0 or start_index >= len(random_numbers):
            print("Invalid start index. It must be between 0 and the length of the random number sequence minus 1.")
            return
        
        Pim, z0 = autocorrelation_test(random_numbers, lag, start_index)
        print(f"Autocorrelation coefficient Pim for lag {lag} and start index {start_index}: {Pim:.2f}")
        print(f"Test statistic z0: {z0:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
