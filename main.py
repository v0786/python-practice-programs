from tkinter import *
import random
import time
root=Tk()

#just a commonly used function
def r(a,b):
    r=random.randint(a,b)
    return r


#veriables
sqr=7
sq=4
locx=r(1,5)
locy=r(1,5)
max=0


#btncolor

b1c="white"
b2c="white"
b3c="white"
b4c="white"
b5c="white"

b21c="white"
b22c="white"
b23c="white"
b24c="white"
b25c="white"

b31c="white"
b32c="white"
b33c="white"
b34c="white"
b35c="white"

b41c="white"
b42c="white"
b43c="white"
b44c="white"
b45c="white"

b51c="white"
b52c="white"
b53c="white"
b54c="white"
b55c="white"

#definations



    
def pointer():
    xcng=True
    global max
    global locx
    global locy
    if 1==1:
        if locx==1:
             if r(0,1)==0:
                  locx+=1
                  xcng=True
             else:
                xcng=False
                
        elif locx==5:
             if r(0,1)==0:
                 locx-=1
                 xcng=True
             else:
                 xcng=False
                 
        elif r(0,1)==1:
            locx+=1
            xcng=True
            
        else:
            locx-=1
            xcng=True
        #If there is no change in the value of x axis then it must change the value of Y axis
        if xcng==False:
            
            if locy==5:
                locy-=1
            elif locy==1:
                locy+=1
            elif r(0,1)==0:
                locy+=1
            else:
                locy-=1

        #if there is a change in the value of x axis then it may change the value of Y axis           
        elif r(0,1)==1:
            if locy==5:
                locy-=1
            elif locy==1:
                locy+=1
            else:
                if r(0,1)==1:
                    locy+=1
                else:
                    locy-=1             
                
            
            
            
    
    else:
        xcng=False    
        


