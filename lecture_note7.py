#객체 지향 함수
"""
이전 섹션들에서는 정수, 문자열, 리스트 등 파이썬에 기본적으로 있는 자료형들로 프로그램을 짰습니다. 그런데 페이스북같은 SNS를 만들려면 '유저'는 어떻게 표현해야 할까요? '유저'는 이름, 이메일, 비밀번호, 생년월일, 친구목록 등 구성이 굉장히 복잡합니다. 문자열 하나로도 표현할 수 없고, 리스트로도 표현할 수 없습니다.

파이썬같은 객체 지향 프로그래밍 언어가 이럴 때 유용해집니다. 기존의 자료형들로 표현하기 어려운 것들은 우리가 새로운 자료형을 만들어서 표현할 수 있습니다. SNS를 위해서는 '유저'라는 새로운 자료형을 만들면 되겠죠?

파이썬에서 새로운 자료형을 만들려면 '클래스'라는 것을 써야합니다. 클래스는 어떤 자료형에 대한 설명서라고 생각할 수 있습니다. 한번 직접 '유저'를 표현할 수 있는 자료형을 만들어봅시다.

클래스 정의
일단 클래스의 정의 안에는 pass만 써두겠습니다. pass는 그냥 다른 내용은 쓰지 않겠다고 표시하는 명령어입니다.
"""
class User:
    pass

# User값들 생성
user1 = User()
user2 = User()

# 파이썬의 기본 자료형
print(type(7))
print(type(3.14))
print(type("hello"))
print(type([1, 2, 3, 4, 5]))

# 우리가 만든 자료형
print(type(user1))
print(type(user2))

"""
<class '__main__.User'>라고 나와있는 것을 확인할 수 있습니다. 1이 int 클래스의 값이고 "hello"는 str 클래스의 값입니다. 
비슷한 개념으로 user1과 user2는 우리가 실행한 파일(main 파일)에 정의되어 있는 User 클래스의 값이란 뜻입니다.
"""

#인스턴스
class User:
    pass

user1 = User()
user2 = User()

print(user1 == user2)

