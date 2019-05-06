my_dict = {"name": "jose", "age": 90, "grade": [56,76,56,99]}
my_dict_num = {1: 15, 2: 90, 3:94} #can be sequence

lottery_player = {
    "name": "Folf",
    'numbers': (24,35,46,57) # can be tuple
}

universities = [
    {
        "name":"Oxford",
        "location": "UK"
    },
    {
        "name": "MIT",
        "location": "US"
    }

]

#WE CAN PUT ANYTHING WE WANT AS A VALUE OF A KEY
# dictionary represent things

dict_in_dict = {
    "key": {
        "name":"Jose"
    }
}

print(sum(lottery_player["numbers"])) #access to this key

lottery_player["name"] = "John"
lottery_player["numbers"][0] = 50 # can't do because it is a tuple

