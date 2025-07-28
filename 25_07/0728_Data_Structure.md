# Data Structure
데이터 구조는 여러 데이터를 효과적으로 사용/관리하기 위한 구조

**(str, list, dict 등)**

### 자료구조
- 컴퓨터 공학에서는 '자료 구조'라고 함
- 각 데이터의 **효율적인 저장, 관리**를 위한 구조를 나눠 놓은 것
- 단순히 데이터를 묶는 것을 넘어, **프로그램의 성능과 효율성**, **유지보수성**에 큰 영향을 미치는 핵심적인 개념

## 메서드
문자열, 리스트, 딕셔너리 등 각 **데이터 구조**의 **메서드**를 호출하여 다양한 **기능**을 활용하기

- 문자열, 리스트, 딕셔너리 등 파이썬의 다양한 데이터 구조는 저마다 고유한 **메서드** 가짐
- 이 메서드들은 해당 데이터 구조의 데이터를 **효율적으로 조작**하거나 **특정 기능을 수행**하기 위해 제공

### 메서드(method)
***객체*****에 속한 함수**

프로그래밍에서 **메서드(Method)**는 ***객체(Object)***가 특정 작업을 수행하도록 정의된 함수

- 메서드는 클래스(class) 내부에 정의되는 함수
- 클래스는 파이썬에서 '타입을 표현하는 방법'이며 이미 은연 중에 사용해왔음
- 예를 들어 help 함수를 통해 str을 호출해보면 class 였다는 것을 확인 가능

```
print(help(str))

"""
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |
 |  Methods defined here:
-- More  --
"""
```

***지금 시점에 알아야 할 것***

메서드는 어딘가(클래스)에 속해 있는 **함수**이며, 각 데이터 타입별로 다양한 **기능**을 가진 **메서드**가 존재

### 메서드 호출 방법
**데이터 타입 객체.메서드()**

```
'hello'.capitalize()
```

우리가 만든 **객체(데이터)**에게 원하는 **명령(메서드)**를 내리는 방법

### 메서드 호출 예시

```
# 문자열 메서드 예시
print('hello'.capitalize())  # Hello

# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)  # [1, 2, 3, 4]
```

# 시퀀스 데이터 구조

## 문자열

### 문자열 조회/탐색 및 검증 메서드

메서드|설명
:-:|:-:
s.find(x)|x의 첫 번째 위치를 반환. 없으면 -1을 반환
s.index(x)|x의 첫 번째 위치를 반환. 없으면 오류 발생
s.isupper()|문자열 내의 모든 문자가 대문자인지 확인
s.islower()|문자열 내의 모든 문자가 소문자인지 확인
s.isalpha()|문자열 내의 모든 문자가 알파벳인지 확인 *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함)

### .find(x)

```
text = 'banana'
print(text.find('a'))  # 1

print(text.find('z'))  # -1
```

### .index(x)

```
text = 'banana'

print(text.index('a'))  # 1

print(text.index('z'))  # ValueError: substring not found
```

### .isupper(x), .islower(x)

```
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  # True
print(string2.isupper())  # False
print(string1.islower())  # False
print(string2.islower())  # False
```

### .isalpha(x)

```
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # True
print(string2.isalpha())  # False
```

### 문자열 조작 메서드(새로운 문자열 반환)

메서드|설명
:-:|:-:
**s.replace(old, new[,count])**|**바꿀 대상 글자를 새로운 글자로 바꿔서 반환**
**s.strip([chars])**|**공백이나 특정 문자를 제거**
**s.split(sep=None, maxsplit=-1)**|**sep를 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트를 반환**
**'separator'.join(*****iterable*****)**|**구분자로** ***iterable*****의 문자열을 연결한 문자열을 반환**
s.capitalize()|가장 첫 번째 글자를 대문자로 변경
s.title()|문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환
s.upper()|모두 대문자로 변경
s.lower()|모두 소문자로 변경
s.swapcase()|대 <-> 소문자 서로 변경

### .replace(old, new[,count])

```
text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')
new_text2 = text.replace('world', 'Python', 1)
print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world
```

### .strip([chars])

```
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)  # Hello, world!
```

> ### ***[chars] 활용***

### .split(sep=None, maxsplit=-1)

```
text = 'Hello, world!'
words1 = text.split(',')
words2 = text.split()
print(words1)  # ['Hello', ' world!']
print(words2)  # ['Hello,', 'world!']
```

> ### ***split maxsplit 추가***

### 'separator'.join(iterable)

