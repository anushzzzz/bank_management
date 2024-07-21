import classes as c

bank=c.Bank()

while True:

    print('\nChoose an option:\n1.Create  2.Display  3.Deposit  4.Withdraw  5.Exit\n')
    ch=int(input('-->'))

    if ch==1:
        name=input('Enter name: ')
        amount=int(input('Enter amount: '))
        bank.createAcc(name, amount)

    elif ch==2:
        acc=int(input('Enter account number: '))        
        bank.display_acc(acc)

    elif ch==3:
        acc=int(input('Enter account number: '))        
        amount=int(input('Enter amount: '))
        bank.dep(acc, amount)

    elif ch==4:
        acc=int(input('Enter account number: '))        
        amount=int(input('Enter amount: '))
        bank.withd(acc, amount)

    elif ch==5:
        break

    else:
        print('invalid choice!')

