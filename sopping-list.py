# inventory and shopping calculator

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}


def receipt():
    # prints inventory and prices
    for key in sorted(prices):
        print key
        print "price: %s" % prices[key]
        print "stock: %s" % stock[key]
        print


receipt()


def compute_bill(food):
    # prints and calculates bought items
    # adjusts inventory
    print "-------------"
    print "YOUR BILL"
    total = 0
    for item in food:
        if stock[item] > 0:
            total = total + prices[item]
            print "%s: %s" % (item, prices[item])
            stock[item] = stock[item] - 1
    return total


# sending a list of items to buy
shopping_list = ["banana", "orange", "apple"]
print "total: %s" % compute_bill(shopping_list)
print "-------------"

receipt()
