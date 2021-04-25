import time
while True:
        a=input("username:")
        b=input("password:")
        if a=='shihab'and b=='root':
                print("\t\t\t\tMSB BANK")
                print("\t\t\t\t=========")
                c=100000
                print("#deposit")
                print("#balance")
                print("#withdraw")
                print('#exit')
                while True:
                        d=input(">>>")
                        if d=='deposit':
                                e=int(input("How much:"))
                                if e<=20000:
                                        c+=e
                                        print("drop the cash to cashbox")
                                        time.sleep(7)
                                        print('money is counting please wait')
                                        time.sleep(7)
                                        print("Money is credited sucessfully")
                                else:
                                        print(" This is high amount goto MSB BANK for deposit")
                        elif d=='balance':
                                print('Balance:',c)
                        elif d=='withdraw':
                                f=int(input("How much:"))
                                if c>0:
                                        if f<=20000:
                                                c-=f
                                                time.sleep(10)
                                                print("Collect the cash")
                                        else:
                                                print("This is high amount goto MSB BANK for more cash")
                                else:
                                        print("Balance is zero")
                        elif d=='exit':
                                exit()
                        else:
                                print('Invaild operation!!!')
        else:
                print("wrong!!!!!!!!")
