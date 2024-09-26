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
        phone=int(input('enter your number : '))
        password=input('enter the password : ')
        print('Registration Succesfull email id is your username')
        user.append({'id':id,'name':name,'email':email,'phone':phone,'password':password,'book':[]})



while True:
    print('''
          1.Register
          2.login
          3.logout''')
    ch=int(input('enter your choice:'))
    if ch==1:
        register()
    elif ch==2:
       