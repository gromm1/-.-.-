immutable_var = 1, 2, 3, True, 'Good'
print (immutable_var)
immutable_var [0] = 53
print (immutable_var) # нельзя изменить элементы кортежа так как он не предполагает изменений элементом и является неким "хранилищем"
mutable_list = ['apple', 'water', True, 1, 2]
mutable_list [2] = False
print (mutable_list)