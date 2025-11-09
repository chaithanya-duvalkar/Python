#set is the collection of the unordered items
#each element in the set must be unique and immutable
#sets are mutable but elements are immutable
# set={}

###############
# SET METHODS
# set.add(val)
# set.remove(val)
# set.clear()
# set.pop()
# set.union(set2)
# set.intersection(set2)

collection={1,2,3,4,"hello","world","world"}
print(collection)
print(len(collection))

set1={20,10,30,50}
set2={10,40,60,20}
print(set1.union(set2))
print(set1.intersection(set2))
