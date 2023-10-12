#bitwise oprators
a = int(input("enter no."))
b = int(input("enter no."))
# a=1
# b=2

print('a=', a, bin(a))
print('b=', b, bin(b))
c=0

#And

c = a & b
print("result of AND is: ", c)

#Or

c = a | b
print("result of OR is: ", c,bin(c))

#EXor

c = a ^ b
print("result of EXOR is: ", c,bin(c))

#compliment
c = ~a
print("result of COMPLEMENRT is: ", c,bin(c))

#left shift

c = a << 2
print("result of LEFT SHIFT is: ", c,bin(c))

#right shift

c = a >> 2
print("result of RIGHT SHIFT is: ", c,bin(c))

