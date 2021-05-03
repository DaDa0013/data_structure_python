class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None
	def __str__(self):
		return str(self.key)
	
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	def __len__(self):
		return self.size
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
	
	def pushFront(self, key):
		new_node=Node(key)
		if self.head==None:
			self.head=new_node
		else:
			new_node.next=self.head
			self.head=new_node
		self.size+=1
		pass
	
	def pushBack(self, key):
		new_node=Node(key)
		if self.head==None:
			self.head=new_node
		else:
			tail=self.head
			while tail.next!=None:
				tail=tail.next
			tail.next=new_node
		self.size+=1
		
	def popFront(self): 
		if self.head==None:
			return None
		else:
			pop_node=self.head
			pop_data=pop_node.key
			self.head=pop_node.next
			self.size-=1
			del pop_node
			return pop_data
		# head 노드의 값 리턴. empty list이면 None 리턴
	def popBack(self):
		if self.size==0:
			return None
		else:
			prev=None
			tail=self.head
			while tail.next!=None:
				prev=tail
				tail=tail.next
			if prev==None:
				self.head=None
			else:
				prev.next=tail.next
			pop_data=tail.key
			del tail
			self.size-=1
			return pop_data
		# tail 노드의 값 리턴. empty list이면 None 리턴
	def search(self, key):
		current=self.head
		while current!=None:
			if current.key==key:
				return current
			current=current.next
		return None
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
	def remove(self, x):
		current=self.head
		prev=None
		if x==None:
			return False
		while current!=None:
			if current==x:
				break
			prev=current
			current=current.next
		if self.size==1:
			self.head=None
		elif prev==None:
			self.head=current.next
		else:
			prev.next=current.next
		del current
		self.size-=1
		return True
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
		# x는 key 값이 아니라 노드임에 유의!

	def reverse(self,key):
		current=self.head
		prev=None
		while current!=None:# current 찾기
			if current.key==key:
				break
			prev=current
			current=current.next
		if current==None:
			return
		Stack=[]
		while current!=None:
			Stack.append(current)
			current=current.next
		if prev!=None:
			prev.next=Stack[-1]
		else:
			self.head=Stack[-1]
		for i in range(1,len(Stack)):
			Stack[-1*i].next=Stack[(-1*i)-1]
		Stack[0].next=None
		
	def findMax(self):
		if self.size==0:
			return None
		else:
			current=self.head
			max_key=current.key
			while current.next!=None:
				current=current.next
				if max_key<current.key:
					max_key=current.key
			return max_key
		# self가 empty이면 None, 아니면 max key 리턴
	def deleteMax(self):
		if self.size==0:
			return None
		else:
			max_key=self.findMax()
			self.remove(self.search(max_key))
			return max_key
		# self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
	def insert(self, k, val):
		new_node=Node(val)
		if k>self.size:
			self.pushBack(val)
		else:
			prev=None
			node=self.head
			self.size+=1
			for i in range(k):
				prev=node
				node=node.next
			new_node.next=node
			prev.next=new_node
	
	def size(self):
		return self.size
	
# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == "pushFront":
		L.pushFront(int(cmd[1]))
		print(int(cmd[1]), "is pushed at front.")
	elif cmd[0] == "pushBack":
		L.pushBack(int(cmd[1]))
		print(int(cmd[1]), "is pushed at back.")
	elif cmd[0] == "popFront":
		x = L.popFront()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from front.")
	elif cmd[0] == "popBack":
		x = L.popBack()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "reverse":
		L.reverse(int(cmd[1]))
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
	elif cmd[0] == "insert":
		L.insert(int(cmd[1]), int(cmd[2]))
		print(cmd[2], "is inserted at", cmd[1]+"-th position.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")