task = input("Enter your task:").lower()
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else: print(f"Reminder: {task} is a high priority task!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a meduim priority task that requires immediate attention today!")
        else: print(f"Reminder: {task} is a medium priority task!")
    case "low":
        if time_bound == "yes":
            print(f"Note: {task} is a low priority task that requires immediate attention today!")
        else: print(f"{task} is a low priority task. Consider completing it when you have free time.")