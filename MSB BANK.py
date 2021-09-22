import time
while True:
    #start up
    print("\t\t\t\tWELCOME TO MSB BANK")
    print("\t\t\t\t===================")
    a=input('card number:')
    b=input('pin:')
    if a=='10101010'and b=='1234':
        print("\t\t\t\tMSB BANK")
        print("\t\t\t\t========")
        c=100000
        print("[1]Deposit")
        print("[2]Balance")
        print("[3]Withdraw")
        print('[4]Tansfer')
        print('[5]Exit')
        while True:
            d=int(input("MSB BANK:"))
            #deposit section
            if d==1:
                print('\tDeposit')
                print('\t=======')
                e=int(input("How much:"))
                if e<100:
                    print(e,"is low amount\n(min cash:100 and max cash:20000)")
                    print('Deposit fail')
                elif e<=20000:
                    c+=e
                    print("drop the cash to cashbox")
                    time.sleep(7)
                    print('money is counting please wait')
                    time.sleep(7)
                    print("Money is credited sucessfully")
                else:
                    print(e,"is high amount goto MSB BANK for deposit\n(min cash:100 and max cash:20000)")
                    print('Deposit fail')
            #balance section
            elif d==2:
                print('\tBalance')
                print('\t=======')
                print('Balance:',c)
            #withdraw section
            elif d==3:
                print('\tWithdraw')
                print('\t========')
                f=int(input("How much:"))
                if c==0:
                    print("Balance is zero")
                    print('Withdraw fail')
                elif f<100:
                    print(f,"is low amount\n(min cash:100 and max cash:20000)")
                    print('Withdraw fail')
                elif c<f:
                    if f<=20000:
                        print('insuficent amount Balance is',c)
                        print('Withdraw fail')
                    else:
                        print(f,"is high amount goto MSB BANK for more cash\n(min cash:100 and max cash:20000)")
                        print('Withdraw fail')
                elif f<=20000:
                    c-=f
                    time.sleep(10)
                    print("Collect the cash")
                else:
                    print(f,"is high amount goto MSB BANK for more cash\n(min cash:100 and max cash:20000)")
                    print('Withdraw fail')
            #transfer section
            elif d==4:
                print('\tTransfer')
                print('\t========')
                aa=input('BANK NAME:')
                ab=input('IFCE CODE:')
                ac=input('ACCOUNT NUMBER:')
                af=input('NAME:')
                ad=int(input('How much:'))
                ae=input('pin:')
                if ae==b:
                    if c==0:
                        print("Balance is zero")
                        print('Transfer fail')
                    elif ad==0:
                        print(ad,"is low amount\n(min cash:1 and max cash:200000)")
                        print('Transfer fail')
                    elif c<ad:
                        if ad<=200000:
                            print('insuficent amount Balance is',c)
                            print('Transfer fail')
                        else:
                            print(ad,"is high amount to transfer\n(min cash:1 and max cash:200000)")
                            print('Transfer fail')
                    elif ad<=200000:
                        c-=ad
                        print('Transfer sucessfull\n')
                        print('*'*25)
                        print('\tRecipt')
                        print('*'*25)
                        print('To:\nBANK NAME:',aa)
                        print('IFCE CODE:',ab)
                        print('ACCOUNT NUMBER:',ac)
                        print('NAME:',af,'\n')
                        print('From:\nBANK NAME:MSB Bank')
                        print('IFCE CODE:MSB100000')
                        print('ACCOUNT NUMBER:10000000')
                        print('NAME:Muhammed Shihab')
                        print('AMOUNT:',ad)
                        print('*'*25)
                    else:
                        print(ad,"is high amount to transfer\n(min cash:1 and max cash:200000)")
                        print('Transfer fail')
                else:
                    print('Transfer fail')
            #exit section
            elif d==5:
                exit()
            else:
                print('Invaild operation!!!')
    else:
        print("wrong!!!!!!!!")
