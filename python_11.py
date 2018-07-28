def print_none():
    print "Hello world!"

def print_one(arg):
    print "Hi,%r,my friend."%arg

def print_two(arg1,arg2):
    print "WARNING!WARNING!WANRING!%r and %r are coming!"%(arg1,arg2)


print_none()
print_one("John")
print_two("Octa","Donu")
