name = input("What is your name?:")
age = float(input("How old are you?:"))
if 16 < age <= 70:
    print("Welcome " + name + ' on our website.')
elif age == 16:
    print("Dear, " + name + ' need to wait one year.')
elif 70 < age < 90:
    print("You are lucky " + name + " and welcome.")
elif 90 <= age <= 121:
    print("Welcome " + name + ' on our website.')
elif age > 121:
    print("You are not real " + name + ".")
else:
    print("I'm sorry " + name + " you are too young.")
