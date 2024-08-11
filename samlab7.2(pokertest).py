import scipy.stats as stats

def poker_test():
    TAB_CHISQUARE_4D = 9.49
    TAB_CHISQUARE_3D = 5.99

    print("Please choose your test:")
    print("1. Three digit poker test")
    print("2. Four digit poker test")
    num = int(input())

    if num == 2:
        # Four digit poker test
        print("\nHow many numbers did you generate:")
        n = int(input())

        print("\nEnter the observed frequencies of: ")
        print("Four different digits:")
        four_diff = int(input())

        print("Four same digits:")
        four_of_a_kind = int(input())

        print("Three of a kind:")
        three_of_a_kind = int(input())

        print("One Pair:")
        one_pair = int(input())

        print("Two Pair:")
        two_pair = int(input())

        if (four_diff + four_of_a_kind + three_of_a_kind + one_pair + two_pair) != n:
            print(f"\nThe sum is not equal to {n}")
        else:
            probabilities_4d = [0.504, 0.001, 0.036, 0.432, 0.027]
            observed_frequency_4d = [four_diff, four_of_a_kind, three_of_a_kind, one_pair, two_pair]
            expected_frequency_4d = [p * n for p in probabilities_4d]

            print("----------------------------------------------------------------------")
            print("\nThe Observed frequencies are:")
            print("\t", "\t".join(map(str, observed_frequency_4d)))

            print("\nAnd their respective expected frequencies are:")
            print("\t", "\t".join(map(lambda x: str(int(x)), expected_frequency_4d)))

            CAL_CHISQUARE = sum(((obs - exp) ** 2) / exp for obs, exp in zip(observed_frequency_4d, expected_frequency_4d))
            print("----------------------------------------------------------------------")
            print(f"\n \n The sum of calculated chi square statistics is : {CAL_CHISQUARE:.2f}")

            print(f"\n The tabulated value for chi square is {TAB_CHISQUARE_4D}")
            if CAL_CHISQUARE <= TAB_CHISQUARE_4D:
                print("\n\nSo, the generated random numbers are independent.")
            else:
                print("\n\nSo, the generated random numbers are not independent.")

    elif num == 1:
        # Three digit poker test
        print("\nHow many numbers did you generate:")
        n = int(input())

        print("\nEnter the observed frequencies of: ")
        print("Three different digits:")
        three_diff = int(input())

        print("Three same digits:")
        three_of_a_kind = int(input())

        print("One Pair:")
        one_pair = int(input())

        if (three_diff + three_of_a_kind + one_pair) != n:
            print(f"\nThe sum is not equal to {n}")
        else:
            probabilities_3d = [0.72, 0.01, 0.27]
            observed_frequency_3d = [three_diff, three_of_a_kind, one_pair]
            expected_frequency_3d = [p * n for p in probabilities_3d]

            print("\nThe Observed frequencies are:")
            print("\t", "\t".join(map(str, observed_frequency_3d)))

            print("\nAnd their respective expected frequencies are:")
            print("\t", "\t".join(map(lambda x: str(int(x)), expected_frequency_3d)))

            CAL_CHISQUARE = sum(((obs - exp) ** 2) / exp for obs, exp in zip(observed_frequency_3d, expected_frequency_3d))
            
            print(f"\n \n The sum of calculated chi square statistics is : {CAL_CHISQUARE:.2f}")

            print(f"\n The tabulated value for chi square is {TAB_CHISQUARE_3D}")
            if CAL_CHISQUARE <= TAB_CHISQUARE_3D:
                print("\n\nSo, the generated random numbers are independent.")
            else:
                print("\n\nSo, the generated random numbers are not independent.")
    else:
        print("\nPlease choose either 1 or 2")

if __name__ == "__main__":
    poker_test()
