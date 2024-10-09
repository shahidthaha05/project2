veh=[]
users=[]

def add_veh():
    if len(veh)==0:
        id=101
    else:
        id=veh[-1]['id']+1
    f=0
    for i in veh:
        if i['id']==id:
            f=1
            add_veh()
    if f==0:
        name=str(input("enter the  name : "))
        brand=str(input("enter the brand : "))
        model=int(input("enter the model : "))
        fueltype=str(input("enter the fueltype : "))
        mileage=int(input("enter the mileage : "))
        insurance=int(input("enter insurance : "))
        stock=int(input("enter the stock : "))
        veh.append({'name':name,'id':id,'brand':brand,'model':model,'fueltype':fueltype,'mileage':mileage,'insurance':insurance,'stock':stock})


def view_veh():
    for i in veh:
        print(i)

def update_veh():
    id=int(input("enter the id : "))
    f=0
    for i in veh:
        if i['id']==id:
            f=1
            fueltype=str(input("enter the fueltype : "))
            insurance=int(input("enter the insurance : "))
            stock=int(input("enter the stock"))
            i['fueltype']=fueltype
            i['insurance']=insurance
            i['stock']=stock
    if f==0:
        print('invalid id')

def delete():
    id=int(input("enter the id : "))
    f=0
    for i in veh: 
        if i['id']==id:
            f=1
            veh.remove(i)
    if f==0:
        print('invalid id')
