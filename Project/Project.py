amount = input('Insert your amount: ') 
TotalValue = 0
FinalValue = 0

# Deposito

def Deposit(amount: int):
    int(amount)
    int(TotalValue)
    FinalValue =  int(TotalValue) + int(amount)

    print('Your Actually Money: R$: ', float(FinalValue))


def Withdraw(amount: int):
    int(amount)
    ValueRetired = input('Insert value your retire: ')
    int(ValueRetired)
    FinalValue = int(amount) - int(ValueRetired)
    print('Your Actually Money: R$: ', float(FinalValue))

Withdraw(amount)