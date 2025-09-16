# numbers = [] 

# while True:
#     user_input = input("Enter a positive number (enter a non-positive number to stop): ")

#     # Check if the input can be converted to a float and is non-negative
#     if user_input.replace('.', '', 1).isdigit() and float(user_input) > 0:
#         numbers.append(float(user_input))
#     elif user_input.replace('-', '', 1).isdigit() and float(user_input) <= 0:
#         break  # Exit the loop if a non-positive number is entered
#     else:
#         print("Invalid input. Please enter a valid positive number.")

# # Data handling after the loop
# if numbers:
#     print(f"You entered the following positive numbers: {numbers}")
# else:
#     print("No positive numbers were entered.")
# nameList = ["harsh", "kaliya", "hardoyi", "baliya"]
# pos = nameList.index("baliya")
# print(pos*3)
# hash()
def findMax(matrix):
    maxVal = matrix[0][0]
    for row in matrix:
        maxVal = max(maxVal, max(row))
    return maxVal
matrixs = [[333,5,3,5],[7,68.3,4,67],[43,68,57,22],[22,56,78,78]]
maximum = findMax(matrixs)
print("\nMaximum Value = ", maximum)
print(float('inf'))
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
newList = [i for i in range(1,1000) if i%2 ==0 ]
print(newList)