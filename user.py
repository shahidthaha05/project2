from admin import *
from log import *
from list import *



def view_profile(users):
    print(users)


def update_pro(cust):
    name=str(input("enter the name : "))
    phone=int(input("enter phone : "))
    cust['name']=name
    cust['phone']=phone
    
def buy_veh(cust):
    id=int(input("enter the id : "))
    f=0
    for i in veh:
        if i['id']==id:
            f=1
            i['stock']-=1
            cust['veh'].append(id)
            print('veh added')
    if f==0:
        print("invalid id")


def veh_in_hand(cust):
    print(cust['veh'])
