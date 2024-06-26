task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task, but try to do this on time!")
        else:
            print(f"Reminder: '{task}' is a medium priority. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task, but try to do this on time!")
        else:
            print(f"Reminder: '{task}' is a low priority. Consider completing it when you have free time.")