def colour():

    global b1
    global b2
    global b3
    global b4
    global b5

    global b21
    global b22
    global b23
    global b24
    global b25

    global b31
    global b32
    global b33
    global b34
    global b35

    global b41
    global b42
    global b43
    global b44
    global b45

    global b51
    global b52
    global b53
    global b54
    global b55

    global b1c
    global b2c
    global b3c
    global b4c
    global b5c

    global b21c
    global b22c
    global b23c
    global b24c
    global b25c

    global b31c
    global b32c
    global b33c
    global b34c
    global b35c

    global b41c
    global b42c
    global b43c
    global b44c
    global b45c

    global b51c
    global b52c
    global b53c
    global b54c
    global b55c

    global max
    pointer()
    
    if locx==1:
        if locy==1:
            b1c="black"
            b1=Button(root,command= bc1,bg=b1c,width=sqr,height=sqr-sq).grid(row=1,column=1)

        elif locy==2:
            b2c="black"
            b2=Button(root,command= bc2,bg=b2c,width=sqr,height=sqr-sq).grid(row=1,column=2)

        elif locy==3:
            b3c="black"
            b3=Button(root,command= bc3,bg=b3c,width=sqr,height=sqr-sq).grid(row=1,column=3)

        elif locy==4:
            b4c="black"
            b4=Button(root,command= bc4,bg=b4c,width=sqr,height=sqr-sq).grid(row=1,column=4)

        elif locy==5:
            b5c="black"
            b5=Button(root,command= bc5,bg=b5c,width=sqr,height=sqr-sq).grid(row=1,column=5)

    elif locx==2:
        if locy==1:
            b21c="black"
            b21=Button(root,command= bc21,bg=b21c,width=sqr,height=sqr-sq).grid(row=2,column=1)

        elif locy==2:
            b22c="black"
            b22=Button(root,command= bc22,bg=b22c,width=sqr,height=sqr-sq).grid(row=2,column=2)

        elif locy==3:
            b23c="black"
            b23=Button(root,command= bc23,bg=b23c,width=sqr,height=sqr-sq).grid(row=2,column=3)

        elif locy==4:
            b24c="black"
            b24=Button(root,command= bc24,bg=b24c,width=sqr,height=sqr-sq).grid(row=2,column=4)

        elif locy==5:
            b25c="black"
            b25=Button(root,command= bc25,bg=b25c,width=sqr,height=sqr-sq).grid(row=2,column=5)

    elif locx==3:
        if locy==1:
            b31c="black"
            b31=Button(root,command= bc31,bg=b31c,width=sqr,height=sqr-sq).grid(row=3,column=1)

        elif locy==2:
            b32c="black"
            b32=Button(root,command= bc32,bg=b32c,width=sqr,height=sqr-sq).grid(row=3,column=2)
        elif locy==3:
            b33c="black"
            b33=Button(root,command= bc33,bg=b33c,width=sqr,height=sqr-sq).grid(row=3,column=3)
        elif locy==4:
            b34c="black"
            b34=Button(root,command= bc34,bg=b34c,width=sqr,height=sqr-sq).grid(row=3,column=4)
        elif locy==5:
            b35c="black"
            b35=Button(root,command= bc35,bg=b35c,width=sqr,height=sqr-sq).grid(row=3,column=5)

    elif locx==4:
        if locy==1:
            b41c="black"
            b41=Button(root,command= bc41,bg=b41c,width=sqr,height=sqr-sq).grid(row=4,column=1)
        elif locy==2:
            b42c="black"
            b42=Button(root,command= bc42,bg=b42c,width=sqr,height=sqr-sq).grid(row=4,column=2)
        elif locy==3:
            b43c="black"
            b43=Button(root,command= bc43,bg=b43c,width=sqr,height=sqr-sq).grid(row=4,column=3)
        elif locy==4:
            b44c="black"
            b44=Button(root,command= bc44,bg=b44c,width=sqr,height=sqr-sq).grid(row=4,column=4)
        elif locy==5:
            b45c="black"
            b45=Button(root,command= bc45,bg=b45c,width=sqr,height=sqr-sq).grid(row=4,column=5)

    elif locx==5:
        if locy==1:
            b51c="black"
            b51=Button(root,command= bc51,bg=b51c,width=sqr,height=sqr-sq).grid(row=5,column=1)
        elif locy==2:
            b52c="black"
            b52=Button(root,command= bc52,bg=b52c,width=sqr,height=sqr-sq).grid(row=5,column=2)
        elif locy==3:
            b53c="black"
            b53=Button(root,command= bc53,bg=b53c,width=sqr,height=sqr-sq).grid(row=5,column=3)
        elif locy==4:
            b54c="black"
            b54=Button(root,command= bc54,bg=b54c,width=sqr,height=sqr-sq).grid(row=5,column=4)
        elif locy==5:
            b55c="black"
            b55=Button(root,command= bc55,bg=b55c,width=sqr,height=sqr-sq).grid(row=5,column=5)
    


def bc1():
    global b1
    global max
    global b1c
    max -=1
    b1c="white"
    b1=Button(root,command= bc1,bg=b1c,width=sqr,height=sqr-sq).grid(row=1,column=1)
    while max <5:
        max +=1
        colour()

def bc2():
    global b2
    global max
    global b2c
    max -=1
    b2c="white"
    b2=Button(root,command= bc2,bg=b2c,width=sqr,height=sqr-sq).grid(row=1,column=2)
    
    while max <5:
        max +=1
        colour()

def bc3():
    global max
    global b3c
    global b3
    max -=1
    b3c="white"
    b3=Button(root,command= bc3,bg=b3c,width=sqr,height=sqr-sq).grid(row=1,column=3)
    while max <5:
        max +=1
        colour()

def bc4():
    global max
    global b4c
    global b4
    max -=1
    b4c= "white"
    b4=Button(root,command= bc4,bg=b4c,width=sqr,height=sqr-sq).grid(row=1,column=4)
    while max <5:
        max +=1
        colour()

def bc5():
    global max
    global b5c
    global b5
    max -=1
    b5c="white"
    b5=Button(root,command= bc5,bg=b5c,width=sqr,height=sqr-sq).grid(row=1,column=5)
    while max <5:
        max +=1
        colour()

def bc21():
    global max
    global b21c
    global b21
    max -=1
    b21c="white"
    b21=Button(root,command= bc21,bg=b21c,width=sqr,height=sqr-sq).grid(row=2,column=1)
    while max <5:
        max +=1
        colour()

