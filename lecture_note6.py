#파일 읽기
#열흘간의 매출이 나와 있는 chicken.txt라는 파일이 있습니다.
#이 파일을 읽기 위해서는 open 내장 함수를 쓰면 됩니다. open에는 첫번째 파라미터로 파일 이름을 넘겨주고, 두번째 파라미터로 파일을
#읽는다는 의미에서 'read'의 약자인 문자열 'r'을 넘겨줍니다. 나중에 파일을 쓸때는 'write'의 약자인 문자열 'w'를 넘겨주는 것을
# 보실 수 있습니다. 이것을 in_file이라는 변수에 저장해둡니다.
#in_file = open('chicken.txt', 'r') -> 인강에서 이렇게 하러그러는데 에러 뜬다!!
in_file = open('chicken.txt', 'r',  encoding='UTF-8') # encoding='UTF-8' 이건 뭐지?????? 왜 이걸해야할까

#이제 이 파일을 한줄씩 읽어봅시다. in_file의 type을 출력해보면 <class '_io.TextIOWrapper'>라고 나오지만, for문에 쓰면
# in_file을 마치 문자열 리스트(list of strings)처럼 다룰 수 있습니다.
for line in in_file:
    print(line)
#for문의 수행부분에 처음 들어갈때는 line이 chicken.txt의 첫번째 줄, 그 다음 들어갈때는 line이 chicken.txt의 두번째 줄...
# 이런식으로 line이 파일의 각 줄을 문자열로 받고, 파일을 다 읽었을때 for문은 끝납니다.

#파일을 다 읽었으면 파일을 닫아주는 것이 좋습니다. 파일을 열면 프로그램이 실행되는 동안 메모리를 차지하고 있는데,
# close 메소드를 쓰면 메모리를 해방시켜줄 수 있습니다.
in_file.close()

#strip 메소드는 문자열의 가장 앞쪽과 뒤쪽에 있는 화이트 스페이스(white space)가 제거된 새로운 문자열을 리턴해줍니다.
print("    Hello world!     ".strip()) #strip은 데이터 분석에 자주 쓰인다

#중간에 있는 화이트 스페이스를 지우려면?
word = "파이썬     재밌어효"
new_word  = word.replace(" ", "") #화이트 스페이스를 전부 empty로 바꿔준다
print(new_word)    # 파이썬재밌어효

"""
만약 chicken.txt 값들을 for loop로 한 줄 한 줄 출력 하면

1일 : 1000

2일 : 123123

이런식으로 줄 사이에 스페이스가 있을것이다 그런 이유는 텍스트에서 한줄이 사실은 1일 : 1000\n으로 되 있기 때문이다
뒤에 한 줄 넘기기가 있는데 for loop로 한줄 씩 프린트할 때도 자연히 한줄 넘기기가 되어 두줄 넘겨지게 된다 
이것이 싫으면 strip을 사용하면 된다
"""

#split 메소드는 파라미터로 넘겨주는 값을 기준으로 문자열을 분리시키고, 분리된 값들이 정리되어 있는 리스트를 리턴해줍니다.
# 이렇게 말해서는 이해가 잘 안 가니까 예제를 봅시다.
print("1. 2. 3. 4. 5. 6".split("."))
#이렇게 하면 "1. 2. 3. 4. 5. 6"을 "." 기준으로 분리를 시켜서 리스트를 생성합니다.
#그런데 인덱스 1의 값부터는 숫자 앞에 띄어쓰기가 하나씩 있습니다. 기존의 문자열을 보면 두 숫자 사이에는 점과 띄어쓰기(". ")가 모두
# 있기 때문이죠. 문제를 고치기 위해서는 파라미터를 "." 대신 ". "를 넘겨주면 됩니다.
print("1. 2. 3. 4. 5. 6".split(". "))
#리스트가 됬으니 인덱싱가능
numbers = "1. 2. 3. 4. 5. 6".split(". ")
print(numbers[0] + numbers[1]) #여기서 리스트가 된 문자열은 str이므로 주의하자
#사실 split메소드의 파라미터는 옵셔널 파라미터입니다. 아무 값도 넘겨주지 않았을 경우 기본값으로 ""가 넘어가게 됩니다.
# 그러면 공백(화이트 스페이스)을 기준으로 문자열을 나누게 되는거죠.
print("1 2 3 4 5 6".split())
#전에도 얘기를 했지만 화이트 스페이스는 띄어쓰기 뿐만 아니라 탭과 엔터를 모두 포함합니다.
print("   \n   1 \t\n     2     \t\t\n\n   3       4   5 \n 6  \t".split())

#practice 장부에서 평균 매출 계산
# 매출 파일 열기
# 파일 경로는 "data/chicken.txt" 입니다.
in_file = open('data/chicken.txt', 'r', encoding = 'UTF-8')

sum = 0
day = 0

for line in in_file:
    account_book = line.strip().split(": ")
    sum += int(account_book[1])
    day += 1  #한달에 날수가 매달 다르므로 이렇게 한다 만약 31로 나누면 그건 하드코딩이라 부른다 특정 경우에만 먹힌다는 것이다

