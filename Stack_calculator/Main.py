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
	
def get_token_list(expr):
	token_list=[]
	o=['+','-','*','/','^','(',')']
	num=""
	for i in expr:
		if i not in o and i!=" ":
			num+=i
		elif i in o:
			if num!="":
				token_list.append(float(num))
				num=""
			token_list.append(i)
		else:
			continue
	if num!="":
		token_list.append(float(num))

	return token_list

	
def infix_to_postfix(token_list):
	operation=Stack()
	postfix=[]
	o=['+','-','*','/','^']
	op={"(":0,"+":1,"-":1,"*":2,"/":2,"^":3}
	for i in token_list: 
		#괄호
		if i=='(':
			operation.push(i)
		elif i==')':
			while operation.top()!='(':
				postfix.append(operation.pop())
			operation.pop()
		#연산자
		elif i in o:
			#첫번째가 아니면
			while operation.empty()!=True:
				if op[i]<=op[operation.top()]:
					postfix.append(operation.pop())
				else:
					break
			operation.push(i)
		#피연산자
		else:
			postfix.append(i)
		
		#operation 비우기	
	while operation.empty()!=True:
		postfix.append(operation.pop())
	return postfix
	
def compute_postfix(token_list):
	result=Stack()
	o=['+','-','*','/','^']
	for i in token_list:
		#연산자
		if i in o:
			op_2=result.pop()
			op_1=result.pop()
			if i=='+':
				result.push(op_1+op_2)
			elif i=='-':
				result.push(op_1-op_2)
			elif i=='*':
				result.push(op_1*op_2)
			elif i=='/':
				result.push(op_1/op_2)
			else:
				result.push(op_1**op_2)
		#피연산자
		else:
			result.push(i)

	return result.top()
# 아래 세 줄은 수정하지 말 것!
expr = input()
value=get_token_list(expr)
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)