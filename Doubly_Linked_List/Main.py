class Node:
	def __init__(self, key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)

class DoublyLinkedList:
	def __init__(self):
		self.head = Node() # create an empty list with only dummy node

	def __iter__(self):
		v = self.head.next
		while v != self.head:
			yield v
			v = v.next
	def __str__(self):
		return " -> ".join(str(v.key) for v in self)

	def printList(self):
		v = self.head.next
		print("h -> ", end="")
		while v != self.head:
			print(str(v.key)+" -> ", end="")
			v = v.next
		print("h")
	# 나머지 코드
	def splice(self,a,b,x):
		ap=a.prev
		bn=b.next
		xn=x.next
		ap.next=bn
		bn.prev=ap
		x.next=a
		a.prev=x
		b.next=xn
		xn.prev=b
		
	def moveAfter(self,a,x):
		self.splice(a,a,x)
		
	def moveBefore(self,a,x):
		self.splice(a,a,x.prev)
		
	def insertBefore(self,x,key):
		self.moveBefore(Node(key),x)
		
	def insertAfter(self,x,key):
		self.moveAfter(Node(key),x)
		
	def pushFront(self,key):
		self.insertAfter(self.head,key)
		
	def pushBack(self,key):
		self.insertBefore(self.head,key)
		
	def deleteNode(self,x):
		if x==None or x==self.head:
			return None
		x.prev.next=x.next
		x.next.prev=x.prev
		del x
		
	def popFront(self):
		if self.isEmpty():
			return None
		key=self.head.next.key
		self.deleteNode(self.head.next)
		return key
	
	def popBack(self):
		if self.isEmpty():
			return None
		key=self.head.prev.key
		self.deleteNode(self.head.prev)
		return key
	
	def search(self,key):
		tmp=self.head.next
		while tmp!=self.head:
			if tmp.key==key:
				return tmp
			tmp=tmp.next
		return None
	
	def first(self):
		return self.head.next.key
	
	def last(self):
		return self.head.prev.key
	
	def isEmpty(self):
		if self.head.next==None:
			return True
		else:
			return False
		
	def findMax(self):
		if self.isEmpty():
			return None
		key=self.head.next
		Max_key=key.key
		while key!=self.head:
			if Max_key<key.key:
				Max_key=key.key
			key=key.next
		return Max_key
	
	def deleteMax(self):
		Max_key=self.findMax()
		Max_Node=self.search(Max_key)
		self.deleteNode(Max_Node)
		return Max_key
	
	def sort(self):
		new_link=DoublyLinkedList()
		tmp=self.head.next
		count=0
		while tmp!=self.head:
			tmp=tmp.next
			count+=1
		for i in range(count):
			new_link.pushFront(self.deleteMax())
		return new_link
L = DoublyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == 'pushF':
		L.pushFront(int(cmd[1]))
		print("+ {0} is pushed at Front".format(cmd[1]))
	elif cmd[0] == 'pushB':
		L.pushBack(int(cmd[1]))
		print("+ {0} is pushed at Back".format(cmd[1]))
	elif cmd[0] == 'popF':
		key = L.popFront()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Front".format(key))
	elif cmd[0] == 'popB':
		key = L.popBack()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Back".format(key))
	elif cmd[0] == 'search':
		v = L.search(int(cmd[1]))
		if v == None: print("* {0} is not found!".format(cmd[1]))
		else: print("* {0} is found!".format(cmd[1]))
	elif cmd[0] == 'insertA':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertAfter(x, int(cmd[2]))
			print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'insertB':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertBefore(x, int(cmd[2]))
			print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'delete':
		x = L.search(int(cmd[1]))
		if x == None:
			print("- {0} is not found, so nothing happens".format(cmd[1]))
		else:
			L.deleteNode(x)
			print("- {0} is deleted".format(cmd[1]))
	elif cmd[0] == "first":
		print("* {0} is the value at the front".format(L.first()))
	elif cmd[0] == "last":
		print("* {0} is the value at the back".format(L.last()))
	elif cmd[0] == "findMax":
		m = L.findMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key is", m)
	elif cmd[0] == "deleteMax":
		m = L.deleteMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key", m, "is deleted.")
	elif cmd[0] == 'sort':
		L = L.sort()
		L.printList()
	elif cmd[0] == 'print':
		L.printList()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")