```
words = ['Hello', 'world!']
text = '-'.join(words)
print(text)  # Hello-world!
```

> ### ***join 구분자 추가***

```
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
new_text2 = text.title()
new_text3 = text.upper()
new_text4 = text.lower()
new_text5 = text.swapcase()

print(new_text1)  # Hello, world!
print(new_text2)  # Hello, World!
print(new_text3)  # HELLO, WORLD!
print(new_text4)  # hello, world!
print(new_text5)  # HEllO, WOrLD!
```

## 리스트

메서드|설명
:-:|:-:
**L.append(x)**|**리스트 마지막에 항목 x를 추가**
**L.extend(m)**|**Iterable m의 모든 항목들을 리스트 끝에 추가 (+=과 같은 기능)**
L.insert(i, x)|리스트 인덱스 i에 항목 x를 삽입
L.remove(x)|리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거, 항목이 존재하지 않을 경우, ValueError
**L.pop()**|**리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거**
**L.pop(i)**|**리스트의 인덱스 i에 있는 항목을 반환 후 제거**
L.clear()|리스트의 모든 항목 삭제

### .append(x)

```
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# append는 None을 반환합니다.
print(my_list.append(5))  # None
```

### .extend(iterable)

```
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]
```

### Extend 주의사항
- append()와의 비교

```
my_list.append([5, 6, 7])
print(my_list)  # [1, 2, 3, 4, 5, 6, [5, 6, 7]]
```

- 반복 가능한 객체가 아니면 추가 불가

```
my_list.extend(100)  
# TypeError: 'int' object is not iterable
```

### .insert(i, x)

```
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  # [1, 5, 2, 3]
```

### .remove(x)

```
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]
```

### .pop(i)

```
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)
print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4]
```

### .clear()

```
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []
```

### 리스트 탐색 및 정렬 메서드

문법|설명
:-:|:-:
L.index(x)|리스트에서 첫 번째로 일치하는 항목 x의 인덱스를 반환
L.count(x)|리스트에서 항목 x의 개수를 반환
**L.reverse(x)**|**리스트의 순서를 역순으로 변경 (정렬 X)**
**L.sort()**|**리스트를 정렬 (매개변수 이용가능)**

### .index(x)

```
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1
```

### .count(x)

```
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)  # 3
```

### .reverse()

```
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
# reverse는 None을 반환
# print(my_list.reverse())  # None
# reverse는 원본 리스트를 변경
print(my_list)  # [9, 1, 8, 2, 3, 1]
```

### .sort()

```
my_list = [3, 2, 100, 1]
my_list.sort()
# sort는 None을 반환
print(my_list.sort())  # None
# sort는 원본 리스트를 변경
print(my_list)  # [1, 2, 3, 100]

# 내림차순 정렬
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]
```

# 복사

## 객체와 참조

### 가변/불변 객체의 개념
- 객체 복사의 핵심을 파악하려면, 파이썬 자료구조의 가변과 불변 두 가지 종류를 살펴봐야 합니다.

**Mutable (가변) 객체**
- 생성 후 **내용을 변경할 수 있는** 객체
    - 예: 리스트(list), 딕셔너리(dict), 집합(set)

**Immutable(불변) 객체**
- 생성 후 **내용을 변경할 수 없는** 객체
    - 예: 정수(int), 실수(float), 문자열(str), 튜플(tuple)

### 변수 할당의 의미
- 파이썬에서 변수 할당은 객체에 대한 참조를 생성하는 과정
    - 변수는 객체의 메모리 주소를 가리키는 Label 역할을 함
    - '='연산자를 사용하여 변수에 값을 할단
        - 할당 시 **새로운 객체**가 생성되거나 **기존 객체에 대한 참조**가 생성됨

**새로운 객체 생성 후 참조**
- 할당되는 값이 새로운 객체일 경우, 파이썬은 먼저 해당 객체를 메모리에 만들고, 변수가 그 객체를 가리키도록 함

**기존 객체에 대한 참조**
- 이미 메모리에 존재하는 객체를 변수에 할당하면, 새로운 객체를 만들지 않고 해당 객체에 대한 참조만 생성함

### 가변 객체 예시
- **생성 후 내용을 변경할 수 있는** 객체

```
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(f'a의 값: {a}')  # [100, 2, 3, 4]
print(f'b의 값: {b}')  # [100, 2, 3, 4]
print(f'a와 b가 같은 객체를 참조하는가? {a is b}')  # True
```

### 불변 객체 예시
- 생성 수 **내용을 변경할 수 없는** 객체

