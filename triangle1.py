#print a triangle based on base
base = int(input("Enter base"))
n = 1
height = 0
#calculate base based on height "*"
ba = abs(base/2)
while n <= base:
  if n%2 != 0:
    height += 1
    emptySpace = int(ba) * " "
    print (str(emptySpace) + "*" * n)
    ba -= 1
  n += 1
print ("the height is: " + str(height))