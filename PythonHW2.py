users=[]
firstN=input("First Name:")
users.append(firstN.capitalize())
lastN=input("Last Name:")
users.append(lastN.capitalize())
age=int(input("Age:"))
users.append(age)
birthYear=int(input("Date of Bith(just year)"))
users.append(birthYear)
for i in users:
    print(i)
if age<18 and birthYear<2002:
     print("You can go out because it's too dangerous")       
else:
        print("You can go out to the street")