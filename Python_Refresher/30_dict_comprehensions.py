users = [
    (0, "Natalia", "password"),
    (1, "Alex", "password1"),
    (2, "Matt", "password2"),
    (3, "Tanya", "password3")
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)
print(username_mapping["Natalia"])

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input] # _ because we don't have

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect!")