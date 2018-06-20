import sys
count = int(input("Set starting number (1-10): "))
if count > 10:
    input("Invalid input")
    sys.exit()
    
highest = int(input("Set number to break loop (1-100): "))
if highest > 100:
    input("Invalid input")
    sys.exit()
    
while count < highest:
	print(count) 
	count +=1
input ("Press Enter to Exit")
