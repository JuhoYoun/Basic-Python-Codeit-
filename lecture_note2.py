def f(x):
    print("f 시작")
    return x + 1
    print("f 끝") #dead code


def g(x):
    print("g 시작")
    return x * x - 1
    print("g 끝") #dead code


print(f(2))  # print(3)과 같음
print(g(3))  # print(8)과 같음
print(f(2) + g(3))  # print(3 + 8)과 같음


def print_square(x):
    print(x * x)


def get_square(x):
    return x * x


print_square(3)
print("--")
get_square(3)
print("--")
print(get_square(3))
print("--")
print(print_square(3))

def secret_number():
    print("우리의 비밀 번호는: ")
    return 486

print(secret_number())

def x_is_one():
    x = 1 # local vriable

x = 2 # global variable

print("------------")

x_is_one()

print(x)

print("------------")

x = 5
def change_global():
    global x
    x = 1

change_global()

print(x)

print("------------")

print("Constant")

PI = 3.14 #대문자로 쓰면 상수가 된다(constant는 대문자로 써야한다) 함수 정의 내에서도 변하지 않는다
PI = 1 #파이썬에서 상수 값은 변할 수 있다. 파이썬에서 상수는 이름만 대문자인 vaiable이나 마찬가지다.
PI = 3.14

def f(r):
    return PI * r * r
r = 3
print(f(r))

print("Style")
# bad
someVariableName = 1
SomeVariableName = 1

def someFunctionName():
    print("Hello")

# good 모든 변수와 함수 이름은 소문자로 써주시고, 여러 단어일 경우 _로 나눠주세요.
some_variable_name = 1

def some_function_name():
    print("Hello")

# bad
someConstant = 3.14
SomeConstant = 3.14
some_constant = 3.14

# good 모든 상수 이름은 대문자로 써주시고, 여러 단어일 경우 _로 나눠주세요.
SOME_CONSTANT = 3.14

# bad
a = 2
b = 3.14
print(b * a * a)

# good 의미 부여
radius = 2
pi = 3.14
print(pi * radius * radius)

# bad
def do_something():
    print("Hello, world!")

# good 의미 부여
def say_hello():
    print("Hello, world!")

# bad
def print_product(a,b,c):
    print(a * b * c)

# bad
def print_product(a , b , c):
    print(a * b * c)

# good 적당한 화이트 스페이스
def print_product(a, b, c):
    print(a * b * c)

# bad
PI = 3.14
radius = 4
print(2 * PI * radius)
print(PI * radius * radius)
print(4 / 3 * PI * radius * radius * radius)
radius = 8
print(2 * PI * radius)
print(PI * radius * radius)
print(4 / 3 * PI * radius * radius * radius)

# good 문단 나누기
PI = 3.14

radius = 4
print(2 * PI * radius)
print(PI * radius * radius)
print(4 / 3 * PI * radius * radius * radius)

radius = 8
print(2 * PI * radius)
print(PI * radius * radius)
print(4 / 3 * PI * radius * radius * radius)

# bad
PI = 3.14

radius = 4
print(2 * PI * radius)
print(PI * radius * radius)
print(4 / 3 * PI * radius * radius * radius)

radius = 8
print(2 * PI * radius)
print(PI * radius * radius)
print(4 / 3 * PI * radius * radius * radius)

# good 추상화
PI = 3.14

def calculate_circumference(r):
    return 2 * PI * r

def calculate_area(r):
    return PI * r * r

def calculate_volume(r):
    return 4 / 3 * PI * r * r * r

radius = 4
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))

radius = 8
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))

# bad (설명 부족)
PI = 3.14

def calculate_circumference(r):
    return 2 * PI * r

def calculate_area(r):
    return PI * r * r

def calculate_volume(r):
    return 4 / 3 * PI * r * r * r

radius = 4
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))

radius = 8
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))

# bad (설명 과다)
PI = 3.14   # 원주율

# 반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    # 둘레는 2 * 파이 * 반지름
    return 2 * PI * r

# 반지름이 r인 원의 넓이 계산
def calculate_area(r):
    # 넓이는 파이 * 반지름 * 반지름
    return PI * r * r

# 반지름이 r인 구의 부피 계산
def calculate_volume(r):
    # 부피는 4 / 3 * 파이 * 반지름 * 반지름 * 반지름
    return 4 / 3 * PI * r * r * r

# 반지름이 4인 경우
radius = 4    # 반지름
print(calculate_circumference(radius))  # 반지름 4인 경우 둘레
print(calculate_area(radius))           # 반지름 4인 경우 넓이
print(calculate_volume(radius))         # 반지름 4인 경우 부피

# 반지름이 8인 경우
radius = 8    # 반지름
print(calculate_circumference(radius))  # 반지름 8인 경우 둘레
print(calculate_area(radius))           # 반지름 8인 경우 넓이
print(calculate_volume(radius))         # 반지름 8인 경우 부피

# good
PI = 3.14   # 원주율

# 반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return 2 * PI * r

# 반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

# 반지름이 r인 구의 부피 계산
def calculate_volume(r):
    return 4 / 3 * PI * r * r * r

# 반지름이 4인 경우
radius = 4    # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))

# 반지름이 8인 경우
radius = 8    # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))

# bad
print("오늘은 " + str(2016) + "년 " + str(4) + "월 " + str(15) + "일 " + "금" + "요일입니다.")

# good 적당한 줄길이 80자 이하
print("오늘은 " + str(2016) + "년 " + str(4) + "월 " + str(15) +
    "일 " + "금" + "요일입니다.")

print("----------")

# is_evenly_divisible 함수
def is_evenly_divisible(number):
    return number % 2 == 0

print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))