print(sum / day)
in_file.close()
"""
#파일 쓰기
out_file = open('new_file.txt', 'w') #이거 또 안되는구만...

out_file.write("Hello world!\n") #\n 안하고 쓰면 줄 띄어쓰기 안되고 다음에 바로 붙어서 쓰여진다
out_file.write("My name is Codeit!")

out_file.close()

#단어장 내 코드
out_file = open('vocabulary.txt', 'w', encoding='UTF-8')
temp = ""
keep_or_quit = 'k'

while keep_or_quit == 'k':
    temp = input("영어 단어를 입력하세요: ")
    if temp == 'q':
        keep_or_quit = 'q'
        continue
    out_file.write(temp)
    temp = input("한국어 뜻을 입력하세요: ")
    out_file.write(": %s\n" % (temp))

out_file.close()

#단어장 선생 코드
out_file = open('vocabulary.txt', 'w')

while True:
    english_word = input("영어 단어를 입력하세요: ")
    
    if english_word == 'q':
        break
    
    korean_word = input("한국어 뜻을 입력하세요: ")
    
    if korean_word == 'q':
        break
    
    out_file.write("%s: %s\n" % (english_word, korean_word))

out_file.close()

#단어 퀴즈
in_file = open('vocabulary.txt', 'r')

for line in in_file:
    data = line.strip().split(": ")
    if input("%s: " % (data[1])) == data[0]:
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 %s입니다." % (data[0]))

in_file.close()

#선생쓰
in_file = open('vocabulary.txt', 'r')

for line in in_file:
    data = line.strip().split(": ")
    english_word = data[0] 
    korean_word = data[1]
    if input("%s: " % (korean_word) == english_word:
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 %s입니다." % (english_word))

in_file.close()
"""
#dictionary
#사전(dictionary)은 순서가 없는 key-value 쌍의 집합입니다.
dict1 = {}
print(type(dict1))

dict1[5] = 25
dict1[2] = 4
dict1[3] = 9

print(dict1)
#보시다시피 dict1에는 key가 2고 value가 4인 쌍, key가 3이고 value가 9인 쌍, 그리고 key가 5고 value가 25인 쌍이 생겼습니다.
#value를 받아오기 위해서 리스트 인덱싱을 하듯이 key를 대괄호 안에 넣어주면 됩니다.
print(dict1[5])
print(dict1[2])
#그럼 key가 정수형인 사전과 그냥 리스트의 차이점은 뭘까요? 리스트는 인덱스 0부터 시작하고 순서대로 채워지지만 사전은 순서가
# 없기때문에 0부터 시작하지 않고 아무 값들을 쓸 수 있습니다.

#사전이 리스트와 가장 다른 점은 key가 정수뿐만 아니라 아무 자료형이나 될 수 있다는 것입니다.
family = {}
family['mom'] = 'grace'
family['dad'] = 'chris'
family['son'] = 'young'
family['daughter'] = 'kay'

print(family['dad'])
print(family['daughter'])

#정수 문자열 믹스 될까?
mix = {}

mix[1] = 'mom'
mix['dad'] = 3
print(mix) #된다

#dictionary 안에 list도 들어갈까?
list_in_dict ={}
list_in_dict[0] = ['cofee', 'donut']
list_in_dict[1] = ['chicken', 'beer']
print(list_in_dict)#성공!

family = {}
family['mom'] = 'grace'
family['dad'] = 'chris'
family['son'] = 'young'
family['daughter'] = 'kay'
#여기서 key들만 모두 받으려면 keys 메소드를 쓰면 됩니다.
print(family.keys())
#family에 어떤 key가 있는지 확인하려면 이렇게 하면 됩니다:
print('son' in family.keys())
print('uncle' in family.keys())

#그리고 family의 key들을 리스트로 쓰고 싶으면 list 함수로 형 변환을 하면 됩니다.
family_keys = list(family.keys())
print(family_keys)
print(type(family_keys))

#value들을 모두 받기 위해서 values 메소드를 쓰면 됩니다.
print(family.values())
#family에 어떤 value가 있는지 확인하려면 이렇게 하면 됩니다:
print('grace' in family.values())
print('yoonsoo' in family.values())
#그리고 family의 value들을 리스트로 쓰고 싶으면 list 함수로 형 변환을 하면 됩니다.
family_values = list(family.values())
print(family_values)
print(type(family_values))

#고급 단어장 -> 파일안에 있는 단어들의 한국 뜻을 랜덤으로 물어보고 답하게 한다 
from random import randint

out_file = open('vocabulary.txt', 'w')
word_dict = {}
index = 0
keep_or_quit = 'k'

for line in out_file:
    word_dict[index] = line.strip().split(': ')
    index += 1

while keep_or_quit == 'k':
    data = word_dict(randint(0, index))
    answer = input('%s: ' % (data[1]))
    if answer == 'q':
        keep_or_quit = 'q'
    elif answer == data[0]:
        print("맞았습니다!")
    else:
        print("틀렸습니다. 정답은 %s입니다." % (data[0]))
out_file.close()

#고쳐봤다!
from random import randint

out_file = open('vocabulary.txt', 'w')
word_dict = {}
keep_or_quit = 'k'

for line in out_file:
    data = line.strip().split(': ')
    english_word = data[0]
    korean_word = data[1]
    word_dict[korean_word] = english_word

keys = list(word_dict.keys())

while keep_or_quit == 'k':
    korean_word = keys(randint(0, len(keys) - 1))
    english_word = word_dict[korean_word]
    answer = input('%s: ' % (korean_word))
    if answer == 'q':
        keep_or_quit = 'q'
    elif answer == english_word:
        print("맞았습니다!")
    else:
        print("틀렸습니다. 정답은 %s입니다." % (english_word))
out_file.close()

"""
루프 부분 선생 코드

while True:
    index = randint(0, len(keys) - 1)
    korean_word = keys(index)
    english_word = word_dict[korean_word]
    answer = input('%s: ' % (korean_word))
    if answer == 'q':
        break
    elif answer == english_word:
        print("맞았습니다!")
    else:
        print("틀렸습니다. 정답은 %s입니다." % (english_word))
"""
"""
코멘트 부분 # 이거를 어떻게 갑자기 풀어주신거에요 어떤키를 사용하신건가요?
Crtl + / 입니다
"""