"""
Course CS2301 MW 1:30-2:50pm
Instructor:Fuentes, Olac
Tovar, Brianna
Date of last modification: 2/16/2019
2nd Lab
This lab is over creating different algorithms to find the median of a randomly
generated list of integars, and compare their running times.
"""
"""
Created on Sat Feb 16 14:46:44 2019

@author: ItsBri
"""

import random

#method to create random lists
"""
builds a list of n length after receiving integar n
"""
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None 

def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Prepend(L,x):
    if IsEmpty(L):
        L.head=Node(x)
        L.tail=L.head
    else:
        L.head=Node(x,L.head)
        
def Search(L,x):
    temp=L.head
    while temp is not None:
        if temp.item==x:
            return temp
        temp=temp.next
    return None
        
def InsertAfter(L,x,item): #correct method
    s=Search(L,x)
    if s is None:
        Append(L,x)
    else:
        s.next=Node(item,s.next)
        
def Concatenate(L1,L2):
        #appends list 1 to 2
        if IsEmpty(L1):
            L1.head=L2.head
            L1.tail=L2.tail
        else:
            if IsEmpty(L2):
                L1.tail=L2.head
            else:
                L1.tail.next=L2.head

def Print(L):
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 
    
def GetLength(L):
    temp=L.head
    count =0
    while temp is not None:
        count+=1
        temp=temp.next
    return count

def Copy(L):
    temp=L.head
    new=List()
    while temp is not None:
        Append(new,temp.item)
        temp=temp.next
    return new

def ElementAt(L,x):
    Search(L,x)
    return

#sorting method to put in order
def Bubble(L):
    change= True
    while change:
        t=L.head
        change= False
        while t.next is not None:
            if t.item>t.next.item:
                temp=t.item
                t.item=t.next.item
                t.next.item=temp
                change= True
            t=t.next
#mergesort, notes from TA: its okay to hvae 2 methods, one to separate(checks), recursion check(comparing each
#elements to each other (single at the end they'll be single elements) and merge by insertafter after comparing
    #and seeing which goes where, can also use the pointer itself
def Merge(L):
    if IsEmpty:
        return None
    else:
        DivideConquor(L)
        return Concatenate(L1,L2) #not sure how to send lists after DivideConquor
    
def DivideConquor(L):
    temp=L.head
    while temp is not None:
            L1= (L.head+L.tail)//2
            L2= (L.head+L.tail)//2 
            if L1.head>L1.tail:
                L1.head=L1.tail.next #here is where im comparing & sorting
            if L1.head<L1.tail:
                return
            if L2.head>L2.tail:
                L2.head=L2.tail.next
            if L2.head<L2.tail:
                return
            temp=temp.next
            return
#not finished
            
#Notes from TA: quicksort, starting with the head, you can compare (going through the list), pivot is head
        #each element to that pivot (the head of the list), when its less than
        #move it to the left, making it before the head(.head) prepend, if its greater, then move
        #it to the right, making the element after the head (head.next) insertafter. you keep going until
        #the end of the list, recursion, and using the commands from exercise, returning median too
        #2-3 test cases, handle up to 100 integars, concate and add pivot to the middle
def Quick(L):
    if IsEmpty:
        return None
    pivot=L.head
    Switch(L,pivot)
def Switch(L,pivot):
    temp=L.head
    while temp is not None:
        if temp.item>=pivot.item:
            temp=InsertAfter(L,temp, temp.item) #not sure if using right variable name
        if temp.item<=pivot.item:
            temp=Prepend(L,temp.item)
        temp=temp.next
        return
#single recursive call with quicksort, mainly focusing on greater than the pivot because the less than will stay the same
def QuickOnce(L):
    if IsEmpty:
        return None
    piv=L.head
    SwitchTwo(L,piv)
def SwitchTwo(L,piv):
    temp=L.head
    while temp is not None:
        if temp>=piv:
            temp=InsertAfter(L,temp, temp.item) #not sure if right variable name
        else:
            temp=Prepend(L,temp.item)
        temp=temp.next
        return
#all medians for each sort
def MedianB(L):
    C = Copy(L)
    Bubble(C)
    return ElementAt(C,GetLength(C)//2)
def MedianM(L):
    C = Copy(L)
    Merge(C)
    return ElementAt(C,GetLength(C)//2)
def MedianQ(L):
    C = Copy(L)
    Quick(C)
    return ElementAt(C,GetLength(C)//2)
def MedianQO(L):
    C = Copy(L)
    QuickOnce(C)
    return ElementAt(C,GetLength(C)//2)

L = List()
print(IsEmpty(L))
n=int(input("Type the length you want your list to be:"))
for i in range(n):
    x=random.randrange(0,10)
    Append(L,x)
Print(L)

Bubble(L)
Print(L)
print(MedianB(L))
Merge(L)
Print(L)
print(MedianM(L))
Quick(L)
Print(L)
print(MedianQ(L))
QuickOnce(L)
Print(L)
print(MedianQO(L))
"""
#Test Cases
L = List()
print(IsEmpty(L))
for i in range(5):
    Append(L,i)
Print(L)

L=List()
L=[]
L=[1,7,2,2,5]
L=[4]
L=[10,8,2,4,1]
"""