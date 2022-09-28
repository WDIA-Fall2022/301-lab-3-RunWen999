import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=3))

#ask the user for the code of the country and save it into a variable
Country = str(input("Please enter the country code:"))

#Scan the list l line by line and add 1 to the counter if the country is the one looked for
counter = 0
for x in l:
    if x == Country:
        counter += 1

#Format and print the result
print("{} cities were found in {}.".format(counter,Country))

#Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer
done = False
while done == False:
    try:
        p = int(input("please enter the population:"))
        done = True
    except:
        print("please enter a vaild number: ")

#Store the population values into a list called l1 (see line 6)
l1 = list(db.ws(ws='Sheet1').col(col=5))

#Initialize a list lstOfRecords to an empty list
lstOfRecords = []

#Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords
Index = 0
for Index in range(len(l1)):
    if l1[Index] > p:
        lstOfRecords.append(Index)
#Print the list l1
print(lstOfRecords)

#Bonus: Print the name of the cities whose index is in l1
cityname = list(db.ws(ws='Sheet1').col(col=2))
for cn in lstOfRecords:
    print("City whose index in l1 is: " + cityname[cn])
