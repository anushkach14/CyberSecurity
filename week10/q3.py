#Dummy credetnials
correct_usrname="admin"
correct_pswd="pass123"

usernames=["user","admin","test"]
pswds=["1234","admin","pass123","qwerty"]

#brute force simulation
for user in usernames:
    for pwd in pswds:
        print(f"trying {user} / {pwd}")
        if user==correct_usrname and pwd==correct_pswd:
            print(f"login succesful with {user} / {[pwd]}")
            break
        else:
            continue
        break