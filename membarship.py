print("I find the no.in list: ")
a = int(input("enter number"))
b = int(input("enter number"))

list = [range(1500, 2700)]
if (a in list):
    print("1- a is in list")
else:
    print("1- a is not in list")

if(b not in list):   
        print("2- b is in list")
else:
         print("2- b is not in list")        

c=b/a
if (c in list):
          print("3- c is in list")
else:
           print("3- c is not in list")