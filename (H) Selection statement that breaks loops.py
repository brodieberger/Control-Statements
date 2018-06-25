x = input("Enter string: ")
#prompts the user to enter a string
y = input("Enter letter to break: ")
#Letter that will break the loop
for letter in x:
   if letter == y:
      break
   print ('Current Letter:', letter)
#prints the string letter by letter until it reaches the letter that breaks the loop.
input ("Press Enter to Exit")
