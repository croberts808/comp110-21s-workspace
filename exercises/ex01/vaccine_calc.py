"""A vaccination calculator."""

__author__ = "730439833"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

# What we ask the user for
population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target: int = int(input("Target percent vaccinated: "))


# Definitions for calculation
people_already_vaccinated: float = doses_administered / 2
people_we_want_vaccinated: int = round((target / 100) * population)
people_need_to_vaccinate: float = people_we_want_vaccinated - people_already_vaccinated
how_many_vaccinate_day: int = round(doses_per_day / 2)
days_it_will_take: int = round(people_need_to_vaccinate / how_many_vaccinate_day)  
# This is for printing in the string concatenation
days: timedelta = timedelta(days_it_will_take)  
# This is for calculating date_will_fall_on using correct format
today: datetime = datetime.today()
total_date: datetime = today + days 


# Output
print(
    "We will reach " + str(target) + "% vaccination in " + str(days_it_will_take),
    "days, which falls on " + str(total_date.strftime("%B %d, %Y") + ".")
)