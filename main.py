print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n1=name1.lower()
n2=name2.lower()

a=n1.count("t")+n1.count("r")+n1.count("u")+n1.count("e")+ n2.count("t")+n2.count("r")+n2.count("u")+n2.count("e")

b=n1.count("l")+n1.count("o")+n1.count("v")+n1.count("e")+n2.count("l")+n2.count("o")+n2.count("v")+n2.count("e")


r = 10*a+b
if r<10 or r>90: 
    print(f"Your score is {r}, you go together like coke and mentos.")

elif r>40 and r<50:
    print(f"Your score is {r}, you are alright together.")
    
else:
    print(f"Your score is {r}.")


