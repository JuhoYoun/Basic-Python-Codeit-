#정렬
#유명한 정렬 알고리즘으로는 bubble sort, insertion sort, selection sort, bucket sort, heapsort, quicksort, merge sort가 있다

#Selection sort
#list1의 처음부터 끝 인덱스 까지들 중 최소값 찾는다 -> 0번과 바꾼다  -> 두번째 인덱스 부터 끝까지 중 최소 찾는다 -> 두번째와 바꾼다 -> ....
#선택 정렬 알고리즘을 구현해보세요. selection_sort 함수는 파라미터로 리스트 my_list를 받고, my_list 자체를 정렬 시켜줍니다.
#즉, selection_sort는 새로운 리스트를 만들어서 리턴해주는 것이 아니고, 파라미터로 넘어온 리스트를 변형시켜주는 것입니다
print("Hooray!")

"""
list1 = [1, 2, 3, 4, 5]

for number in list1:
    if number > 3:
        number = 3
print(list1)

결과는 [1, 2, 3, 4, 5] -> number는 그냥 인덱스에 들어있는 그 값 자체구나 
"""
"""
list1 = [1, 2, 3, 4, 5]

copy = list1[2:]
copy[0] = 10

print(list1)

결과는 [1, 2, 3, 4, 5] -> 이 경우는 copy가 list1의 주소를 받는게 아니고 메모리가 생성되는듯??
"""
# 선택 정렬
def selection_sort(my_list):
    # 코드를 입력하세요.
    for i in range(len(my_list)):
        least_value = my_list[i]
        index_to_swap = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < least_value:
                least_value = my_list[j]
                index_to_swap = j
        temp = my_list[i]
        my_list[i] = least_value
        my_list[index_to_swap] = temp


some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)

#선생놈 답
# 선택 정렬
def selection_sort(my_list):
    # 바깥쪽 반복문
    for i in range(len(my_list)):
        min_index = i

        # 안쪽 반복문
        for j in range(i + 1, len(my_list)):
            value = my_list[j]
            if value < my_list[min_index]:
                min_index = j

        # 자리 바꾸기
        temp = my_list[i]
        my_list[i] = my_list[min_index]
        my_list[min_index] = temp

# 테스트
some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)

#내껄 좀 더 간단히 만들어보겠다
# 선택 정렬
def selection_sort(my_list):
    # 코드를 입력하세요.
    for i in range(len(my_list)):
        smallest_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[smallest_index]:
                smallest_index = j
        temp = my_list[i]
        my_list[i] = my_list[smallest_index]
        my_list[smallest_index] = temp

some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)
#goooooooood

#Insertion sort
#선택 정렬은 0번 인덱스부터 시작해서 하나씩 각 자리에 들어갈 값들을 찾아주는 알고리즘
#삽입 정렬은 0번 인덱스부터 시작해서 하나씩 각 값의 자리를 찾아주는 알고리즘
#My code
# 삽입 정렬
def insertion_sort(my_list):
    # 코드를 입력하세요.
    for i in range(1, len(my_list)):
        for j in range(0, i):
            if my_list[i - j] < my_list[i - j - 1]:
                temp = my_list[i - j - 1]
                my_list[i - j - 1] = my_list[i - j]
                my_list[i - j] = temp
            else:
                break

some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort(some_list)
print(some_list)
###### 선생놈이랑 너무 다르다 ㅋㅋㅋㅋㅋ 그 전에 이게 인썰션이 맞나????

"""
힌트 1: 삽입 정렬에서의 자리 찾기
'삽입 정렬'에서는 0번 인덱스에 있는 값이 들어갈 자리를 찾고, 1번 인덱스에 있는 값이 들어갈 자리를 찾고, 2번 인덱스에 있는 
값이 들어갈 자리를 찾고... 이런 식으로 각 값이 들어갈 자리를 찾아서 정렬을 해야 합니다.

현재 자리를 찾아야 하는 값을 key라고 부릅시다. 일단 반복문을 쓰면:

for i in range(len(some_list)):
    key = some_list[i]
매번 반복문의 수행 부분에 들어갈 때 이 두 가지를 생각하고 있어야 합니다:

my_list[:i](0번 인덱스부터 i - 1번 인덱스까지)는 정렬되어 있다.
key를 my_list[:i]에서 들어갈 수 있는 자리에 삽입해야 한다.

자리 찾기
my_list[:i]는 이미 정렬되어 있기 때문에 my_list[:i]에서 i - 1번 인덱스의 값이 가장 큰 값입니다. i - 1번 인덱스에 있는 
값이 key보다 작거나 같으면 key는 이미 올바른 자리에 있기 때문에 그냥 두면 됩니다.

만약 i - 1번 인덱스에 있는 값이 key보다 크면 key보다 오른쪽으로 가야하기 때문에 key가 있던 자리에 넣어줍니다. 그리고 이제 
똑같이 key를 i - 2번에 있는 값과 비교해서 key가 더 크면 그냥 두고, 아니면 i - 2번 값을 key의 자리에 넣어줍니다.

이런식으로 key가 큰 경우가 생기면 바로 끝낼 수 있고, 아니면 0번에 있는 값을 확인할 때까지 반복해야 합니다.

# i - 1부터 시작해서 왼쪽으로 하나씩 확인
# 왼쪽 끝까지(0번 인덱스) 다 봤거나
# key가 들어갈 자리를 찾으면 끝냄
j = i - 1
while j >= 0 and my_list[j] > key:
    my_list[j + 1] = my_list[j]
    j = j - 1

# key가 들어갈 자리에 삽입
# 왼쪽 끝까지 가서 j가 -1이면 0번 인덱스에 key를 삽입
my_list[j + 1] = key
"""