"""
분명 user1과 user2는 똑같이 User()를 써서 생성하였는데 왜 False가 출력될까요?
User()를 호출하면 메모리의 특정 공간에 새로운 User 값이 생성되고, 그 메모리 주소가 리턴돼서 user1과 user2에 저장됩니다. 
그런데 User()를 호출할때마다 새로운 메모리 공간(서로 다른 메모리 주소)에 값을 생성하기 때문에 user1과 user2는 엄밀히 따지면 다른 값, 또는 다른 
인스턴스입니다. 따라서 user1 == user2는 False가 나오는 것입니다!
"""
"""
복습한번 해보자

x = [1, 2, 3]  #리스트가 생성되고 리스트의 메모리 주소에 x라는 이름표가 붙는다
y = x          #같은 주소에 y이름표도 붙는다
y[0] = 0       #y가 붙어있는 메모리 주소의 리스트 첫번째 인덱스를 0으로 바꾼다
print(x)
#이라면 x[0]도 0 으로 바뀐다

x = 5  #5 생성 x라는 이름표가 5가 저장된 메모리에 붙는다
y = x  #그 메모리 주소에 y 이름표도 붙는다
y = 3  #3이 메모리에 생성되고 y이름표가 그 주소로 옮겨 붙는다
print(x) #그래서 y가 변한다고 x까지 3으로 변하지 않는다 리스트의 경우와 다르다
"""
list1 = [1, 2]
list2 = [1, 2]
print(list1 == list2)
#이 경우 list1과 list2는 다른 인스턴스인데 왜 트루가 나올까?
"""
모든 클래스에는 __eq__()라는 메소드가 있습니다. 우리가 ==을 사용하게 될 때는 이 __eq__()라는 메소드
를 호출하게 되는 것입니당. 사용자가 클래스를 만들 때 정의되어 있지 않다면 object 라는 최상위 클래스의 __eq__() 메소드를 
가져오게 됩니당 이런 경우는 객체의 identity 를 비교합니다. 즉 메모리 주소를 말하는 것이죵. 달리 생각해보면 만약 클래스의 
비교를 어떤 기준으로 정의해보고 싶다면, __eq__() 메소드를 override(재정의)하면 됩니당^^
필요하다면 같은 클래스에서 만들어진 instance 를 ==으로 비교했을 때 같다고 만들수가 있는 것이죵
"""
"""
값 더하기
3 + 5를 하면 8이 나오고, [1, 2, 3] + [1, 3, 5]를 하면 [1, 2, 3, 1, 3, 5]가 나오고, "hello" + "world"를 하면 "helloworld"가 
나오는 이유는 무엇일까요? 그냥 컴퓨터가 저절로 알아서 +를 이해하고 각 경우에 따라서 맞는 방식으로 더하는 것일까요?

사실은 각 class에 +를 어떻게 쓸지 정의해 놓았기 때문에 저런 결과값들이 나오는 것입니다.

class SomeClass:
    def __init__(self, x):
        self.attr1 = x

ex1 = SomeClass(5)
ex2 = SomeClass(3)
print(ex1 + ex2)
파이썬은 SomeClass의 두 값을 더하는 방법을 모르기 때문에 오류가 나옵니다.

TypeError: unsupported operand type(s) for +: 'SomeClass' and 'SomeClass'
이 문제를 고치기 위해서 +를 쓰는 방법을 설명해주는 __add__ 메소드를 정의해야합니다.

class SomeClass:
    def __init__(self, x):
        self.attr1 = x

    def __add__(self, other):
        return self.attr1 + other.attr1

ex1 = SomeClass(5)
ex2 = SomeClass(3)
print(ex1 + ex2)
ex1 + ex2는 ex1.__add__(ex2)와 같습니다. 따라서 ex1.attr1 + ex2.attr1의 결과값인 8이 나오겠죠.

8
값 비교하기
마찬가지로 ==도 어떤 결과값을 낼지 각 class에 정의를 할 수 있습니다. 리스트의 경우에는 순서대로 모두 같은 값을 보관하고 있으면 True가 나옵니다.

그러면 이 경우에는 어떻게 나올까요?

class SomeClass:
    def __init__(self, x):
        self.attr1 = x

ex1 = SomeClass(5)
ex2 = SomeClass(5)
print(ex1 == ex2)
False
==가 어떻게 쓰여야하는지 정의해주지 않으면, 두 자료형이 같은 인스턴스면 True, 아니면 False가 나옵니다. ex1과 ex2는 다른 
인스턴스이기 때문에 False가 나옵니다. ==가 어떻게 쓰이는지 설정하기 위해서는 __eq__ 메소드를 쓰면 됩니다.

class SomeClass:
    def __init__(self, x):
        self.attr1 = x

    def __eq__(self, other):
        return self.attr1 == other.attr1

ex1 = SomeClass(5)
ex2 = SomeClass(5)
print(ex1 == ex2)
ex1 == ex2는 ex1.__eq__(ex2)와 같습니다. 따라서 ex1.attr1 == ex2.attr1의 결과값인 True가 나오겠죠.

같은 인스턴스인지 확인하기
==를 떠나서 두 값이 같은 인스턴스인지, 즉 두 값이 같은 메모리 주소를 가리키고 있는지 확인하는 방법이 있습니다.

class SomeClass:
    def __init__(self, x):
        self.attr1 = x

    def __eq__(self, other):
        return self.attr1 == other.attr1

ex1 = SomeClass(5)
ex2 = SomeClass(5)
print(ex1 is ex2)

list1 = [2, 3, 4, 5]
list2 = [2, 3, 4, 5]
print(list1 is list2)
이렇게 is를 쓰면 두 값이 같은 인스턴스인지 아닌지 확인할 수 있습니다.

False
False
"""

"""
Python에서는 class안에 멤버변수를 정의하지 않아도 인스턴스를 생성한 후에 값을 그냥 넣을 수 있나요??? 설명에서 그렇게 하시길래 궁금해서 질문합니다.

class 를 비워놓은 상태에서 인스턴스를 통해 값을 넣는 걸 말씀하시나용? 가능합니당^^

그런 기능이 허용되는 이유를 알 수 있을까요?? 이 기능의 장점이 무엇인지 궁금합니다. 실제 코딩시 그 기능을 사용하는 것은 좋은가요 
나쁜가요?? 그리고 그 기능이 쓰인다면 어떤 경우에 쓰이는지 궁금합니다.

저도 확실하지는 않지만 그 기능은 사용하지 않는게 좋은 것 같습니다. 보통 클래스 안에 무슨 속성이 있는지, 무슨 메소드가 있는지를 
보고 클래스를 이해하는데 속성이 클래스 외부에서 정의된다면 무슨 속성이 있는지 파악하기 어려울 것 같습니다. 속성은 __init__()함수 
안에서 정의하는게 가장 좋은 것 같습니다.
"""

