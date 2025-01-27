from datetime import datetime
class system:
    def ___init___(self):
        pass
    def open_users(self):
        users = open("users.txt","r")
        users = users.read().splitlines()
        for i in range(len(users)):
            users[i]=users[i].split("/")
        return users
    def open_log(self):
        log = open("log.txt","r")
        log = log.read().splitlines()
        for i in range(len(log)):
            log[i]=log[i].split(",")
        return log
    def open_book(self):
        libry = open("libry.txt","r")
        libry = libry.read().splitlines()
        for i in range(len(libry)):
            libry[i]=libry[i].split("/")
        return libry
    def check_user(self,name,pas,users):
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
    def check_admin(self,users,i):
        if "admin" in users[i][2] or "main" in users[i][2] :
            return True
        return False
    def check_main(self,users,i):
        if "main" in users[i][2]:
            return True
        return False
    def check_book(self,B_Name,libry):
        for i in range(len(libry)):
            if B_Name in libry[i][0] and (int(libry[i][1])>0):
                print("Book is available")
                return True
        print("Book is unavailable")
        return False
class user:
    def ___init___(self):
        pass
    def libry_list(self,libry):
        for i in libry:
            print(i[0])
    def add_book(self,book_name,num,libry):
        libry.append([book_name,num])
        new_file=open("libry.txt","w")
        for line in libry: 
            new_file.write('/'.join(line) + '\n')
        print("book added")
        return
    def edit_book(self,book_name,num,libry):
        for i in range(len(libry)):
            if book_name in libry[i][0] :
                libry[i][1] = str(num)
                new_file=open("libry.txt","w")
                for line in libry: 
                    new_file.write('/'.join(line) + '\n')
            else:
                print('book not found')
                return
        print("edit successful")
        return
    def del_book(self,book_name,libry):
        for i in range(len(libry)):
            if book_name in libry[i][0] :
                libry[i][1] = "0"
                new_file=open("libry.txt","w")
                for line in libry: 
                    new_file.write('/'.join(line) + '\n')
        print("delete successful")
        return
    def add_user(self,user,pas,type,main,users):
        if type == "admin" and main == True :
            users.append([user,pas,type])
        elif type == user :
            users.append([user,pas,type])
        else:
            print("type incorrect")
            return
        new_file=open("users.txt","w")
        for line in users: 
            new_file.write('/'.join(line) + '\n')
        new_file.close()
        print("user added")
        return
    def edit_user(self,pas,last_pas,new_pas,rpt_new_pas,users,user_num):
        if last_pas == pas:
            if rpt_new_pas == new_pas:
                users[user_num][1]=new_pas
                new_file=open("users.txt","w")
                for line in users: 
                    new_file.write('/'.join(line) + '\n')
                new_file.close()
                print("edit successful")
                return
            else:
                print("password incorrect")
                return
        else:
            print("password incorrect")
            return
    def del_user(self,user,approval,main,users):
        if main==True:
            if approval == "y":
                for i in range(len(users)):
                    if user in users[i][0]:
                        del users[i]
                        new_file=open("users.txt","w")
                        for line in users: 
                            new_file.write('/'.join(line) + '\n')
                        new_file.close()
                        break
                print("delete successful")
                return
            else:
                print("delete cancelled")
                return
        else:
            print("you can't delete user")
        return
    def get_book(self,username,book,log,libry):
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
        print("get book successful")
        return
    def my_book(self,username,log):
        a=[]
        for i in range(len(log)):
            if log[i][0]==username and log[i][3]=="1":
                a.append("Book name: "+log[i][1]+" Date taking: "+log[i][2])
        if len(a)==0:
                print("you didn't get a book")
        else:
            for i in a:
                print(i)
        return
    def give_back_book(self,username,book,log,libry):
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
        print("get back book successful")
        return
    def all_log(self,log):
        for i in log:
            if i[3]=="1":
                print(i[0]+" dar tarikh "+i[2]+" ketabe "+i[1]+" ra gerefte")
        return
    def all_user_data(self,main,users):
        if main==True:
            for i in users:
                print(i)
        else:
            print("you are not main")
        return