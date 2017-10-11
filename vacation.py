# Vacation calculator

def hotel_cost(nights):
  # should make cost per night
  # user input
  return 140 * nights

def plane_ride_cost(city):
  # all the magic numbers :(
  if city == 'Charlotte':
    return 183
  elif city == 'Tampa':
    return 220
  elif city == 'Pittsburgh':
    return 222
  elif city == 'Los Angeles':
    return 475

def rental_car_cost(days):
  total = 40 * days
  if days >= 7:
    return total - 50
  elif days >= 3:
    return total - 20
  else:
    return total

def trip_cost(city, days, spending_money):
  print 'Flight round trip: %s' % plane_ride_cost(city)
  print 'Hotel stay: %s' % hotel_cost(days)
  print 'Rental car: %s' % rental_car_cost(days)
  print 'Spending money: %s' % spending_money

  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print 'Total: %s' % trip_cost('Los Angeles', 5, 600)
