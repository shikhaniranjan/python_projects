'''
stack basic operations like push ,pop and reverse stack
'''

class stack():
    def __init__(self):
        self.Elements=[]
    def push(self,value):
        self.Elements.append(value)

    def pop(self):
        return self.Elements.pop()

    def empty(self):
        return self.Elements == []


    def show(self):
        for value in reversed(self.Elements):
            print (value)


def BottomInsert(s,value):
    if s.empty():
        s.push(value)

    else:
        popped =s.pop()
        BottomInsert(s,value)
        s.push(popped)


def Reverse(s):

       if s.empty():
           pass
       else:
           popped =s.pop()
           Reverse(s)
           BottomInsert(s,popped)

stk =stack()
stk.push(34)
stk.push(53)
stk.push(8)
stk.push(90)
print ("Original Stack")
stk.show()
value =int(input("Enter the value you want to add in bottom of the stack "))
Bottom_insert = BottomInsert(stk,value)
print ("Printing stack after adding element at the bottom of the stack")
stk.show()
reverse_stack = Reverse(stk)
print("Printing stack after reverse")
stk.show()
