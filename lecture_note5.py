#for 반복문 -> 특정 상황에 따라 while보다 코드가 더 깔끔하게 쓸 수 있다
# 빅뱅 멤버들
big_bang = ["지드래곤", "태양", "탑", "대성", "승리"]

i = 0
while i < len(big_bang):
    print(big_bang[i])
    i = i + 1

#첫째로, i라는 변수는 인덱싱을 위한 용도일 뿐, 그 이외에는 아무런 쓸모가 없습니다. 둘째로, len(big_bang)도 i와의 비교 이외에는
# 별도의 쓰임이 없습니다. for문을 쓰면 이런 불필요한 점들 없이, 깔끔하고 직관적이게 코드를 짤 수 있습니다.

# 빅뱅 멤버들
big_bang = ["지드래곤", "태양", "탑", "대성", "승리"]

for member in big_bang: #member는 for안에서 리스트의 마지막 값까지 갈 때 까지 반복된다
    print(member)

#위의 코드에서 member는 for문의 수행부분에서만 쓰이고 사라지는 local 변수입니다. 수행부분으로 처음 들어갈 때는 member가 big_bang
#리스트의 0번 인덱스 요소 "지드래곤"을 갖게 됩니다. 그 다음 들어갈 때는 member가 1번 인덱스의 요소 "태양", 그 다음은 2번
#인덱스 요소 "탑", 3번 인덱스 요소 "대성", 그리고 마지막으로 4번 인덱스 요소 "승리"를 갖게 됩니다. 결과적으로 "지드래곤", "태양",
#"탑", "대성", "승리"가 출력됩니다. 여기서 쓴 member는 제가 임의로 정한 이름으로, x나 i 등 어떤 (허용된) 이름을 붙이더라도 문제
#없이 프로그램이 실행됩니다. 하지만 늘 강조하듯이 member같은 의미 있는 이름을 주는 것이 좋습니다. 지금까지 while문과 for문을
#사용하여 빅뱅 맴버들을 출력해보았습니다. 이처럼 while 반복문으로 만들 수 있는 프로그램은 for 반복문으로도 만들 수 있고, 반대로
#for 반복문으로 만들 수 있는 프로그램은 모두 while문으로도 만들 수 있습니다. 따라서 이 파트를 배운다고 해서 새로운 문제 해결 능력이
#길러지는 것은 아닙니다. 하지만 for문을 잘 활용하면, 코드를 훨씬 읽고 쓰기 쉽게 만들 수 있습니다. 이와 같이 프로그래밍 언어에서
#동일한 기능을 깔끔하게 만들어 놓은 것을 'syntactic sugar'(꿀)라고 부릅니다.

for num in [1, 3, 5, 7, 9]: #for은 리스트를 다루는데 최적화되있다!!
    print(num * num)

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)
#만약에 1부터 100까지의 리스트가 필요하다면? -> 실재로 리스트를 만드는건 바보! -> range를 쓴다

#range(n, m)은 n부터 m - 1까지의 수들을 의미합니다.
#for i in range(n, m):
#    print(i)

for i in range(1, 11): #for문에서 range(1, 11)이라는 코드를 쓰면, 1부터 10까지의 수이기 때문에,
    print(i) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]이라는 리스트를 쓰는 것과 동일한 효과를 얻게 됩니다.

#range(m)은 0부터 m - 1까지의 수들을 의미합니다.
#for i in range(m):
#    print(i)

#for문에서 range(10)이라는 코드를 쓰면, 0부터 9까지의 수이기 때문에, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]라는 리스트를
# 쓰는 것과 동일한 효과를 얻게 됩니다.
for i in range(10):
    print(i)

#range(n, m, s)은 n부터 m - 1까지의 수 중 간격이 s인 수들을 의미합니다.
#for i in range(n, m, s):
#    print(i)

#for문에서 range(3, 17, 3)이라는 코드를 쓰면, 3부터 16까지의 수 중 간격이 3인 수이기 때문에,
#[3, 6, 9, 12, 15]를 쓰는 것과 동일한 효과를 얻게 됩니다.
for i in range(3, 17, 3):
    print(i)

"""
range 함수의 장점은 다음과 같습니다:

간편하고 깔끔합니다. 굳이 리스트를 만들지 않아도, 동일한 효과를 낼 수 있습니다.
메모리가 효율적입니다. 1부터 100까지의 리스트를 쓰면 파이썬에서 그만큼의 공간을 마련해야 하는 반면, range 함수를 쓰면 
1의 값을 쓰고 버리고 2의 값을 쓰고 버리고 하는 식으로 메모리 공간을 아낄 수 있습니다.
"""

