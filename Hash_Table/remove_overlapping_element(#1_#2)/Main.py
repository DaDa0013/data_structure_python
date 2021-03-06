#
# HashOpenAddr 클래스 선언
class HashOpenAddr:
	def __init__(self, size=10):
		self.size = size
		self.keys = [None]*self.size
		self.values = [None]*self.size
	def __str__(self):
		s = ""
		for k in self:
			if k == None:
				t = "{0:5s}|".format("")
			else:
				t = "{0:-5d}|".format(k)
			s = s + t
		return s

	def __iter__(self):
		for i in range(self.size):
			yield self.keys[i]

	def find_slot(self, key):
		i = self.hash_function(key)
		start = i
		while self.keys[i] != key and self.keys[i] != None:
			i = (i + 1) % self.size
			if i == start:
				return None
		return i

	def set(self, key, value=None):
		i = self.find_slot(key)
		if i == None:
			return None
		if self.keys[i] == key:
			self.values[i]= value
		else:
			self.keys[i] = key
			self.values[i] = value
		return key

	def hash_function(self, key):
		return key % self.size

	def remove(self, key):
		i = self.find_slot(key)
		if self.keys[i] == None:
			return None
		j = i
		while True:
			self.keys[i] = None
			while True:
				j = (j + 1) % self.size
				if self.keys[j] == None:
					return key
				k = self.hash_function(self.keys[j])
				if k <= i < j or i < j < k or j < k <= i:
					break
			self.keys[i] = self.keys[j]
			i = j

	def search(self, key):
		i = self.find_slot(key)
		if i==None:
			return None
		if self.keys[i] != None:
			return key
		else:
			return None
			
	def __getitem__(self, key):
		return self.search(key)
	def __setitem__(self, key, value):
		self.set(key, value)


# 입력
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
#
# 코드 (hash table을 이용해야 함)

M=HashOpenAddr(int(len(A)*1.5))
J=HashOpenAddr(int(len(B)*1.5))
for i in A:
	M.set(i)
for m in B:
	J.set(m)
	
count=[0]*100000 #물건 번호의 인덱스에 물건 갯수 저장하는 리스트
for k in A:
	if J.search(k)!=None:
		count[k]+=1
		
for x in B:
	if count[x]!=0: 
		print(x,end=' ')
		count[x]-=1
print()
	
for j in B:
	if M.search(j)!=None:
		print(j,end=' ')
		M.remove(j)
		
	


	







