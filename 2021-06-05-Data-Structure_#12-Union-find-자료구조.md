---
title: "Data Structure_#12 Union-find 자료구조"
categories:
  - Data Structure
  - Python
tags:
  - Data Structure
  - Python
---

## Union-find 자료구조

![image-20210605174405336](C:\Users\yttn0\AppData\Roaming\Typora\typora-user-images\image-20210605174405336.png)

## 연산

1. make-set(x): {x}  				=> O(n)

2. find(x): x가 속한 집합의 대표값 리턴  =>O(log n)

3. union(x, y): x, y의 합집합  =>O(logn )

## 구현 방법

​	1. 원형 양방향 연결리스트  => 0(n)이 될 수 있기 때문에 비효율적

![image-20210605174630045](C:\Users\yttn0\AppData\Roaming\Typora\typora-user-images\image-20210605174630045.png)

​	2. 트리  => O(h)

​		: **부모링크만 가지고 있고**, **root는 자기 자신을 가리키게**

 ![image-20210605174707582](C:\Users\yttn0\AppData\Roaming\Typora\typora-user-images\image-20210605174707582.png)



​      Height가 작아지도록 height가 큰쪽에서 작은쪽으로 union

![image-20210605174739412](C:\Users\yttn0\AppData\Roaming\Typora\typora-user-images\image-20210605174739412.png)

![image-20210605174744196](C:\Users\yttn0\AppData\Roaming\Typora\typora-user-images\image-20210605174744196.png)