#practice
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 인덱스와 원소 출력
# 코드를 입력하세요.
for i in range(len(numbers)):
    print("%d %d" % (i, numbers[i])) #for 밖에서 i를 따로 안만들어도 인덱스와 리스트 값 모두 프린트 할 수 있다
#tip
for i in range(len(numbers)):
    print(i, numbers[i]) #파이썬에서 이렇게 프린트할 값들 그냥 쓰면 하나 프린트 하고 뛰고 하나 프린트하고 이렇게 된다
print("---------------")

#거듭제곱
for power in range(11):
    print("2^%d = %d" % (power, 2 ** power))

#구구단
for gugu in range(1, 10):
    for dan in range(1, 10):
        print("%d * %d = %d" % (gugu, dan, gugu * dan))

#피타고라스 수란 피타고라스의 정리(a^2 + b^2 = c^2)를 만족하는 세 자연수 쌍 (a, b, c) 입니다.
#예를 들어, 3^2 + 4^2 = 5^2이기 때문에 (3, 4, 5)는 피타고라스 수입니다.
#a < b < c일때, a + b + c = 1000을 만족하는 피타고라스 수 (a, b, c)는 단 하나입니다. 이 경우, a * b * c는 얼마인가요?
for a in range(1, 333):  # a < b < c
    for b in range(1, 500):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(a * b * c)

#Aliassing 가명
x = 5
y = x
y = 3
print(x)
print(y)
"""
첫 번째 줄에서는 정수 5가 변수 x에 지정됩니다. 그리고 두 번째 줄에서는 x의 값이 현재 5이기 때문에, 정수 5가 변수 y에 지정됩니다. 
세 번째 줄에서는 y의 값이 3으로 바뀝니다. 따라서 이를 실행하면 5와 3이 차례로 출력됩니다.
"""

x = [2, 3, 5, 7, 11]
y = x
y[2] = 4
print(x)
print(y)

"""
앞서 본 변수의 예처럼 x는 [2, 3, 5, 7, 11]이 나오고, y는 [2, 3, 4, 7, 11]이 나올줄 알았는데, 결과가 예상과 다르죠? 
y의 원소만 바꾸었을 뿐인데, 왜 x와 y가 똑같이 [2, 3, 4, 7, 11]로 변했을까요? 엘리어싱(Aliasing)이라는 개념 때문입니다. 
코드의 첫 번째 줄에서는 [2, 3, 5, 7, 11] 리스트에 x라는 이름표를 달아줍니다. 두 번째 줄에서 y = x라는 명령에 의해, 
그 같은 리스트에 y라는 이름표를 달아줍니다. 세 번째 줄에서 리스트 y의 인덱스 2의 값을 4로 바꿔주면, 리스트는 
[2, 3, 4, 7, 11]이 됩니다. 그런데 바뀐 [2, 3, 4, 7, 11]이라는 리스트가 y라는 이름표 뿐만 아니라, x라는 이름표도 갖고 
있었죠? 그래서 x와 y를 출력하라는 명령이 있을 때, 모두 같은 [2, 3, 4, 7, 11]이 출력되는 것입니다. 두 변수가 서로 이름은 
다르지만, 사실 같은 메모리 주소에 있는 값을 가리키고 있기 때문에 동일한 리스트가 출력된거죠. y는 x의 Alias(가명)라고 
얘기할 수 있습니다.
"""

x = [2, 3, 5, 7, 11]
y = list(x)
y[2] = 4
print(x)
print(y)

