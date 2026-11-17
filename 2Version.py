from datetime import datetime

event = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event = event.strip().upper()

date = datetime(year, month, day)

print("\nFormatted Output:")
print("Event:", event)
print("Date:", date.strftime("%B %d, %Y"))
print("Year:", year)
print("Month:", date.strftime("%B"))
print("Day:", day)
print("Weekday:", date.strftime("%A"))
