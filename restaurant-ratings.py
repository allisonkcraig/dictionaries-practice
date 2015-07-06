opened_file = open('scores.txt')

restaurant = {}

for line in opened_file:
    new_line = line.rstrip().split(":")
    restaurant[new_line[0]] = new_line[1]

for restaurant_name, rating in restaurant.items():
    print "%s is rated at %s" % (restaurant_name, rating)