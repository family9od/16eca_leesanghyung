import traffic_card_module_00 as my_card

help(my_card)
print("my_card.check() = %s" % my_card.check())
print("my_card.deposit(10000) = %s" % my_card.deposit(10000))
print("my_card.check() = %s" % my_card.check())
print ("my_card.pay(1250) = %s" % my_card.pay(1250))
print ("my_card.check() = %s" % my_card.check())

import traffic_card_module_00 as your_card

print ("your_card.check() = %s" % your_card.check())
