# set declare

set1 = set([1,2,3,4,5])
set2 = {1,3,5,7,9}
set3 = set("hello")
# print(set1, set2, set3)

# set does have duplication and unordered.

print(set1 & set2)
print(set1.intersection(set2))
print(set1 | set2)
print(set1.union(set2))
print(set1 - set2)
print(set2 - set1)

set2.add(11)
print(set2)
set2.update([13,15])
print(set2)
set2.remove(3)
print(set2)