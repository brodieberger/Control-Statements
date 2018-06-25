import sys
count = int(input("Set starting number (1-10): "))
if count > 10:
    input("Invalid input")
    sys.exit()
#condition that will terminate the program if not met. (1-10)
    
highest = int(input("Set number to break loop (1-100): "))
if highest > 100:
    input("Invalid input")
    sys.exit()
#condition that will terminate the program if not met. (1-100)
    
while count < highest:
	print(count) 
	count +=1
#adds one to the count until it reaches the specified highest number
input ("Press Enter to Exit")
