user=[]
from registration import *

while True:
    print('''
          1.Register
          2.Login
          3.Exit''')
    ch=int(input("Enter the choice"))
    if ch==1:
        register()
