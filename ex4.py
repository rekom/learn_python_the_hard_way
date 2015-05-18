# nombre de car
cars = 100
# place disponible dans le car
space_in_a_car = 4.0
# nombre de drivers
drivers = 30
# nombre de passagers
passengers = 90
# nombre de car non conduit
cars_not_driven = cars - drivers
# nombre de drivers
cars_driven = drivers
# taille du nombre de passager maximum possible
carpool_capacity = cars_driven * space_in_a_car
# moyenne de passager par car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
