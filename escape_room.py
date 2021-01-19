import time 
import random

output = []
items = []

#random factor 1
handle_bad_input = ["Do not know what that is.",
                    "There is no such a thing.",
                    "Your choices are limited, darling.",
                    "You cannot do this.",
                    "Are you sure this is a wise choice?",
                    "Whatever is this, it is a very bad choice..."]
# random factor 2
message1 = ("You appreached the doors, and both doors disappear. \n"
            "You were surprised and took a step back; \n"
            "The doors reappread again.")

message2 = ("You tried to open both, but they seem locked. \n"
            "You need a key to open them. \n"
            "You step back.")

message3 = ("You approached the doors; the doors move away from you. \n"
            "You run after the doors, but you cannot catch them. \n"
            "You step back and the doors went back to their original place.")

door_message = [message1, message2, message3]


def print_pause(message): # print messages and pause for 3 sec
    print(message)
    time.sleep(2)



def valid_input(prompt, options): # handling bad inputs
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause(random.choice(handle_bad_input))
        print_pause("Try again...") 


def intro(): # The game begins 
    print_pause("\nYou were kidnapped and trapped in an abandoned house. "
                "This place is unfamiliar to you.")
    print_pause("You do not know what happened, and who kidnapped you.\n")
    print_pause("What do you do?")
    
    intro_choice()

def intro_choice(): 
    response = valid_input("Press 1: Look around\n" 
                        "Press 2: Walk towards the door\n",
                        "1" "2") 
    if "1" in response:
        room()
    elif "2" in response: 
        door()

def room(): 
    print_pause("\nThe room is quite dark, only a desk lamp to light up the place.")
    print_pause("You see a message left on the wall.")
    print_pause("\"Try to espace if you can!\" ")
    print_pause("You see a bunch of furniture, suggesting you are in the bedroom.")
    print_pause("There is: a single bed, a desk lamp, a bureau and a closet.\n")
    print_pause("What do you do?")
    
    response = valid_input("Press 1: Inspect the furniture\n"
                            "Press 2: Walk towards the door\n", "1" "2") 

    if "1" in response:  
        furniture() 
    elif "2" in response:  
        door()

def furniture(): # Give the list of furniture to inspect
    print_pause("\nWhat furniture do you want to inspect?")
    response = valid_input ("- The bed\n"
                            "- The desk lamp\n"
                            "- The desk\n"
                            "- The closet\n"
                            "- Walk towards the door.\n"
                            "Please: enter your key word:\n",
                            "bed" "lamp" "desk" "closet" "door" ) 

    if "bed" in response: 
        bed()
    elif "lamp" in response:
        lamp()
    elif "desk" in response:
        desk()
    elif "closet" in response:
        closet()
    elif "door" in response: 
        door()

def bed():
    print_pause("\nYou inspect the bed. ")
    print_pause("There is only a pillow and a duvet. \n")
    print_pause("What do you do?")
    
    bed_inspection()

def bed_inspection():
    response = valid_input("- Sit on the bed\n"
                            "- Lie on the bed\n"
                            "- Check the pillow\n"
                            "- Check the duvet\n"
                            "- Check under the bed\n"
                            "- Check something else\n"
                            "Please: enter your key words:\n",
                            "sit" "lie" "pillow" "duvet" "under the bed" "something else") 
                    
    
    if "sit" in response: # sit on the bed
        print_pause("\nYou sit on the bed and wait. ")
        print_pause("Nothing happened. \n")
        print_pause("What now?")
        
        bed_inspection()


    elif "lie" in response: # lie on the bed
        if "big key" in items:
            print_pause("\nYou lie on the bed and the bed broke. ")
            print_pause("You fall into a dark tunnel. ")
            print_pause("You continued to fallm following the tunnel.")
            print_pause("You arrived in a very dark park.\n")
            print_pause("Congratulation, you have found the fastest way out.")
            time.sleep(2)
            print_pause("Or not...")
            print_pause("This park is part of the house too...")
            print_pause("You are trapped inside...\n")
            
            try_again()
        else:
            print_pause("\nYou lie down on the bed and wait.")
            print_pause("Nothing happened.\n")
            print_pause("What now?")
            bed_inspection()


    elif "pillow" in response: # check the pillow
        print_pause("\nYou throw the pillow away.")
        print_pause("There is a key.")
        print_pause("You took the key.\n")
        print_pause("What now?")
        items.append("key")
        response = valid_input("Press 1: continue to inspect the bed\n"
                                "Press 2: find a use to that key\n", 
                                "1" "2") 
        if "1" in response:
            bed_inspection()
        elif "2" in response:
            furniture()


    elif "duvet" in response: # check the duvet
        print_pause("\nYou lift the duvet.")
        print_pause("Cockroaches attack you.\n" )
        print_pause("Unfortunately, you died...\n")
        try_again()


    elif "under the bed" in response: # check under the bed
        print_pause("\nYou check under the bed.")
        print_pause("You found a big heavy box.")
        print_pause("You decided to look inside.\n")
        if "torch" in items:
            print_pause("You use you torch to light up inside the box.")
            print_pause("The box was filled with figurines collections.")
            print_pause("You dig inside and found a big key.\n")
            items.append("big key")
            print_pause("What now?")
            response = valid_input("Press 1: continue to inspect the bed\n"
                                    "Press 2: find a use to that key\n",
                                    "1" "2") 
            if "1" in response: 
                bed_inspection()
            elif "2" in response:
                furniture()
        else:
            print_pause("\nThere is nothing inside...\n")
            print_pause("What now?")
            bed_inspection()


    elif "something else" in response: # Go back the the list of furniture
        furniture()

