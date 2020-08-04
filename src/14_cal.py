"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime
import pandas as pd

# print(datetime.now().month)
# cy = datetime.now().year
# cm = datetime.now().month

# needs to be printed out to terminal to look like a regular calendar.
if len(sys.argv) == 2:
  cm = int(sys.argv[1])
elif len(sys.argv) == 3:
  cm = int(sys.argv[1])
  cy = int(sys.argv[2])
else:
  cy = datetime.now().year
  cm = datetime.now().month
# making a list of each day for the values to be added to.
mon = []
tues = []
wed = []
thurs = []
fri = []
sat = []
sun = []
#making another list for the months to make below print statement nicer to read.
months = ['January', 'February', 'March', 'April', 'May',
          'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(f"A calendar for {months[cm-1]}, {cy}.")
for item in calendar.monthcalendar(year=cy, month=cm):
  mon.append(item[0])
  tues.append(item[1])
  wed.append(item[2])
  thurs.append(item[3])
  fri.append(item[4])
  sat.append(item[5])
  sun.append(item[6])

cal_dict = {'Mon': mon,
            'Tues': tues,
            'Wed': wed,
            'Thurs': thurs,
            'Fri': fri,
            'Sat': sat,
            'Sun': sun}
df = pd.DataFrame(cal_dict)
# calendar.prmonth()
print(df)