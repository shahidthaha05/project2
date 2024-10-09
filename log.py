
veh=[]
users=[]

def register():
    if len(users)==0:
        id=1
    else:
        id=user[-1]['id']+1
    

    email=str(input("enter the email :"))
    f=0
    for i in users:
        if i['email']==email:
            f=1
            register()
    if f==0:
        name=str(input("enter the name :"))
        username=email
        phone=int(input("enter the no :"))
        password=str(input("enter password :"))
        users.append({'name':name,'id':id,'email':email,'phone':phone,'veh':[],'username':username,'password':password})

def login():
    uname=input("enter uname : ")
    passw=input("enter passw : ")
    f=0
    if uname == 'admin' and passw == 'admin':
        f=1
    cust=''
    for i in users:
        if uname == i['email'] and passw == i['password']:
            f=2
            cust=i
    return f,cust