def lamp():
    print_pause("\nYou inspect the lamp.")
    print_pause("You found a piece of paper with a message under the lamp.")
    print_pause("\"Either one or both are lying...\" \n")
    print_pause("What do you do?")
    response = valid_input("- Check the desk\n"
                            "- Continue to check to room\n"
                            "- Walk to the door\n",
                            "desk" "room" "door") 
    if "desk" in response: 
        desk()
    elif "room" in response: 
        furniture()
    elif "door" in response:
        door()

def desk():
    print_pause("\nYou decide to inspect the desk.")
    if "key" in items:
        print_pause("\nYou took the key you found under the pillow and insert it.")
        print_pause("You opened the drawer and find a torch.\n")
        items.append("torch")
    else:
        print_pause("\nThe desk seems to be locked.")
        print_pause("A key is needed to open it.\n")
    print_pause("What now?")
    response = valid_input("Press 1: continue to inspect the desk\n"
                            "Press 2: continue to inspect the room\n",
                            "1" "2") 
    if "1" in response:
        print_pause("\nNothing else to be found here.")
        print_pause("You should inspect something else.\n")
        furniture()
    elif "2" in response: 
        furniture()

def closet():
    print_pause("\nYou approached the closet.")
    print_pause("You heard some noise coming from inside...")
    print_pause("You opened it.\n")
    print_pause("A white cat stars at you...\n")
    print_pause("What do you do?")
    response = valid_input("Press 1: close the closet door\n"
                            "Press 2: take the cat with you.\n"
                            "Press 3: try to pet the cat.\n",
                            "1" "2" "3") 
    if "1" in response: 
        print_pause("\nYou looked at the cat, the cat looked at you.")
        print_pause("You realised it was a stuffed animal.") 
        print_pause("You closed the closet door.\n")
        print_pause("The noise you heard from before went back again.\n")
    elif "2" in response: 
        print_pause("\nYou looked at the cat, the cat looked at you.")
        print_pause("You realised it was a stuffed animal.")
        print_pause("But you decided to take it with you.\n")
        print_pause("You closed the closet door, you realised the noises were gone.\n")
        items.append("cat")
    elif "3" in response:
        print_pause("\nYou looked at the cat, the cat looked at you.")
        print_pause("You realised it was a stuffed animal.")
        print_pause("But you try to pet the animal nevertherless.\n")
        print_pause("Nothing happened...")
        print_pause("You closed the closet door.")
        print_pause("The noise stopped.\n")
    print_pause("What now?")
    response = valid_input("Press 1: continue to inspect the closet\n"
                            "Press 2: continue to inspect the room\n",
                            "1" "2") 
    if "1" in response:
        closet()
    elif "2" in response:
        furniture()

def door():
    if "big key" in items:
        print_pause("\nYou apprached the door.")
        print_pause("A message appeared on each of them.")
        print_pause("Door A: This door is the way out.")
        print_pause("Door B: This door is not the way out.\n")
        response = valid_input("Choose a door, A or B?\n", "a" "b") 
        if "a" in response:
            print_pause("\nYou used the big key to open the door, a bright light blinds you.")
            print_pause("\nYou were drawn by an invisible force and trapped into an empty"+
                        " bright space forever.\n")
            try_again()
        elif "b" in response: # Door to the way out
            print_pause("\nYou took the big key our of your pocket.")
            print_pause("The key is drawn by the door.")
            print_pause("The door opened and the lights blinds you.")
            print_pause("\nYou passed through the door. You arrived at a sunflower field.")
            if "cat" in items:
                print_pause("\nThe stuffed cat that you took with you, become alive.")
                print_pause("The cat thank you for free him from his curse.\n")
                end_game()
            else:
                end_game()
    else: # if you dont have the key
        print_pause("\nYou see there are two doors standing next to each other on a "+
                    "different side of the wall.")
        print_pause(random.choice(door_message))
        print_pause("\nSeems like you need to stay a little bit longer.")
        print_pause("You go back and check the room.\n")
        room()

def end_game():
    print_pause("Congratulations! You have successfully escaped the house.")
    print_pause("You can live happily ever after.")
    print_pause("Thank you for playing the game! See you next time!")

def try_again():
    response = valid_input("Would you like to try again? Enter 'Yes' or 'No'.\n", "yes" "no") 
    
    if "yes" in response:
        intro()
    elif "no" in response:
        print_pause("Well, maybe next time...")


intro()