#인스턴스 메쏘드 정리
"""
클래스를 쓰는 이유는 기존의 자료형들로 간단히 표현되지 않는 것들을 표현하기 위해서입니다.

인스턴스 변수
SNS의 이용자들을 표현하기 위해서는 User라는 자료형을 만들었는데, 각 이용자는 '이름', '나이', '이메일', '비밀번호' 등의 값을 보관해야 합니다.

다행히 각 인스턴스는 여러가지 인스턴스 변수를 보관할 수 있습니다.

class User:
    pass

# 첫번째 유저 값 설정
user1 = User()
user1.name = "Bill Gates"
user1.age = 60
user1.email = "bill@microsoft.com"
user1.password = "gates1234"
위의 코드에서는 user1의 인스턴스 변수 name, age, email, 그리고 password를 정의하였습니다. 이 변수들을 '인스턴스 변수'라고 
부르는 이유는 각 변수가 User 클래스 전체에 해당되는 것이 아니라 User 클래스의 한 인스턴스인 user1에 해당되기 때문입니다.

저장된 인스턴스 변수를 불러오려면 그냥 아래처럼 쓰면 됩니다:

print(user1.name, user1.age, user1.email, user1.password)
Bill Gates 60 bill@microsoft.com gates1234

정의되지 않은 인스턴스 변수
정의되지 않은 인스턴스 변수를 불러오면 에러가 나옵니다.

class User:
    pass

# 첫번째 유저 값 설정
user1 = User()
user1.name = "Bill Gates"
user1.age = 60
user1.email = "bill@microsoft.com"
user1.password = "gates1234"

# 두번째 유저 값 설명
user2 = User()

print(user2.name, user2.age, user2.email, user2.password)
Traceback (most recent call last):
  File "e.py", line 14, in <module>
    print(user2.name, user2.age, user2.email, user2.password)
AttributeError: 'User' object has no attribute 'name'

따라서 모든 인스턴스 변수는 처음부터 초기값을 설정해주는 것이 중요합니다!

class User:
    pass

# 첫번째 유저 값 설정
user1 = User()
user1.name = "Bill Gates"
user1.age = 60
user1.email = "bill@microsoft.com"
user1.password = "gates1234"

# 두번째 유저 값 설명
user2 = User()
user2.name = "Mark Zuckerberg"
user2.age = 32
user2.email = "mark@facebook.com"
user2.password = "zuck123"

print(user1.name, user1.age, user1.email, user1.password)
print(user2.name, user2.age, user2.email, user2.password)
Bill Gates 60 bill@microsoft.com gates1234
Mark Zuckerberg 32 mark@facebook.com zuck123

메소드
클래스는 변수뿐만 아니라 함수도 보관할 수 있습니다. 클래스에 정의된 함수는 메소드라고 부릅니다. 이용자에 대한 간단한 정보를 출력하는 메소드를 써봅시다.

class User:
    def introduce(some_user):
        print("%s is %d years old." % (some_user.name, some_user.age))

# 첫번째 유저 값 설정
user1 = User()
user1.name = "Bill Gates"
user1.age = 60
user1.email = "bill@microsoft.com"
user1.password = "gates1234"

# 두번째 유저 값 설명
user2 = User()
user2.name = "Mark Zuckerberg"
user2.age = 32
user2.email = "mark@facebook.com"
user2.password = "zuck123"

User.introduce(user1)
User.introduce(user2)
Bill Gates is 60 years old.
Mark Zuckerberg is 32 years old.
이렇게 User(클래스 이름), .(마침표), introduce(메소드 이름)을 쓰면 메소드를 호출할 수 있습니다. 여기에 파라미터로 인스턴스 
user1을 넘겨주면 user1.name과 user1.age가 불려오고 문자열 포맷팅에 의해 "Bill Gates is 60 years old."가 출력되는거죠. 
마찬가지로 파라미터로 user2를 넘겨주면 "Mark Zuckerberg is 32 years old"가 출력됩니다.

Syntactic Sugar
그러나 대부분의 경우에 파라미터로 user1이나 user2같은 User 클래스의 인스턴스를 넘겨줄 것이기 때문에, 파이썬에서는 아예 메소드 
호출을 쉽게 쓰는 방법을 만들어 놓았습니다.

# 이 두 줄은 같음
User.introduce(user1)
user1.introduce()

# 이 두 줄은 같음
User.introduce(user2)
user2.introduce()
Bill Gates is 60 years old.
Bill Gates is 60 years old.
Mark Zuckerberg is 32 years old.
Mark Zuckerberg is 32 years old.

user1.introduce()처럼 앞에 클래스 이름(User)이 아닌 인스턴스(user1)를 쓰면, 그 인스턴스(user1)가 introduce 메소드의 
첫번째 파라미터로 넘어갑니다. 따라서 user1.introduce는 User.introduce(user1)과 똑같은 Syntactic Sugar인 셈이죠.

파라미터가 여러개인 경우를 봅시다. introduce 메소드가 두번째 파라미터로 정수 n을 받고 자기 소개를 n번 하도록 써보겠습니다.

class User:
    def introduce(some_user, n):
        for i in range(n):
            print("%s is %d years old." % (some_user.name, some_user.age))
이 경우에 Syntactic Sugar를 활용하여 쓴다면 이렇게 됩니다:

# 이 두 줄은 같음
User.introduce(user1, 3)
user1.introduce(3)

# 이 두 줄은 같음
User.introduce(user2, 2)
user2.introduce(2)
Bill Gates is 60 years old.
Bill Gates is 60 years old.
Bill Gates is 60 years old.
Bill Gates is 60 years old.
Bill Gates is 60 years old.
Bill Gates is 60 years old.
Mark Zuckerberg is 32 years old.
Mark Zuckerberg is 32 years old.
Mark Zuckerberg is 32 years old.
Mark Zuckerberg is 32 years old.

self

user1.introduce()를 호출할때처럼 보통 첫번째 파라미터로 현재 주인공인 인스턴스를 넘겨줍니다. 그렇기 때문에 메소드의 
첫번째 파라미터 이름은 self라고 지어주는 것이 파이썬 커뮤니티의 약속입니다. some_user라고 지어줘도 오류가 나지 않지만 
코드의 일관성을 위해 약속을 꼭 지켜주세요!

class User:
    def introduce(self):
        print("%s is %d years old." % (self.name, self.age))
"""

