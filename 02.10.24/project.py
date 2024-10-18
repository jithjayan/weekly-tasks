# user=[]
from registration import *
from login import *
from admin import *
from user import *
while True:
    print('''
          1.Register
          2.Login
          3.Exit''')
    ch=int(input("Enter the choice"))
    if ch==1:
        register()
    elif ch==2:
        f,u=login()
        if f==1:
            while True:
                print('''
                      1.Add charges
                      2.view stops
                      3.update
                      4.delete
                      5.view user
                      6.exit''')
                num=int(input("enter the choice"))
                if num==1:
                    add_stop()
                elif num==2:
                    view_stop()
                elif num==3:
                    update_stop()
                elif num==4:
                    delete_stop()
                elif num==5:
                    view_usr()
                elif num==6:
                    break
                else:
                    print("invalid input")
        elif f==2:
            while True:
                print('''
                    1.view profile
                    2.book ticket
                    3.update profile
                    4.view tickes
                    5.logout''')
                c1=int(input('enter your choice : '))
                if c1==1:
                    view_pro(u)
                elif c1==2:
                    book_t()
                elif c1==3:
                    update_usr(u)
                elif c1==4:
                    order(u)
                elif c1==5:
                    break
                else:
                    print('invalid option')


                             
                            
