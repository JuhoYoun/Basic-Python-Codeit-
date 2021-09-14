print(3 + 5)
print(2 - 5)
print(2 ** 4) # a number after ** is power of the number before **
print(4 % 3)
print(4 / 2)
print(4 / 3)
print("Hello" + ' World')
print('He said, "I`m yours"')
print("Hey" * 3)
string1="Hello "
print(string1 * 3)
print(int(3.2))
print(float(2))
print(int("2") + int("5"))
print(float("3.3") + float("2.2"))
print(str(2)+str(3))
print(int(3.4))
print(float(3))
print(int("2")+int("3"))
print(float(1.2)+float(2.2))
print(str(2)+str(4))
print("오늘은 %d년 %d월 %d일 %s일입니다."%(12, 3, 23 + 1, "토"))
print("소수 안나와 %d"%(3/4))
print("소수 나와 %f"%(3/4))
print("소수 4자리 까지만 %.4f"%(1/3))
wage = 5                  # 시급 (1시간에 5달러)
exchange_rate = 1142.16   # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("%d시간에 %d%s 벌었습니다." % (1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("%d시간에 %d%s 벌었습니다." % (5, wage * 5, "달러"))

# "1시간에 5710.8원 벌었습니다." 출력
print("%d시간에 %d%s 벌었습니다." % (1, wage * 1*exchange_rate, "원"))

# "5시간에 28554.0원 벌었습니다." 출력
print("%d시간에 %d%s 벌었습니다." % (5, wage * 5*exchange_rate, "원"))

print(False)
print(True)
print("True")
print(type(1))
print(type(1.0))
print(type("1"))
print(type(True))
print(type(print))
print(4//3)
print(4.0//3)
print(round(3.13, 1))
print(round(3.1232, 3))
print("haha \nhaha")

def hello(): #Header
    print("Hello") #body

hello()

def hello(name):
    print("Hello, %s" %(name))

hello("Youn")

def sum(a, b):
    print(a + b)

sum(2, 3)
sum("a", "b")

def print_residue(a, b):
    print(a % b)

print_residue(7, 3)


def calculate_change(payment, cost):
    fifty_thousand = 0
    ten_thousand = 0
    five_thousand = 0
    one_thousand = 0
    change = 0

    change = payment - cost

    fifty_thousand = int(change / 50000)
    change = change % 50000

    ten_thousand = int(change / 10000)
    change = change % 10000

    five_thousand = int(change / 5000)
    change = change % 5000

    one_thousand = int(change / 1000)
    change = change % 1000

    print("50000원 지폐: %d장" % (fifty_thousand))
    print("10000원 지폐: %d장" % (ten_thousand))
    print("5000원 지폐: %d장" % (five_thousand))
    print("1000원 지폐: %d장" % (one_thousand))


calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

x = 2

# 다음 두 줄은 같습니다 syntactic sugar
x = x + 2
x += 2

# 다음 두 줄은 같습니다
x = x * 2
x *= 2

# 다음 두 줄은 같습니다
x = x - 3
x -= 3

# 다음 두 줄은 같습니다
x = x / 2
x /= 2

# 다음 두 줄은 같습니다
x = x % 7
x %= 7

# optional parameter
def myself(name, age, nationality = "한국"):
    print("내 이름은 %s" % name)
    print("나이는 %d살" % age)
    print("국적은 %s" % nationality)

myself("코드잇", 1)            # 기본값이 설정된 파라미터를 바꾸지 않을 때
myself("코드잇", 1, "미국")     # 기본값이 설정된 파라미터를 바꾸었을 때

def f(x):
    print("start")
    return x + 1
    print ("end") #dead code. never show up

print(f(1))

def f1(x):
    print("start")

print(f1(1))