"""
리스트 복사
하지만 간혹 엘리어싱을 이용하지 않고 리스트의 원본을 그대로 둔 채, 리스트의 복사본만 바꾸고 싶을 때가 있습니다.
즉 x라는 원본의 리스트는 그대로 둔 채, y 리스트의 값만 바꾸고 싶은 경우. 이럴 때는 list 함수를 사용하면 됩니다. 
list 함수는 원본을 복사해서 새로운 공간에 붙여넣고, 그 새로운 공간의 리스트를 리턴시켜줍니다.
첫 번째 줄에서 [2, 3, 5, 7, 11]을 가진 리스트에 x라는 이름표가 달립니다. 두 번째 줄에서 y = list(x)라는 명령에 의해, 
x 리스트의 복사본이 새로운 공간에 만들어지고 그 복사본에 y라는 이름표가 달립니다. 즉 x와 y의 리스트는 서로 다른 메모리 
주소에 저장되어 있는거죠. 따라서 세 번째 줄에서 y 리스트의 인덱스 2의 값을 바꾸는 행위는, x 리스트에 아무런 영향을 미치지 
않습니다. 이로써 x와 y를 출력하라는 명령이 있을 때, 각각 [2, 3, 5, 7, 11]과 [2, 3, 4, 7, 11]이 출력되는 것입니다.
"""
"""
aliasing 문제는 mutable 객체에서만 일어납니다. mutable 객체에는 list, dict, set이 대표적입니다. 반면 immutable 
객체인 숫자형,문자,튜플 등에서는 일어나지 않습니다

단순 값에서는 일어나지 않는 Aliasing이 다차원 값에서만 일어나는 이유는 단순 값은 x라는 변수의 주소에 해당 값을 저장합니다. 
x = 10이라고 했을때 x가 1번주소라면 1번주소에 10이라는 값이 저장됩니다. 하지만 x = [1,2,3]과 같은 경우 1, 2, 3의 
값은 x와 다른 주소에 저장이 되고x[n]이 해당 주소가 됩니다. 간단하게 x는 1,2,3의 값이 아닌 1,2,3이 저장된 주소들을 가지는 
것이죠. 그리고 x의 값을 받는 y역시 해당 주소들을 받습니다. 위와 같은 이유로 mutable객체에서 Aliasing이 일어납니다.

c는 컴파일 언어고, 파이썬은 스크립트 언어입니다. 따라서 파이썬에서 만들어지는 배열객체를 저장하는 변수는 당연히 레퍼런스 
변수입니다. 비슷하게 구현하고 싶다면 c에서 포인터를 쓰세요.
"""

#practice 리스트 뒤집기
#my code
numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
# 코드를 입력하세요.
temp_list = list(numbers)

for i in range(len(numbers)):
    numbers[i] = temp_list[- 1 - i]

del temp_list

print("뒤집어진 리스트: " + str(numbers))

#Teacher code
numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
for left_index in range(int(len(numbers) / 2)):
    # 오른쪽 인덱스 계산
    right_index = len(numbers) - left_index - 1

    # 원소 바꾸기
    temp = numbers[left_index]
    numbers[left_index] = numbers[right_index]
    numbers[right_index] = temp

print("뒤집어진 리스트: " + str(numbers))
"""
리스트에 요소가 7개 있으면 가장 왼쪽 인덱스는 0이고 가장 오른쪽 인덱스는 6입니다. 왼쪽에서 두번째 인덱스는 1이고 오른쪽에서 
두번째 인덱스는 5입니다. 왼쪽에서 세번째 인덱스는 2이고 오른쪽에서 세번째 인덱스는 4입니다. 리스트를 가운데를 기점으로 
반으로 나누면 대칭되는 두 인덱스의 합은 늘 6입니다. 
이걸 통해서 알 수 있는 것은: 왼쪽 인덱스 + 오른쪽 인덱스 = 총 요소 개수 - 1
이걸 코드로 표현해봅시다. 리스트 numbers와 왼쪽 인덱스 left_index가 주어졌을 때, right_index는 이렇게 계산할 수 
있습니다: right_index = len(numbers) - left_index - 1

range(len(numbers)) 대신 range(int(len(numbers) / 2))를 하는 이유는 뭘까요?
->질문 주셨던 range(len(numbers)) 로 for문을 만들어 보았어요~ 이 때, 한번 반복문이 돌 때마다 인덱스를 출력해보았는데요!
3번째 루프 이후부터, 기존에 할당해주었던 값이 재할당됨을 볼 수 있어요~ (3번째 인덱스는 자기자신을 할당하니 예외로 치고요ㅎㅎ)
이 때문에 for문이 돌았음에도 불구하고, 입력하였던 값 그대로 남아 있게 됩니다.
"""

