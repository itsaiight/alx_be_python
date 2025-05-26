task = input("Enter your task:")
priority = input("Priority (high, medium, low): ").lower()
time_bound = input("Is it time_bound? (yes/no): ").lower()

if priority == "high" and time_bound == "yes":
    print(f"'{task}' is a high priority. It should be addressed immediately.")
elif priority == "high" and time_bound == "no":
    print(f"'{task}' is a high priority but not time-bound. It should be addressed as soon as possible.")
elif priority == "medium" and time_bound == "yes":
    print(f"'{task}' is a medium priority but time-bound task. It should be addressed soon.")
elif priority == "medium" and time_bound == "no":
    print(f"'{task}' is a medium priority. It can be addressed later.")
elif priority == "low" and time_bound == "yes":
    print(f"'{task}' is a low priority but time-bound. It should be addressed soon.")
elif priority == "low" and time_bound == "no":
    print(f"'{task}' is a low priority. It can be addressed at your convenience.")
else:
    print("Invalid input. Please ensure priority is one of 'high', 'medium', or 'low' and time_bound is either 'yes' or 'no'.")
