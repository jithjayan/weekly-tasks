
from admin import *
from login import *
from registration import *
def view_pro(u):
    print('NAME : ',u['name'])
    print('ID : ',u['id'])
    print('Email : ',u['email'])
    print('Phone : ',u['phone'])
    print('Password : ',u['password'])
    print('tickets : ',u['tickets'])


def book_t():
    strt=str(input("from"))
    stop=str(input("stop"))
    f=0
    for i in data:
        if i['stplace']==strt and i['stoplace']==stop:
            ['tickets'].append(stop)
            print("price=",i['price'])
            f=1
    if f==0:
        print("invalid input")

def update_usr(u):
    phone=int(input('enter your number : '))
    password=input('enter new password')
    u['phone']=phone
    u['password']=password
    print('updated')

def order(u):
    print(u['tickets'])        
