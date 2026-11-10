import time 
import random 
hunger = random.randint(60, 80)
energy = random.randint(50, 75)
health = random.randint(85, 100)
def title(txt: str, spaces: str):
    print("------------------------------------")
    print(f"{spaces}{txt}")
    print("------------------------------------")
score = 0
onedeath = False
title("SPACE MISSION SIMULATOR", "        ")
time.sleep(2)
print("Choose a name for your spaceship...")
ship_name = input("Name: ")
print("Great! Where would you like to take your new ship to?")
time.sleep(1)
print("Type one: \n 1. Moon \n 2. Mars ")
dest = input("Input: ")

if dest == "1": #DA MOON "‾" <- Use for images
    title("Destination Selected: The Moon!", "")
    radiatelvl = "Low"
    time.sleep(1)
    print("Preparing your spaceship...")
    time.sleep(10)
    print("Here are a few things you should know before arriving...")
    time.sleep(1)
    print("The Moon has a sixth of Earth's gravity. It'll take some time to get used to it.")
    time.sleep(3.5)
    print("Make sure to keep track of radiation levels, stay away from large craters, and keep track of your spacesuit.")
    time.sleep(1)
    print("You have arrived at your destination.")
    time.sleep(1)
    title("DAY ONE", "             ")
    print("What would you like to do first?")
    print("Options: \n 1. Explore the space base and get settled \n 2. Take a peek outside \n 3. Go take a ride on the lunar vehicle")
    act1 = input("Input: ")

    if act1 == "1": #DAY 1
        print("Where would you like to go first?")
        time.sleep(0.5)
        print("Options: \n 1. Main Hallway \n 2. Left wing \n 3. Right wing")
        mdest = input("Destination: ")
        if mdest == "1":
            print("You walk ahead, and find the food court. You decide to grab some food. +20 hunger!")
            hunger += 20
            time.sleep(1)
            print(f"You are {hunger}% full!")
        elif mdest == "2":
            print("You take a left and continue walking. On the way, you find the garden and the tech room.")
        elif mdest == "3":
            print("You take a right and find the sleeping bunks, along with the gym. You decide to take a rest. +25 energy!")
            energy += 25
            time.sleep(1)
            print(f"You are {energy}% awake")
        else:
            print("You bump into a wall and get a concussion. The End.")
            onedeath = True
        
    elif act1 == "2":
        print("You put on your spaceship, walk outside, watching the calm, gray landscape, streching as far as the eye can see.")
        time.sleep(1)
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("|‾‾‾‾‾‾\*                          *  |")
        print("|      |                              |")
        print("|      |               *              |")
        print("|  /‾‾\|                              |")
        print("|  |   |           _______    ________|")
        print("|__|___|___       /       \  /        |")
        print("|          \     /         ‾‾         |")
        print("|           ‾‾‾‾‾                     |")
        print("|_____________________________________|")
        time.sleep(1)
        print("Options: \n 1. Explore a bit further \n 2. Head inside")
        time.sleep(1)
        print(f"The radiaton level is {radiatelvl}")
        deathchance= random.randint(1, 50)
        act1_2a = input("Input: ")
        if act1_2a == "1" and deathchance <= 10:
            print("You fall into a large crater, and barely manage to exit. -25 health.")
            health -= 25
            time.sleep(1)
            print(f"Your health is {health}%")
        elif act1_2a == "1" and deathchance > 10:
            print("You walk around, exploring the craters, and manage to get in the base before the radiation level rose. -15 energy.")
            energy -= 15
            time.sleep(1)
            print(f"You are {energy}% energized")
        elif act1_2a == "2":
            print("You decide to go inside, and go to the food court to grab some food. +10 hunger!")
            hunger += 10
            time.sleep(1)
            print(f"You are {hunger}% full")
        else:
            print("You fall asleep, and your oxygen runs out. The End.")
            onedeath = True
    elif act1 == "3":
        rlvl = random.randint(20, 40)
        radiatelvl = "Moderate"
        suitmal = random.randint(1, 10)
        deathchance = random.randint(60, 100) - rlvl
        if suitmal <= 2:
            print("You never put on your spacesuit right. The End.")
            onedeath = True
        else:
            print(f"Radiation level is {radiatelvl}. \nWhat would you like to do first?")
            time.sleep(3)
            print("Options: \n 1. Drive around the area \n 2. Explore further")
            act1_3a = input("Input: ")
            if act1_3a == "1" and deathchance < 10:
                print("The radiation got to you. -25 health.")
                health -= 25 
                time.sleep(1)
                print(f"Your health levels are {health}%")
            elif act1_3a == "1" and deathchance > 10:
                print("You drive around and have some fun, then go inside. -10 energy.")
                time.sleep(1)
                energy -= 10
                print(f"You are {energy}% energized")
            elif act1_3a == "2" and deathchance < 25:
                onedeath = True
                print("You set off to explore the craters, and never return. Who knows what happened? Maybe it was the radiation, or maybe you fell in a crater.")
            elif act1_3a == "2" and deathchance > 25:
                radiatelvl == "High"
                print("You explore further, and eventually stumble upon a cave. Do you go in?")
                time.sleep(3)
                print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
                print("|                                  /‾‾‾‾‾‾|")
                print("|                                 | _  /| |")
                print("|                               _/ / \ | \|")
                print("|                              |   | | /_/|")
                print("|              |‾‾‾\___       /    |  \/  |")
                print("|              |_______\      |   /‾‾/‾   |")
                print("|               0     0 ______|_/‾___|____|")
                print("|             /‾‾‾‾‾‾‾‾‾                  |")
                print("|_/‾‾‾‾‾‾‾‾‾‾‾                            |")
                print("|_________________________________________|")

                time.sleep(1)
                print("Options: \n 1. Explore further \n 2. Leave")
                time.sleep(2)
                print(f"Radiation level is {radiatelvl}.")
                act1_3b = input("Input: ")
                dchance = deathchance - 20
                if act1_3b == 1 and dchance > 35:
                    print("The radiation got to you. The End.")
                    onedeath = True
                else:
                    print("You turn back, and surprisingly make it inside alive. -30 energy.")
                    time.sleep(3)
                    energy -= 30
                    print(f"You are {energy}% energized")
                
    else:
        print("You spend so much time figuring out what to do that by the time you have decided, the next day has begun.")
    if onedeath == False: #DAY TWO
        score += 1
        title("DAY TWO", "            ")
        print("Ah, a brand new day! What are you planning to do?")
        time.sleep(2)
        print("Options: \n 1. Take a rest \n 2. Use the telescope \n 3. Explore the gym")
        time.sleep(1)
        act2 = input("Input: ")
        if act2 == "1":
            print("You decide to spend the day in your room and take a nap. Health and energy restored!")
            health = 100
            energy = 100
            time.sleep(1)
            print(f"Your health is {health}%, and you are {energy}% awake!")
        elif act2 == "2":
            print("You take a look through the telescope, and take some cool images.")
            time.sleep(3)
            print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
            print("|               *             *    |")
            print("|    *   *                         |")
            print("|           *                      |")
            print("|             *     *    *         |")
            print("|   *           *       *          |")
            print("|                  *   *       *   |")
            print("|           *                      |")
            print("|__________________________________|")
        elif act2 == "3":
            print("You go into the gym and exercise. -10 energy.")
            energy -= 10
            time.sleep(1)
            print(f"You are {energy}% awake")
        else:
            print('By the time you decide, the day has already passed.')
    else:
        print("")
    if onedeath == False: #‾
        score += 1
        elecFixed = False
        sarrayFixed = False
        title("DAY THREE", "           ")
        time.sleep(3)
        print("Hello! A few duties await you today...")
        time.sleep(1)
        title("TASKS FOR TODAY:")
        time.sleep(1)
        print("\n 1. Fix the generator \n 2. Repair the left solar array")
        radiatelvl = "Moderate"
        time.sleep(1)
        print(f"The radiation level is {radiatelvl}, although this is expected to increase over time.")
        rlvl = random.randint(20, 40)
        deathchance = random.randint(70, 100) - rlvl
        time.sleep(1)
        print("Which would you like to do first?")
        time.sleep(1)
        act3 = input("Input: ")
        if act3 == "1": #Day 3, Task No. 1
            elecFixed = True
            print("You enter the tech room, and open the generator, only to find that water flooded the generator. What do you do?")
            time.sleep(1)
            print("Options:\n  1. Rely on solar power and ignore the generator \n 2. Find the old backup generator \n 3. Try to fix the current generator")
            time.sleep(2)
            act3a = input("Input: ")
            if act3a == "1":
                print("Task skipped.")
            elif act3a == "2":
                print('You enter the old storage room and find the backup generator. You find that it works. Mission Complete!')
            elif act3a == "3":
                print("After hours of trying, you find that the generator, will not work. - 20 energy.")
                energy -= 20
                time.sleep(1)
                print(f"You are {energy}% awake")
            else:
                print("You decide to skip this task and fix the solar panels.")
            elecFixed = True
        elif act3 == "2":
            sarrayFixed = True
            print("You put on your spacesuit to find that a power cable has been damaged. What do you do?")
            time.sleep(3)
            print("Options: \n 1. Disconnect the solar panel \n 2. Replace the cable \n 3. Ignore it")
            act3b = input("Input: ")
            if act3b == "1":
                print("You disconnect the solar panel the cable was attached to. You have a little less power, but you'll survive. Mission Successful!")
            elif act3b == "2":
                print("You find some cable in the storage room, and successfully rewire the cable. Mission Successful!")
            elif act3b == "3":
                print("Skipped task.")
            else:
                print("Skipped task.")
            sarrayFixed = True
        else:
            print("The base runs out of power. The End.")
            onedeath = True
            time.sleep(3)
        if elecFixed == False:# Day Three, Task No. 2
            print('Now, we need to replace the generator.')
            time.sleep(1)
            print("You enter the tech room, and open the generator, only to find that water flooded the generator. What do you do?")
            time.sleep(1)
            print("Options: \n 1. Skip Task \n 2. Find the old backup generator \n 3. Try to fix the current generator")
            time.sleep(2)
            act3a = input("Input: ")
            if act3a == "1":
                print("You run out of power. The End.")
                onedeath = True
            elif act3a == "2":
                print('You enter the old storage room and find the backup generator. You find that it works. Mission Complete!')
            elif act3a == "3":
                print("After hours of trying, you find that the generator, will not work. - 20 energy.")
                energy -= 20
                time.sleep(1)
                print(f"You are {energy}% awake")
            else:
                print("You run out of power. The End.")
                onedeath == True
            elecFixed = True
            sarrayFixed = True
        elif sarrayFixed == False and deathchance > 20:
            print("Now, we need to fix the solar arrays.")
            print("You put on your spacesuit to find that a power cable has been damaged. What do you do?")
            time.sleep(3)
            print("Options: \n 1. Disconnect the solar panel \n 2. Replace the cable \n 3. Ignore it")
            act3b = input("Input: ")
            if act3b == "1":
                print("You disconnect the solar panel the cable was attached to. You have a little less power, but you'll survive. Mission Successful!")
            elif act3b == "2":
                print("You find some cable in the storage room, and successfully rewire the cable. Mission Successful!")
            else:
                print("You run out of power. The End.")
                onedeath = True
            sarrayFixed = True
        elif sarrayFixed == True and deathchance < 20:
            print("The radiation got to you while you were trying to fix the solar panels. The End.")
            onedeath = True
            elecFixed = True
        else:
            print("")
        time.sleep(1)
        print("After a long day of working, you grab lunch at the food court, then go to bed. Hunger and energy restored!")
        time.sleep(1)
        hunger = 100
        energy = 100
        print(f"You are {hunger}% full and {energy}% awake")
    else:
        print("")
    if onedeath == False:
        score += 1
        title("DAY FOUR", "            ")
        time.sleep(1)
        print("Ah, a brand new day! Wha-")
        time.sleep(2.5)
        print("WARNING! WARNING!")
        time.sleep(0.5)
        print("ALERT! ALERT! OXYGEN LEVELS DECREASING!")
        time.sleep(0.25)
        print("ERROR! ERROR! OXYGEN FILTER DAMAGED!")
        time.sleep(0.1)
        print("WARNING! WARNING!")
        time.sleep(0.5)
        print("ALERT! ALERT! OXYGEN LEVELS DECREASING!")
        time.sleep(0.25)
        print("ERROR! ERROR! OXYGEN FILTER DAMAGED!")
        time.sleep(0.1)
        print("WARNING! WARNING!")
        time.sleep(0.5)
        print("ALERT! ALERT! OXYGEN LEVELS DECREASING!")
        time.sleep(0.25)
        print("ERROR! ERROR! OXYGEN FILTER DAMAGED!")
        time.sleep(1)
        print("You rush towards the technology room to find the oxygen filter severly damaged. You assess the damage, and find that the filter is unrepairable.")
        time.sleep(3)
        oTime = "1 hour"
        oMins = 60
        print(f"You have {oTime} of oxygen left, use it wisely.")
        time.sleep(1)
        print("Where do you search first?")
        print("Options: \n 1. Outdoor shed \n 2. Storage room \n 3. Emergency storage")
    else:
        print("")
    if onedeath == False:
        score += 1
        title("THE FINAL DAY: DAY 5", "   ")
    else:
        print("")
    if onedeath == True:
        score = score
    else:
        score += 1
    time.sleep(1)
    title("GAME OVER")
    print(f"\n    DAYS SURVIVED: {score}        ")
    print(f"    Health = {health} \n    Hunger = {hunger} \n    Energy = {energy}")




elif dest == "2": #MARS
    title("Destination Selected: Mars!", "  ")
    radiatelvl = "Moderate"
    print("Preparing your spaceship...")
    time.sleep(3)
    print("Here are a few things you should know about your trip...")
    time.sleep(1)
    print(f"You will arrive in a few months. Your ship, the {ship_name}, will require maintanence at least twice a month.")
    time.sleep(2)
    print("Keep an eye out for asteroids.")
    time.sleep(1)
    print("Upon arrival of Mars, you will recieve more information.")
else:
    print("You set off in your spaceship and crashed into an asteroid. The End.")
time.sleep(3)
title("Thank you for playing!", "      ")