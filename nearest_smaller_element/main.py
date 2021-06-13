class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        try:
            return self.data.pop()
        except IndexError:
            return -1

    def top(self):
        try:
            return self.data[-1]
        except IndexError:
            return -1

    def empty(self):
        return len(self.data) == 0

def nearestSmaller(A):
    S = Stack()
    B=[]
    for i in range(len(A)):
        if S.empty():
            B.append(None)
            S.push(A[i])
        else:
            while not S.empty() and A[i]< S.top():
                S.pop()
            if S.empty():
                B.append(None)
            else:
                B.append(S.top())
            S.push(A[i])
    return B

A= list(map(int, input().split()))
print(nearestSmaller(A))