all_friends = {"Bob", "Rolf", "Anne"}
abroad_friends = {"Bob", "Anne"}
# local_friends = {"Rolf"}
local_friends = all_friends.difference(abroad_friends)
print(local_friends)
local_friends = abroad_friends.difference(all_friends)
print(local_friends)

abroad = {"Bob", "Anne"}
local = {"Rolf"}
friends = local.union(abroad)
print(friends)


art = {"Bob","Jen", "Rolf", "Charlie"}
science = {"Bob","Jen", "Adam", "Anne"}

art_only = art.difference(science)
print(art_only)

science_only = science.difference(art)
print(science_only)

both_subjects = art.intersection(science)
print(both_subjects)

both_subjects = science.intersection(art)
print(both_subjects)