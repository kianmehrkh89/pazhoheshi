# import tkinter module 
import classs
from datetime import datetime
from tkinter import *
from tkinter.ttk import *        
import time     
#files
#RGB
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb 
system = classs.system()
api = classs.user()
users=system.open_users()
libry = system.open_book()

#TKinter
user_input_var , user_num_var , username_var , password_var = None , None , None , None
def check_user(username,pas,users,root):
    global user_input_var , user_num_var , username_var , password_var
    user_input_var , user_num_var = system.check_user(username,pas,users)
    if user_input_var == TRUE:
        username_var , password_var = username , pas
        root.destroy()
    return
def signin(users):
    root1=Tk()
    root1.geometry("200x100")
    name_label = Label(root1, text = 'نام کاربری:')
    username_get = Entry(root1)
    passw_label = Label(root1, text = 'رمز عبور:')
    pas=Entry(root1)
    sub=Button(root1,text = 'تایید', command = lambda:check_user(username_get.get(), pas.get(), users, root1))
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
    root.geometry('300x300')
    root.configure(bg="palegoldenrod")
    for i in lis:
        tx = Label(root, text=i)
        tx.pack(side = "top")
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom')
    root.mainloop()
    return
def get_book():
    root = Tk()           
    root.geometry('300x300') 
    root.configure(bg=_from_rgb((255, 255, 200)))
    book_label = Label(root, text = 'کتابی که می‌خواهید: ')
    book_entry = Entry(root)
    def gt(event):
        api.get_book(username,book_entry.get(),log,libry,root)
        return
    book_entry.bind("<Return>", gt)
    sub =Button(root,text = 'تایید', 
                command = lambda:api.get_book(username,book_entry.get(),log,libry,root))
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy) 
    book_label.grid(row=0,column=0)
    book_entry.grid(row=0,column=1)
    sub.grid(row=1,column=1)
    btn_quit.grid(row=2,column=1)
    root.mainloop()
    return
def give_back_book():
    root = Tk()           
    root.geometry('300x300') 
    root.configure(bg=_from_rgb((255, 255, 200)))
    book_label = Label(root, text = 'کتابی که می‌خواهید برگردانید: ')
    book_entry = Entry(root)
    sub =Button(root,text = 'تایید', 
                command = lambda:api.give_back_book(username,(book_entry.get()),log,libry,root))
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy)
    def gt(event):
        api.give_back_book(username,(book_entry.get()),log,libry,root)
        return
    book_entry.bind("<Return>", gt)
    book_label.grid(row=0,column=0)
    book_entry.grid(row=0,column=1)
    sub.grid(row=1,column=1)
    btn_quit.grid(row=2,column=1)
    root.mainloop()
    return
def add_user():
    root = Tk()         
    root.geometry('300x300') 
    root.configure(bg=_from_rgb((255, 210, 210)))
    name_label = Label(root, text = 'نام کاربری:')
    username_get = Entry(root)
    pass_label = Label(root, text = 'رمز عبور:')
    password=Entry(root)
    type_label = Label(root, text = 'نوع کاربر:')
    type = Combobox(root)
    type['values'] = ("ادمین", "کاربر")
    sub =Button(root,text = 'ثبت', 
                command = lambda:api.add_user(username_get.get(),password.get(),type.get(),main,users,root))
    btn_quit = Button(root, text = 'بازگشت',
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
    root.geometry('300x300') 
    pas_label = Label(root, text = 'رمز عبور قبلی:')
    pas_get = Entry(root)
    newpas_label = Label(root, text = 'رمز عبور جدید:')
    newpas=Entry(root)
    rpt_newpas_label = Label(root, text = 'تکرار رمز عبور جدید:')
    rpt_newpas=Entry(root)
    sub =Button(root,text = 'تایید', 
                command = lambda:api.edit_user(pas,pas_get.get(),newpas.get(),rpt_newpas.get(),users,user_num,root))
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy)
    pas_label.grid(row=0,column=0)
    pas_get.grid(row=0,column=1)
    newpas_label.grid(row=1,column=0)
    newpas.grid(row=1,column=1)
    rpt_newpas_label.grid(row=2,column=0)
    rpt_newpas.grid(row=2,column=1)
    sub.grid(row=3,column=1)
    btn_quit.grid(row=4,column=1)
    root.mainloop()
    return
