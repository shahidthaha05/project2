from admin import *
from log import *
from user import *
from list import *



while True:
    print('''
    1.register
    2.login
    3.exit 
''')
    choice=int(input("enter the choice :"))
    if choice==1:
        register()
    elif choice==2:
        f,cust=login()
        if f==1:
            while True:
                print('''
                1.add veh
                2.view veh
                3.update veh
                4.delete
                5.view user
                6.exit
                ''')
                sub_choice=int(input("enter the choice : "))
                if sub_choice==1:
                    add_veh()
                elif sub_choice==2:
                    view_veh()
                elif sub_choice==3:
                    update_veh()
                elif sub_choice==4:
                    delete()
                elif sub_choice==5:
                    view_user()
                elif sub_choice==6:
                    break
                else:
                    print('invalid choice')
        elif f==2:
            while True:
                print('''
                1.view profile
                2.view veh
                3.update profile
                4.buy veh
                5.veh in hand
                6.exit
                ''')
                sub_ch=int(input("enter the choice : "))
                if sub_ch==1:
                    view_profile(cust)
                elif sub_ch==2:
                    view_veh()
                elif sub_ch==3:
                    update_pro(cust)
                elif sub_ch==4:
                    buy_veh(cust)
                elif sub_ch==5:
                    veh_in_hand(cust)
                elif sub_ch==6:
                    break
                else:
                    print("invalid choice")
        else:
            print('invalid username or password')
    elif choice==3:
        break
    else:
        print('invalid')