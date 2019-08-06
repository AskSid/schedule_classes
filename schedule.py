# This program is used for students to know what classes they have on different
# days of the school week. It is based off of a 7 block waterfall schedule where
# the student has 6 classes a day.

# The program takes in either a preset name/schedule or the different classes in
# the schedule, and returns what 'day' of the schedule it is that day of the
# week and what classes the student will have.

from datetime import date
from datetime import timedelta

# The class for each day in a schedule
class Day():
    def __init__(self, name, c1, c2, c3, c4, c5, c6):
        self.name = name
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5
        self.c6 = c6

# The function to create a schedule that contains 7 days
def CreateSchedule(c):
    c = c.split(", ")

    d1 = Day("Day 1", c[0], c[1], c[2], c[3], c[4], c[5])
    d2 = Day("Day 2", c[6], c[0], c[1], c[2], c[3], c[4])
    d3 = Day("Day 3", c[5], c[6], c[0], c[1], c[2], c[3])
    d4 = Day("Day 4", c[4], c[5], c[6], c[0], c[1], c[2])
    d5 = Day("Day 5", c[3], c[4], c[5], c[6], c[0], c[1])
    d6 = Day("Day 6", c[2], c[3], c[4], c[5], c[6], c[0])
    d7 = Day("Day 7", c[1], c[2], c[3], c[4], c[5], c[6])

    schedule = [d1, d2, d3, d4, d5, d6, d7]
    return schedule

# The variables needed for the today function. startDate is the first date to
# start the function. startDay is the day of the schedule on startDate. today is
# just the date today
startDate = date(2018, 10, 24)
startDay = 5
today = date.today()
passdays = [(2018, 10, 25)]

# The function to find out what day of the schedule it is today
def Today(startDate, startDay, today, schedule):
    while startDate != today:
        if startDate + timedelta(days = 1) in passdays:
            startDate += timedelta(days = 1)
        else:
            if startDate.weekday() == 4:
                startDate += timedelta(days = 1)

            elif startDate.weekday() == 5:
                startDate += timedelta(days = 1)

            else:
                if startDay == 7:
                    startDay = 1
                    startDate += timedelta(days = 1)

                else:
                    startDay += 1
                    startDate += timedelta(days = 1)

    dayToday = schedule[startDay - 1]
    print("Today is %s" % (dayToday.name))
    print("You have %s, %s, %s, %s, %s, and %s today" % (dayToday.c1, dayToday.c2 ,dayToday.c3, dayToday.c4, dayToday.c5, dayToday.c6))


# The preset for Sid's classes
SidClasses = "Spanish, History, Math, English, AP Biology, Chemistry, Gym"
SidSchedule = CreateSchedule(SidClasses)

# The starting sequence
def StartSchedule():
    name = input("What is your name? ")
    if name == "Sid":
        Today(startDate, startDay, today, SidSchedule)

    else:
        c = input("List your 7 classes separated by commas: ")
        schedule = CreateSchedule(c)
        Today(startDate, startDay, today, schedule)


StartSchedule()
