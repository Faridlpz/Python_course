def create_stack():
    stack = []
    return stack

def null_stack(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print("pushed item: " + item)

def pop(stack):
    if (null_stack(stack)):
        return "stack is empty"

    return stack.pop()

mi=create_stack()
push(mi,str(1))
push(mi,str(2))
push(mi,str(3))
push(mi,str(4))
print("popped item: " + pop(mi))
print("popped item: " + pop(mi))
print("stack after popping an element: " + str(mi))

