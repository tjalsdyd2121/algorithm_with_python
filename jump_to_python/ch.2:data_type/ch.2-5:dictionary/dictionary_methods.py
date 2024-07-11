a = {'name': 'min yong', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys()) 
for i in a.keys() : 
  print(i)
# .keys() return dict_keys object.

print(a.items())
for i in a.items() : 
  print(i)
# .items() return dict_items object.
# key-value exists as tuple type.

print(a.get('name'))
print(a.get('no_key'))
# .get() is same as accessing with [], but return >> None << if there is no key matched.

print('no_key' in a , 'name' in a)