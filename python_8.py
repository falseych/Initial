#from sys import argv
#scrip,rainbow = argv
rainbow=raw_input("Please input the filename\n")
fp=open(rainbow)
print "The content of %s:"%rainbow
print fp.read()
