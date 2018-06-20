import sys
x = "no"
y = "no"
print("You sit in your house alone, you gaze out the window, longing for an adventure to break up this boring life. You get up, go to the door, and step outside.")
while True:
    fanswer = input('Outside you see a forest and a cave. Which one will you go?" \n 1. Forest \n 2. Cave \n 3. Go back inside \n Make your selection: ')
    if fanswer in ('1', '2', '3'):
        break
    print ('Invalid input.')
if fanswer == '1':
    y = "forest"
elif fanswer == '2':
    x = "cave"
else:
    print ('You turn back around and go into your house where you stay alone and isolated. You die of old age. \n GAME OVER')
    input("press enter to exit")

if x == "cave":
    answer = input('You enter the pitch black cave. Its very spooky. \n 3. Exit the game. Its too spooky man \n 4. Go further into the cave \n Make your selection: ')
else:
    answer = input('You walk into the forest and see a branch lying on the floor. What do you do? \n 1. Pick up the branch \n 2. Eat it \n Make your selection: ')

if answer == '1':
    print("You walk over to pick up the branch, but you end up tripping and falling on top of it, impaling you through the heart. \n GAME OVER")
elif answer== '2':
    print("You eat the stick and die \n GAME OVER")
elif answer == '3':
    sys.exit()
elif answer== '4':
    print("something happens probably")
input ("Press Enter to Exit")
