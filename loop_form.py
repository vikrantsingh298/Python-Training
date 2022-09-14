while True:
   fname= input("Enter your First name: ")
   if fname.isalpha():
            if fname=="" :
                print("Invalid.....")
                pass
            else:
                    break
   else:
        print("Enter Valid Name....")            
while True:
   sname= input("Enter your Surname name: ")
   if sname.isalpha():
            if sname=="" :
                print("Invalid.....")
                pass
            else:
                    break   
   else:
        print("Enter Valid Name....") 

while True:
    age =input("Enter age:")
    if age.isnumeric():

    
                if int(age)>60 or age=="" or int(age)<20:
                    print("Enter A valid age..")
                else:
                    break    
    else :
        print("Enter age in numbers...")

    
while True:
    salary=(input("Enter your salary: ")) 
    if salary.isnumeric():  

        if int(salary)<0 or salary=="":
             print("Enter Valid Salary...")
             pass
        else:
            break
    else:
        print("Enter Salary in Numbers...") 

while True:
    numb=input("Enter your mobile Number: ")  
    if numb.isnumeric: 
            if numb=="" or len(numb)<10 or len(numb)>10 :
                print("Enter Again....")
                pass
            else:
                break
    else:
        print("Enter in Number format....")

while True:
    city=input("Enter your City: ")   
    if city=="" or city.isnumeric()==True :
        print("Enter Again....")
        pass
    else:
        break

while True:
    depart=input("Enter your Department: ")   
    if depart=="" or depart.isnumeric()==True :
        print("Enter Again....")
        pass
    else:
        break    


k=input("To Print Form: PRESS y \n To Exit: PRESS n\n")

if k=="y":
    print(f"Name = {fname} {sname}\n")
    print(f"Age = {age}\n")
    print(f"Salary = {salary}\n")
    print(f"Mobile Number = {numb}\n")
    print(f"City Name = {city}")
    print(f"City Name = {depart}")
else:
    pass


       





    



        

