def get_book (libry,users):
    log = open("log.txt","a")
    esm=input("esm karbar: ")
    if esm in users :
        print("karbar yaft shod")
        esm_ketab=input("esm ketab mored nazar: ")
        if esm_ketab in libry :
            log.write(esm +" "+ esm_ketab +"\n")
            print("anjam shod")
        else:
            print("ketab yaft nashod")
            return
    else:
        print('karbar yaft nashod')
        return
libry = open("libry.txt","r")
users = open("users.txt","r")
libry = libry.read().splitlines()
users = users.read().splitlines()
get_book(libry,users)
