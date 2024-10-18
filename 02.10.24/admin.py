
data=[{'id':1,'stplace':'jln','stoplace':'klr','price':5},{'id':2,'stplace':'jln','stoplace':'twn','price':10}]
from registration import *
def add_stop():
    print('ADD STOP DETAILS')
    if len(data)==0:
        id=1
    else:
        id=data[-1]['id']+1
    stplace=str(input('enter start place : '))
    stoplace=str(input('enter stop place : '))
    price=int(input('enter the price : '))
    # stock=int(input('enter the stock availible : '))
    data.append({'id':id,'stplace':stplace,'stoplace':stoplace,'price':price})


def delete_stop():
    id=int(input('enter the id : '))
    f=0
    for i in data:
        if i['id']==id:
            data.remove(i)
            print('data deleted')
            f=1
    if f==0:
        print('Invalid id')


def view_stop():
    print('STOPS')
    print("{:<5}{:<10}{:<10}{:<10}".format('ID','START','STOP','PRICE'))
    print('_'*30)
    for i in data:
        print("{:<5}{:<10}{:<10}{:<10}".format(i['id'],i['stplace'],i['stoplace'],i['price']))

def update_stop():
    id=int(input('enter the id : '))
    f=0
    for i in data:
        if i['id']==id:
            price=int(input('enter the price : '))
            i['price']=price
            print('Details Updated')
            f=1
    if f==0:
        print('invalid id')


def view_usr():
    print('USERS DETAILS')
    print("{:<10}{:<15}{:<15}{:<15}".format('ID','NAME','EMAIL','PHONE'))
    print('_'*55)
    for i in user:
        print("{:<10}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['email'],i['phone']))
