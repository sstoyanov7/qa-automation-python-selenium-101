class Bill(object):
    def __init__(self, amount):
        if not isinstance(amount, int):
            raise TypeError('Amount is not integer')

        if amount < 0:
            raise ValueError('Amount is negative')
        self._amount = amount

    def __str__(self):
        return "A " + str(self._amount) + "$ bill"

    def __repr__(self):
        return self._amount

    def __int__(self):
        return self._amount

    def __eq__(self, other_bill):
        if self._amount == int(other_bill):
            return True
        else:
            return False

    def __hash__(self):
        return hash(self._amount)


class BatchBill(object):
    def __init__(self, bills):
        self.bills = bills

    def __int__(self):
        return self.total()

    def __len__(self):
        return self.bills.count

    def total(self):
        s = 0
        for bill in self.bills:
            s += int(bill)
        return s

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk(object):
    def __init__(self):
        self.banknotes = {}

    def take_bill(self, bill):
        amount = bill._amount
        if not (amount in self.banknotes):
            self.banknotes[amount] = 1
        else:
            self.banknotes[amount] += 1
        return

    def take_money(self, money):
        if isinstance(money, Bill):
            self.take_bill(money)
        else:
            for m in money:
                self.take_bill(m)
        return

    def total(self):
        s = 0
        for banknote in self.banknotes:
            count = self.banknotes[banknote];
            s += count * banknote
        return s

    def inspect(self):
        s = f'We have a total of {self.total()}$ in the desk\n'
        s += 'We have the following count of bills, sorted in ascending order:'
        keys = sorted(self.banknotes.keys())
        for k in keys:
            s += '\n' + str(k) + '$ bills - ' + str(self.banknotes[k])
        return s


if __name__ == "__main__":
    a = Bill(10)

    values = [10, 20, 50, 100]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    for bill in batch:
        print(bill)

    # A 10$ bill
    # A 20$ bill
    # A 50$ bill
    exit(0)