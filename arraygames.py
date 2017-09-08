#matrix addition for variable size arrays
summ = []
matrix1 = [[1, 3], [2, 4], [2, 0]] 
matrix2 = [[5, 2], [1, 0], [3, 6]]
#resulting matrix must be [[6,5], [3,4], etc]
#create variables that show length of array elements
array_length = len(matrix1)
element_length = len(matrix1[0])
#iterate across arrays to retrieve data and sum values
for i in range(0, array_length):
  for x in range(0, element_length):
    summ.append(matrix1[i][x] + matrix2[i][x])
#splice one dimentional list into 2D array
return_array = []
for n in range(0, (array_length*element_length), element_length):# where element_length is a step
  return_array.append(summ[n:n+element_length])

#produce result
print ("Final array: {}".format(return_array))