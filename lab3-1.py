#Avery Sledz
#Lab 3-1
#6-21-25
print("Numeric Workday Translator")
print("")
day = int(input("Enter in the numeric value of the workday you wish to translate:"))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day in [0, 7, 6,]:
    print ("weekend")
else:
    print ("Invalid")
    
