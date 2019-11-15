class BankAccount(object):
    def __init__(self, account, balance, currency):
        if (balance < 0):
            raise ValueError(f'Balance is negative: {str(balance)}.')

        if (currency == ''):
            raise ValueError('Currency is missing.')

        self._account = account
        self._balance = balance
        self.currency = currency
        self._history = ['Account was created']

        return

    def deposit(self, amount):
        if (amount < 0):
            raise ValueError(f'Amount is negative: {str(amount)}.')
        self._balance += amount
        self._history.append(f'Deposited {amount}{self.currency}')

        return

    def balance(self):
        self._history.append(f'Balance check -> {self._balance}{self.currency}')
        return self._balance

    def withdraw(self, amount):
        balance_before_withdraw = self._balance - amount

        if (balance_before_withdraw < 0):
            successful = False
            self._history.append( f'Withdraw failed {amount}{self.currency}')
        else:
            successful = True
            self._balance = balance_before_withdraw
            self._history.append(f'Deposited {amount}{self.currency}')

        return successful

    def __str__(self):
        return f'Bank account for {self._account} with balance of {self._balance}{self.currency}'

    def __int__(self):
        self._history.append(f'__int__ check -> {self._balance}{self.currency}')

        return self._balance

    def history(self):
        return self._history

    def transfer_to(self, to_account, amount):
        successful = False

        if (amount < 0):
            raise ValueError(f'Can`t withdraw negative amount: {amount}')

        if (self.currency == to_account.currency):
            successful = self.withdraw(amount)
            if (not successful):
                raise ValueError(f'Not enough funds. Can\'t withdraw {amount}. Available: {self.balance()}')

            to_account.deposit(amount)
            successful = True
        else:
            raise TypeError(f'Currency {self.currency} is different than to {to_account.currency}')

        return successful



