shop=[]
while True:
    print('''
          1.Registration
          2.View
          3.Update
          4.Delete
          5.Search
          6.bill
          ''')
    num=int(input("Enter the input"))
    if num==1:
        cname=str(input("Enter customer name"))
        vnum=input("Enter vehicle number")
        phnum=int(input("Enter phone number"))
        while True:
            print(''' 
            1.full wash
            2.exterior
            3.interior''')
            n=int(input("enter the value"))
            if n==1:
                price=10000
                type='full'
                break
            elif n==2:
                price=5000
                break
            elif n==3:
                price=7000
                break
            else:
                print("Invalid choice")
        washtype=type 
        wprice=price      
        shop.append({"cname":cname,"vnum":vnum,"phnum":phnum,"washtype":washtype,"wprice":price})
    elif num==2:
         for i in shop:
            print(i)
    elif num==3:
         a=input('enter vehicle number')
         for i in shop:
              f=0
              if i['vnum']==a:
                   nprice=input("enter new price")
                   i['pprice']=nprice
                   f=1               
         if f==0:
              print("product not found")       
    elif num==6:
        z=input("v num")
        f=0
        for i in shop:
            if i["vnum"]==z:
                print(i['cname'],i['vnum'],i['phnum'],i['washtype'])
                print('Amount payable') 
                print(i['wprice'])
elif
pt



