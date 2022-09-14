'''
for i in range(10):
   name= input("Enter your full name: ")
   if name=="":
      print("This field is mandatory")
      pass
   else:
        break
for i in range(10):
    age=int(input("Enter your age: "))  
    if   age<18 :
        print ("Error...")
        pass
    else:
        break
for i in range(10):
    salary=int(input("Enter your salary: "))    
    if salary<20000 :
        print("Error....")
        pass
    else:
        break
for i in range (10):
    numb=input("Enter your mobile Number: ")   
    if numb=="" or len(numb)<10 or len(numb)>10:
        print("Enter Again....")
        pass
    else:
        break

company=input("Enter your Company's Name: ") 


k=input("To Print Form: PRESS y \n To Exit: PRESS n\n")

if k=="y":
    print(f"Name = {name}\n")
    print(f"Age = {age}\n")
    print(f"Salary = {salary}\n")
    print(f"Mobile Number = {numb}\n")
    print(f"Company's Name = {company}")
else:
    pass
'''





    



        

