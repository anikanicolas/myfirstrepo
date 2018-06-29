# --- Define your functions below! ---
#future functions
#create goodbye function
#make it tell a joke
#make it recite a poem
#guess my age
#return makes function become true or false, but print only prints true or false on the surface level, the function doesn't have a value of true or false
from rockPaperScissors import *
def intro ():
    print("Hello.")
    print("My name is Chatbot")
    name = input("What's your name?")
    print("Nice to meet you "+name) #or %s." %name)
    answer = input("How are you today?")
    if answer == "good":
        print("Awesome!")
    else:
        print("Hope you have a great day!")
    playAGame=input("Would you like to play a game of rock, paper, scissors? \n")
    if playAGame == "yes":

    else:
        print("You're no fun")

def default ():
    print("That's cool and Shnazzy!")
def angryResponse ():
    print("That's not nice.")

def process_input (anyInput): #userInput takes on the value of answer
    acceptableHellos = ["Hi", "hi", "hey", "hello", "Hey", "Hello"]
    if is_valid_input(acceptableHellos, anyInput):
        intro()
    acceptableAngry = ["RAWRxD", "NO", "angereyreaccs"]
    if is_valid_input(acceptableAngry,anyInput):
        angryResponse()
    else:
        default()

def is_valid_input (acceptableResponses, anInput):
    if anInput in acceptableResponses:
        return True
    else:
        return False




# --- Put your main program below! ---
def main():
    while True:
        answer = input("(What will you say?) ")
        acceptableResponses = ["Hi", "hi", "hey", "hello", "Hey", "Hello"]
        process_input(answer)



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
