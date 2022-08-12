'''#Task 

for i in range(3):

    z=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))

    if z > y:
            print("The first number is greater than the second")
    if y > z:
        print("The second number is greater than the first")
    if z >= y:
        print("The first number is either greater or equal")
    if y >= z:
        print("The second number greater or equal than the first:")
    if z != y:
        print("The first number is not equal to the second")
    if    y != z:
        print("The second numer is not equal to the first")
    if 10 > y > 100:
        print("This checks if the number is in the range ") '''
                                                                          
#Task 2

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")
 
if month_name == "February":
    print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
    print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 day")
else:
    print("Wrong month name")