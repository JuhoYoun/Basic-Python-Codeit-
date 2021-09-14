##module##  ->실행하는 목적이 아니라 나중에 쓸 함수들을 정의해논 파이썬 파일.
#모듈(module)이란 변수, 함수, 클래스 등을 모아 놓은 파일입니다. 모듈에 정보를 한번만 정의해두면 여러 프로그램에서 쉽게 가져다 쓸 수 있습니다.

from calculator_module import sum #sum만 불러오기

print(sum(1, 2))

from calculator_module import sum, difference #쉼표를 이용해서 두개 이상 함수 부를 수 있다

print(difference(2, 1))

from calculator_module import *  #전부다 불러오기

print(square(2))

#*를 쓰면, 모듈 안에 정의된 모든 변수/함수/클래스를 불러올 수 있습니다. 그러나 모듈 파일의 일부만 사용하려고 할 때, *를 쓰는 것은
# 좋지 않은 습관(practice)입니다. 100개의 함수가 정의되어 있는데 4개만 사용하려고 한다면, *를 이용하기보다 하나 하나 직접 호출하는게
#  낫습니다. 스스로 상황 별로 적절히 잘 판단하여, 하나하나 직접 호출할지, 아니면 모듈에 정의된 모든 것을 호출할지 결정해야 합니다.

#random module (파이썬 가본 모듈)
from random import randint, uniform #randint -> 두 수 포함 두 수 사이의 임의의 정수 리턴, uniform -> 두수 포함 두 수 사이의
                                     # 임의의 소수 리턴

print(randint(0, 3))
print(uniform(0, 5))

print(type(sum))

#input -> input 함수를 쓰면 사용자로부터 값을 입력 받을 수 있습니다.
#name = input("이름을 입력하세요: ") #input 함수의 리턴값으로 문자열 "Codeit"이 변수 name에 지정된거죠.
#print("Hello " + name)

#x = input("숫자를 입력하세요: ")
#print(type(x)) #input으로 받은 입력값은 항상 문자열로 저장된다

#x = int(input("첫 번째 정수: "))
#y = int(input("두 번째 정수: "))
#print("두 정수의 합: %d" % (x + y)) #type casting

"""
#숫자 맞추기
from random import randint

SOLUTION = randint(1, 20)
opportunity = 4

while opportunity != 0:
    answer = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % (opportunity)))

    if answer == SOLUTION:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (5 - opportunity))
        break
    elif answer > SOLUTION:
        print("Down")
    else:
        print("UP")

    opportunity -= 1
    if opportunity == 0:
        print("아쉽습니다. 정답은 %d였습니다." % (SOLUTION))
"""
"""
#teacher solution

from random import randint

#상수
NUM_TRIES = 4
ANSWER = randint(1, 20)

#변수
tries = 0
guess = -1

#시도가 남았고 아직 답을 못 맞췄을 경우
while tries < NUM_TRIES and guess != ANSWER:
    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % (NUM_TRIES - tries)))
    tries = tries + 1
    
    if guess < ANSWER:
        print("Up")
    elif guess > ANSWER:
        print("Down")

if guess == ANSWER:
    print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (tries))
else:
    print("아쉽습니다. 정답은 %d였습니다." % (ANSWER))
"""


print("---------------")

#리스트
# 리스트 정의
numbers = [1, 2, 3, 4, 5, 6]
names = ["윤수", "혜린", "태호", "영훈"]

# 리스트 출력하기
print(numbers)
print(names)

# 인덱싱을 통해 원소 출력하기
print(numbers[0])
print(numbers[1])
print(numbers[0] + numbers[1])
print(numbers[5])
#print(numbers[6]) #numbers는 index5 까지만 있다  이 경우 error가 생긴다

numbers = [1, 2, 3, 4, 5, 6]
names = ["윤수", "혜린", "태호", "영훈"]

print(names[-1])
print(names[-2])
print(names[-4])
print(numbers[-1])
print(numbers[-2])
print(numbers[-6])
#print(numbers[-7]) #numbers는 index5 까지만 있다  이 경우 error가 생긴다

#Slicing
numbers = [1, 2, 3, 4, 5, 6]

# 슬라이싱을 통해 원소 출력하기
print(numbers[0:4]) #index0 이상 index4 미만
print(numbers[0:-3]) #index0 이상 index3 미만
print(numbers[2:]) #index2 이상 부터 끝까지
print(numbers[:3]) #index3 미만부터 처음까지

#원소 바꾸기
numbers = [1, 2, 3, 4, 5, 6]
names = ["윤수", "혜린", "태호", "영훈"]

numbers[0] = 7
print(numbers)

numbers[1] = numbers[1] + numbers[2]
print(numbers)

