import pyttsx3

engine = pyttsx3.init()
engine.say("Hello homies, good day! Can you fill up this friendship form I have? and hoping after this we can be friends <3")
engine.runAndWait()
engine.stop()

engine = pyttsx3.init()
engine.say("What's your name?")
engine.runAndWait()
engine.stop()

name = input("What's your name?:\n ")

while name == "": 
    print("You did not enter your name >:((")   
    name = input("Enter your name: \n")

else: 
    print(f"Hello there, {name}, nice meeting you! <3\n\n")

engine = pyttsx3.init()
engine.say("Hello there, Erich Marie B. Estella! nice meeting you!")
engine.runAndWait()
engine.stop()

engine = pyttsx3.init()
engine.say("How old are you?")
engine.runAndWait()
engine.stop()


age = input("How old are you?:\n")

while age == "":
    print("You did not type how old are you. I wanna know :((")
    age = input("Enter your age:\n")

else:
    print(f"Wow, so you are {age} years old. Awesome, me too! that's so cool! ")

engine = pyttsx3.init()
engine.say("Wow, so you are 18 years old. Awesome, me that's so cool!\n ")
engine.runAndWait()
engine.stop()

engine = pyttsx3.init()
engine.say("Last question, where do you live?")
engine.runAndWait()
engine.stop()


address = input("Last question, where do you live?:\n")

while address == "":
      print("I won't go to there, I promise! I just wanna know :(" )
      address = input ("Enter where do you live?:\n")

else:
    print (f"Woah, so {address} that's the place where you live in. How wonderful! I'm glad to know that :)\n") 

engine = pyttsx3.init()
engine.say("Woah, so at Building 1 407, Katuparan, Vitas, Tondo, Manila, that's the place where you live in. How wonderful! I'm glad to know that :) ")
engine.runAndWait()
engine.stop()

engine = pyttsx3.init()
engine.say("I hope we can be friends, thank you for filling up this friendship form <3")
engine.runAndWait()
engine.stop()

print("I hope we can be friends, thank you for filling up this friendship form <3")