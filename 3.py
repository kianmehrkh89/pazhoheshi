# import tkinter module 
import classs
from datetime import datetime
from tkinter import *        
from tkinter.ttk import *
import time  
#files
system = classs.system()
api = classs.user()
libry = system.open_book()
users=system.open_users()
#TKinter
input_var , num_var , username_var , password_var = None , None , None , None
def check_user(username,pas,users,root):
    global user_input_var , user_num_var , username_var , password_var
    user_input_var , user_num_var = system.check_user(username,pas,users)
    if user_input_var == TRUE:
        username_var , password_var = username , pas
        print(user_input_var , user_num_var , username_var , password_var)
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
    root1.mainloop()
    return
def lib_list():
    lis = api.libry_list(libry)
    root = Tk()           
    root.geometry('250x400')
    for i in lis:
        tx = Label(root, text=i)
        tx.pack(side = "top")
    btn_quit = Button(root, text = 'quit',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom')
    root.mainloop()
    return
def get_book():
    root = Tk()           
    root.geometry('500x400') 
    book_label = Label(root, text = 'Book you want: ')
    book_entry = Entry(root)
    sub =Button(root,text = 'continue', 
                command = lambda:api.get_book(username,book_entry.get(),log,libry,root))
    btn_quit = Button(root, text = 'quit',
                command = root.destroy) 
    book_label.grid(row=0,column=0)
    book_entry.grid(row=0,column=1)
    sub.grid(row=1,column=1)
    btn_quit.grid(row=2,column=1)
    root.mainloop()
    return
def give_back_book():
    root = Tk()           
    root.geometry('500x400') 
    book_label = Label(root, text = 'Book you want to return: ')
    book_entry = Entry(root)
    sub =Button(root,text = 'continue', 
                command = lambda:api.give_back_book(username,(book_entry.get()),log,libry))
    btn_quit = Button(root, text = 'quit',
                command = root.destroy)
    book_label.grid(row=0,column=0)
    book_entry.grid(row=0,column=1)
    sub.grid(row=1,column=1)
    btn_quit.grid(row=2,column=1)
    root.mainloop()
    return
def add_user():
    root = Tk()         
    root.geometry('500x400') 
    name_label = Label(root, text = 'Username')
    username_get = Entry(root)
    pass_label = Label(root, text = 'Password')
    password=Entry(root)
    type_label = Label(root, text = 'select type')
    type = Combobox(root)
    type['values'] = ("admin", "user")
    sub =Button(root,text = 'continue', 
                command = lambda:api.add_user(username_get.get(),password.get(),type.get(),main,users))
    btn_quit = Button(root, text = 'quit',
                command = root.destroy) 
    name_label.grid(row=0,column=0)
    username_get.grid(row=0,column=1)
    pass_label.grid(row=1,column=0)
    password.grid(row=1,column=1)
    type_label.grid(row=2,column=0)
    type.grid(row=2,column=1)
    sub.grid(row=3,column=1)
    btn_quit.grid(row=4,column=1)
    root.mainloop()
    return
def edit_user():
    root = Tk()         
    root.geometry('500x400') 
    pas_label = Label(root, text = 'last password')
    pas_get = Entry(root)
    newpas_label = Label(root, text = 'new Password')
    newpas=Entry(root)
    rpt_newpas_label = Label(root, text = 'rpt new password')
    rpt_newpas=Entry(root)
    sub =Button(root,text = 'continue', 
                command = lambda:api.edit_user(pas,pas_get.get(),newpas.get(),rpt_newpas.get(),users,user_num))
    btn_quit = Button(root, text = 'quit',
                command = root.destroy)
    pas_label.grid(row=0,column=0)
    pas_get.grid(row=0,column=1)
    newpas_label.grid(row=1,column=0)
    newpas.grid(row=1,column=1)
    rpt_newpas_label.grid(row=2,column=0)
    rpt_newpas.grid(row=2,column=1)
    sub.grid(row=3,column=1)
    btn_quit.grid(row=4,column=0)
    root.mainloop()
    return
def del_user():
    root = Tk()         
    root.geometry('500x400') 
    username_label = Label(root, text = 'Username')
    username_get = Entry(root)
    check_label = Label(root, text = 'are you sure?')
    check = Combobox(root)
    check['values'] = ("yes", "no")
    sub =Button(root,text = 'continue', 
                command = lambda:api.del_user(username_get.get(),check.get(),main,users))
    btn_quit = Button(root, text = 'quit',
                command = root.destroy) 
    username_label.grid(row=0,column=0)
    username_get.grid(row=0,column=1)
    check_label.grid(row=1,column=0)
    check.grid(row=1,column=1)
    sub.grid(row=2,column=1)
    btn_quit.grid(row=4,column=1)
    root.mainloop()
    return
def add_book():
    root = Tk()         
    root.geometry('500x400') 
    name_label = Label(root, text = "new BookName: ")
    BookName = Entry(root)
    num_label = Label(root, text = "num of Book: ")
    num=Entry(root)
    sub=Button(root,text = 'Submit',
                command = lambda:api.add_book(BookName.get(),num.get(),libry))
    btn_quit = Button(root, text = 'quit',
                command = root.destroy) 
    name_label.grid(row=0,column=0)
    BookName.grid(row=0,column=1)
    num_label.grid(row=1,column=0)
    num.grid(row=1,column=1)
    sub.grid(row=2,column=1)
    btn_quit.grid(row=3,column=1)
    root.mainloop()
    return
def edit_book():
    root = Tk()         
    root.geometry('500x400') 
    name_label = Label(root, text = "BookName: ")
    BookName = Entry(root)
    num_label = Label(root, text = "new num of Book: ")
    num=Entry(root)
    sub=Button(root,text = 'Submit',
                command = lambda:api.edit_book((BookName.get(),num.get(),libry)))
    btn_quit = Button(root, text = 'quit',
                command = root.destroy) 
    name_label.grid(row=0,column=0)
    BookName.grid(row=0,column=1)
    num_label.grid(row=1,column=0)
    num.grid(row=1,column=1)
    sub.grid(row=2,column=1)
    btn_quit.grid(row=3,column=1)
    root.mainloop()
    return
def del_book():
    root = Tk()         
    root.geometry('500x400') 
    name_label = Label(root, text = "BookName: ")
    BookName = Entry(root)
    sub=Button(root,text = 'Submit',
                command = lambda:api.del_book(BookName.get(),libry))
    btn_quit = Button(root, text = 'quit',
                command = root.destroy) 
    name_label.grid(row=0,column=0)
    BookName.grid(row=0,column=1)
    sub.grid(row=1,column=1)
    btn_quit.grid(row=2,column=1)
    root.mainloop()
    return
def check_book():
    root = Tk()         
    root.geometry('500x400') 
    name_label = Label(root, text = "BookName: ")
    BookName = Entry(root)
    sub=Button(root,text = 'Submit',
                command = lambda:system.check_book(BookName.get(),libry))
    btn_quit = Button(root, text = 'quit',
                command = root.destroy) 
    name_label.grid(row=0,column=0)
    BookName.grid(row=0,column=1)
    sub.grid(row=1,column=1)
    btn_quit.grid(row=2,column=1)
    root.mainloop()
    return
def my_book():
    a = api.my_book(username,log)
    root = Tk()         
    root.geometry('500x400')
    if len(a)==0:
        tx = Label(root, text =  "you didn't get a book")  
        tx.pack(side = "top")      
    else:
        for i in a:
           tx = Label(root, text =  i) 
           tx.pack(side = "top")
    btn_quit = Button(root, text = 'quit',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom')
    root.mainloop()
    return
def all_log():
    root = Tk()         
    root.geometry('500x400')
    a = api.all_log(log)
    for i in a:
        tx = Label(root, text =  i) 
        tx.pack(side = "top")
    btn_quit = Button(root, text = 'quit',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom')
    root.mainloop()
def user_maneger():
    root = Tk()           
    root.geometry('500x400') 
    tx = Label(root, text='select a option:')
    tx.pack(side = "left")
    btn_add_user = Button(root, text = 'add user', 
                    command = lambda:add_user())
    btn_add_user.pack(side = 'top')
    btn_del_user = Button(root, text = 'del user', 
                    command = lambda:del_user())
    btn_del_user.pack(side = 'top')
    btn_quit = Button(root, text = 'back',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom') 
    root.mainloop()
    return
def book_maneger():
    root = Tk()           
    root.geometry('500x400') 
    tx = Label(root, text='select a option:')
    tx.pack(side = "left")
    btn_add_book = Button(root, text = 'add book', 
                    command = lambda:add_book()) 
    btn_add_book.pack(side = 'top')
    btn_edit_book = Button(root, text = 'edit book', 
                    command = lambda:edit_book()) 
    btn_edit_book.pack(side = 'top')
    btn_del_book = Button(root, text = 'del book', 
                    command = lambda:del_book()) 
    btn_del_book.pack(side = 'top')
    btn_quit = Button(root, text = 'back',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom') 
    root.mainloop()
    return
def loan():
    root = Tk()           
    root.geometry('500x400') 
    tx = Label(root, text='select a option:')
    tx.pack(side = "left")
    btn_get_book = Button(root, text = 'get book', 
                    command = lambda:get_book())
    btn_get_book.pack(side = 'top') 
    btn_get_back_book = Button(root, text = 'get back book', 
                    command = lambda:give_back_book())
    btn_get_back_book.pack(side = 'top')
    btn_quit = Button(root, text = 'back',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom') 
    root.mainloop()
    return
def libry_detail():
    root = Tk()           
    root.geometry('500x400') 
    tx = Label(root, text='select a option:')
    tx.pack(side = "left")  
    btn_libry_list = Button(root, text = 'show libry list', 
            command = lambda:lib_list())
    btn_libry_list.pack(side = 'top')
    btn_search_book = Button(root, text = 'search a book', 
                command = lambda:check_book()) 
    btn_search_book.pack(side = 'top')
    btn_my_book = Button(root, text = 'my book', 
                    command = lambda:my_book()) 
    btn_my_book.pack(side = 'top')
    btn_quit = Button(root, text = 'back',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom') 
    root.mainloop()
    return
def log_detail():
    root = Tk()           
    root.geometry('500x400') 
    tx = Label(root, text='select a option:')
    tx.pack(side = "left")
    btn_all_log = Button(root, text = 'all log', 
                    command = lambda:all_log()) 
    btn_all_log.pack(side = 'top')
    btn_all_users_data = Button(root, text = 'all users data', 
                    command = lambda:api.all_user_data(main,users))
    btn_all_users_data.pack(side = 'top')
    btn_quit = Button(root, text = 'back',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom') 
    root.mainloop()
    return
q=False
# sign in
signin(users)
user_input , user_num , username , pas =user_input_var , user_num_var , username_var , password_var 
#check admin and main
if user_input==True:
    admin = system.check_admin(users,user_num)
    main = system.check_main(users,user_num)
log = system.open_log()

if user_input==True and admin==True:
    root = Tk()           
    root.geometry('300x300') 
    tx = Label(root, text='select a option:')
    tx.pack(side = "left")
    btn_loan = Button(root, text = 'loan',
                    command = lambda:loan())
    btn_loan.pack(side = 'top')
    btn_user_maneger = Button(root, text = 'user maneger',
                    command = lambda:user_maneger())
    btn_user_maneger.pack(side = 'top')
    btn_book_maneger = Button(root, text = 'book maneger',
                    command = lambda:book_maneger())
    btn_book_maneger.pack(side = 'top')
    btn_libry_detail = Button(root, text = 'libry detail',
                    command = lambda:libry_detail())
    btn_libry_detail.pack(side = 'top')
    btn_log_detail = Button(root, text = 'log detail',
                    command = lambda:log_detail())
    btn_log_detail.pack(side = 'top')
    btn_edit_user = Button(root, text = 'change password', 
                    command = lambda:edit_user())
    btn_edit_user.pack(side = 'top') 
    btn_quit = Button(root, text = 'quit',
                    command = root.destroy) 
    btn_quit.pack(side = 'top')
    root.mainloop() 
elif user_input==True:
    root = Tk()           
    root.geometry('600x350')
    tx = Label(root, text='select a option:')
    tx.pack(side = "left")   
    btn_loan = Button(root, text = 'loan',
                    command = lambda:loan())
    btn_loan.pack(side = 'top')
    btn_libry_detail = Button(root, text = 'libry detail',
                    command = lambda:libry_detail())
    btn_libry_detail.pack(side = 'top')
    btn_edit_user = Button(root, text = 'change password', 
                    command = lambda:edit_user())
    btn_edit_user.pack(side = 'top') 
    btn_quit = Button(root, text = 'quit',
                    command = root.destroy) 
    btn_quit.pack(side = 'top')
    root.mainloop() 