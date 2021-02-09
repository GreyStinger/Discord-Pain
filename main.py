import time

import discord_pain
import grey

repeat = True
print("Welcome to pain.")

while repeat is True:

    end_check = False
    sentence = str(input("Enter your sentence here: "))
    finished_sentence = discord_pain.main(sentence=sentence)

    grey.clear()
    print("Working...")
    time.sleep(1)
    grey.clear()

    print(f"Your Discord pain sentence is:\n{finished_sentence}\n")

    while end_check is False:
        continue_on = (input("Would you like to run this again or quit? Answer with 'yes' or 'no':")).lower()
        if continue_on == "no":
            end_check = True
            repeat = False
            grey.clear()
        elif continue_on == "yes":
            end_check = True
            grey.clear()
        else:
            print("Invalid input. Please try again.")
            time.sleep(2)
            grey.clear()

print("Goodbye then, probably better if I don't see you again soon.")
time.sleep(5)
