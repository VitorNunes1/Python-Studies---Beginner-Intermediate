class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return None if self.is_empty() else self.stack.pop()

    def  __str__(self):
        string = "Stack: ["
        for i in range(len(self.stack)):
            if i > 0: string += ","
            string += str(self.stack[i])
        string += "]"
        return string

    

stack = Stack()
for a in range(2):
    stack.push("A")
    stack.push("B")
    print(stack)
    print(stack.pop())
    stack.push("C")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())