# import tkinter module 
import classs
from datetime import datetime
from tkinter import *        
from tkinter.ttk import *
import time  
#libry file
user_input_var = None
user_num_var = None
def check_user(username,pas,users,root):
    user_input_var , user_num_var = system.check_user(username,pas,users)
    if user_input_var == TRUE:
        root.destroy()
    return
def signin(users):
    root1=Tk()
    root1.geometry("200x100")
    name_label = Label(root1, text = 'Username')
    username_get = Entry(root1)
    passw_label = Label(root1, text = 'Password')
    pas=Entry(root1)
    sub=Button(root1,text = 'Submit', command = lambda:check_user(username_get.get(), pas.get(), users, root1))
    name_label.grid(row=0,column=0)
    username_get.grid(row=0,column=1)
    passw_label.grid(row=1,column=0)
    pas.grid(row=1,column=1)
    sub.grid(row=2,column=1)
    username = username_get.get()
    password = pas.get()
    root1.mainloop()
    return user_input_var , user_num_var , username , password
system = classs.system()
api = classs.user()  
libry = system.open_book()
#users file
users=system.open_users()
q=False
user_input , user_num , username , pas = signin(users) 
if user_input==True:
    admin = system.check_admin(users,user_num)
    main = system.check_main(users,user_num)
log = system.open_log()
if user_input==True and admin==True:
    root = Tk()
    root.geometry('800x800')
    tx = Label(root, text='select a option:')
    tx.pack(side = "left")   
    btn_libry_list = Button(root, text = 'show libry list', 
            command = lambda:api.libry_list(libry))
    btn_libry_list.pack(side = 'top')
    btn_get_book = Button(root, text = 'get book',
                    command = lambda:api.get_book(username,input("Book you want: "),log,libry))
    btn_get_book.pack(side = 'top') 
    btn_get_back_book = Button(root, text = 'get back book', 
                    command = lambda:api.give_back_book(username,input("The book you want to return: "),log,libry))
    btn_get_back_book.pack(side = 'top')
    btn_add_user = Button(root, text = 'add user', 
                    command = lambda:api.add_user(input("new username: "),input("pasword: "),input("user Type: "),main,users))
    btn_add_user.pack(side = 'top') 
    btn_edit_user = Button(root, text = 'edit user', 
                    command = lambda:api.edit_user(pas,input("last password: "),input("new password: "),input("repeat new password: "),users,user_num)) 
    btn_edit_user.pack(side = 'top')
    btn_del_user = Button(root, text = 'del user', 
                    command = lambda:api.del_user(input("username: "),input("are you sure?(y/n) "),main,users)) 
    btn_del_user.pack(side = 'top')
    btn_add_book = Button(root, text = 'add book', 
                    command = lambda:api.add_book(input("new BookName: "),input("num of Book: "),libry)) 
    btn_add_book.pack(side = 'top')
    btn_edit_book = Button(root, text = 'edit book', 
                    command = lambda:api.edit_book(input("BookName: "),input("new num of Book: "),libry)) 
    btn_edit_book.pack(side = 'top')
    btn_del_book = Button(root, text = 'del book', 
                    command = lambda:api.del_book(input("Book name: "),libry)) 
    btn_del_book.pack(side = 'top')
    btn_search_book = Button(root, text = 'search a book', 
                command = lambda:system.check_book(input("Book name: "),libry)) 
    btn_search_book.pack(side = 'top')
    btn_my_book = Button(root, text = 'my book', 
                    command = lambda:api.my_book(username,log)) 
    btn_my_book.pack(side = 'top')
    btn_all_log = Button(root, text = 'all log', 
                    command = lambda:api.all_log(log)) 
    btn_all_log.pack(side = 'top')
    btn_all_users_data = Button(root, text = 'all users data', 
                    command = lambda:api.all_user_data(main,users))
    btn_all_users_data.pack(side = 'top')
    btn_quit = Button(root, text = 'quit',
                    command = root.destroy) 
    btn_quit.pack(side = 'top')
    root.mainloop() 
elif user_input==True:
    root = Tk()           
    root.geometry('400x350')  
    tx = Label(root, text='select a option')
    tx.pack(side = "left") 
    btn_libry_list = Button(root, text = 'show libry list', 
            command = lambda:api.libry_list(libry))
    btn_libry_list.pack(side = 'top')
    btn_get_book = Button(root, text = 'get book', 
                    command = lambda:api.get_book(username,input("Book you want: "),log,libry))
    btn_get_book.pack(side = 'top') 
    btn_get_back_book = Button(root, text = 'get back book', 
                    command = lambda:api.give_back_book(username,input("The book you want to return: "),log,libry))
    btn_get_back_book.pack(side = 'top')
    btn_edit_user = Button(root, text = 'edit user', 
                    command = lambda:api.edit_user(pas,input("last password: "),input("new password: "),input("repeat new password: "),users,user_num)) 
    btn_edit_user.pack(side = 'top')
    btn_search_book = Button(root, text = 'search a book', 
                command = lambda:system.check_book(input("Book name: "),libry)) 
    btn_search_book.pack(side = 'top')
    btn_my_book = Button(root, text = 'my book', 
                    command = lambda:api.my_book(username,log)) 
    btn_my_book.pack(side = 'top')
    btn_quit = Button(root, text = 'quit',
                    command = root.destroy) 
    btn_quit.pack(side = 'top')
    root.mainloop() 

# Set the position of button on the top of window 

