#알고리즘 -> 문제를 해결하기 위한 자세한 방법
#컴퓨터 알고리즘 -> 컴퓨터가 문제를 해결하기 위한 방법(ex 리스트 뒤집기 팔린드롬 리스트 정렬...)
#최단거리 계산 알고리즘 -> 네비게이션, 맵 어플
#암호화 알고리즘 -> 인터넷 보안
#데이터 압축 알고리즘 -> 더 작은 크기로 정보 보관, 전송
#머신 러닝 -> 인터넷에서 나에게 맞는 제품 추천, 스피치 & 문자 인식, 알파고
#이번 섹션 -> 알고리즘 분석법 배운다 -> 점근 표기법(Asymptotic notation) -> 알고리즘 효율 분석
#-> 리스트에서 값 탐색 알고리즘(Binary search)도 배운다
#-> Breadth first search(aka BFS 최단 거리 계산 알고리즘)도 배운다
#거듭 제곡 -> 2^3 = 2 * 2 * 2, 2^2 = 2^3 / 2, 2^1 = 2^2 / 2, 2^0 = 2^2 / 2, 2^-1 = 2^0 / 2
#로그 -> loga(b) -> b를 a로 몇번 나누어야 1이 되는가

#선형 탐색
#'선형 탐색(Linear Search)' 알고리즘을 사용해서 어떤 원소가 리스트 안에 포함되어 있는지 확인하려고 합니다. 선형 탐색이란, 리스트의
# 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘입니다.파라미터로 탐색할 값 element와 리스트 some_list를 받는 함수
# linear_search를 작성하세요. 0번 인덱스부터 순서대로 하나씩 확인해서 만약 element를 some_list에서 발견할 시 그 위치(인덱스)를
# 리턴해주면 됩니다. element가 some_list에 존재하지 않는 값이면 None을 리턴해주세요.
#Mycode
def linear_search(element, some_list):
    # 코드를 작성하세요.
    i = 0
    while i < len(some_list):
        if element == some_list[i]:
            return i
        i += 1
    return "None"

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))

#for 써서
def linear_search(element, some_list):
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i
    return None

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))

"""
이진 탐색 - 반복문
'이진 탐색(Binary Search)' 알고리즘을 사용해서 어떤 원소가 리스트 안에 포함되어 있는지 확인하려고 합니다. 이진 탐색 
알고리즘은 선형 탐색 알고리즘과 달리, 정렬된 리스트를 전제로 합니다. 정렬된 리스트가 아니면 이 알고리즘은 적용이 불가능합니다.

왜 이 알고리즘의 이름이 '이진 탐색'일까요? 1회 비교를 거칠 때마다 탐색 범위가 절반으로 줄어들기 때문입니다.

예시
예를 들어 [1, 2, 3, 5, 8, 13, 21, 34, 55]에서 3을 찾는 경우, 알고리즘의 진행 방식은 다음과 같습니다:

시도 1
리스트의 첫 번째 인덱스와 마지막 인덱스의 값을 합하여 2로 나눈 후, 중간 인덱스로 지정합니다. 그리고 그 인덱스에 해당하는 
값이 3인지 확인해봅니다.

이 경우 리스트의 첫 번째 인덱스는 0이고 마지막 인덱스는 8이므로, 중간 인덱스는 4이고 해당 원소는 8입니다.

찾고자 하는 원소(3)는 중간 원소(8)에 비해 작습니다. 리스트는 정렬되어있으므로, 인덱스 4~8은 탐색 범위에서 제외됩니다. 
탐색 범위가 절반으로 줄어든 것이죠.

시도 2
탐색 범위는 이제 인덱스 0~3입니다. 탐색 범위의 리스트의 첫 번째 인덱스는 0이고 마지막 인덱스는 3이므로, 중간 인덱스는 
(0 + 3) // 2인 1입니다. 인덱스 1에 해당 원소는 2이죠.

찾고자 하는 원소(3)는 중간 원소(2)에 비해 큽니다. 리스트는 정렬되어 있으므로, 인덱스 0~1은 탐색 범위에서 제외됩니다. 
탐색 범위가 다시 절반으로 줄어든 것이죠.

시도 3
탐색 범위는 이제 인덱스 2~3입니다. 탐색 범위의 리스트의 첫 번째 인덱스는 2이고 마지막 인덱스는 3이므로, 중간 인덱스는 
(2 + 3) // 2인 2입니다. 인덱스 2에 해당하는 원소의 값은 3이죠.

찾고자 하는 원소(3)는 중간에 해당하는 원소(3)와 일치합니다. 값을 찾았으니, 인덱스 2를 리턴해주며, 알고리즘을 종료합니다.

재귀 대신 반복문을 사용하셔야 합니다. 재귀로 이진 탐색을 구현하는 것은 바로 다음 과제입니다!

"""
#바이너리 서치 내 코드
def binary_search(element, some_list):
    # 코드를 작성하세요.
    first_index = 0
    last_index = len(some_list) - 1
    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2
        if some_list[middle_index] == element:
            return middle_index
        elif some_list[middle_index] < element:
            first_index = middle_index + 1
        else:
            last_index = middle_index - 1
    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

