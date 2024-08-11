# Define the probabilities
p_rain_tomorrow_given_rain_today = 0.4
p_not_rain_tomorrow_given_rain_today = 0.6
p_rain_tomorrow_given_not_rain_today = 0.2
p_not_rain_tomorrow_given_not_rain_today = 0.8

# Calculate the probability of not raining the day after tomorrow given not raining today
p_not_rain_day_after_tomorrow_given_not_rain_tomorrow = p_not_rain_tomorrow_given_not_rain_today
p_not_rain_day_after_tomorrow_given_rain_tomorrow = p_not_rain_tomorrow_given_rain_today

p_not_rain_day_after_tomorrow_given_not_rain_today = (
    p_not_rain_day_after_tomorrow_given_not_rain_tomorrow * p_not_rain_tomorrow_given_not_rain_today +
    p_not_rain_day_after_tomorrow_given_rain_tomorrow * p_rain_tomorrow_given_not_rain_today
)

print("The probability of not raining the day after tomorrow given not raining today is:", p_not_rain_day_after_tomorrow_given_not_rain_today)
