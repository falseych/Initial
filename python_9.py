from sys import argv
scrip,butterfly = argv

#fairy = open(butterfly,"w")
fairy = open(butterfly,"a+")


print "\nThe origin content of %s:"%butterfly
print fairy.read()


line1="It is a boring task, unless--"
line2="Unless you could learn more via the Internet."
line3="AND SACRIFICE ...............(blutter words hard to recognize)"

fairy.write(line1)
fairy.write("\n")
fairy.write(line2)
fairy.write("\n")
fairy.write(line3)
fairy.write("\n")

fairy.close()


fairy = open(butterfly,"a+")
print "\n\nThe revised %s:"%butterfly
print fairy.read()