#Binary search teacher
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif element < some_list[midpoint]:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1

    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

"""
이진 탐색 - 재귀
'이진 탐색(Binary Search)' 알고리즘의 개념은 앞에서 설명되어 있고, 반복문을 사용하여 문제를 해결하셨을 것입니다. 이번에는 
재귀(recursion)를 사용하여 문제를 해결해보세요!

템플릿에 있는 함수 정의를 보시면 optional parameter를 사용하는데요. 이 내용이 기억 안 나시면 '추상화' 섹션의 '추상화 꿀팁' 
노트를 보시면 됩니다!

end_index의 기본값을 None으로 설정한 후, 함수 내에서 len(some_list) - 1로 바꾼 이유가 궁금하실 것입니다. 파라미터를 받을 
때 파이썬은 some_list의 존재를 모르기 때문에, 정의를 이렇게:

def binary_search(element, some_list, start_index = 0, end_index = len(some_list) - 1):
쓰면 이런 오류 메시지가 나옵니다:

NameError: name 'some_list' is not defined
이 때문에 먼저 None으로 설정한 후, 함수 안에서 end_index의 값이 특별히 설정되지 않았을 경우에는 end_index를 
len(some_list) - 1로 바꾸어주는 것입니다.

Base Case
리스트가 정렬되어 있으므로, 재귀 함수를 통해 함수가 호출되는 과정에서 start_index가 end_index보다 클 경우에는 원소가 
포함되어있지 않다는 이야기입니다. 따라서 이 경우에 None을 리턴해주면 됩니다.

Recursive Case
element가 some_list[midpoint]와 일치한다면, 그 인덱스를 리턴하고 종료합니다.
element가 some_list[midpoint]보다 작다면, 탐색 범위의 후반부는 제외시켜도 됩니다. 따라서 end_index를 
midpoint - 1로 업데이트해줍니다. 그 후 binary_search(element, some_list, start_index, end_index)를 리턴해주어 
재귀적으로 문제를 해결합니다.
element가 some_list[midpoint]보다 크다면, 탐색 범위의 전반부는 제외시켜도 됩니다. 따라서 start_index를 midpoint + 1로 
업데이트해줍니다. 그 후 binary_search(element, some_list, start_index, end_index)를 리턴해주어 재귀적으로 문제를 해결합니다.
"""
#My code
def binary_search(element, some_list, start_index = 0, end_index = None):
    if end_index == None:
        end_index = len(some_list) - 1
    if start_index > end_index:
        return None
    middle_point = (start_index + end_index) // 2
    if some_list[middle_point] == element:
        return middle_point
    elif some_list[middle_point] < element:
        start_index = middle_point + 1
        binary_search(element, some_list, start_index, end_index)
    else:
        end_index = middle_point - 1
        binary_search(element, some_list, start_index, end_index)

    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
