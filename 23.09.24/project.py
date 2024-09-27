user=[]
shop=[]

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
        user.append({'id':id,'name':name,'age':age,'email':email,'phone':phone,'password':password,'book':[]})
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
                1.Add book
                2.View Book
                3.Update Book Details
                4.Delete book
                5.View Users
                6.Logout''')

                c1=int(input('enter your choice : '))
                if c1==1:
                    add_bk()
                elif c1==2:
                    view_bk()
                elif c1==3:
                    update_bk()
                elif c1==4:
                    delete_bk()
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
                    2.view book
                    3.update profile
                    4.Rent a book
                    5.Return a book
                    6.Books in hand
                    7.logout''')
                c1=int(input('enter your choice : '))
                if c1==1:
                    view_pro(u)
                elif c1==2:
                    view_bk()
                elif c1==3:
                    update_usr(u)
                elif c1==4:
                    rent(u)
                elif c1==5:
                    return_bk(u)
                elif c1==6:
                    bkhnd(u)
                elif c1==7:
                    break
                else:
                    print('invalid option')
        else:
            print('invalid username or password')       