mountains = ["Mount Fuji", "Denali", "Kilimanjaro", "Mount Everest", "Aconcagua"]

print(mountains[0])
mountains[0] = "Mount Rainier"
print(mountains)

mountains.append("Mount Fuji")
mountains.insert(1, "Matterhorn")
print(mountains)

del mountains[1]
popped_mountain = mountains.pop()
print(popped_mountain)
popped_mountain = mountains.pop(1)
print(popped_mountain)

mountains.remove("Kilimanjaro")
print(mountains)

print(sorted(mountains))
print(mountains)
mountains.reverse()
print(mountains)
mountains.reverse()
mountains.sort()
print(mountains)
mountains.sort(reverse=True)
print(mountains)

print(f"There are {len(mountains)} mountains in the list.")