#Task: In this task, we are going to write a program test6.py that reports Consumer Price Index and its average value for any year selected by the user. 
# Additionally, the user will be able to choose the months of the year they want to display. 
# The program will have to use list comprehension for transforming the list of months into the list of corresponding CPI values.

import urllib.request, shelve

# Step-by-step implementation:
#Use urllib.request to download CPI data from http://nancymcohen.com/csci133/cpiai.txt.
#Provide a user interface to look up the CPI values for any year. 
# The program should read a year number from the keyboard and print out the list of CPI values for that year. 
# After that, it should print out the average CPI for that year (by computing the average of the reported list).

url = 'https://futureboy.us/frinkdata/cpiai.txt'
response = urllib.request.urlopen(url)
lines = response.readlines()
cpi = {}
for line in lines:
    items = line.decode().split()
    if len(items) > 0 and items[0].isdigit():
        cpi[int(items[0])] = [float(item) for item in items[:13]]  # index 0 = year, 1–12 = months

shelf = shelve.open('cpi')
shelf['cpi'] = cpi
shelf.close()
shelf = shelve.open('cpi')
cpi = shelf['cpi']

#Enhance the program by allowing the user to specify the list of months they want to see. 
# A valid query may in addition to the year number contain a list of month numbers separated by spaces.
#For example, 1950 1 3 5 7 requests the data for January, March, May, and July of 1950. 
# If the months are not specified, report full year. The average should be computed only for the reported months.

while True:
    query = input("Enter query: ")
    if query == "":
        break

    parts = query.split()
    year = int(parts[0])

    if year not in cpi:
        print("Year not found.")
        continue

    if len(parts) == 1:
        values = cpi[year][1:]
    else:
        months = [int(m) for m in parts[1:]]
        values = [cpi[year][m] for m in months] #step 4

    total = 0
    for value in values:
        total += value
    average = total / len(values)

    print(values, average)

shelf.close()
