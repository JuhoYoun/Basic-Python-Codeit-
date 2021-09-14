#Recursion 재귀함수! -> 자기 자신을 호출하는 함수
def countdown(n):
    if n > 0:
        print(n)
        countdown(n-1)

countdown(10)

#재귀적으로 문제를 푼다 -> 문제를더 같은 형태의 더 작은 형태의 문제로 쪼개서 푼다
#Factorial
def factorial(n):
    if n == 0: #base case
        return 1
    if n > 0: #recursive case
        return n * factorial(n - 1)

print(factorial(5))

#더 간단하게
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#n번째 삼각수(triangle number)는 자연수 1부터 n까지의 합입니다. 파라미터로 정수값 n을 받고 n번째 삼각수를 리턴해주는 재귀 함수
# triangle_number를 쓰세요. n은 1 이상의 자연수라고 가정합시다.
# 1부터 n까지의 합을 리턴
def triangle_number(n):
    # 코드를 입력하세요
    if n == 1:
        return 1
    return n + triangle_number(n - 1)

# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))

#피보나치
# n번째 피보나치 수를 리턴
def fib(n):
    # 코드를 입력하세요.
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))

#파라미터로 정수값 n을 받고 n의 각 자릿수의 합을 리턴해주는 재귀함수 sum_digits를 쓰세요. 반복문을 쓰지 말고, 재귀(recursion)의
# 개념을 활용해주세요!

#내 코드
# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # 코드를 작성하세요.
    if n == 0:
        return 0
    return (n % 10) + sum_digits(int(n / 10))

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

#선생 코드
# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    if n < 10:
        return n
    else:
        str_n = str(n)
        return int(str_n[0]) + sum_digits(int(str_n[1:]))

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

#리스트 뒤집기
# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    # 코드를 입력하세요.
    if len(some_list) < 2: #base case는 리스트가 원소가 하나도 없거나 하나일 때다 왜냐면 그럴 때 리스트는 그 자체가 거꾸로
        return some_list  #뒤집어진 리스트와 똑같기 때문이다 나는 처음에 len(some_list) == 1로 하려했는데 이러면 아무것도 없는
    return flip(some_list[1:]) + flip(some_list[:1]) #리스트일 때를 포함 못한다
#베이스 케이스 찾는 법 -> 이번꺼는 거꾸로 뒤집기니까 베이스 케이스는 그 자체로 거꾸로 뒤집어진 리스트여서 뒤집을 필요가 없는것들이다
#-> 다른 문제도 이런식으로 생각해보자
""" 요건 재귀파트 푸는 논리!
Recursive Case
Recursive case는 리스트의 요소가 두개 이상인 경우입니다.

파라미터 some_list로 리스트 [9, 2, 1, 3, 0]을 받고, flip 함수가 뒤집힌 리스트를 제대로 리턴해준다고 가정합시다. 
뒤집힌 some_list([9, 2, 1, 3, 0])를 어떻게 재귀적으로 표현할까요? 보통 재귀적으로 문제를 풀때는 문제의 사이즈를 줄이는 
것이 목표입니다. 원래 파라미터였던 [9, 2, 1, 3, 0]을 쪼개서 [9]와 [2, 1, 3, 0]으로 나눠봅시다. flip 함수가 제대로 
작동하기 때문에 flip([2, 1, 3, 0])은 [0, 3, 1, 2]를 리턴해주겠죠? 그리고 그 끝에 [9]를 붙여주면 [0, 3, 1, 2, 9]가 
나옵니다. 이걸 더 일반적으로 표현하면 flip(some_list[1:]) 뒤에 some_list[:1]를 붙여준 셈이죠.
"""

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

"""
하노이의 탑
하노이의 탑 게임 아시나요? 이 게임의 목표는 왼쪽 기둥에 있는 원판들을 모두 오른쪽 기둥으로 옮기는 것입니다. 지켜야할 규칙은 
두가지입니다:

한 번에 하나의 원판만 옮길 수 있다.
큰 원판이 작은 원판 위에 있어서는 안 된다.

과제
하노이의 탑 게임의 해답을 출력해주는 함수 hanoi를 쓰세요. hanoi는 파라미터로 원판 수 num_disks, 게임을 시작하는 기둥 
번호 start_peg, 그리고 목표로 하는 기둥 번호 end_peg를 받고, 재귀적으로 문제를 풀어 원판을 옮기는 순서를 모두 출력합니다.

def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.

# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)
1번 원판을 1번 기둥에서 3번 기둥으로 이동
2번 원판을 1번 기둥에서 2번 기둥으로 이동
1번 원판을 3번 기둥에서 2번 기둥으로 이동
3번 원판을 1번 기둥에서 3번 기둥으로 이동
1번 원판을 2번 기둥에서 1번 기둥으로 이동
2번 원판을 2번 기둥에서 3번 기둥으로 이동
1번 원판을 1번 기둥에서 3번 기둥으로 이동
가장 작은 원판의 번호는 1번이고 가장 큰 원판의 번호는 num_disks번입니다. 그리고 왼쪽 기둥이 1번, 가운데 기둥이 2번, 오른쪽 
기둥이 3번입니다.

시작하는 기둥을 start_peg, 목표 기둥을 end_peg, 그리고 나머지 기둥을 other_peg라고 부릅시다. 그러면 문제 풀이 방식을 
이렇게 정리할 수 있습니다:

가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동
가장 큰 원판을 start_peg에서 end_peg로 이동
나머지 원판들을 other_peg에서 end_peg로 이동
일단 start_peg와 end_peg가 주어졌을 때 other_peg는 어떻게 구할까요? 1번 기둥, 2번 기둥, 3번 기둥이 있기 때문에 
start_peg + end_peg + other_peg는 항상 6입니다. 이 관계를 이용해, other_peg를 적절히 정의해보세요.

원판이 하나도 없을 때가 base case입니다. 원판이 없으면 아무것도 할 필요 없기 때문에 return을 써서 그냥 함수 실행을 끝내주면 됩니다.
"""
"""
#하노이 마이 코드 실패
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    disk_num = num_disks
    # base case
    if num_disks == 1:
        move_disk(disk_num, start_peg, end_peg)
        return
    ########

    # Deciding spare peg
    if 1 != start_peg and 1 != end_peg:
        spare_peg = 1
    elif 2 != start_peg and 2 != end_peg:
        spare_peg = 2
    else:
        spare_peg = 3
    ########

    # recursive case
    hanoi(num_disks - 1, start_peg, spare_peg)
    hanoi(num_disks, start_peg, end_peg)
    hanoi(num_disks - 1, spare_peg, end_peg)
    ################ -> 이건 실패했다
"""

# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)


#하노이 마이 코드
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    disk_num = num_disks
    # base case
    if num_disks == 1:
        move_disk(disk_num, start_peg, end_peg)
        return
    ########

    # Deciding spare peg
    if 1 != start_peg and 1 != end_peg:
        spare_peg = 1
    elif 2 != start_peg and 2 != end_peg:
        spare_peg = 2
    else:
        spare_peg = 3
    ########

    # recursive case
    hanoi(num_disks - 1, start_peg, spare_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks - 1, spare_peg, end_peg)
    ################


# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)

##선생 모범 답안
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg = 1, end_peg = 3):
    if num_disks == 0:
        return
    else:
        other_peg = 6 - start_peg - end_peg #아 왜 이 생각을 못했지
        hanoi(num_disks - 1, start_peg, other_peg)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks - 1, other_peg, end_peg)

hanoi(3, 1, 3)