#while
i = 1
while i <= 4:
    print(i)
    i += 1
#while문을 사용하여 100 이상의 자연수 중 가장 작은 23의 배수를 출력해보세요.

i = 100
j = True

while j:
    if i % 23 == 0:
        j = False
    if j:
    	i += 1
print(i)

#Teacher version 훨씬 간단

i = 100

while i % 23 != 0:
    i += 1

print(i)

print("----------")

# while -> loop, if -> conditional

a = 5
b = 3

if a < b:
    print("a는 b보다 작습니다.")
else:
    print("a는 b보다 작지 않습니다.")

a = 5
b = 3

if a < b:
    print("a는 b보다 작습니다.")
else:
    if a == b:
        print("a와 b는 같습니다.")
    else:
        print("a는 b보다 큽니다.")

# elif를 이용해서 더 간단하게

a = 5
b = 3

if a < b:
    print("a는 b보다 작습니다.")
elif a == b:
    print("a와 b는 같습니다.")
else:
    print("a는 b보다 큽니다.")

#학점 계산
def print_grade(midterm, final):
    total = midterm + final
    if total >=  90:
        print("You get an A")
    elif total >= 80:
        print("You get a B")
    elif total >= 70:
        print("You get a C")
    elif total >= 60:
        print("You get a D")
    else:
        print("You fail")

# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)

#while문과 if문을 활용하여, 1000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써보세요.

#1
i = 1
total = 0

while i < 1000:
    if i % 2 == 0:
        total += i
        i += 1
    elif i % 3 == 0:
        total += i
        i += 1
    else:
        i += 1

print(total)

#2
i = 1
total = 0

while i < 1000:
    if i % 2 == 0:
        total += i

    elif i % 3 == 0:
        total += i

    #else: 이렇게 else를 하니까 밑에 i += 1 이 indent 안되있다고 에러가 뜬다 else: 하고 바디가 없을거면 애초에  else: 쓰지말하야겠다

    i += 1

print(total)

#3
i = 1
total = 0

while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        total += i
    i += 1

print(total)

print("----------")

i = 1
count = 0

while i <=120:
    if 120 % i == 0:
        print(i)
        count += 1
    i += 1

print("120의 약수는 총 %d개입니다." % (count))

print("---------")

INTEREST_RATE = 0.12
APARTMENT_VALUE_2016 = 1100000000

year = 1988
value = 50000000

while year < 2016:
    value = value * (1 + INTEREST_RATE)
    year += 1

if value > APARTMENT_VALUE_2016:
    print("%d원 차이로 동일 아저씨의 말씀이 맞습니다." % (value - APARTMENT_VALUE_2016))
elif APARTMENT_VALUE_2016 > value:
    print("%d원 차이로 미란 아주머니의 말씀이 맞습니다." % (APARTMENT_VALUE_2016 - value))
else:
    print("Same")

print("____________")

#피보나치

current_number = 1
previous_number = 1
temp = 0
i = 1

while i <= 20:
    if i == 1 or i == 2:
        print("1")
        i += 1
    else:
        temp = current_number
        current_number = current_number + previous_number
        previous_number = temp

        print(current_number)
        i += 1
#Solution
count = 0
current = 1
previous = 0
temp = 0

while count < 20:

    print(current)

    temp = current
    current = current + previous
    previous = temp

    count += 1

print("---------------")

#구구단 nested while loop

i = 1
j = 1

while i <= 9:
    while j <= 9:
        print("%d * %d = %d" % (i, j, i * j))
        j += 1
    j = 1
    i += 1

#solution
i = 1
j = 1

while i <= 9:
    j = 1         #j를 앞에서 초기화 해주는게 더 좋은 코딩인가?
    while j <= 9:
        print("%d * %d = %d" % (i, j, i * j))
        j += 1
    i += 1

#break and continue

#만약 while문의 조건부분과 상관 없이 반복문에서 나오고 싶으면 break문을 쓰면 됩니다.
i = 100
while True:
    # i가 23의 배수면 반복문을 끝냄
    if i % 23 == 0:
        break
    i = i + 1

print(i)

#만약 현재 진행되고 있는 수행부분을 중단시키고 바로 조건부분을 다시 확인하고 싶으면 continue문을 쓰면 됩니다.
i = 0
while i < 15:
    i = i + 1

    # i가 홀수면 print(i) 안하고 바로 조건부분으로 돌아감
    if i % 2 == 1:
        continue
    print(i)