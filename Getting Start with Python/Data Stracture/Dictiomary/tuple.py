tpl = (1,5,9,13,17)
diff = tpl[1]- tpl[0]
print(tpl[(len(tpl)-1)])
lst = tpl[(len(tpl)-1)]
print(tpl+tuple([lst+i*diff for i in range(1,4)]))