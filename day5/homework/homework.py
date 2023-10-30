age=int(input("შეიყვანეთ თქვენი ასაკი "))
father_age=int(input("შეიყვანეთ მამათქვენის ასაკი "))
year=int(input("შეიყვანეთ რომელი წელია ახლა "))

for i in range(1,10):
    print(str(year+i)+" წელს მამათქვენი იქნება თქვენზე იქნება "+str((father_age+i)/(age+i)) + " ჯერ დიდი.")
    
