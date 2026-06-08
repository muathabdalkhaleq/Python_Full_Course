# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")
space = username.find(" ")
if len(username) > 12 :
    print("your user name can not be more than 12 charcters")
elif not space == -1 :
    print("your user name can not be contain space")
elif not username.isalpha():
    print("your user name can not contain numbers")
else:
    print(f"welcome {username}")