##### -> 이 코드는 틀렸다 왜 그럴까!!!!!! 잘 생각해보자

###고친 코드
def binary_search(element, some_list, start_index = 0, end_index = None):
    if end_index == None:
        end_index = len(some_list) - 1
    if start_index > end_index:
        return None
    middle_point = (start_index + end_index) // 2
    if some_list[middle_point] == element:
        return middle_point
    elif some_list[middle_point] < element:
        start_index = middle_point + 1
        return binary_search(element, some_list, start_index, end_index)
    else:
        end_index = middle_point - 1
        return binary_search(element, some_list, start_index, end_index)

    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

"""
선형 검색 vs 이진 검색

리스트 길이가 n일 때

선형 검색의 가장 오래 걸리는 경우 -> n번째에 끝나는 경우

이진 검색의 가장 오래 걸리는 경우 -> Log2(n) 

n이 커질수록 바이너리 서치가 훨낀 효율 적이다!!
"""

"""
점근 표기법

효율적인 알고리즘 = 문제를 빨리 해결하는 알고리즘
프로그램 속도에 영향을 주는 것들 : 컴퓨터 사양, 컴퓨터 상태(사용량), 프로그래밍 언어 종류, 컴파일러 종류 ... 
-> 단순히 걸린 시간 측정해서 알고리즘 효율성 비교는 어렵다
이런것들 영향 없이 알고리즘의 효율성을 계산하는 법 -> 점근 표기법
인풋이 커질수록 시간은 얼마나 더 오래 걸리는가??

def linear_search(element, some_list):
    i = 0 #a
    while i < len(some_list): #b
        if element == some_list[i]:#c
            return i#c
        i += 1#c
    return "None"#:d

총 걸리는 시간은 a + n(b + c) + d = (b + c)n + a + d (n은 리스트 길이)
예를 들어 20n + 30이라 하자 n이 커질수록 30은 쓸모 없어진다 
n이 백배 되면 총 걸리는 시간도 얼추 백배 된다 
그러면 걸리는 시간은 20n + 30이 아니라 20n으로 나타낼 수 있다(n이 클 때) -> 이게 점근 표기법
20n + 30 -> 20n 이것이 big O of n 알고리즘
n^2 + 3n + 1 -> n^2 이거시 big O of n^2 알고리즘
2n^3 - 30n +100 -> 2n^3 이것이 big O of n^3 알고리즘
"""

"""
Graph 

페이스북을 생각해보자 여러 사용자가 있고 친구인 사용자들끼리는 선으로 이어져 있다 
각각의 사용자를 정점(vertex)라 하고 사용자들을 잇는 선을 변(edge)라 한다
이런 표현 방식이 그래프이다
페이스북은 친구면 둘 다 서로에게 친구다 -> 변에 방향성이 없다 -> Undirected graph
트위터나 인스타는 친구 관계 개념이 아니라 한명이 한명을 팔로우 하는거다 -> 변에 방향성이 있다 -> directed graph
이렇게 페북 트위터 인스타는 친구나 팔로우 관계에 정도나 거리 개념이 없다 더 친한 친구나 좀 덜친한 친구를 구현하지 않는다
-> 변 길이에 차이가 없다 -> unweighted graph
그럼 각각의 vertex 를 도시라고 생각해보고 그 도시들을 서로 잇는 edge의 크기를 weight라고 하자(거리)
-> 정점 사이의 거리가 존재 -> weighted graph
지하철 최단 경로 구할 때 weighted graph를 쓰는 것이 맞지만 일단 비교적 간단한 BFS 알고리즘을 사용하기 위해 모든 역 사이의
거리가 같다고 가정하고 unweighted graph를 쓰도록 하자
"""