```
a = 20
b = a
b = 10

print(a)  # 20
print(b)  # 10
print(a is b)  # False
```

### id() 함수를 사용한 메모리 주소 확인
- id() 함수를 사용하여 객체의 메모리 주소를 확인 가능
- is 연산자를 통해 두 변수가 같은 객체를 참조하는지 확인 가능

```
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(f'x의 id: {id(x)}')   # x의 id : 1682231207424
print(f'y의 id: {id(y)}')   # y의 id : 1682231207424
print(f'z의 id: {id(z)}')   # z의 id : 1682231224896
print(f'x와 y는 같은 객체인가? {x is y}')   # True
print(f'x와 z는 같은 객체인가? {x is z}')   # False
```

### 가변/불변 메모리 관리 방식
- 가변 객체
    - 생성 후에도 그 내용을 수정할 수 있음
    - 객체의 내용이 변경되어도 같은 메모리 주소를 유지

- 불변 객체
    - 생성 후 그 값을 변경할 수 없음
    - 새로운 값을 할당하면 새로운 객체가 생성되고, 변수는 새 객체를 참조하게 됨

### 가변/불변 메모리 관리 방식의 이유
- 성능 최적화
    - **불변 객체**: 변경이 불가능하므로, **여러 변수가 동일한 객체를 안전하게 공유**할 수 있음
    - **가변 객체**: 내용 수정이 빈번할 때, 새로운 객체를 생성하는 대신 **기존 객체를 직접 수정**할 수 있음. 이로 인해 객체 생성 및 삭제에 드는 비용을 절감하여 성능을 향상시킴
    
- 메모리 효율성
    - **불변 객체**: 동일한 값을 가진 여러 변수가 같은 객체를 참조할 수 있어 **메모리 사용을 최소화**할 수 있음
    - **가변 객체**: 크기가 큰 데이터를 효율적으로 수정할 수 있음

## 얕은 복사(Shallow Copy)
객체의 **최상위 요소**만 새로운 메모리에 복사하는 방법

내부에 **중첩된 객체**가 있다면 그 객체의 **참조**만 복사됨

***얕은 복사의 함정,*** **'가변 객체'!**
- 얕은 복수 후 **중첩된 리스트**나 딕셔너리 같은 **가변 객체**를 수정하면, 원본 객체와 복사본 객체가 함께 변경됨.
- 이는 복사본의 중첩 객체가 여전히 원본 객체의 **중첩 객체를 참조**하고 있기 때문.

### 얕은 복사 구현 방법
1. 리스트 슬라이싱
2. copy() 메서드
3. list() 함수

### 얕은 복사 예시
- 1차원 리스트에서의 얕은 복사
    - 리스트 슬라이싱

```
a = [1, 2, 3]
b = a[:]

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]
```

- 1차원 리스트에서의 얕은 복사
    - copy() 메서드

```
a = [1, 2, 3]
b = a.copy()

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]
```

- 1차원 리스트에서의 얕은 복사
    - list() 함수

```
a = [1, 2, 3]
d = list(a)
a[0] = 100

print(a)  # [100, 2, 3]
print(d)  # [1, 2, 3]
```

### 얕은 복사의 한계
- 2차원 리스트와 같이 변경 가능한 객체 안에 변경 가능한 객체가 있는 경우

```
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [999, 2, [3, 4, 5]]

b[2][1] = 100
print(a)  # [1, 2, [3, 100, 5]]
print(b)  # [999, 2, [3, 100, 5]]

print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # True
```

- a와 b의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경됨

### 1차원 리스트와 다차원 리스트에서의 차이점
- 1차원 리스트
    - 얕은 복사로 충분히 독립적인 복사본을 만들 수 있음
- 다차원 리스트
    - 최상위 리스트만 복사되고, 내부 리스트는 여전히 원본과 같은 객체를 참조

## 깊은 복사(Deep Copy)
객체의 모든 수준의 요소를 새로운 메모리에 복사하는 방법

**중첩된 객체까지** 모두 새로운 객체로 생성됨

***완전한 독립성 보장***
- 깊은 복사는 원본 객체와 복사본이 **완전히 독립적**임을 보장함.
- 복사본의 어떤 수준에 있는 중첩된 내용을 변경하더라도 **원본 객체**에는 **절대 영향을 주지 않음.**

- copy 모듈에서 제공하는 deepcopy() 함수를 사용

```
import copy
new_object = copy.deepcopy(original_object)
```

### 깊은 복사 예시

```
import copy
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100

print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [1, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # False
```

