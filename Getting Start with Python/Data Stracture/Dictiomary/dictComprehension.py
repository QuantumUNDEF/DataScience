dict = {1:1, 2:4, 3:9, 4:16, 5:25}
dict2 = {i:i*i for i in range(1,6)}
print(dict)
print(dict2)
print(dict == dict2)
dct = ['num_' + str(i) for i in range(1,101)]
print(dct)
dct = ['num_' + str(i) for i in range(1,101) if i%2 == 0]
print(dct)