# 팁 : 리스트의 마지막 요소를 접근할 경우 lst[-1]을 사용하시면 됩니다. 아니면 마지막 요소를 빼고 리스트를 복사(슬라이스)하고 싶으시면
#      lst[:-1]을 사용하시면 됩니다! 마지막 요소에 접근할 때 많이 쓰입니당. list[:-1] 이면 길이에 상관 없이 항상 마지막 원소를
#      가리키게 되니까용

#practice
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
i = 0

"""
while greetings[i]:     #이렇게 할 경우 i가 7이 되고 다시 loop 조건문에 들어가는 순간 greetings[7]은 존재하지 않으므로
    print(greetings[i]) #error가 발생하고 프로그램은 거기서 멈춘다
    i += 1
"""
i = 0
while i < len(greetings):
    print(greetings[i])
    i += 1
print("--------------")

#List functions
alphabet = ["a", "b", "c", "d", "e", "f"] #len

print("리스트의 길이는: %d" % len(alphabet))

#insert와 append를 사용하여 리스트에 원소를 추가할 수 있습니다.
numbers = []

# 마지막 위치에 5 추가
numbers.append(5)
print(numbers)

# 마지막 위치에 8 추가
numbers.append(8)
print(numbers)

# 마지막 위치에 10 추가
numbers.append(10)
print(numbers)

# 인덱스 0 자리에 0 추가 index0 포함해서 나머지는 뒤로 한칸씩 밀림
numbers.insert(0, 0)
print(numbers)

# 인덱스 3 자리에 12 추가
numbers.insert(3, 12)
print(numbers)

#del 함수를 사용함으로써 원하는 리스트의 원소를 삭제할 수 있습니다.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# 인덱스 3에 있는 값 삭제
del numbers[3]
print(numbers)

# 인덱스 4부터 마지막 값까지 삭제
del numbers[4:]
print(numbers)

# 처음부터 인덱스 -2(인덱스 2) 미만 값 삭제
del numbers[:-2]
print(numbers)

#sorted 함수는 리스트의 원소들을 오름차순으로 정렬한 새로운 리스트를 리턴해줍니다.
numbers = [8, 6, 2, 4, 5, 7, 1, 3]
numbers = sorted(numbers) #sorted function은 새로운 list을 생성하고 그 새로운 list을 return값으로 가진다 parameter로 들어가는
                          #List에는 아무 영향도 끼치지 않는다

print(numbers)

numbers = [3, 2, 6, 4, 1]
numbers = sorted(numbers)

print(numbers)

alphabets = ["a", "c", "f", "d", "b"]
alphabets = sorted(alphabets)

print(alphabets)

alphabet_list = ['cat', 'apple', 'smartphone', 'pen', 'people']
alphabet_list.sort() #sort method는 none을 return 하고 새로운 list를 생성하지 않는다

print(alphabet_list)

list1 = ["1", "a", "3", "x", "c", "10"]

lists = sorted(list1)
print(lists) #숫자가 먼저 온다

#리스트들을 +로 연결할 수 있습니다.
alphabet1 = ["a", "b", "c"]
alphabet2 = ["d", "e", "f"]
alphabet = alphabet1 + alphabet2

print(alphabet)

print("--------------")

mixed_list = [1, 2, "three", "Four", 5.0] #심심해서 해봤는데 타입 다른 엘리먼트들 저장 가능한듯
print(mixed_list)
#mixed_list = sorted(mixed_list) #정렬시 중요한건 배열안의 데이터 타입이 동일해야 정렬이 가능합니다. 이런 경우 error.


print("-------------")

#practice 온도 바꾸기
# 화씨 온도에서 섭씨 온도로 바꿔주는 함수
def fahrenheit_to_celsius(fahrenheit):
    # 코드를 입력하세요.
	return (fahrenheit - 32) * 5 / 9
# 테스트용 온도 리스트
sample_temperature_list = [40, 15, 32, 64, -4, 11]

# 화씨 온도 출력
print("화씨 온도 리스트: " + str(sample_temperature_list))

# 리스트의 값들을 화씨에서 섭씨로 변환
# 코드를 입력하세요.
i = 0
while i < len(sample_temperature_list):
    sample_temperature_list[i] = round(fahrenheit_to_celsius(sample_temperature_list[i]), 1)
    i += 1

# 섭씨 온도 출력
print("섭씨 온도 리스트: " + str(sample_temperature_list)) #str(list) 하면 리스트 [~~~] 전체가 하나의 문자열이 됨
#print("섭씨 온도 리스트: " + sample_temperature_list) #can only concatenate str (not "list") to str 라고 에러 뜸

#practice 환전하기
# 원(￦)에서 달러($)로 바꿔주는 함수
def krw_to_usd(won):
    # 코드를 입력하세요.
    return won * 1 / 1000


