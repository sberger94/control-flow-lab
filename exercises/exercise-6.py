# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

input_month = input("Enter the month of the year (Jan - Dec): ")
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
months_31 = ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']
months_30 = ['apr', 'jun', 'sep', 'nov']

while input_month.lower() not in months:
    print("I don't recognize that month!")
    input_month = input("Enter the month of the year (Jan - Dec): ")

input_day = int(input("Enter the day of the month: "))

if input_month.lower() in months_31:   
    while input_day not in range(1, 32):
        print("Please choose a valid day")
        input_day = int(input("Enter the day of the month: "))
elif input_month.lower() in months_30:
    while input_day not in range(1, 31):
        print("Please choose a valid day")
        input_day = int(input("Enter the day of the month: "))
else:
    while input_day not in range(1, 30):
        print("Please choose a valid day")
        input_day = int(input("Enter the day of the month: "))

if (input_month.lower() == 'dec' and input_day >= 21) or input_month.lower() in ['jan', 'feb'] or (input_month.lower() == 'mar' and input_day <= 19):
    season = 'Winter'
elif (input_month.lower() == 'mar' and input_day >= 20) or input_month.lower() in ['apr', 'may'] or (input_month.lower() == 'jun' and input_day <= 20):
    season = 'Spring'
elif (input_month.lower() == 'jun' and input_day >= 21) or input_month.lower() in ['jul', 'aug'] or (input_month.lower() == 'sep' and input_day <= 21):
    season = 'Summer'
else:
    season = 'Fall'

print(f"{input_month.capitalize()} {input_day} is in {season}")