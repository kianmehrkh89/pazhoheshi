from datetime import datetime
import time
def open_users():
    users = open("users.txt","r")
    users = users.read().splitlines()
    for i in range(len(users)):
        users[i]=users[i].split("/")
    return users
def open_log():
    log = open("log.txt","r")
    log = log.read().splitlines()
    for i in range(len(log)):
        log[i]=log[i].split(",")
    return log
def check_user(name,pas,users):
    for i in range(len(users)):
        if users[i][0] == name:
            if pas in users[i][1]:
                print("login successful")
                return True , i
            else:
                print("password incorrect")
                return False , -1
    print("user not found")
    return False , -1
def check_admin(users,i):
    if "admin" in users[i][2] :
        return True
    return False
def add_user(user,pas,tipe,admin,users):
    if admin == True:
        users.append([user,pas,tipe])
        new_file=open("users.txt","w")
        for line in users: 
            new_file.write('/'.join(line) + '\n')
        new_file.close()
        print("user added")
    else:
        print("you can't add user")
    return
def edit_user(pas,last_pas,new_pas,rpt_new_pas,users,user_num):
    if last_pas == pas:
        if rpt_new_pas == new_pas:
            users[user_num][1]=new_pas
            new_file=open("users.txt","w")
            for line in users: 
                new_file.write('/'.join(line) + '\n')
            new_file.close()
            print("edit successful")
        else:
            print("password incorrect")
    else:
        print("password incorrect")
def del_user(user,approval,admin,users):
    if admin==True:
        if approval == "y":
            for i in range(len(users)):
                if user in users[i][0]:
                    del users[i]
                    new_file=open("users.txt","w")
                    for line in users: 
                        new_file.write('/'.join(line) + '\n')
                    new_file.close()
                print("delete successful")
        else:
            print("delete cancelled")
    else:
        print("you can't delete user")
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
            print("Book is available")
            return True
    print("Book is unavailable")
    return False
def add_book(book_name,num,admin,libry):
    if admin == True:
        libry.append([book_name,num])
        new_file=open("libry.txt","w")
        for line in libry: 
            new_file.write('/'.join(line) + '\n')
        print("book added")
    else:
        print("you can't add book")
    return
def edit_book(book_name,num,admin,libry):
    if admin == True:
        for i in range(len(libry)):
            if book_name in libry[i][0] :
                libry[i][1] = str(num)
                new_file=open("libry.txt","w")
                for line in libry: 
                    new_file.write('/'.join(line) + '\n')
        print("edit successful")
    else:
        print("you can't edit book")
    return
def del_book(book_name,admin,libry):
    if admin == True:
        for i in range(len(libry)):
            if book_name in libry[i][0] :
                libry[i][1] = "0"
                new_file=open("libry.txt","w")
                for line in libry: 
                    new_file.write('/'.join(line) + '\n')
        print("delete successful")
    else:
        print("you can't delete book")
    return
def get_book(username,book,log,libry):
    now = datetime.now()
    now = now.strftime("%y/%m/%d")
    new_log = open("log.txt","w")
    log.append([username,book,now,"1"])
    for line in log: 
        new_log.write(','.join(line) + '\n')
    for i in range(len(libry)):
        if libry[i][0] == book:
            libry[i][1]=str((int(libry[i][1])-1))
    new_libey = open("libry.txt","w")
    for line in libry: 
        new_libey.write('/'.join(line) + '\n')
    new_libey.close()

    return
def give_back_book(username,book,log,libry):
    for i in range(len(log)):
        if log[i][0] == username and log[i][1] == book:
             log[i][3]="0"
    new_log = open("log.txt","w")
    for line in log: 
        new_log.write(','.join(line) + '\n')
    for i in range(len(libry)):
        if libry[i][0] == book:
            libry[i][1]=str((int(libry[i][1])+1))
    new_libey = open("libry.txt","w")
    for line in libry: 
        new_libey.write('/'.join(line) + '\n')
    new_libey.close()
    new_log.close()
    return
def my_book(username,log):
    for i in range(len(log)):
        if log[i][0]==username and log[i][3]=="1":
            print("Book name: "+log[i][1]+" Date taking: "+log[i][2])
    return

#libry file
libry = open_book()
#users file
users=open_users()
q=False
username=input("username: ")
pas=input("password: ")
user_input , user_num=check_user(username,pas,users)
if user_input==True:
    admin = check_admin(users,user_num)
log = open_log()
#get_book(username,input("book name: "),log,libry)
#edit_user(pas,input("last password: "),input("new password: "),input("repeat new password: "),users,user_num)
#if admin == True :
 #   del_user(input(),input("are you sure?(y/n) "),users)
#if admin == True: 
#    add_user(input("new user name: "),input("new user password: "),input("Type of user: "),users)
while q==False and user_input==True:
    print("1.show libry list\n2.get book\n3.give back book\n4.add user\n5.edit user\n6.del user\n7.add book\n8.edit book\n9.del book\n10.search a book\n11.my book\n12.all log0.quit")
    work = int(input())
    if work==1:
        print([a[0] for a in libry if int(a[1])>0])
    elif work==2:
        get_book(username,input("book name: "),log,libry)
    elif work==3:
        give_back_book(username,input("book name: "),log,libry)
    elif work==4:
        add_user(input("new username: "),input("pasword: "),input("user Type: "),admin,users)
    elif work==5:
        edit_user(pas,input("last password: "),input("new password: "),input("repeat new password: "),users,user_num)
    elif work==6:
        del_user(input("username: "),input("are you sure?(y/n) "),admin,users)
    elif work==7:
        add_book(input("new BookName: "),input("num of Book: "),admin,libry)
    elif work==8:
        edit_book(input("new BookName: "),input("num of Book: "),admin,libry)
    elif work==9:
        del_book(input("Book name: "),admin,libry)
    elif work==10:
        check_book(input("Book name: "),libry)
    elif work==11:
        my_book(username,log)
    elif work==12:
        print(log)
    elif work==0:
        q=True
    else:
        print("num is out of range")
    time.sleep(2)
