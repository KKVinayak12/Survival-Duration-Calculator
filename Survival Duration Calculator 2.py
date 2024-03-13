#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Survival_Calculator(age, time_unit):
    print("*****Welcome to Survival Duration Calculator******")
    if time_unit.lower() == 'months' or time_unit == 'M':
        duration = age * 12
        return f"You lived for {duration} Months"
    elif time_unit.lower() == 'weeks' or time_unit.lower() == 'w':
        duration = age * 52
        return f"You lived for {duration} Weeks"
    elif time_unit.lower() == 'days' or time_unit.lower() == 'd':
        duration = age * 365
        return f"You lived for {duration} Days"
    elif time_unit.lower() == 'hours' or time_unit.lower() == 'h':
        duration = age * 365 * 24
        return f"You lived for {duration} Hours"
    elif time_unit.lower() == 'minutes' or time_unit.lower() == 'm':
        duration = age * 365 * 24 * 60
        return f"You lived for {duration} Minutes"
    elif time_unit.lower() == 'seconds' or time_unit.lower() == 's':
        duration = age * 365 * 24 * 60 * 60
        return f"You lived for {duration} Seconds"
    else:
        return "Invalid Input"


def main():
    age = int(input("What's your age? "))
    time_unit = input("Please choose time unit: Months, Weeks, Days, Hours, Minutes, Seconds. \nNote: You can write the first letter (Use Captical M for Months) or the full name of the time unit. ")
    duration = Survival_Calculator(age, time_unit)
    print(duration)
    
if __name__ == "__main__":
    main()


# In[ ]:




