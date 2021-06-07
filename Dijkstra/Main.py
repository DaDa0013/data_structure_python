class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.weight = 0

    def __str__(self):
        return str(self.key)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def printList(self):  # 변경없이 사용할 것!
        v = self.head
        while (v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

    def pushFront(self, key):
        new_node = Node(key)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        pass

    def pushBack(self, key):
        new_node = Node(key)
        if self.head == None:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):
        if self.head == None:
            return None
        else:
            pop_node = self.head
            pop_data = pop_node.key
            self.head = pop_node.next
            self.size -= 1
            del pop_node
            return pop_data

    # head 노드의 값 리턴. empty list이면 None 리턴
    def popBack(self):
        if self.size == 0:
            return None
        else:
            prev = None
            tail = self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if prev == None:
                self.head = None
            else:
                prev.next = tail.next
            pop_data = tail.key
            del tail
            self.size -= 1
            return pop_data

    # tail 노드의 값 리턴. empty list이면 None 리턴
    def search(self, key):
        current = self.head
        while current != None:
            if current.key == key:
                return current
            current = current.next
        return None

    # key 값을 저장된 노드 리턴. 없으면 None 리턴
    def remove(self, x):
        current = self.head
        prev = None
        if x == None:
            return False
        while current != None:
            if current == x:
                break
            prev = current
            current = current.next
        if self.size == 1:
            self.head = None
        elif prev == None:
            self.head = current.next
        else:
            prev.next = current.next
        del current
        self.size -= 1
        return True

    # 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
    # x는 key 값이 아니라 노드임에 유의!

    def reverse(self, key):
        current = self.head
        prev = None
        while current != None:  # current 찾기
            if current.key == key:
                break
            prev = current
            current = current.next
        if current == None:
            return
        Stack = []
        while current != None:
            Stack.append(current)
            current = current.next
        if prev != None:
            prev.next = Stack[-1]
        else:
            self.head = Stack[-1]
        for i in range(1, len(Stack)):
            Stack[-1 * i].next = Stack[(-1 * i) - 1]
        Stack[0].next = None

    def findMax(self):
        if self.size == 0:
            return None
        else:
            current = self.head
            max_key = current.key
            while current.next != None:
                current = current.next
                if max_key < current.key:
                    max_key = current.key
            return max_key

    # self가 empty이면 None, 아니면 max key 리턴
    def deleteMax(self):
        if self.size == 0:
            return None
        else:
            max_key = self.findMax()
            self.remove(self.search(max_key))
            return max_key

    # self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
    def insert(self, k, val):
        new_node = Node(val)
        if k > self.size:
            self.pushBack(val)
        else:
            prev = None
            node = self.head
            self.size += 1
            for i in range(k):
                prev = node
                node = node.next
            new_node.next = node
            prev.next = new_node

    def size(self):
        return self.size

class AdaptedHeap:  # min_heap으로 정의함!
    def __init__(self):
        self.A = []

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A) - 1)

    # code here
    # key 값이 최종 저장된 index를 리턴한다!

    def heapify_up(self, k):
        while k > 0 and self.A[(k - 1) // 2] > self.A[k]:
            a = self.A[k]
            b = self.A[(k - 1) // 2]
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            k = (k - 1) // 2

    # code here: key 값의 index가 변경되면 그에 따라 D 변경 필요

    def heapify_down(self, k):
        n = len(self.A)
        while n >= 2 * k + 1:  # 자식 노드가 있는가?
            L, R = 2 * k + 1, 2 * k + 2
            m = k  # m = (A[k], A[L], A[R]) 중 작은 값을 가지는 index
            if L < n and self.A[k] > self.A[L]:
                m = L
            if n > R:
                if self.A[m] > self.A[R]:
                    m = R
            if k == m:
                break
            else:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m

    # code here: key 값의 index가 변경되면 그에 따라 D 변경 필요

    def find_min(self):
        # 빈 heap이면 None 리턴, 아니면 min 값 리턴
        # code here
        if len(self.A) == 0:
            return None
        return self.A[0]

    def delete_min(self):
        # 빈 heap이면 None 리턴, 아니면 min 값 지운 후 리턴
        # code here
        if len(self.A) == 0:
            return None
        key = self.A[0]
        self.A[0], self.A[-1], = self.A[-1], self.A[0]
        self.A.pop()
        self.heapify_down(0)
        return key

    def update_key(self, old_key, new_key):
        # old_key가 힙에 없으면 None 리턴
        # 아니면, new_key 값이 최종 저장된 index 리턴
        # code here
        if old_key not in self.A:
            return None

        for i in range(len(self.A)):
            if self.A[i] == old_key:
                self.A[i] = new_key
                if old_key < new_key:
                    self.heapify_down(i)
                else:
                    self.heapify_up(i)
                return i


class Dijkstra:
    def __init__(self):
        self.dist = [float("inf")]*n
        self.dist[0] = 0

    def relax(self, u, v):
        if self.dist[v.key] > self.dist[u.key] + v.weight:
            self.dist[v.key] = self.dist[u.key] + v.weight

    def give_dist(self):
        H = AdaptedHeap()
        for i in range(n):
            H.insert(self.dist[i])
        return H

    def fix_dist(self, H, Graph):
        check_u=[]
        while len(H) != 0:
            w = H.delete_min()

            for i in range(len(self.dist)):
                if self.dist[i] == w and i not in check_u:
                    u = i
                    break
            check_u.append(u)

            if Graph[u]!=None:
                G = Graph[u].search(u)
                U = G
                while G.next:
                    old_key = self.dist[G.next.key]
                    self.relax(U, G.next)
                    H.update_key(old_key, self.dist[G.next.key])
                    G = G.next
        return self.dist

n = int(input())
m = int(input())
Graph = [None]*n

for i in range(m):
    cmd = input().split()
    u, v, w = int(cmd[0]), int(cmd[1]), int(cmd[2])
    if Graph[u] == None:
        Graph[u] = SinglyLinkedList()
        Graph[u].pushBack(u)
    Graph[u].pushBack(v)
    a = Graph[u].search(v)
    a.weight = w

T = Dijkstra()
H = T.give_dist()
dist = T.fix_dist(H, Graph)

result = ""
for i in dist:
    result = result + str(i) + " "
print(result)