"""
BFS 알고리즘을 구현하기 위해서는 'queue'라는 것을 사용해야 합니다.

Queue는 직역을 하면 '(무엇을 기다리는 사람, 자동차 등의) 줄', 또는 '대기 행렬'입니다.

컴퓨터 프로그래밍에서 queue는 리스트처럼 여러 값을 보관하는데요. Queue에 값을 추가하면 순서대로 대기를 하고, queue에서 
값을 빼면 들어간 순서대로 나오게 됩니다.

deque
파이썬에서 queue를 사용하기 위해서는 'deque (double-ended queue)'라는 것을 사용해야 하는데요. 예시를 통해 알아보겠습니다.

from collections import deque

# 새로운 queue 생성
numbers = deque()

# queue에 값 추가
numbers.append(2)
numbers.append(3)
numbers.append(5)
numbers.append(7)

print(numbers)
print(len(numbers))

# queue에서 하나 제거
x = numbers.popleft()
print(x)
print(numbers)
print(len(numbers))

# queue에서 하나 제거
x = numbers.popleft()
print(x)
print(numbers)
print(len(numbers))

###결과
deque([2, 3, 5, 7])
4
2
deque([3, 5, 7])
3
3
deque([5, 7])
2
"""

#지하철 최단 경로 찾기 BFS

class Station:
    def __init__(self, name):
        self.name = name

    def add_connection(self, another_station):
        self.neighbors.append(another_station.name)
        another_station.neighbors.append(self.name)

stations = {}
in_file = open('stations.txt')
round_trip = in_file.strip().split(" - ")

for station in round_trip:
    stations[station] = Station(station)


"""
Station 클래스
init 메소드
파라미터로 받은 name을 인스턴스 변수 name에 지정해주고, neighbors는 일단 빈 리스트로 설정해줍니다.

def __init__(self, name):
    self.name = name
    self.neighbors = []
add_connection 메소드
def add_connection(self, another_station):
    self.neighbors.append(another_station)
    another_station.neighbors.append(self)
파일 읽기
각 줄에 각 호선이 정리되어 있고, 각 역은 "-"으로 나누어져 있습니다. split을 이용해서 사용할 수 있는 형태로 바꿔줍니다.

또, 역들을 연결하기 위해 가장 최근 본 역을 previous_station에 보관합니다.

# 파일 읽기
stations = {}
in_file = open('stations.txt')

for line in in_file:
    previous_station = None
    data = line.strip().split("-")
그리고 각 역을 보고, 이미 봤던 역이면 stations 사전에서 찾아 쓰고, 새로 보는 역이면 새로운 Station 인스턴스를 만들어서 stations 사전에 추가합니다.

그리고 previous_station과 current_station을 연결해주면 되겠죠?

for line in in_file:
    previous_station = None
    data = line.strip().split("-")

    for name in data:
        station_name = name.strip()
        if station_name not in stations.keys():
            current_station = Station(station_name)
            stations[station_name] = current_station
        else:
            current_station = stations[station_name]

        if previous_station != None:
            current_station.add_connection(previous_station)

        previous_station = current_station

in_file.close()
BFS 알고리즘
Pseudocode를 파이썬 코드로 변형시켜보겠습니다.

def bfs(start, goal):
    # 변수 정의
    previous = {}
    queue = deque()
    current = None

    # 초기 설정
    previous[start] = None
    queue.append(start)

    # 탐색
    while len(queue) > 0 and current != goal:
        current = queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in previous.keys():
                queue.append(neighbor)
                previous[neighbor] = current

    # 길이 있으면 경로를 만들어서 리턴
    if current == goal:
        path = [goal]
        x = goal

        while previous[x] != None:
            x = previous[x]
            path.append(x)

        return path

    # 길이 없으면 None 리턴
    return None
    
    모범 답안
from collections import deque

# 지하철역 클래스
class Station:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_connection(self, another_station):
        self.neighbors.append(another_station)
        another_station.neighbors.append(self)


# Breadth-First Search 알고리즘
def bfs(start, goal):
    # 변수 정의
    previous = {}
    queue = deque()
    current = None

    # 초기 설정
    previous[start] = None
    queue.append(start)

    # 탐색
    while len(queue) > 0 and current != goal:
        current = queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in previous.keys():
                queue.append(neighbor)
                previous[neighbor] = current

    # 길이 있으면 경로를 만들어서 리턴
    if current == goal:
        path = [goal]
        x = goal

        while previous[x] != None:
            x = previous[x]
            path.append(x)

        return path

    # 길이 없으면 None 리턴
    return None


# 파일 읽기
stations = {}
in_file = open('stations.txt')

for line in in_file:
    previous_station = None
    data = line.strip().split("-")

    for name in data:
        station_name = name.strip()
        if station_name not in stations.keys():
            current_station = Station(station_name)
            stations[station_name] = current_station
        else:
            current_station = stations[station_name]

        if previous_station != None:
            current_station.add_connection(previous_station)

        previous_station = current_station

in_file.close()


# 테스트
start_name = "이태원"
goal_name = "잠원"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
for station in path:
    print(station.name)

"""

