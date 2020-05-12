log_on_dictionary={"admin00":"admin000",
                   "uv":"password",
                   "minion":"helloooo",
                   "dv":"yuvarajan",
                   "hi":"passkeyy"}
user_input=input("Enter ur user name:")
if user_input in log_on_dictionary.keys():
    password_input=input("Enter the password:")
    if password_input==log_on_dictionary[user_input]:
        print("welcome")
    if user_input=="admin00":
        for key,value in log_on_dictionary.items():
            print("username:"+key+" password:"+value)
    else:
        password_change=input("would u like to change the password (yes/no):")
        if password_change=="yes":
            new_password=input("Enter new password:")
            if len(new_password >= 8):
                log_on_dictionary[user_input]=new_password
            else:
                print("minimum 8 characters")
else:
    print("incorrect password")