# 달러($)에서 엔(￥)로 바꿔주는 함수
def usd_to_jpy(dollars):
    # 코드를 입력하세요.
    return dollars * 1000 / 8


# 원(￦)으로 각각 얼마인가요?
amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐: " + str(amounts))

# amounts를 원(￦)에서 달러($)로 바꿔주기
# 코드를 입력하세요.
i = 0
while i < len(amounts):
    amounts[i] = krw_to_usd(amounts[i])
    i += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔(￥)으로 바꿔주기
# 코드를 입력하세요.
i = 0
while i < len(amounts):
    amounts[i] = usd_to_jpy(amounts[i])
    i += 1

# 엔(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(amounts))

#practice 리스트 활용
# 빈 리스트 만들기
numbers = []

# numbers에 자연수 1부터 10까지 추가
# 코드를 입력하세요
i = 1
while i < 11:
    numbers.append(i)
    i += 1
print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    else: #이부분 주의 else 를 안하고 그냥 i += 1을 안다면 2 4 6 9 10은 테스트가 되지 않는다 이렇게 앞에 index부터 지워나가면
        i += 1 #리스트 엘리멘트들이 한칸씩 땡겨짐과 동시에 i가 증가함에 따라 테스트가 안되는 엘리먼트들이 생길 수 있다
print(numbers)
""" #위 문제의 잘못된 솔루션이다 위의 코드와 결과는 똑같이 나오지만 그건 운이 좋을 뿐이고 이렇게 하면 짝수가 테스트 안된다
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    i += 1
"""
#이런 지워지는 인덱스에 의한 영향을 안받을면? 인덱스 뒤에 넘버부터 지우면 된다
i = len(numbers) - 1
while i >= 0:
    if numbers[i] % 2 != 0:
        del numbers[i]
    i -= 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
numbers.sort()
print(numbers)

#리스트 꿀팁스
# value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))

#이런 기능을 하는 함수?가 이미 파이썬에 내장되 있다 -> in
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)

#없는지 확인하는거 -> out
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 not in primes)
print(12 not in primes)

#Nested list
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)

#sort method
numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)

#reverse method -> 순서 뒤집기
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)

#index method -> some_list.index(x)는some_list에서 x의 값을 갖고 있는 원소의 인덱스를 리턴해줍니다.
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))

#remove method - > some_list.remove(x)는some_list에서 첫 번째로 x의 값을 갖고 있는 원소를 삭제해줍니다.
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)

print("-----------------")

#practice 숫자야구
#First code
"""
numbers = []
answers = []
i = 0 #1. i 와 같은 변수명은 아쉽습니다. 직업적으로 하는게 아닐지라도, 최소한 의미가 있는 단어로는 써주시는 것을 권장합니다^^
temp = 10
temp_list = []
strike = 0
ball = 0
count = 0

while i < 3:
    temp = str(randint(0, 9))
    if temp not in numbers:
        numbers.append(temp)
        i += 1
    else: #필요할까요? 반복문 진행과정에 좇아 생각해보시면 좋겠습니다.
        continue #요할까요? 반복문 진행과정에 좇아 생각해보시면 좋겠습니다.
print("Solution is " + str(numbers))

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다. ")

i = 0
while i < 3: #수 입력의 경우 이 줄의 반복문에 의존하여 세 수를 다 입력하게 됩니다. 그 보다는 별도의 반복문을 통해 구현해보시면 어떨까요?

    if i == 0:  #그럼 좀 더 읽기 쉽고 유지보수하기 좋은 코드가 될 것입니다. 요 줄의 조건문을 쓰지 않아도 될 것이구요.
        print("세 수를 하나씩 차례대로 입력하세요.") #수 입력에서 범위를 벗어나는 경우에 대한 코드도 구현이 되어있어야 합니다

    temp = input("%d번째 수를 입력하세요: " % (i + 1))
    if temp not in answers:
        answers.append(temp)
        i += 1
    else:
        print("중복되는 수 입니다. 다시 입력해주세요.")

    print(answers)

    if i == 3:
        count += 1

        temp_list = list(numbers)
        i = len(temp_list) - 1
        while i >= 0: #while문 안에 while문이 있는 것 처럼 들여쓰기가 중첩되는걸 depth가 증가한다고 표현하기도 합니다.
            if answers[i] == temp_list[i]: #이렇게 depth가 증가되면 판단해야할 부분도 많아지고, 가독성도 떨어지게 되기
                strike += 1                #때문에 되도록 최소화 해주시는게 좋습니다.
                del answers[i]
                del temp_list[i]
            i -= 1

        i = 0

        while i < len(answers):        #스트라이크와 볼 판단은 조금 복잡한데, 생각해보면 answers와 numbers의 각 인덱스를 비교하여
            if answers[i] in temp_list:#같으면 strike, 동일 인덱스끼리의 값은 같지 않지만 다른 인덱스에 같은 값이 있다면 ball 일 것입니다. 
                ball += 1               #이를 하나의 반복문으로 간결하게 구현해볼 수도 있지 않을까요?
            i += 1
        print("%dS %dB" % (strike, ball))
        if strike == 3:
            print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (count))
            break

        i = 0
        strike = 0
        ball = 0
        answers = []

#문제 -> 첫번째 반복 때는 3S던 다른 결과던 맞는 결과값이 나오고 3S면 프로그램 종료 아니면 다시 반복되요. 하지만 두번째
#반복 부터는 자꾸 틀린 스트라이크 볼 값을 주는데 왜 그런걸까요? 두번째 반복 부터는 정답을 넣어도 3S가 안되고 다른 어떤 값을 
#넣어도 틀린 S, B 값을 돌려줍니다

#해결 -> temp_list를 del 을 하게 되면 numbers도 지워지게 됩니당. 강의 중 alising 부분을 참고해보세용^^

#에러 생겼던것
#Traceback (most recent call last): File "C:/Users/matty/PycharmProjects/codeit/lecure_note4.py", line 459, in
#temp_list = list(numbers) TypeError: 'list' object is not callable
#이 에러는 코드 내에 list라는 이르을 가진 변수나 리스트가 존재할 때 list 내장함수를 불러올 수 없어서 일어난다 -> 빌트인 함수랑 같은
#이름 변수나 상수 만들지 말자!!

#세 수 뽑는거 힌트
from random import randint

numbers = []

# 세개 뽑을때까지 반복
while len(numbers) < 3:
    new_number = randint(0, 9)

    # 새로운 수 나올때까지 다시 뽑기
    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)

"""