"""
안녕하세요, 종종 encoding 문제에 관해 질문을 해주시는 분들이 계십니다. 저도 처음에 python 을 배울 때 많이 고민했던 부분이기도 하고 다른 분들도 한번쯤 궁금해 하셨을 것 같아서 제가 이해한 바를 적어보려 합니다.

더 깊게 들어가면 너무 복잡해지기 때문에 기본적인 이해를 위한 내용들만 서술했습니다. 정확한 전달과 쉬운 표현을 위해 최대한 노력했지만, 일부 표현이 잘못되었거나 틀린 내용이 있을 수도 있습니다. 계속 수정에 수정을 거듭했지만 공개 시일이 늦춰지는 것 같아서 먼저 올려봅니다. 추후 일부 내용이 수정될 수도 있음을 참고해주시기 바랍니다. 혹시 잘못된 표현은 피드백 주시면 확인 후 수정하도록 하겠습니다.

글자를 표현하는 방식
컴퓨터에서 문자를 표현하기 위해 사람들은 문자를 표현할 수 있는 집합을 만들었습니다. 초기에 쓰던 것이 미국에서 정한 ASCII 라는 것 입니다.

ASCII는 7비트(비트: 데이터의 크기를 나타내는 단위)를 이용하게 되는데 1비트는 0, 1 두가지 경우의 수를 표현할 수 있습니다. 그러므로 2의 7승, 즉 128개의 문자를 표현할 수 있습니다.

영어권 문화의 사람들은 불편함이 없었습니다. 하지만 스페인, 독일 등 영어보다 더 많은 글자 표현이 필요한 나라의 사람들은 ASCII 로 만족할 수 없었습니다. 그래서 8비트를 사용하는 별도의 집합(character set) 을 만들게 되었습니다.

그래도 불편을 겪는 사람들이 있었으니 바로 아시아 문화권의 사람들입니다. 한글, 일어, 한자 등이 이 8비트로도 다 표현을 할 수 없었던 것입니다. 그리하여 16비트를 활용한 character set을 만들게 되었습니다. 종종 에러가 날 때 볼 수 있는 cp949도 그 중 하나입니다.(cp949는 MS 사의 한글 인코딩 방식입니다. 리눅스나 mac 은 utf-8 이 기본 인코딩 방식입니다.)

그.러.나

이제는 다 해결된 줄 알았는데, 문제가 있었습니다. 서로 다른 character set을 쓰다보니, 호환이 되지 않았습니다. 그래서 각 언어마다 다른 character set을 쓸게 아니라 하나의 문자코드로 쓰기 위해 탄생된 것이 유니코드 라는 것입니다. 유니코드도 2바이트로 모든 문자를 표현했는데, 언어라는게 계속 추가되다보니 또 다시 2비트로 부족한 경우가 생겼습니다. 끝이 없네요.ㅎㅎ

이 문제들을 해결하기 위해 UTF-8, UTF-16과 같이 인코딩하는 방식을 정의하였습니다. 그럼 인코딩이란 무엇일까요?

인코딩(부호화)
간단하게 말하면 문자를 숫자로 바꾸는 방법입니다.

character = "한"
utf8_encoded_word = character.encode('utf-8')    # b'\xed\x95\x9c' 
한글이란 문자를 utf-8 방식으로 인코딩을 하였습니다. 유니코드(문자)를 utf-8 방식으로 인코딩하면 bytes 타입이 됩니다.

b' 는 bytes 리터럴이라고 하는데 이렇게 b'가 있으면 bytes 객체라고 생각하시면 됩니다. 뒤에 쓰여있는 \x는 이스케이프 문자로 뒤에 오는 수가 16진수라는 것을 의미합니다. 그래서 0xed, 0x95, 0x9c, 이렇게 총 3바이트의 16진수로 변환이 됩니다( 링크 ). (e.g. 링크 에서 ctrl+F 를 통해 '한'을 쳐보시면 유니코드표와 ed, 95, 9c가 쓰여있는 걸 보실 수 있을 것입니다.)

디코딩(복호화)
그럼 디코딩은 무엇일까요? 아까 유니코드를 bytes 로 변환하였으니 bytes 를 유니코드 방식으로 변환하는 것을 디코딩이라고 합니다.

utf8_decoded_word = utf8_encoded_word.decode('utf-8')    # 한
유의하실 점은 인코딩을 한 방식과 같은 방식으로 디코딩을 해야합니다. 그렇지 않으면 흔히 볼 수 있는 UnicodeDecodeError 가 발생하는 것입니다.

cp949_decded_Word = utf8_encoded_word.decode('cp949')

# UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 0: illegal multibyte sequence
Error 는 그럼 왜 발생하나요?
결국 오류는 encoding 방식과 decoding 방식이 일치하지 않기 때문에 생깁니다. 이번엔 UnicodeEncodeError를 살펴보겠습니다. 특히 pycharm 쓰시는 분들이 자주 보실 것입니다.

import locale

print(locale.getpreferredencoding())    # US-ASCII

file = open("test.txt", "w")
print(file)    # <_io.TextIOWrapper name='test.txt' mode='w' encoding='US-ASCII'>

while True:
    data = input("입력하세요: ")
    file.write(data)
    break
file.close()
파일을 열 때 encoding 인자를 쓰지 않는다면 locale.getpreferredencoding() 에 의해 기본 값이 설정됩니다. 제 mac os에서 파이참으로 실행시 기본값이 us-ascii 네요. 그래서 터미널에서도 한번 실행해봤습니다. 그런데 터미널은 utf-8 이 나옵니다 ㅎㅎ

python 공식문서에서는 locale.getpreferredencoding() 에 대해 아래와 같이 설명하고 있습니다.

Return the encoding used for text data, according to user preferences. User preferences are expressed differently on different systems, and might not be available programmatically on some systems, so this function only returns a guess.

사용자 환경 설정에 따라 텍스트 데이타에 사용되는 인코딩 방식을 반환하는 함수네요. 끝에 이 반환값을 완전히 신뢰하지 말라고는 써있긴 하지만, 어쨋든 지금 pycharm에서는 ascii 로 인코딩 된 건 확실해보입니다.

많이 아시다시피 인자로 encoding="utf-8" 을 포함해주면 해결되지만, 사실 open 을 여러번해야 한다면 매번 쓰는 것도 여간 귀찮은 일이 아닐 것입니다. fluent python 이라는 책에 의하면 기본 인코딩 방식에 의존하지 말라고는 되어 있습니다. 실제 프로젝트를 수행할 때는 차치하고 적어도 코드잇 과제할 때 만이라도 번거로움을 피하기 위해 pycharm 을 쓰시는 분은 다음과 같이 해보시기 바랍니다.

해결방법
pycharm 메뉴에서 File - Preferences로 이동 후 Tools를 검색하시고 Terminal로 이동합니다.

아래 이미지와 같이 LC_CTYPE에 ko_KR.UTF-8 을 입력해주시고 OK를 클릭합니다.

Apply 클릭을 하시면 다음부터는 encoding="utf-8" 을 쓰지 않으셔도 될 것입니다.
"""