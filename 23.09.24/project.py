  user=[{'id': 1000, 'name': 'ww','age':'11', 'email': 'qq','phone': 920712, 'password': 'asd','products':[1]}]
shop=[{'id': 1, 'name': 'aa', 'price': 11, 'stock': 22}]

def register():
    print('Registration Page')
    if len(user)==0:
        id=1000
    else:
        id=user[-1]['id']+1
    email=str(input('enter your email :'))
    f=0
    for i in user:
        if i['email']==email:
            f=1
            print('email already exists enter another one')
            register()
    if f==0:
        name=str(input('enter your name : '))
        age=int(input('enter your age : '))
        phone=int(input('enter your number : '))
        password=input('enter the password : ')
        print('Registration Succesfull email id is your username')
        user.append({'id':id,'name':name,'age':age,'email':email,'phone':phone,'password':password,'products':[]})
def login():
    usern=str(input('Enter Username : '))
    passw=input('Enter password : ')
    f=0
    u=''
    if usern=='admin' and passw=='admin':
        f=1
    for i in user:
        if usern==i['email'] and passw==i['password']:
            f=2
            u=i
    return f,u

def add_prdt():
    print('ADD PRODUCTS')
    if len(shop)==0:
        id=1
    else:
        id=shop[-1]['id']+1
    name=str(input('enter name : '))
    price=int(input('enter the price : '))
    stock=int(input('enter the stock availible : '))
    shop.append({'id':id,'name':name,'price':price,'stock':stock})
def view_prdt():
    print('BOOK DETAILS')
    print("{:<5}{:<10}{:<10}{:<10}".format('ID','PRODUCT','PRICE','STOCK'))
    print('_'*30)
    for i in shop:
        print("{:<5}{:<10}{:<10}{:<10}".format(i['id'],i['name'],i['price'],i['stock']))

def update_prdt():
    id=int(input('enter the id : '))
    f=0
    for i in shop:
        if i['id']==id:
            price=int(input('enter the price : '))
            stock=int(input('enter the stock : '))
            i['price']=price
            i['stock']=stock
            print('Details Updated')
            f=1
    if f==0:
        print('invalid id')

def delete_prdt():
    id=int(input('enter the id : '))
    f=0
    for i in shop:
        if i['id']==id:
            shop.remove(i)
            print('data deleted')
            f=1
    if f==0:
        print('Invalid id')
        
def view_usr():
    print('USERS DETAILS')
    print("{:<10}{:<15}{:<15}{:<15}".format('ID','NAME','EMAIL','PHONE'))
    print('_'*55)
    for i in user:
        print("{:<10}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['email'],i['phone']))

def view_pro(u):
    print('NAME : ',u['name'])
    print('ID : ',u['id'])
    print('Email : ',u['email'])
    print('Phone : ',u['phone'])
    print('Password : ',u['password'])
    print('products : ',u['products'])

def update_usr(u):
    phone=int(input('enter your number : '))
    password=input('enter new password')
    u['phone']=phone
    u['password']=password
    print('updated')
    
def buy(u):
    id=int(input('enter the id : '))
    f=0
    for i in shop:
        if i['id']==id:
            f=1
            i['stock']-=1
            u['products'].append(id)
            print('product purchased')
    if f==0:
        print('invalid ID')
        
def order(u):
    print(u['products'])        
        
while True:
    print('''
          1.Register
          2.login
          3.logout''')
    ch=int(input('enter your choice:'))
    if ch==1:
        register()
    elif ch==2:
       f,u=login()
       if f==1:
            while True:
                print('''
                1.Add products
                2.View products
                3.Update product Details
                4.Delete product
                5.View Users
                6.Logout''')

                c1=int(input('enter your choice : '))
                if c1==1:
                    add_prdt()
                elif c1==2:
                    view_prdt()
                elif c1==3:
                    update_prdt()
                elif c1==4:
                    delete_prdt()
                elif c1==5:
                    view_usr()
                elif c1==6:
                    break
                else:
                    print('invalid Choice')
       elif f==2:
            while True:
                print('''
                    1.view profile
                    2.view products
                    3.update profile
                    4.buy product 
                    5.orders
                    6.logout''')
                c1=int(input('enter your choice : '))
                if c1==1:
                    view_pro(u)
                elif c1==2:
                    view_prdt()
                elif c1==3:
                    update_usr(u)
                elif c1==4:
                    buy(u)
                elif c1==5:
                    order(u)
                elif c1==6:
                    break
                else:
                    print('invalid option')
       else:
            print('invalid username or password')       
