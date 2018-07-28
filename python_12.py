def add(a,b):
    return a+b

def minus(a,b):
    return a-b

groupA=20
groupB=30
total=add(groupA,groupB)
print "%d+%d=%d\n"%(groupA,groupB,total)

f1=float(raw_input("Please enter the a in \"a-b\"\n"))
f2=float(raw_input("Please enter the b in \"a-b\"\n"))
diff=minus(f1,f2)
print "%f-%f=%f\n"%(f1,f2,diff)
