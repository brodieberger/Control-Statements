x = int(input("Select starting number: "))
highest = int(input("Select number that will break the loop: "))
while x < highest:
    print(x)
    x = x + 1
else:
    print("Starting number has reached", highest, "terminating loop")
input("press enter to exit")
