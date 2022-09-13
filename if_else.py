'''
c=list(map(int, input("Enter").split()))
d=max(c)
print(d)'''
 
a= int(input("Enter number of Classes Attended:"))

d= (a/235)*100

if d>70 and d<=100:
    print ("Eligible for exam....")
elif  d<70 and d>0:
    print("Not Eligible......")
else:
     print ("Fu** Off..")    