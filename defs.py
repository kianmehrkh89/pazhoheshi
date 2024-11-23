def check_user(name,pas,users):
    for i in range(len(users)):
        if name in users[i][0]:
            if pas in users[i][1]:
                print("1")
                return True
    return False
def check_book(BName,libry):
    for i in range(len(libry)):
        if BName in libry[i][0] and (int(libry[i][1])>0):
            print("2")
            return True
    return False
#libry file
libry = open("libry.txt","r")
libry = libry.read().splitlines()
for i in range(len(libry)):
    libry[i]=libry[i].split("/")
#users file
users = open("users.txt","r")
users = users.read().splitlines()
for i in range(len(users)):
    users[i]=users[i].split("/")
print(users)
check_book(input(),libry)
user_input=check_user(input("username"),input("pas"),users)
