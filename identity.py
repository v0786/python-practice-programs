a = int(input("enter number"))
b = int(input("enter number"))

print('1','a=',a,':',id(a),  'b=',b,':',id(b),)
if(a is b):
    print("2 - a and b have same identity")
else:
    print("2 - a and b do not have same identity")

if(id(a) == id(b)):
    print("3 - a and b have same identity")
else:
     print("3 - a and b do not have same identity")

if (a is not b):
     print("4 - a and b do not have same identity")
else:
     print("4 - a and b have same identity")