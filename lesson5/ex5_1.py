my_name = 'Demis Bhojoo'
my_age = 27 # not a lie
my_height = 1.72 # metres
my_weight = 70 # kgs
my_eyes = 'Brown'
my_teeth = 'Coffee Yellow'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %f metres tall." % my_height
print "He's %d kilograms heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
