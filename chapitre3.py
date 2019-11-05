locations = ["Haiti","Jamaica","Martinique","France","USA"]
print("The original List:")
print(locations)

"""To maintain the original order of a list but present it in a sorted order, you
can use the sorted() function instead of sort() because unlike sorted(), sort will sort the list permanently"""
print(" \nA sorted list:")
print(sorted(locations))

print("\nThe original list:")
print(locations)

locations.reverse()
print("\nThe reverse list :",locations)

locations.sort()
print("\nThe new sorted list",locations)

locations.reverse()
print("\nThe reverse list :",locations)


print("I'm from",locations[0]," but I was born in ",locations[3])

print("\nI havent visited:")
print(locations.pop(1))
print(locations.pop(1)) 
print(locations.pop(2))

print(" \nThe new list of countries", locations)
