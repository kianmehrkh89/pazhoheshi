from datetime import datetime
from tkinter import *
from tkinter.ttk import *
import pandas as pd
import time
class system:
    def ___init___(self):
        pass
    def open_users(self):
        users = pd.read_csv("users.csv")
        return users
    def open_log(self):
        log = pd.read_csv("log.csv")
        return log
    def open_book(self):
        libry = pd.read_csv("libry.csv")
        return libry
    def check_user(self,name,pas,users):
        a=0
        print(users["pass"],"-------")
        print(users["name"][0])
        for i in range(len(users["name"])):
            if users["name"][i] in name:
                if str(pas) == str(users["pass"][0]):
                    print("login successful")
                    return True , i
        print("user not found")
        return False , -1
    def check_admin(self,users,i):
        if "admin" == users["type"][i] or "main" == users["type"][i] :
            return True
        return False
    def check_main(self,users,i):
        if "main" == users["type"][i]:
            return True
        return False
    def check_book(self,B_Name,libry,root):
        for i in range(len(libry["book"])):
            print(B_Name)
            if libry["book"][i] in B_Name and (int(libry["num"][i])>0):
                return_label = Label(root, text = 'کتاب موجود است')
                return_label.grid(row=4,column=0)
                root.update()
                time.sleep(2)
                root.destroy()
                return True
        return_label = Label(root, text = 'کتاب موجود نیست')
        return_label.grid(row=4,column=0)
        root.update()
        time.sleep(2)
        root.destroy()
        return False
class user:
    def ___init___(self):
        pass
    def libry_list(self,libry):
        a=[]
        for i in range(len(libry["book"])):
            a.append(libry["book"][i])
        return a
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
        elif type == "user" :
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
            if approval == "yes":
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
    def get_book(self,username,book,log,libry,root):
        check=0
        print(log)
        print(libry)
        now = datetime.now()
        now = now.strftime("%y/%m/%d")
        print(log)
        for i in range(len(libry["book"])):
            if libry["book"][i] == book and int(libry["num"][i])>0:
                check=1
                new_line={"name": username,"book": book,"date": now,"approval": "1"}
                log._append(new_line, ignore_index=True)
                log. to_csv('log.csv', index=False)
                
                #libry.loc["num"][i]=(str((int(libry["num"][i])-1)))
                libry. to_csv('libry.csv', index=False)
                return_label = Label(root, text = 'کتاب دریافت شد')
                return_label.grid(row=4,column=0)
                root.update()
        if check==0 :
            return_label = Label(root, text = 'کتاب موجود نیست')
            return_label.grid(row=4,column=0)
            root.update()
        time.sleep(2)
        root.destroy()
        return
    def my_book(self,username,log):
        a=[]
        for i in range(len(log["name"])):
            if log["name"][i]==username and int(log["approval"][i])==1:
                a.append("Book name: "+log["book"][i]+" Date taking: "+log["date"][i])
        return a
    def give_back_book(self,username,book,log,libry,root):
        for i in range(len(log)):
            if log[i][0] == username and log[i][1] == book and int(log[i][3])==1:
                log[i][3]="0"
                return_label = Label(root, text = 'get back is Successfull')
                return_label.grid(row=4,column=0)
                root.update()
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
                time.sleep(2)
                root.destroy()
                return
        return_label = Label(root, text = 'book not found')
        return_label.grid(row=4,column=0)
        root.update()
        time.sleep(2)
        root.destroy()
        return
    def all_log(self,log):
        a=[]
        for i in range(len(log["name"])):
            if int(log["approval"][i]) == 1:
                a.append(log["name"][i]+" dar tarikh "+log["date"][i]+" ketabe "+log["book"][i]+" ra gerefte")
            print(a)
        return a
    def all_user_data(self,main,users):
        a=[]
        if main==True:
            for i in range(len(users["name"])):
                a.append("name: "+str(users["name"][i])+" password: "+str(users["pass"][i])+" type: "+str(users["type"][i]))
        else:
            a.append("you are not main")
        print(a)
        return a