#선생놈
# 삽입 정렬
def insertion_sort(my_list):
    for i in range(len(my_list)):
        key = my_list[i]

        # i - 1부터 시작해서 왼쪽으로 하나씩 확인
        # 왼쪽 끝까지(0번 인덱스) 다 봤거나
        # key가 들어갈 자리를 찾으면 끝냄
        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j = j - 1

        # key가 들어갈 자리에 삽입
        # 왼쪽 끝까지 가서 j가 -1이면 0번 인덱스에 key를 삽입
        my_list[j + 1] = key

some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort(some_list)
print(some_list)

##Merge sort
#합병 정렬은 재귀함수가 들어간다
#선택이나 삽입보다 어렵지만 효율적
#재귀적 용법의 대표적 예인 분할정복 알고리즘 (Divide and Conquer)
# 분할 정복 -> 문제를 같은 형태의 작은 문제로 분할해서 풀고, 작은 문제들의 결과들을 합쳐서
#본 문제의 답을 찾는 방식

"""
    while i < len(list1):
        while j < len(list2):
            if list1[i] >= list2[j]:
                list_sum[i + j] = list2[j]
                j += 1
                break
            else:
                list_sum[i + j] = list1[i]
                i += 1
                break
이럴 경우 자꾸 IndexError: list assignment index out of range 라고 에러뜬다 왜 그럴까?
list_sum은 초반에 빈 리스트이기 때문에 그런가 보다 append 메소드를 써야할듯하다 

# 두 리스트 합치기
def merge(list1, list2):
    # 코드를 입력하세요.
    i = 0
    j = 0
    list_sum = []
    while i < len(list1):
        while j < len(list2):
            if list1[i] >= list2[j]:
                list_sum.append(list2[j])
                j += 1
                break
            else:
                list_sum.append(list1[i])
                i += 1
                break
    return list_sum

list1 = [1, 2, 4, 7, 9]
list2 = [3, 5, 6, 8, 10]

print(merge(list1, list2))

이렇게 고쳐도 문제가 생긴다
[1, 2, 3, 4, 5, 6, 7, 8, 9]
두 리스트 중 먼저 하나가 먼저 끝나버리면 남은 다른 하나의 남은 엘리먼드들을 저장하지 않는다
"""
#합병 정렬 마이 코드
# 두 리스트 합치기
def merge(list1, list2):
    # 코드를 입력하세요.
    i = 0
    j = 0
    list_sum = []
    while  i < len(list1) and j < len(list2):
        if list1[i] >= list2[j]:
            list_sum.append(list2[j])
            j += 1
        else:
            list_sum.append(list1[i])
            i += 1
    if i == len(list1):
        list_sum = list_sum + list2[j:]
    else:
        list_sum = list_sum + list1[i:]
    return list_sum

def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) == 0 or len(my_list) == 1:
        return my_list

    return merge(merge_sort(my_list[:len(my_list) // 2]), merge_sort(my_list[len(my_list) // 2:]))

list1 = [1, 2, 4, 7, 9]
list2 = [3, 5, 6, 8, 10]

print(merge(list1, list2))

my_list = [3, 5, 1, 2, 10, 7, 9, 8, 4, 6]

print(merge_sort(my_list))

##선생놈 코드
# 두 리스트 합치기
def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0

    # 정렬되어 있는 list1과 list2의 원소들을 차례로 비교하여, 더 작은 원소를 merged_list에 추가하기
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # list1에 남은 원소가 있다면, merged_list에 추가하기
    if i < len(list1):
        while i < len(list1):
            merged_list.append(list1[i])
            i += 1

    # list2에 남은 원소가 있다면, merged_list에 추가하기
    if j < len(list2):
        while j < len(list2):
            merged_list.append(list2[j])
            j += 1

    return merged_list

# 합병 정렬
def merge_sort(my_list):
    # Base Case
    if len(my_list) <= 1:
        return my_list

    # Recursive Case: left와 right로 my_list를 나누어준다.
    left = my_list[:len(my_list) // 2]
    right = my_list[len(my_list) // 2:]

    # Recursive Case: my_list를 잘게 쪼개는 과정을 재귀적으로 반복하고, merge 함수를 사용하여 합쳐준다.
    return merge(merge_sort(left), merge_sort(right))

some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)