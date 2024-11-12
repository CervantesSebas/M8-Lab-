#Sebastian Cervantes 
#November 12, 2024 
#Tells user true is the year is a leap year, tells user false if not a leap year
year = int(input("What year: "))

if year % 4 == 0: 
    print ("True ")
elif year % 100 == 0:
     print("False")
else:
     print("False")


