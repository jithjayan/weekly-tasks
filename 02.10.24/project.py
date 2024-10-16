# user=[]
from registration import *
from login import *
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
                      1.Add text''')

        

