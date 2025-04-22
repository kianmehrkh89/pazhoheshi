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
        for i in range(len(users["name"])):
            if users["name"][i] in name:
                if str(pas) == str(users["pass"][0]):
                    return True , i
        return False , -1
    def check_admin(self,users,i):
        if "admin" == users["type"][i] or "main" == users["type"][i] :
            return True
        return False
    def check_main(self,users,i):
        if "main" == users["type"][i]:
            return True
        return False
    def check_book(self,B_Name,libry,root,log,username):
        def about_book(i,libry):
            root = Tk()         
            root.geometry('300x300') 
            root.configure(bg="palegoldenrod")
            author1_lable = Label(root, text = "نویسنده:")
            author_lable = Label(root, text = libry["author"][i])
            detail1_lable = Label(root, text = 'معرفی کتاب:')
            datail_lable = Label(root, text = libry["about"][i])
            author1_lable.grid(row=0,column=0)
            author_lable.grid(row=0,column=1)
            detail1_lable.grid(row=1,column=0)
            datail_lable.grid(row=1,column=1)
            btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy) 
            btn_quit.grid(row=2,column=1)
            root.mainloop()
            return
        for i in range(len(libry["book"])):
            if (libry["book"][i] in B_Name or libry["name_fa"][i] in B_Name) and (int(libry["num"][i])>0):
                return_label = Label(root, text = 'کتاب موجود است')
                about=Button(root,text = 'درباره کتاب', 
                    command = lambda:about_book(i,libry))
                get = Button(root, text = 'دریافت کتاب',
                    command = lambda:user.get_book(self , username , B_Name , log , libry , root))
                return_label.grid(row=4,column=0)
                about.grid(row=5,column=1)
                get.grid(row=6,column=1)
                root.update()
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
    def add_book(self,book_name,num,libry,root):
        libry.loc[libry.shape[0]] = [book_name, num]
        libry.to_csv('libry.csv', index=False)
        return_label = Label(root, text = 'کتاب با موفقیت اضافه شد')
        return_label.grid(row=4,column=0)
        root.update()
        time.sleep(2)
        return_label.destroy()
        return
    def edit_book(self,book_name,num,libry,root):
        for i in range(len(libry["book"])):
            if book_name == libry["book"][i] :
                libry.iloc[i,3]=num
                libry.to_csv('libry.csv', index=False)
                return_label = Label(root, text = 'اطلاعات کتاب با موفقیت ویرایش شد')
                return_label.grid(row=4,column=0)
            else:
                return_label = Label(root, text = 'کتاب پیدا نشد')
                return_label.grid(row=4,column=0)
        root.update()
        time.sleep(2)
        return_label.destroy()
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
    def add_user(self,user,pas,type,main,users,root):
        if type == "ادمین" and main == True :
            users.loc[users.shape[0]] = [user,pas,"admin"]
            users.to_csv('users.csv', index=False)
        elif type == "کاربر" :
            users.loc[users.shape[0]] = [user,pas,"user"]
            users.to_csv('users.csv', index=False)
        return_label = Label(root, text = 'کاربر اضافه شد')
        return_label.grid(row=4,column=0)
        root.update()
        time.sleep(1)
        root.destroy()
        return
    def edit_user(self,pas,last_pas,new_pas,rpt_new_pas,users,user_num,root):
        if last_pas == pas:
            if rpt_new_pas == new_pas:
                users.iloc[user_num,1]=new_pas
                users.to_csv('users.csv', index=False)
                return_label = Label(root, text = 'رمز عبور با موفقیت تغییر یافت')
                return_label.grid(row=4,column=0)
            else:
                return_label = Label(root, text = 'تکرار رمز جدید اشتباه است')
                return_label.grid(row=4,column=0)
                root.update()
        else:
            return_label = Label(root, text = 'رمز عبور اشتباه است')
            return_label.grid(row=4,column=0)
            root.update()
        root.update()
        time.sleep(1)
        root.destroy()
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
        now = datetime.now()
        now = now.strftime("%y/%m/%d")
        for i in range(len(libry["book"])):
            if libry["book"][i] == book and int(libry["num"][i])>0:
                check=1
                log.loc[log.shape[0]] = [username, book, now , "1"]
                log.to_csv('log.csv', index=False)
                libry.iloc[i,3]=(str((int(libry["num"][i])-1)))
                libry.to_csv('libry.csv', index=False)
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
        for i in range(len(log["name"])):
            if log["name"][i] == username and log["book"][i] == book and int(log["approval"][i])==1:
                log.iloc[i,3]=0
                return_label = Label(root, text = 'کتاب با موفقیت برگردانده شد')
                return_label.grid(row=4,column=0)
                root.update()
                for i in range(len(libry["book"])):
                    if libry["book"][i] == book:
                        libry.iloc[i,3]=(str((int(libry["num"][i])+1)))
                log.to_csv('log.csv', index=False)
                libry.to_csv('libry.csv', index=False)
                time.sleep(2)
                root.destroy()
                return
        return_label = Label(root, text = 'کتاب یافت نشد')
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
        return a
    def all_user_data(self,main,users):
        a=[]
        if main==True:
            for i in range(len(users["name"])):
                a.append("name: "+str(users["name"][i])+" password: "+str(users["pass"][i])+" type: "+str(users["type"][i]))
        else:
            a.append("you are not main")
        return a