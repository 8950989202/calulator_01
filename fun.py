from cal import*
while(True):
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.divide")
    print('enter x to exit')
    choice = input("Enter your choice (1,2,3,4): ")
    x=float(input('enter the no'))
    y=float(input('enter the no'))
    if choice == '1' or choice=='add' or choice=='+':
        add(x,y)
    elif choice == '2' or choice=='sub' or choice=='-':
        sub(x,y)
    elif choice == '3' or choice=='mul' or choice=='*':
        mul(x,y)
    elif choice == '4' or choice=='div' or choice=='/':
        divide(x,y)
    else:
        print("EXIT")
'''

import a

c=a.b['name']
print(c)
'''
