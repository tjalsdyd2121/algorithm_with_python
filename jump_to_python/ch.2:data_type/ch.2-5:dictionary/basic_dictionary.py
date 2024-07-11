# the biggest difference between list and dictionary is that list is ordered and dictionary is >> unordered << .

# values are accessed by not ordering, but key.

dic1 = {'fruit': 'apple', 'color': 'red', 'price': 1000}

print(dic1['fruit'] + '  ' + str(dic1['price']))

dic2 = {3.14 : 'pi', 'test' : dic1}
# value can be >> any <<  data type.

print(dic2['test'])

dic1['phone'] = 'iphone'
print('\n'+dic1['phone'])
del dic2['test']
print(dic2)
# elements can be deleted and added.

a = {1:'a', 1:'b'}
print(a)
# key is unique.

# a = {[1,2] : 'hi'} --> error
# key must be immutable. as like int, string, tuple.


