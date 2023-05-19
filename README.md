# -Datastructure-Array
Datastructure Array

## 簡介：

循序性的資料結構，也是一種線性串列，陣列佔有連續性的記憶體空間，陣列提供索引值(index)可以取用個別元素

## 特性:

- 可以用來儲存一群相同類型的資料
- 使用一段連續記憶體空間來存放資料
- 必須明確定義資料型態

## 構造:

一維陣列:如果是一維陣列就可以想像是一個值的盒子，每個盒子上面有編號，而每個盒子內部擺放了相同資料型態的資料。

二維陣列:可以想像是一個四方形的盒子，每個盒子有一組編號(0,1)來記錄這個格子的位置，而盒子內部也放了相同資料型態的資料

三維陣列:以此類推就可以想像成一個立方體的盒子，而每個盒子有一組編號(0,1,1)來記錄位置

## 儲存方式:

如果以python為例有三種表示陣列的方式

#array 與 list 比較以及記憶體操作

([https://medium.com/@t0915290092/用記憶體管理講解為何-python-的-list-那麼慢-bf2cd80bbf72](https://medium.com/@t0915290092/%E7%94%A8%E8%A8%98%E6%86%B6%E9%AB%94%E7%AE%A1%E7%90%86%E8%AC%9B%E8%A7%A3%E7%82%BA%E4%BD%95-python-%E7%9A%84-list-%E9%82%A3%E9%BA%BC%E6%85%A2-bf2cd80bbf72))

***Array:***

python所提供的原生資料型態(**高效率的數值型陣列**)，這個資料型態完全符合上述所定義的陣列，速度也是最快的，使用時必須導入array使用方式如下:

```python
from array import array

a = array("I",[1,2,3])
print(a[1])
for i in a:
    print(i)

print("append")
for j in range(5):
    a.append(10+j)
print(a)

print("POP")
for j in range(len(a)):
    print(a.pop())
```

必須給陣列指定型態，且放入陣列的型態必須都符合指定的型態。

***numpy.array:***

一個第三方套件numpy，其中的array資料型態與上述資料型態相同，但是與原生array較大的不同在於numpy.array是一個固定大小的array，原生array則是動態擴增的空間。

```python
import numpy as np

a = np.array([1,2,3,4])
print(a)
a = np.full((5, 3), [1, 2,3])
print(a)

a = np.array([1,2,3,4])
b = np.insert(a,0,5)
print(a)
print(b)

a = np.array([[1,2],[3,4]])
b = np.insert(a,2,[5,6],axis=0)
print(a)
print(b)

a = np.array([1,2,3,4])
b = np.delete(a,2)
print(a)
print(b)

a = np.array([[1,2],[3,4],[5,6]])
b = np.delete(a,1,axis=0)
print(a)
print(b)
```

***List***

也是屬於python原生的資料型態，但list中可以放入不同資料型態不同長度的其他list或是數值

```python
a = [1,2,3,"a","abc",[55,66],["123","abc"]]
print(a[0])
print(a[3])
print(a[4][1])
```

很方便但是速度很慢