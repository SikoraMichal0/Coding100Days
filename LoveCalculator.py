# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lwc = name1.lower()
name2_lwc = name2.lower()
name1_true = name1_lwc.count("t") + name1_lwc.count("r") + name1_lwc.count("u") + name1_lwc.count("e")
name2_true = name2_lwc.count("t") + name2_lwc.count("r") + name2_lwc.count("u") + name2_lwc.count("e")
name_true = int(name1_true + name2_true)
name1_love = name1_lwc.count("l") + name1_lwc.count("o") + name1_lwc.count("v") + name1_lwc.count("e")
name2_love = name2_lwc.count("l") + name2_lwc.count("o") + name2_lwc.count("v") + name2_lwc.count("e")
name_love = int(name1_love + name2_love)
name_true_string = str(name_true)
name_love_string = str(name_love)
name_finish = (name_true_string + name_love_string)

if name_finish < str(10) or name_finish > str(90):
    print(f"Your score is {name_finish}, you go together like coke and mentos.")
elif str(40) <= name_finish <= str(50):
     print(f"Your score is {name_finish}, you are alright together.")
else:
    print(f"Your score is {name_finish}.")
