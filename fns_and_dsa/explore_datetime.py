from datetime import datetime
from datetime import timedelta
current_date = datetime.now()
num_days = int(input("Enter the number of days to add to the current date: "))

def display_current_datetime():
    print(f'Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}')

def calculate_future_date():
    future_date = current_date + timedelta(days=num_days)
    print(f'Future date: {future_date.strftime("%Y-%m-%d")}')
