from os import system as s
import os
import sys
from time import sleep as w
global clr
if sys.platform == 'unix' or sys.platform == 'linux':#Check if we are a unix platform so things dont break
    clr = 'clear'
else:
    clr = 'cls'
def c():
    s(clr)
def zt(cmd):
    s('zerotier-cli '+cmd)
print("""
███████╗███████╗██████╗  ██████╗ ████████╗██╗███████╗██████╗
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝██╔══██╗
  ███╔╝ █████╗  ██████╔╝██║   ██║   ██║   ██║█████╗  ██████╔╝
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║   ██║   ██║██╔══╝  ██╔══██╗
███████╗███████╗██║  ██║╚██████╔╝   ██║   ██║███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝╚══════╝╚═╝  ╚═╝

GUI USING CLI CLIENT | Getting spicy please hold | NOT OFFICIAL
    """)
w(3)
if clr == 'clear':
    if os.getuid() == 0:
        ok = True
    else:
        print("PLEASE EXECUTE AS root/sudo.")
        w(3)
        exit()
    #if os.getuid() != '0' or os.getuid() != 0 or os.getuid() != ' 0': NOT WORKING FOR SOME REASON
    #    print(os.getuid())
#        print("PLEASE EXECUTE AS root/sudo")
#        w(3)
#        exit()
#    else:
#        print('OK.')

while True:
    c()
    print("""
    ███████╗███████╗██████╗  ██████╗ ████████╗██╗███████╗██████╗
    ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝██╔══██╗
      ███╔╝ █████╗  ██████╔╝██║   ██║   ██║   ██║█████╗  ██████╔╝
     ███╔╝  ██╔══╝  ██╔══██╗██║   ██║   ██║   ██║██╔══╝  ██╔══██╗
    ███████╗███████╗██║  ██║╚██████╔╝   ██║   ██║███████╗██║  ██║
    ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝╚══════╝╚═╝  ╚═╝

    GUI USING CLI CLIENT                         | NOT OFFICIAL
    =================================================================
    1) Join Network                     4) List Networks
    2) Leave Network                    5) List Moons
    3) List peers                       6) Bad decision please get me out of here
    """)
    selection = input("SELECT?> ")
    if selection == '1':
        sid = input("Enter the network ID: ")
        print('\n')
        zt('join '+sid)
        input("\nPress any key to return to the menu")
    elif selection == '2':
        sid = input("Enter the network ID: ")
        print('\n')
        zt('leave '+sid)
        input("\nPress any key to return to the menu")
    elif selection == '3':
        print('\n')
        zt('listpeers')
        input("\nPress any key to return to the menu")
    elif selection == '4':
        print('\n')
        zt('listnetworks')
        input("\nPress any key to return to the menu")
    elif selection == '5':
        print('\n')
        zt('listmoons')
        input("\nPress any key to return to the menu")
    elif selection == '6':
        print('\n')
        print("How sad. It was nice knowing you.")
        w(1)
        print("Goodbye")
        w(2)
        exit()
    elif selection == '1337':
        print('\n')
        print("I <3 C0mmun1sm")
    elif selection == '7':
        print('\n')
        print("ERROR: WRONG OPINION PLEASE TRY AGAIN")
    else:
        print('\n')
        print("Mistakes are BaDDdDDdDDD")
        w(1)
        print("You typed something in wrong")
        w(2)
        input("\nPress any key to return to the menu")
