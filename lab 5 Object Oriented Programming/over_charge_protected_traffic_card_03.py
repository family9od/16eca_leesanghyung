import traffic_card_class_02 as tcc

class NoOverChargeCard(tcc.TrafficCardClass):
    def pay(self, amount):
        if self.balance_won > int(amount):
            super(NoOverChargeCard, self).pay(amount)
        else:
            raise ValueError('Not enough balance')

import os
print("__name__ in %s = %s" % (os.path.basename(__file__), __name__))

if "__main__" == __name__:
    my_card = NoOverChargeCard()
    print("my-card.chek() = %s" % my_card.check())
    print("my_card.deposit(10000) = %s" % my_card.deposit(10000))
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