def bc22():
    global max
    global b22c
    global b22
    max -=1
    b22c="white"
    b22=Button(root,command= bc22,bg=b22,width=sqr,height=sqr-sq).grid(row=2,column=2)
    while max <5:
        max +=1
        colour()


def bc23():
    global max
    global b23c
    global b23
    max -=1
    b23c="white"
    b23=Button(root,command= bc23,bg=b23,width=sqr,height=sqr-sq).grid(row=2,column=3)
    while max <5:
        max +=1
        colour()

def bc24():
    global max
    global b24c
    global b24
    max -=1
    b24c="white"
    b24=Button(root,command= bc24,bg=b24,width=sqr,height=sqr-sq).grid(row=2,column=4)
    while max <5:
        max +=1
        colour()

def bc25():
    global max
    global b25c
    global b25
    max -=1
    b25c="white"
    b25=Button(root,command= bc25,bg=b25,width=sqr,height=sqr-sq).grid(row=2,column=5)
    while max <5:
        max +=1
        colour()

def bc31():
    global b31
    global max
    global b31c
    max -=1
    b31c="white"
    b31=Button(root,command= bc31,bg=b31c,width=sqr,height=sqr-sq).grid(row=3,column=1)
    while max <5:
        max +=1
        colour()

def bc32():
    global b32
    global max
    global b32c
    max -=1
    b32c="white"
    b32=Button(root,command= bc32,bg=b32c,width=sqr,height=sqr-sq).grid(row=3,column=2)
    
    while max <5:
        max +=1
        colour()

def bc33():
    global max
    global b33c
    global b33
    max -=1
    b33c="white"
    b33=Button(root,command= bc33,bg=b33c,width=sqr,height=sqr-sq).grid(row=3,column=3)
    while max <5:
        max +=1
        colour()

def bc34():
    global max
    global b34c
    global b34
    max -=1
    b34c= "white"
    b34=Button(root,command= bc34,bg=b34c,width=sqr,height=sqr-sq).grid(row=3,column=4)
    while max <5:
        max +=1
        colour()

def bc35():
    global max
    global b35c
    global b35
    max -=1
    b35c="white"
    b35=Button(root,command= bc35,bg=b35c,width=sqr,height=sqr-sq).grid(row=3,column=5)
    while max <5:
        max +=1
        colour()

def bc41():
    global b1
    global max
    global b41c
    max -=1
    b41c="white"
    b41=Button(root,command= bc41,bg=b41c,width=sqr,height=sqr-sq).grid(row=4,column=1)
    while max <5:
        max +=1
        colour()

def bc42():
    global b42
    global max
    global b42c
    max -=1
    b42c="white"
    b42=Button(root,command= bc42,bg=b42c,width=sqr,height=sqr-sq).grid(row=4,column=2)
    
    while max <5:
        max +=1
        colour()

def bc43():
    global max
    global b43c
    global b43
    max -=1
    b43c="white"
    b43=Button(root,command= bc43,bg=b43c,width=sqr,height=sqr-sq).grid(row=4,column=3)
    while max <5:
        max +=1
        colour()

def bc44():
    global max
    global b44c
    global b44
    max -=1
    b44c= "white"
    b44=Button(root,command= bc44,bg=b44c,width=sqr,height=sqr-sq).grid(row=4,column=4)
    while max <5:
        max +=1
        colour()

def bc45():
    global max
    global b45c
    global b45
    max -=1
    b45c="white"
    b45=Button(root,command= bc45,bg=b45c,width=sqr,height=sqr-sq).grid(row=4,column=5)
    while max <5:
        max +=1
        colour()

def bc51():
    global b51
    global max
    global b51c
    max -=1
    b51c="white"
    b51=Button(root,command= bc51,bg=b51c,width=sqr,height=sqr-sq).grid(row=5,column=1)
    while max <5:
        max +=1
        colour()

def bc52():
    global b52
    global max
    global b52c
    max -=1
    b52c="white"
    b52=Button(root,command= bc52,bg=b52c,width=sqr,height=sqr-sq).grid(row=5,column=2)
    
    while max <5:
        max +=1
        colour()

