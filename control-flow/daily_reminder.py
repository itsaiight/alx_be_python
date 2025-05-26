task = input("Enter your task:")
priority = input("Priority (high, medium, low): ").lower()
time_bound = input("Is it time_bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Task '{task}' is a high priority and time-bound task. It should be addressed immediately.")
        else:
            print(f"Task '{task}' is a high priority but not time-bound. It should be addressed as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Task '{task}' is a medium priority and time-bound task. It should be addressed soon.")
        else:
            print(f"Task '{task}' is a medium priority but not time-bound. It can be addressed later.")
    case "low":
        if time_bound == "yes":
            print(f"Task '{task}' is a low priority and time-bound task. It should be addressed soon.")
        else:
            print(f"Task '{task}' is a low priority but not time-bound. It can be addressed at your convenience.")
    case _:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
        
