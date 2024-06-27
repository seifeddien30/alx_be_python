task = input("Enter your task:").lower()
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
            reminder = f"Reminder: {task} is a high priority task"
    case _:
          reminder = f"Note: {task} is a {priority} task"
if time_bound == "yes":
      reminder += " that requires immediate attention today!"
else:
      reminder += " Consider completing it when you have free time."
print(reminder)