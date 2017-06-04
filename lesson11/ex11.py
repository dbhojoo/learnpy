print "How old are you?",
age = float(raw_input())
print "What units?",
au = raw_input()

print "How tall are you?",
height = float(raw_input())
print "What units?",
tu = raw_input()

print "How much do you weigh?",
weight = float(raw_input())
print "What units?",
wu = raw_input()

print "So, you're %f %r old, %f %r tall and %f %r heavy." % (
    age, au, height, tu, weight, wu)