#def del_user():
    root = Tk()         
    root.geometry('300x300') 
    root.configure(bg=_from_rgb((255, 210, 210)))
    username_label = Label(root, text = 'Username')
    username_get = Entry(root)
    check_label = Label(root, text = 'are you sure?')
    check = Combobox(root)
    check['values'] = ("yes", "no")
    sub =Button(root,text = 'continue', 
                command = lambda:api.del_user(username_get.get(),check.get(),main,users))
    btn_quit = Button(root, text = 'back',
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
    root.geometry('300x300') 
    root.configure(bg=_from_rgb((210, 255, 210)))
    name_label = Label(root, text = "نام کتاب جدید به لاتین: ")
    BookName = Entry(root)
    author_label = Label(root, text = "نام نویسنده به لاتین ")
    author = Entry(root)
    about_label = Label(root, text = "توضیحات کتاب: ")
    about = Entry(root)
    num_label = Label(root, text = "تعداد کتاب: ")
    num=Entry(root)
    sub=Button(root,text = 'تایید',
                command = lambda:api.add_book(BookName.get(),num.get(),author.get(),about.get(),libry,root))
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy) 
    name_label.grid(row=0,column=0)
    BookName.grid(row=0,column=1)
    num_label.grid(row=1,column=0)
    num.grid(row=1,column=1)
    sub.grid(row=2,column=1)
    author_label.grid(row=3,column=0)
    author.grid(row=3,column=1)
    about_label.grid(row=4,column=0)
    about.grid(row=4,column=1)
    btn_quit.grid(row=5,column=1)
    root.mainloop()
    return
def edit_book():
    root = Tk()         
    root.geometry('300x300') 
    root.configure(bg=_from_rgb((210, 255, 210)))
    name_label = Label(root, text = "نام کتاب: ")
    BookName = Entry(root)
    num_label = Label(root, text = "تعداد موجود: ")
    num=Entry(root)
    sub=Button(root,text = 'تایید',
                command = lambda:api.edit_book((BookName.get(),num.get(),libry,root)))
    btn_quit = Button(root, text = 'بازگشت',
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
    root.geometry('300x300') 
    root.configure(bg=_from_rgb((210, 255, 210)))
    name_label = Label(root, text = "نام کتاب: ")
    BookName = Entry(root)
    sub=Button(root,text = 'تایید',
                command = lambda:api.del_book(BookName.get(),libry))
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy) 
    name_label.grid(row=0,column=0)
    BookName.grid(row=0,column=1)
    sub.grid(row=1,column=1)
    btn_quit.grid(row=2,column=1)
    root.mainloop()
    return
def about_book():
    root = Tk()         
    root.geometry('300x300') 
    root.configure(bg="palegoldenrod")
    id_label = Label(root, text = "ایدی کتاب:")
    id_ = Entry(root)
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy)
    def gt(event):
        for i in range(len(libry["id"])):
            print(i)
            if libry["id"][i] == id_.get():
                root.destroy()
                system.about_book(i,libry)
        return
    id_.bind("<Return>", gt)
    id_label.grid(row=0,column=0)
    id_.grid(row=0,column=1)
    btn_quit.grid(row=1,column=1)
    root.mainloop()
    return
