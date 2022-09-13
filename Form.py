'''
from datetime import date
a= input("First name:")
b= input("Last name:")
c= int(input("Id Number:"))
d= input("E-mail:")
e= int(input("Mobile number:"))
print("Enter DOB...")

f=date(int(input("Year:")), int(input("Month:")), int(input("Date:")))
today = date.today()
age = int((date.today() - f).days/365)

g= input("Company Name:")
h= input("Hometown:")
i= input("Blood Group:")


print("\n\n\n\nProfile is shown below:\n\n")

print(f"Name: {a} {b}\n")
print(f"Id Number: {c}\n")
print(f"Email: {d}\n")
print(f"Mobile Number: {e}\n")
print(f"Date of Birth: {f}\n")
print(f"Age: {age}\n")
print(f"Company Name: {g}\n")
print(f"Hometown: {h}\n")
print(f"Blood Group: {i}")
'''
a= "My name is Vikrant"
print (a.center(30,"i"))