#다시 새 판 짜보자!

# practice 숫자야구

numbers = []
answers = []
index_list = 0
temp = 10
temp_list = []
strike = 0
ball = 0
count = 0

while index_list < 3:
    temp = str(randint(0, 9))
    if temp not in numbers:
        numbers.append(temp)
        index_list += 1

print("Solution is " + str(numbers))

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다. ")

index_list = 0

while index_list < 3:

    if index_list == 0:
        print("세 수를 하나씩 차례대로 입력하세요.")

    temp = input("%d번째 수를 입력하세요: " % (index_list + 1))

    if int(temp) not in range(0, 10):   #not in range(0, 10) 되네 ㅋㅋㅋ
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
    elif temp not in answers:
        answers.append(temp)
        index_list += 1
    else:
        print("중복되는 수 입니다. 다시 입력해주세요.")

    print(answers)

    if index_list == 3:
        count += 1
        index_list = 0

        while index_list < 3:
            if answers[index_list] == numbers[index_list]:
                strike += 1
            elif answers[index_list] in numbers:
                ball += 1
            index_list += 1

        print("%dS %dB" % (strike, ball))
        if strike == 3:
            print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (count))
            break
        index_list = 0
        strike = 0
        ball = 0
        answers = []

"""
from random import randint

# 번호 뽑기
def generate_numbers():
    # 숫자 3개를 보관할 리스트 생성
    numbers = []

    # 3개의 요소가 있을때까지 반복
    while len(numbers) < 3:
        # 새로 뽑은 수가 numbers에 없을 경우에만 추가
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    # 리스트 리턴
    return numbers

# 정답 뽑기
ANSWER = generate_numbers()

# 변수 초기값 설정
tries = 0        # 시도 횟수
strike_count = 0 # 스트라이크 개수
ball_count = 0   # 볼 개수

# 번호를 모두 맞출때까지 반복
while strike_count < 3:
    # 번호 3개 입력 받기
    guess = []
    while len(guess) < 3:
        # 새로 입력한 수가 guess에 없을 경우에만 추가
        new_number = int(input("%d번째 수를 입력하세요: " % (len(guess) + 1)))

        # 범위를 벗어나면 설명 메시지 출력
        if new_number < 0 or new_number > 9:
            print("0에서 9까지의 수를 입력해주세요!")
        # 중복된 수를 입력하면 설명 메시지 출력
        elif new_number in guess:
            print("새로운 수를 입력해주세요!")
        # 타당한 값이면 guess에 추가
        else:
            guess.append(new_number)

    # 스트라이크, 볼 개수 세기
    strike_count = 0 # 스트라이크 개수
    ball_count = 0   # 볼 개수
    i = 0            # 인덱싱 변수

    while i < 3:
        if guess[i] == ANSWER[i]:
            strike_count = strike_count + 1
        elif guess[i] in ANSWER:
            ball_count = ball_count + 1
        i = i + 1

    print("%dS %dB" % (strike_count, ball_count))

    # 시도 횟수 추가
    tries = tries + 1

# 축하 메시지
print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (tries))


"""



