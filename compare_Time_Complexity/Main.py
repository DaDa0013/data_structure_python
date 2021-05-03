import random,time
def unique_n(A):
	B=[]
	for i in range(2*len(A)+1):
		B.append("O")
		#리스트 A의 범위가 -n부터 n으로 총 2n+1개이므로 새로운 리스트 B에 "O"를 2n+1개 삽입
	
	for k in A: # 리스트 A의 요소만큼 반복
		if B[k] == "O": 
			B[k] = "X"   # B[k]가 "O"인 것은 중복이 아니므로 해당 값에 "X" 대입
		else:
			return "NO" #B[k]가 "X"인 경우는 중복인 경우이므로 "NO" 반환
			
	return "YES" #for문을 빠져나왔다는 것은 중복이 없는 경우이므로 "YES" 반환

def unique_nlogn(A):
	A.sort() #리스트 A를 오름차순으로 정렬
	for i in range(len(A)-1): #리스트 A의 길이만큼 반복
		a=int(A[i])
		if A[i+1]==a: #리스트 A의 순차적으로 두 값을 비교
			return "NO" #두 값이 같을 경우 중복이므로 "NO" 반환

	return "YES" #for문을 빠져나왔다는 것은 중복이 없는 경우이므로 "YES" 반환

def unique_n2(A):
	for i in range(len(A)): 
		for j in range(i+1,len(A)):
			if A[i]==A[j]: #이중 for문으로 리스트 A의 한 값에 대하여 리스트 A 전체의 값 비교해 중복 찾음
				return "NO"
	
	return "YES"

# input: 값의 개수 n

n = int(input())
# -n과 n 사이의 서로 다른 값 n 개를 랜덤 선택해 A 구성
A = random.sample(range(-n, n+1), n)

s=time.process_time()
unique_n(A)
e=time.process_time()
print("unique_n(A) 수행시간 =", e-s)

s=time.process_time()
unique_nlogn(A)
e=time.process_time()
print("unique_nlogn(A) 수행시간 =", e-s)

s=time.process_time()
unique_n2(A)
e=time.process_time()
print("unique_n2(A) 수행시간 =", e-s)