"""
List vs 문자열

두 자료형은 공통적으로 인덱싱이 가능합니다.

# 알파벳 리스트의 인덱싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0])
print(alphabets_list[1])
print(alphabets_list[4])
print(alphabets_list[-1])

# 알파벳 문자열의 인덱싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0])
print(alphabets_string[1])
print(alphabets_string[4])
print(alphabets_string[-1])

두 자료형은 공통적으로 인덱싱이 가능합니다. 따라서 for 반복문에도 활용할 수 있습니다.

# 알파벳 리스트의 반복문
alphabets_list = ['C', 'O', 'D', 'E', 'I', 'T']
for alphabet in alphabets_list:
    print(alphabet)

# 알파벳 문자열의 반복문
alphabets_string = 'CODEIT'
for alphabet in alphabets_string:
    print(alphabet)

두 자료형은 공통적으로 슬라이싱이 가능합니다.

# 알파벳 리스트의 슬라이싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])
print(alphabets_list[4:])
print(alphabets_list[:4])

# 알파벳 문자열의 슬라이싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0:5])
print(alphabets_string[4:])
print(alphabets_string[:4])

두 자료형에게 모두 덧셈은 "연결"하는 연산입니다.

# 리스트의 덧셈 연산
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)

# 문자열의 덧셈 연산
string1 = '1234'
string2 = '5678'
string3 = string1 + string2
print(string3)

두 자료형은 모두 길이를 재는 len 함수를 쓸 수 있습니다.

# 리스트의 길이 재기
print(len(['H', 'E', 'L', 'L', 'O']))

# 문자열의 길이 재기
print(len("Hello, world!"))

Mutable (수정 가능) vs. Immutable (수정 불가능)
하지만 차이점이 있습니다. 리스트는 데이터를 바꿀 수 있지만, 문자열은 데이터를 바꿀 수 없다는 것입니다. 리스트와 같이 수정 
가능한 자료형을 'mutable'한 자료형이라고 부르고, 문자열과 같이 수정 불가능한 자료형을 'immutable'한 자료형이라고 부릅니다. 
숫자, 불린, 문자열은 모두 immutable한 자료형입니다.

# 리스트 데이터 바꾸기
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

리스트 numbers의 인덱스 0에 5를 새롭게 지정해주었습니다. [5, 2, 3, 4]가 출력되었습니다. 이처럼 리스트는 데이터의 생성, 
삭제, 수정이 가능합니다.

# 문자열 데이터 바꾸기
name = "codeit"
name[0] = "C"
print(name)

문자열 name의 인덱스 0 에 "C"를 새롭게 지정해주었더니 오류가 나왔습니다. TypeError: 'str' object does not support 
item assignment는 문자열은 변형이 불가능하다는 메시지입니다. 이처럼 문자열은 리스트와 달리 데이터의 생성, 삭제, 수정이
불가능합니다. 문자열 끼리 더하기는 된다.
"""

#practice 자리수 합 구하기
# 자리수 합 리턴 my code
def sum_digit(num):
    temp = str(num)
    sum = 0

    for i in temp:
        sum += int(i)

    return sum


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
sum = 0
for i in range(1, 1001):
    sum += sum_digit(i)

print(sum)

#Teacher code -> 변수 이름을 더 의미있게
# 자리수 합 리턴
def sum_digit(num):
    str_num = str(num)
    sum = 0

    # 각 자리수를 sum_digit에 추가
    for digit in str_num:
        sum = sum + int(digit)
    return sum

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
total = 0
for i in range(1, 1001):
    total = total + sum_digit(i)
print(total)

#주민등록 번호 마지막 네자리 숨기기
def mask_security_number(security_number):
    # 코드를 입력하세요.
    numbers_showing = security_number[:-4]
    return numbers_showing + "****"

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

"""
위에거를 어렵게 해보자

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = []
    for i in range(len(security_number)):
        num_list.append(security_number[i])

사실 문자열을 한번에 리스트로 바꾸고 싶으면 곧바로 형 변환을 쓸 수도 있습니다.

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)    -> 문자열을 리스트로 형 변환할 수 있다!

이제 마지막 네 요소, 즉 인덱스 len(num_list) - 4부터 인덱스 len(num_list) - 1의 값들을 *로 바꿔주면 하면 됩니다.

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

마지막으로 이 리스트를 이제 다시 문자열로 만들어서 리턴시켜 주어야합니다.

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

    # 리스트를 문자열로 복구
    total_str = ""
    for i in range(len(num_list)):
        total_str += num_list[i]

    return total_str

사실 이것도 파이썬에서는 한번에 할 수 있는 방법이 있고요...

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

    # 리스트를 문자열로 복구
    total_str = "".join(num_list)   ->아무것도 없는 빈 문자열에 리스트에 있는 값들을 형 변환해 문자열로 더한다!

    return total_str

"""

#practice 팔린드롬
#"토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 팔린드롬(palindrome)이라고 부릅니다. 문자열 word가 팔린드롬인지 확인하는
#함수 is_palindrome를 쓰세요. is_palindrome은 word가 팔린드롬이면 True를, 팔린드롬이 아니면 False를 리턴합니다.
def is_palindrome(word):
    # 코드를 입력하세요.
    for i in range(int(len(word))):
        if word[i] != word[- i - 1]:
            return False
        if i == int(len(word) - 1):  #생각해보니 구지 이렇게 if문 안쓰고 for문 밖에 마지막에 return True 하면 더 간단
            return True


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

#Teacher ->Teacher는 right index 랑 left index 나랑 좀 다르네 나는 right index는 -로 하는데
def is_palindrome(word):
    for left in range(len(word) // 2):  #//이 뭐더랑 int(len(word))랑 똑같군 
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
