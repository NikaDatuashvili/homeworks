user1 = input("You Are User 1. Please Enter Your Full Name: ")
user2 = input("You Are User 2. Please Enter Your Full Name: ")

a_counter = 0
for element in user1, user2:
    for char in element:
        if char == "a":
            a_counter += 1
print(a_counter)