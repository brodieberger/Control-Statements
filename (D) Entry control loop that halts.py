x = int(input("Select starting number: "))
highest = int(input("Select number that will break the loop: "))
#sets the starting number and the number that will break the loop
while x < highest:
    print(x)
    x = x + 1
else:
    print("Starting number has reached", highest, "terminating loop")
#adds one to the starting number until it reaches the specified number that breaks the loop
input("press enter to exit")
