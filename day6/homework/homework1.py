total = 0 
total_num = 0


for i in range(5):
    num=int(input("Enter Your Score "))
    total+=num 
    total_num+=1 


print(total/total_num)
avrg_score=total/total_num
if avrg_score>9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები")
elif avrg_score<5:
    print("გილოცავ გაექეცი მატრიცას")
elif avrg_score>5 and avrg_score<10:
    print("YOU ARE MID")
elif avrg_score>10 and avrg_score<0:
    print("here is something wrong with you")
