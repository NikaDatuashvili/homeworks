name=input("შეიყვანეთ თქვენი სახელი: ")
print("გამარჯობა " + name)
age=int(input("შეიყვანეთ თქვენი ასაკი: "))
year=int(input("შეიყვანეთ წელი: "))
for i in range(10):
    print(str(name+" შენ იქნები "+str(age+i)+"წლის "+str(year+i)+" წელს"))
