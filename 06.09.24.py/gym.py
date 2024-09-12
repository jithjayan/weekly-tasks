gym=[{"cname":'hufu',"vnum":11,"phnum":3534,"washtype":'full',"wprice":10000}]
while True:
    print('''
          1.Registration
          2.View
          3.Update
          4.Delete
          5.Search
          6.bill
          7.exit
          ''')
    num=int(input("Enter the input"))
    if num==1:
        cname=str(input("Enter customer name"))
        age=int(input("Enter the age"))
        phnum=int(input("Enter phone number"))
        print("Gender:")
        print("Select plan")
        while True:
            print(''' 
            1.monthly
            2.6 month
            3.yearly''')
            n=int(input("enter the value"))
            if n==1:
                price=10000
                type='monthly'
                break
            elif n==2:
                price=5000
                type='6 month'
                break
            elif n==3:
                price=7000
                type='yearly'
                break
            else:
                print("Invalid choice")
        plan=type 
        amount=price      
        gym.append({"cname":cname,"phnum":phnum,"plan":plan,"price":price})
    elif num==2:
         for i in gym:
            print(i)
    elif num==3:
         a=int(input('enter vehicle number'))
         f=0
         for i in gym:
              if i["vnum"]==a:
                   nprice=input("enter new price")
                   i['wprice']=nprice
                   f=1               
         if f==0:
              print(" not found")   
    elif num==4:
        a=int(input("Enter vehicle number"))
        f=0
        for i in gym:
            if i['vnum']==a:
                gym.remove(i)
                f=1
        if f==0:
                print(" not found")
    elif num==5:
        a=int(input("Enter vehicle number"))
        f=0
        for i in gym:
            if i['vnum']==a:
                print(i)
                f=1
        if f==0:
            print("Invalid id")

    elif num==6:
        z=int(input("v num"))
        f=0
        for i in gym:
            if i["vnum"]==z:
                print(i['cname'],i['vnum'],i['phnum'],i['washtype'])
                print('Amount payable') 
                print(i['wprice'])
                f=1
        if f==0:
            print("not found")
    elif num==7:
        break
    else:
        print("Invalid input")
            


