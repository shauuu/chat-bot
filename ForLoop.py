# ITERATING OVER A LIST
myList = ["This", "Is", "A", "Boy"]
for w in myList:
    print(len(w),w)

    #ITERATING OVER A STRING
x = "This is a string"
for y in x:
    print(y, len(x))

#USING RANGE
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
if a<b:
    for i in range(a,b):
        if i%2 == 0:
            print(str(i)+" is an even number")
        else:
             print(str(i)+ " is an odd number")
else:
    print(str(a) + " Is Bigger than " + str(b))
c = sum(range(7))
print (c)