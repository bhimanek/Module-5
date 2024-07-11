# Part 1: Average Rainfall Calculation

total_months = 0
total_rainfall = 0

# Prompt user for number of years
years = int(input("Enter the number of years: "))

for year in range(1, years + 1):
    print(f"Year {year}")
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall for month {month}: "))
        total_rainfall += rainfall
        total_months += 1

# Calculate average rainfall
average_rainfall = total_rainfall / total_months

# Display results
print(f"\nTotal number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month: {average_rainfall}")
