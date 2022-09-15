import mariadb 
import sys

conn = mariadb.connect(
        user="root",
        password="Vikrants298@",
        host="localhost",
        port=3306,
        database="employees" )
cur=conn.cursor() 
conn.autocommit = True

try:
    cur.execute("CREATE TABLE people (First_Name VARCHAR(30), Surname VARCHAR(30),AGE INT(11),Salary INT(11),Mobile_Number VARCHAR(20),City VARCHAR(20), Department VARCHAR(20))")

except Exception as y:
    print (y)


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




cur.execute("""INSERT INTO people(First_Name,Surname,AGE,Salary,Mobile_Number,City,Department) VALUES(?,?,?,?,?,?,?)""",(fname,sname,age,salary,numb,city,depart))

conn.commit()

    



       





    



        