#initialize
class User:
    # initialize 메소드를 여기 쓰세요
    # def initialize...)
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
user3.initialize("Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
user4.initialize("Lisa", "lisa@codeit.kr", "abc123")

print(user1.email)
print(user2.name)
print(user3.password)
print(user4.email)

"""
함수 헤더(header) 작성
class User:
    # initialize 메소드를 여기 쓰세요
    # def initialize...

# 테스트
user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")
여기서 user1.initialize("Young", "young@codeit.kr", "123456")을 호출하면 User 클래스의 initialize 메소드가 실행되고 
첫번째 파라미터로 인스턴스 user1이 넘어가게 됩니다. 그리고 "Young", "young@codeit.kr", "123456" 이 순서대로 2~4번째 파라미터로 넘어가게 됩니다.

따라서 아래 두 줄은 같다고 볼 수 있습니다:

user1.initialize("Young", "young@codeit.kr", "123456")
User.initialize(user1, "Young", "young@codeit.kr", "123456")
위의 두 줄 중 두번째 줄을 보니까 initialize는 파라미터로 4개의 값을 받아야겠죠? 저번 강의에서 말했듯이 첫번째로는 인스턴스로 
self를 받고, 그 다음 문자열 name, 문자열 email, 문자열 password를 받으면 됩니다.

initialize 메소드의 헤더("header") 부분은 아래와 같이 쓸 수 있습니다:

class User:
    def initialize(self, name, email, password):
        pass
여기서 self는 user1, user2와 같은 인스턴스를 받기 때문에 인스턴스 변수 user1.name, user2.name에 각각 어떤 값을 지정하고 
싶으면 self.name에 지정하면 됩니다.

class User:
    def initialize(self, name, email, password):
        self.name = name

user1.initialize("Young", "young@codeit.kr", "123456")
함수 바디(body) 작성
이렇게 쓰면 user1이 self로 넘어가고, "Young"이 name으로 넘어갑니다. 따라서 self.name = name은 user1.name = "Young"과 같은거죠.

똑같은 개념으로 initialize 메소드에서 '이메일'과 '비밀번호'에 해당하는 인스턴스 변수의 초기값도 설정해주려면 이렇게 하면 됩니다:

class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
"""
"""
정의되어 있지 않은 인스턴스 변수를 사용하면 오류가 나오기 때문에 꼭 모든 인스턴스 변수를 정의해야 합니다. 그래서 저번 과제로 
모든 인스턴스 변수를 초기값으로 설정해주는 initialize 메소드를 써봤습니다.

class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# 샘플 유저 생성
user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
user3.initialize("Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
user4.initialize("Lisa", "lisa@codeit.kr", "abc123")
그런데 보시다시피 매번 User 인스턴스를 생성하는 줄을 하나 쓰고, 초기값을 설정해주기 위해서 initialize 메소드를 호출하는 줄을 
하나 썼습니다. 뭔가 좀 번거롭죠?

__init__ 매직 메소드
다행히 파이썬은 인스턴스 생성과 초기값 설정을 한번에 해결할 수 있도록 __init__이라는 특별한 메소드를 쓸 수 있게 해줍니다.

원래 써놓은 initialize 메소드의 이름만 __init__으로 바꾸겠습니다.

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
__init__ 메소드를 정의해놓으면 이제 유저 생성과 초기값 설정을 이렇게 깔끔하게 할 수 있습니다:

# 깔끔한 유저 생성 및 초기값 설정
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")
여기서 일어나는 일은 3가지입니다. 첫번째 유저 생성을 예로 들면:

메모리가 할당되고 User 인스턴스가 생성됩니다.
__init__ 메소드가 호출됩니다. 파라미터 self로는 생성된 인스턴스가 넘어가고 name, email, password로는 
"Young", "young@codeit.kr", "123456"이 각각 넘어갑니다. 이 경우 인스턴스 변수들의 초기값이 모두 설정되는 거죠.
만들어진 User 인스턴스가 리턴돼서 변수 user1에 저장됩니다.
앞으로는 인스턴스 변수가 있는 클래스에는 무조건 __init__ 메소드를 써주시고, __init__ 메소드에 모든 인스턴스 변수의 초기값을 
지정해주세요!
"""

#자기 소개 practice
# sns의 유저
class User:
    # 초기값 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # 자기 소개 (이름, 이메일)
    def introduce(self):
        # 코드를 입력하세요.
        print("My name is %s." % (self.name))
        print("My email address is %s" % (self.email))

    # 자기 소개 두번
    def introduce_twice(self):
        # 코드를 입력하세요.
        self.introduce() #print 안써도 클래스 내의 function을 이용해서 할 수 있다
        self.introduce()

# 테스트
user1 = User("Young", "young@codeit.kr", "123456")
user1.introduce()
user1.introduce_twice()
User.introduce_twice(user1)

"""
introduce_twice 메소드
introduce_twice 메소드도 물론 introduce 메소드처럼 이렇게 쓸 수 있습니다:

def introduce_twice(self):
    print("My name is %s" % self.name)
    print("My email address is %s" % self.email)
    print("My name is %s" % self.name)
    print("My email address is %s" % self.email)
하지만 이미 써놓은 코드를 또 쓰는 것은 프로그래머로서 다시 생각해봐야할 일이죠? 그래서 과제에서 introduce_twice 메소드에는 
print를 쓰면 안 된다고 했습니다.

어떻게 고쳐볼 수 있을까요?

user1.introduce_twice()는 User.introduce_twice(user1)과 같습니다. 파라미터 self로 user1이 넘어간다는 뜻이죠. 
그렇다면 이 코드는 어떤가요?

def introduce_twice(self):
    self.introduce()
    self.introduce()
self는 user1과 같기 때문에 self.introduce()는 user1.introduce()와 동일합니다. 그래서 그냥 self.introduce()를 두번 
호출해주면 됩니다!
"""

#practice 맞팔해요
class User:
    # 초기값 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.following_list = []  # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []  # 이 유저를 팔로우하는 유저 리스트

    # 팔로우
    def follow(self, another_user):
        # 코드를 입력하세요.
        self.following_list.append(another_user)
        another_user.followers_list.append(self)

    # 몇명을 팔로우하는지 리턴
    def num_following(self):
        # 코드를 입력하세요.
        return len(self.following_list)

    # 팔로워가 몇명인지 리턴
    def num_followers(self):
        # 코드를 입력하세요.
        return len(self.followers_list)


# 유저들 생성
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 테스트
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())

