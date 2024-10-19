def get_book (libry,users):
    log = open("log.txt","a")
    esm=input("esm karbar: ")
    if esm in users :
        print("karbar yaft shod")
        esm_ketab=input("esm ketab mored nazar: ")
        if esm_ketab in libry :
            khat = libry.index(esm_ketab)
            if (int(libry_n[khat])>0):
                log.write(esm +" "+ esm_ketab +"\n")
                print("anjam shod")
            else:
                print("katab mojod nist")
                return
        else:
            print("ketab yaft nashod")
            return
    else:
        print('karbar yaft nashod')
        return
libry = open("libry.txt","r")
users = open("users.txt","r")
libry_n = open("libry_n.txt","r")
libry = libry.read().splitlines()
users = users.read().splitlines()
libry_n = libry_n.read().splitlines()
get_book(libry,users)