- 중첩된 객체에서의 깊은 복사

```
original = {
    'a': [1, 2, 3],
    'b': {'c': 4, 'd': [5, 6]},
}
copied = copy.deepcopy(original)

copied['a'][1] = 100
copied['b']['d'][0] = 500

print(f'원본: {original}')  # {'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}
print(f'복사본: {copied}')  # {'a': [1, 100, 3], 'b': {'c': 4, 'd': [500, 6]}}
print(
    f"original['b']와 copied['b']가 같은 객체인가? {original['b'] is copied['b']}"
)  # False
```

# 참고

## List Comprehension
간결하고 효율적인 리스트 생성 방법

***"Pythonic"*** 한 코드
- 파이썬 개발자들이 선호하는 스타일로, 코드를 더 **"파이썬답게"** 작성하는 방법 중 하나

### List Comprehension 구조

```
[expression for 변수 in iterable]
list(expression for 변수 in iterable)

[expression for 변수 in iterable if 조건식]
list(expression for 변수 in iterable if 조건식)
```

***[표현식 for 변수 in 순회 가능한 객체 if 조건]***

**각 구성 요소의 역할**
- 표현식은 결과 리스트에 추가될 값, 변수는 순회 중인 현재 요소, 순회 가능한 객체는 반복할 데이터, 조건식은 필터링 조건
- if 조건식 부분은 선택 사항이며, 조건을 명시하지 않으면 모든 요소에 대해 표현식이 적용됨.

- 사용 전/후 구조

```
# 사용 전
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)  # [1, 4, 9, 16, 25]


# 사용 후
numbers = [1, 2, 3, 4, 5]

squared_numbers = [num**2 for num in numbers]
print(squared_numbers)  # [1, 4, 9, 16, 25]
```

### List Comprehension 활용 예시
- 2차원 배열 생성 시(인접행렬 생성)

```
data1 = [[0] * (5) for _ in range(5)]
# 또는
data2 = [[0 for _ in range(5)] for _ in range(5)]

# 결과
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
```

***Comprehension을 남용하지 말자.***

## 메서드 체이닝(Method Chaining)
여러 매서드를 연속해서 호출하는 방식

### 문자열에서의 메서드 체이닝 예시

```
text = 'heLLo, woRld!'

new_text = text.swapcase().replace('l', 'z')

print(new_text) # HEzzO, WOrLD!
```

- 코드는 다음 순서로 실행됨
1. text.swapcase(): 대소문자를 반전시킴
    - 'heLLo, woRld!' -> 'HEllO, WOrLD!'
2. .replace('l', 'z'): 소문자 'l'을 'z'로 교체
    - 'HEllO, WOrLD!' -> 'HEzzO, WOrLD!'

```
# 1. 단계별로 실행하기
text = 'heLLo, woRld!'
step1 = text.swapcase()
print('1단계 결과:', step1)  # HEllO, WOrLD!

step2 = step1.replace('l', 'z')
print('2단계 결과:', step2)  # HEzzO, WOrLD!

# 2. 한 줄로 실행하기 (위와 동일한 결과)
new_text = text.swapcase().replace('l', 'z')
print('최종 결과:', new_text)  # HEzzO, WOrLD!
```

### 리스트에서의 메서드 체이닝 예시
- copy()로 리스트를 복사한 후 sorted() 함수로 정렬

```
numbers = [3, 1, 4, 1, 5, 9, 2]
result = numbers.copy().sort()
print(numbers)  # [3, 1, 4, 1, 5, 9, 2] (원본은 변경되지 않음)
print(result)  # None (sort() 메서드는 None을 반환하기 때문)

# 올바른 체이닝 예시
sorted_numbers = sorted(numbers.copy())
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]
```

### 메서드 체이닝 주의사항
- 모든 메서드가 체이닝을 지원하는 것은 아님
    - 메서드가 객체를 반환할 때만 체이닝이 가능
- None을 반환하는 메서드는 메서드 체이닝이 불가능
    - ex) 리스트의 append(), sort()
- 메서드 체이닝을 사용할 때는 각 메서드의 반환 값을 잘 이해하고 있어야 함

## 문자 유형 판별 메서드
- 문자열에 포함된 문자들의 유형을 판별하는 메서드
    - isdecimal()
        - 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
    - isdigit()
        - isdecimal()과 비슷하지만, 유니코드 숫자도 인식 ('①'도 숫자로 인식)
    - isnumeric()
        - isdigit()과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식(분수, 지수, 루트 기호도 숫자로 인식)