def bc53():
    global max
    global b53c
    global b53
    max -=1
    b53c="white"
    b53=Button(root,command= bc53,bg=b53c,width=sqr,height=sqr-sq).grid(row=5,column=3)
    while max <5:
        max +=1
        colour()

def bc54():
    global max
    global b54c
    global b54
    max -=1
    b54c= "white"
    b54=Button(root,command= bc54,bg=b54c,width=sqr,height=sqr-sq).grid(row=5,column=4)
    while max <5:
        max +=1
        colour()

def bc55():
    global max
    global b55c
    global b55
    max -=1
    b55c="white"
    b55=Button(root,command= bc55,bg=b55c,width=sqr,height=sqr-sq).grid(row=5,column=5)
    while max <5:
        max +=1
        colour()


#button sets

while max <5:
    colour()
    max+=1


b1=Button(root,command= bc1,bg=b1c,width=sqr,height=sqr-sq).grid(row=1,column=1)
b2=Button(root,command=bc2,bg=b2c,width=sqr,height=sqr-sq).grid(row=1,column=2)
b3=Button(root,command=bc3,bg=b3c,width=sqr,height=sqr-sq).grid(row=1,column=3)
b4=Button(root,command=bc4,bg=b4c,width=sqr,height=sqr-sq).grid(row=1,column=4)
b5=Button(root,command=bc5,bg=b5c,width=sqr,height=sqr-sq).grid(row=1,column=5)

b21=Button(root,command=bc21,bg=b21c,width=sqr,height=sqr-sq).grid(row=2,column=1)
b22=Button(root,command=bc22,bg=b22c,width=sqr,height=sqr-sq).grid(row=2,column=2)
b23=Button(root,command=bc23,bg=b23c,width=sqr,height=sqr-sq).grid(row=2,column=3)
b24=Button(root,command=bc24,bg=b24c,width=sqr,height=sqr-sq).grid(row=2,column=4)
b25=Button(root,command=bc25,bg=b25c,width=sqr,height=sqr-sq).grid(row=2,column=5)


b31=Button(root,command=bc31,bg=b31c,width=sqr,height=sqr-sq).grid(row=3,column=1)
b32=Button(root,command=bc32,bg=b32c,width=sqr,height=sqr-sq).grid(row=3,column=2)
b33=Button(root,command=bc33,bg=b33c,width=sqr,height=sqr-sq).grid(row=3,column=3)
b34=Button(root,command=bc34,bg=b34c,width=sqr,height=sqr-sq).grid(row=3,column=4)
b35=Button(root,command=bc35,bg=b35c,width=sqr,height=sqr-sq).grid(row=3,column=5)

b41=Button(root,command=bc41,bg=b41c,width=sqr,height=sqr-sq).grid(row=4,column=1)
b42=Button(root,command=bc42,bg=b42c,width=sqr,height=sqr-sq).grid(row=4,column=2)
b43=Button(root,command=bc43,bg=b43c,width=sqr,height=sqr-sq).grid(row=4,column=3)
b44=Button(root,command=bc44,bg=b44c,width=sqr,height=sqr-sq).grid(row=4,column=4)
b45=Button(root,command=bc45,bg=b45c,width=sqr,height=sqr-sq).grid(row=4,column=5)

b51=Button(root,command=bc51,bg=b51c,width=sqr,height=sqr-sq).grid(row=5,column=1)
b52=Button(root,command=bc52,bg=b52c,width=sqr,height=sqr-sq).grid(row=5,column=2)
b53=Button(root,command=bc53,bg=b53c,width=sqr,height=sqr-sq).grid(row=5,column=3)
b54=Button(root,command=bc54,bg=b54c,width=sqr,height=sqr-sq).grid(row=5,column=4)
b55=Button(root,command=bc55,bg=b55c,width=sqr,height=sqr-sq).grid(row=5,column=5)

"""
while max <5:
    colour()
    max+=1
    print(max)
    b1=Button(root,command= bc1,bg=b1c,width=sqr,height=sqr-sq).grid(row=1,column=1)
print(";",max)
"""
root.mainloop()