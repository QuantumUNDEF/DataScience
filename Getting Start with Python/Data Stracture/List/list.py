def findMax(matrix):
    maxVal = matrix[0][0]
    for row in matrix:
        maxVal = max(maxVal, max(row))
    return maxVal
matrixs = [[333,5,3,5],[7,68.3,4,67],[43,68,57,22],[22,56,78,78]]
maximum = findMax(matrixs)
print("\nMaximum Value = ", maximum)
# print(float('inf'))
# list comprehension_________________
lst = [ 1,3,5,6,45,76,46,34,76,45,45,6,3,6,3]
print(len(lst))
for i in lst:
    lst[lst.index(i)] =i*i
print(lst)
print(len(lst))
lst = [i**2 for i in lst]
print(len(lst))
lst = [i%2 == 0 for i in lst]
print(lst)
# Even list
newList = [i for i in range(1,21) if i%2 ==0 ]
print(newList)
# multidimensional list
print([[j for j in range(5)] for i in range(5)])
mullist= [[j for j in range(5)] for i in range(5)]
flatlist = [j for i in mullist for j in i]
print(flatlist)