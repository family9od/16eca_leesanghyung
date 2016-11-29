class TrafficCardClass(object):
    def __init__(self):
        self.balance_won = 0

    def deposit(self, amount):
        self.balance_won += int(amount)

    def pay(self, amount):
        self.balance_won -= int(amount)

    def check(self):
        return self.balance_won

import os
print("__name__ in %s = %s" % (os.path.basename(__file__), __name__))

if "__main__" == __name__:
    my_card = TrafficCardClass()
    print("my-card.chek() = %s" % my_card.check())
    print("my_card.deposit(10000) = %s" % my_card.deposit(10000))
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())

    your_card = TrafficCardClass()
    print("your_card.check() = %s" % your_card.check())

    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
    print("my_card.pay(1250) = %s" % my_card.pay(1250))
    print("my_card.check() = %s" % my_card.check())
