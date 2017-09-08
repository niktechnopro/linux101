#calculate triangle based on height
height = int(input("Enter height"))
#calculate base based on height
n = 1
base = height * 2
#calculate base based on height "*"
ba = abs(base/2)
while n <= base:
  if n%2 != 0:
    height += 1
    emptySpace = int(ba) * " "
    print (str(emptySpace) + "*" * n)
    ba -= 1
  n += 1
if (base%2 == 0):
  base = base - 1
print ("the base is: " + str(base))