def check_book():
    root = Tk()         
    root.geometry('300x300') 
    root.configure(bg="palegoldenrod")
    name_label = Label(root, text = "نام کتاب: ")
    BookName = Entry(root)
    sub=Button(root,text = 'تایید',
                command = lambda:system.check_book(BookName.get(),libry,root,log,username))
    btn_quit = Button(root, text = 'بازگشت',
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
    root.geometry('300x300')
    root.configure(bg="palegoldenrod")
    if len(a)==0:
        tx = Label(root, text =  "شما کتابی دریافت نکردید")  
        tx.pack(side = "top")      
    else:
        for i in a:
           tx = Label(root, text =  i) 
           tx.pack(side = "top")
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom')
    root.mainloop()
    return
def all_log():
    root = Tk()         
    root.geometry('300x300')
    root.configure(bg=_from_rgb((240, 180, 255))) 
    a = api.all_log(log)
    for i in a:
        tx = Label(root, text =  i) 
        tx.pack(side = "top")
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom')
    root.mainloop()
def all_user_data():
    root = Tk()
    root.geometry('300x300')
    root.configure(bg=_from_rgb((240, 180, 255))) 
    a = api.all_user_data(main,users)
    for i in a:
        tx = Label(root, text =  i) 
        tx.pack(side = "top")
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom')
    root.mainloop()
def user_maneger():
    root = Tk()           
    root.geometry('300x300') 
    root.configure(bg=_from_rgb((255, 210, 210)))
    btn_add_user = Button(root, text = 'اضافه کردن کاربر', 
                    command = lambda:add_user())
    btn_add_user.pack(side = 'top')
    #btn_del_user = Button(root, text = 'del user', 
                    #command = lambda:del_user())
    #btn_del_user.pack(side = 'top')
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom') 
    root.mainloop()
    return
def book_maneger():
    root = Tk()           
    root.geometry('300x300')
    root.configure(bg=_from_rgb((210, 255, 210)))
    btn_add_book = Button(root, text = 'اضافه کردن کتاب', 
                    command = lambda:add_book()) 
    btn_add_book.pack(side = 'top')
    btn_edit_book = Button(root, text = 'تغییر موجودی کتاب', 
                    command = lambda:edit_book()) 
    btn_edit_book.pack(side = 'top')
    btn_del_book = Button(root, text = 'حذف کتاب', 
                    command = lambda:del_book()) 
    btn_del_book.pack(side = 'top')
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom') 
    root.mainloop()
    return
def loan():
    root = Tk()           
    root.geometry('300x300')
    root.deiconify()
    root.configure(bg=_from_rgb((255, 255, 200)))
    btn_get_book = Button(root, text = 'گرفتن کتاب', 
                    command = lambda:get_book())
    btn_get_book.pack(side = 'top') 
    btn_get_back_book = Button(root, text = 'پس دادن کتاب', 
                    command = lambda:give_back_book())
    btn_get_back_book.pack(side = 'top')
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom') 
    root.mainloop()
    return
def libry_detail():
    root = Tk()           
    root.geometry('300x300')
    root.configure(bg="palegoldenrod")
    btn_libry_list = Button(root, text = 'نمایش لیست کتابخانه', 
            command = lambda:lib_list())
    btn_libry_list.pack(side = 'top')
    btn_search_book = Button(root, text = 'جست‌وجوی کتاب', 
                command = lambda:check_book()) 
    btn_search_book.pack(side = 'top')
    btn_about_book = Button(root, text = 'درباره کتاب(فقط بارکد)', 
                command = lambda:about_book()) 
    btn_about_book.pack(side = 'top')
    btn_my_book = Button(root, text = 'کتاب‌های من', 
                    command = lambda:my_book()) 
    btn_my_book.pack(side = 'top')
    btn_quit = Button(root, text = 'بازگشت',
                command = root.destroy) 
    btn_quit.pack(side = 'bottom') 
    root.mainloop()
    return
def log_detail():
    root = Tk()           
    root.geometry('300x300')
    root.configure(bg=_from_rgb((240, 180, 255))) 
    btn_all_log = Button(root, text = 'کتاب‌های دریافت شده', 
                    command = lambda:all_log()) 
    btn_all_log.pack(side = 'top')
    btn_all_users_data = Button(root, text = 'اطلاعات تمام کاربران', 
                    command = lambda:all_user_data())
    btn_all_users_data.pack(side = 'top')
    btn_quit = Button(root, text = 'بازگشت',
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
    root.configure(bg=_from_rgb((170, 210, 255))) 

    btn_loan = Button(root, text='قرض', command=lambda: loan())
    btn_loan.pack(side='top')

    btn_user_maneger = Button(root, text='مدیریت کاربران', command=lambda: user_maneger())
    btn_user_maneger.pack(side='top')

    btn_book_maneger = Button(root, text='مدیریت کتاب‌ها', command=lambda: book_maneger())
    btn_book_maneger.pack(side='top')

    btn_libry_detail = Button(root, text='جزئیات کتاب‌ها', command=lambda: libry_detail())
    btn_libry_detail.pack(side='top')

    btn_log_detail = Button(root, text='جزئیات اطلاعات', command=lambda: log_detail())
    btn_log_detail.pack(side='top')

    btn_edit_user = Button(root, text='تغییر رمز عبور', command=lambda: edit_user())
    btn_edit_user.pack(side='top') 

    btn_quit = Button(root, text='خروج', command=root.destroy) 
    btn_quit.pack(side="bottom")

    root.mainloop() 
elif user_input==True:
    root = Tk()           
    root.geometry('300x300')   
    btn_loan = Button(root, text = 'قرض',
                    command = lambda:loan())
    btn_loan.pack(side = 'top')
    btn_libry_detail = Button(root, text = 'جزئیات کتابخانه',
                    command = lambda:libry_detail())
    btn_libry_detail.pack(side = 'top')
    btn_edit_user = Button(root, text = 'تغییر رمز عبور', 
                    command = lambda:edit_user())
    btn_edit_user.pack(side = 'top') 
    btn_quit = Button(root, text = 'خروج',
                    command = root.destroy) 
    btn_quit.pack(side = 'top')
    root.mainloop() 