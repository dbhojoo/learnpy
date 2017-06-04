#this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# okay, that *arg is actually pointless and we can just do this ...
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this takes none
def print_none():
	print "I got nothin'."


#declarations

print_two("dem","bho")
print_two_again("dem","bho")
print_one("dem")
print_none()

#ending comment
