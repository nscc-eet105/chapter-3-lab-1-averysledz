#Avery Sledz
#Lab 3-1
#6-21-25
print("Numeric Workday Translator")
print("")
day = int(input("Enter in the numeric value of the workday you wish to translate:"))

if day == 1:
    print("The work day is Monday")
elif day == 2:
    print("The work day is Tuesday")
elif day == 3:
    print("The work day is Wednesday")
elif day == 4:
    print(" The work day is Thursday")
elif day == 5:
    print("The work day is Friday")
elif day in [0, 7, 6,]:
    print ("The work day is a weekend")
else:
    print ("The work day is Invalid")
