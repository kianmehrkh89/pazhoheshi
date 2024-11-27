def open_users():
    users = open("users.txt","r")
    users = users.read().splitlines()
    for i in range(len(users)):
        users[i]=users[i].split("/")
    return users
def check_user(name,pas,users):
    for i in range(len(users)):
        if name in users[i][0]:
            if pas in users[i][1]:
                print("login successful")
                return True , i
            else:
                print("password incorrect")
                return False
    print("user not found")
    return False
def check_admin(users,i):
    if "admin" in users[i][2] :
        return True
    return False
def add_user(user,pas,tipe,users):
    users.append([user,pas,tipe])
    new_file=open("users.txt","w")
    for line in users: 
        new_file.write('/'.join(line) + '\n')
    new_file.close()
    return
def edit_user(pas,last_pas,new_pas,rpt_new_pas,users,user_num):
    if last_pas == pas:
        if rpt_new_pas == new_pas:
            users[user_num][1]=new_pas
            new_file=open("users.txt","w")
            for line in users: 
                new_file.write('/'.join(line) + '\n')
            new_file.close()
    else:
        print("password incorrect")
def del_user(user,approval,users):
    if approval == "y":
        for i in range(len(users)):
            if user in users[i][0]:
                del users[i]
                new_file=open("users.txt","w")
                for line in users: 
                    new_file.write('/'.join(line) + '\n')
                new_file.close()
    else:
        print("")
    return
def open_book():
    libry = open("libry.txt","r")
    libry = libry.read().splitlines()
    for i in range(len(libry)):
        libry[i]=libry[i].split("/")
    return libry
def check_book(B_Name,libry):
    for i in range(len(libry)):
        if B_Name in libry[i][0] and (int(libry[i][1])>0):
            print("2")
            return True
    return False
def add_book(book_name,num,libry):
    libry.append([book_name,num])
    new_file=open("libry.txt","w")
    for line in libry: 
        new_file.write('/'.join(line) + '\n')
    return
def edit_book(book_name,num,libry):
    for i in range(len(libry)):
        if book_name in libry[i][0] :
            libry[i][1] = str(num)
            new_file=open("libry.txt","w")
            for line in libry: 
                new_file.write('/'.join(line) + '\n')
    return
def del_book(book_name,num,libry):
    for i in range(len(libry)):
        if book_name in libry[i][0] :
            libry[i][1] = "0"
            new_file=open("libry.txt","w")
            for line in libry: 
                new_file.write('/'.join(line) + '\n')
    return

#libry file
libry = open_book()
#users file
users=open_users()

username=input("username: ")
pas=input("password: ")
user_input , user_num=check_user(username,pas,users)
admin = check_admin(users,user_num)
if user_input == True :
    print([a[0] for a in libry])
#edit_user(pas,input("last password: "),input("new password: "),input("repeat new password: "),users,user_num)
#if admin == True :
 #   del_user(input(),input("are you sure?(y/n) "),users)
if admin == True: 
    add_user(input("new user name: "),input("new user password: "),input("Type of user: "),users)