# import tkinter module 
import classs
from datetime import datetime
from tkinter import *        
from tkinter.ttk import *
import time  
#libry file
system = classs.system()
api = classs.user()
libry = system.open_book()
#users file
users=system.open_users()
q=False
username=input("username: ")
pas=input("password: ")
user_input , user_num=system.check_user(username,pas,users)
if user_input==True:
    admin = system.check_admin(users,user_num)
    main = system.check_main(users,user_num)
log = system.open_log()

if admin==True:
    root = Tk()           
    root.geometry('600x350')   
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
else:
    root = Tk()           
    root.geometry('600x350')   
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

