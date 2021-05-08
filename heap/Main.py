class AdaptedHeap: # min_heap으로 정의함!
	def __init__(self):
		self.A = []
		self.D = {}  # dictionary D[key] = index

	def __str__(self):
		return str(self.A)
	def __len__(self):
		return len(self.A)

	def insert(self, key):
		self.A.append(key)
		self.D[key]=len(self.A)-1
		self.heapify_up(len(self.A)-1)
		return self.D[key]
		# code here
		# key 값이 최종 저장된 index를 리턴한다!

	def heapify_up(self, k):
		while k > 0 and self.A[(k-1)//2] > self.A[k]:
			a=self.A[k]
			b=self.A[(k-1)//2]
			self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
			self.D[a],self.D[b] = (k-1)//2, k
			k = (k-1)//2
		# code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
	
	def heapify_down(self, k):
		n=len(self.A)
		while n>= 2*k +1:# 자식 노드가 있는가?
			L, R= 2*k + 1, 2*k + 2
			m = k # m = (A[k], A[L], A[R]) 중 작은 값을 가지는 index
			if self.A[k] > self.A[L]:
				m = L
			if n > R:
				if self.A[m] > self.A[R]:
					m = R
			if k == m:
				break
			else:
				a=self.A[k]
				b=self.A[m]
				self.A[k], self.A[m]= self.A[m], self.A[k],
				self.D[a], self.D[b] = m, k
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
		if len(self.A)==0:
			return None
		key=self.A[0]
		a=self.A[-1]
		self.A[0],self.A[-1], = self.A[-1],self.A[0]
		self.D[key],self.D[a] = len(self.A)-1,0
		self.A.pop()
		del self.D[a]
		self.heapify_down(0)
		return key

	def update_key(self, old_key, new_key):
		# old_key가 힙에 없으면 None 리턴
		# 아니면, new_key 값이 최종 저장된 index 리턴
		# code here
		for i in range(len(self.A)):
			if self.A[i]==old_key:
				n=self.D[old_key]
				del self.D[old_key]
				self.A[n]=new_key
				self.D[new_key]=n
				
				if old_key < new_key:
					self.heapify_down(n)
				else:
					self.heapify_up(n)
				return n
		return None

		
		
# 아래 명령 처리 부분은 수정하지 말 것!
H = AdaptedHeap()
while True:
	cmd = input().split()
	if cmd[0] == 'insert':
		key = int(cmd[1])
		loc = H.insert(key)
		print(f"+ {int(cmd[1])} is inserted")
	elif cmd[0] == 'find_min':
		m_key = H.find_min()
		if m_key != None:
			print(f"* {m_key} is the minimum")
		else:
			print(f"* heap is empty")
	elif cmd[0] == 'delete_min':
		m_key = H.delete_min()
		if m_key != None:
			print(f"* {m_key} is the minimum, then deleted")
		else:
			print(f"* heap is empty")
	elif cmd[0] == 'update':
		old_key, new_key = int(cmd[1]), int(cmd[2])
		idx = H.update_key(old_key, new_key)
		if idx == None:
			print(f"* {old_key} is not in heap")
		else:
			print(f"~ {old_key} is updated to {new_key}")
	elif cmd[0] == 'print':
		print(H)
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")