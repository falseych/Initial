from sys import argv
scrip,butterfly = argv

fairy = open(butterfly,"a+")

rainbow=raw_input("Please input the file to be copied.\n")
rainbow_fp=open(rainbow)

print "\nThe origin content of \"%s\":"%butterfly
print fairy.read()

cp_content = rainbow_fp.read()
fairy.write(cp_content)

fairy.seek(0,0)
print "\n\nThe revised \"%s\":"%butterfly
print fairy.read()

fairy.close()




