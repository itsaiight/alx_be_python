import datetime
def display_current_datetime():
    #Returns the current date and time in YYYYMMDD HHMMSS.
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date

print(f"Current date and time: {display_current_datetime()}")

def calculate_future_date (future_date):
    #Calculates the date after a specified number of days from today.
    today = datetime.datetime.now()
    future_date = today + datetime.timedelta(days)
    return future_date.strftime("%Y-%m-%d")
days = int(input("Enter the number of days to add: "))
print(f"Future date after {days} days: {calculate_future_date(days)}")

