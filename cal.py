def sal():
    global salary
    salary=int(input("Enter Your Salary: "))
    

def hra():
    h= salary*0.5
    return h

def da():
    d= salary*0.15
    return d

def bonus():
    b= salary*0.1
    return b

def total():
    a= hra()+da()+bonus()+salary
    return a
    

