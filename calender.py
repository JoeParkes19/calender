# Calender

def selection():
    global year, months
    print("Please choose your month")
    mth = int(input("> "))

    print("Please Choose your day")
    day = int(input("> "))

    if day < 0 or day > len(year[mth])-1:
        print("Please try again and enter a valid date")
        return selection()
    else:
        return mth, day

def menu():
    print("Choose a task:")
    print("1. Add an event to the calender")
    print("2. View an event on the calender")
    print("3. Delete an event off the calender")
    choice = int(input("> "))
    return choice

def Calender():
    cal = []
    for i in range(12):
        cal.append([])
        for x in range(30):
            cal[i].append(x+1)
    cal[0].append(31)
    cal[1].pop()
    cal[1].pop()
    cal[2].append(31)
    cal[4].append(31)
    cal[6].append(31)
    cal[7].append(31)
    cal[9].append(31)
    cal[11].append(31)
    return cal


months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
year = Calender()

while True:
    choice = menu()
    if choice == 1:
        print("What event would you like to add?")
        event = input("> ")
        month, day = selection()
        year[month][day] = event
        print("Your event is saved.")
    elif choice == 2:
        month, day = selection()
        if year[month][day] == "":
            print("There are no events saved on this day.")
        else:
            print(year[month][day])
    elif choice == 3:
        month, day = selection()
        if year[month][day] == "":
            print("There are no events saved for this day.")
        else:
            print(year[month][day])
            print("Would you like to delete this event? (yes or no)")
            request = input("> ")
            if request == "yes":
                year[month][day] = ""
                print("Event deleted.")
            else:
                print("Event still saved")
    else:
        exit()









