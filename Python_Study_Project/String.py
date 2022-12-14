print("---------------------문자열------------------------------")

enter = "\n"
print("Index\n")
"""
1. Line 10 ~ 89    -> 파이썬에서 문자열을 표현하는 방법

2. Line 94 ~ 157   -> 여러 줄인 문자열을 변수에 대입하고 싶을 때 (\n, \t... etc)

3. Line 160 ~ 236  -> 문자열 연산하기 (문자열 더하기, 곱하기, 길이 구하기, 인덱싱과 슬라이싱)

4. Line 240 ~ 424  -> 문자열 인덱싱과 슬라이싱 

5. Line 429 ~ 441  -> 문자열 안의 문자를 바꿔보기

6. Line 447 ~ 937  ->  문자열 포매팅 (포맷 코드, 각종 포맷팅)

7. Line 945 ~ 1086 -> 문자열 관련 함수 (내장 함수)
"""

"""
파이썬에서 문자열을 표현하는 방법은 총 4가지가 있다.
There are 4 ways to express String in Python.

1. 큰따옴표로(")로 양쪽 둘러싸기 Double Quotation 

2. 작은따옴표(')로 양쪽 둘러사기 Single Quotation

3. 큰따옴표 3개를 연속으로("*3) 써서 양쪽 둘러싸기 Putting Double Quotations 3 times

4. 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기 Putting Single Quotations 3 times
"""

#Example

print("\n1. Hello World")

print('\n2. Python is fun for now')

print("""\n3. Life is too short, You need Python""")

print('''\n4. My favorite food is mopo tofu''')


#As you can see the result, you can use 4 ways to print the sentences using quotations.
#Reason why:
"""
1. 문자열에 작은따옴표(') 포함시키기 Include Single Quotation in String

ex) Python's favorite food is perl -> 문장 안에 작은 따옴표를 넣고 싶으면 문자열을 큰 따옴표로 둘러싸야한다. If you want to put single quotation in a sentence, you need to use Double Quotation in String.
 
Error occurs if:

food = 'Python's favorite food is perl'
Output -> File "<stdin>", Line 1
            food = Python's favorite food is perl'
                                   ^
          SyntaxError: invalid syntax

2. 문자열에 큰따옴표(") 포함시키기 Include Double Quotation in String

ex) Python is very easy." he says.

위와 같이 큰따옴표(")가 포함된 문자열이라면 문자열을 작은 따옴표(')로 둘러싸면 된다. To include Double Quotation in a sentence, You need to put single quotation in String


3. 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기 Use BackSlash(\) to Include Single and Double Quotation in String and a sentence

작은따옴표(')나 큰따옴표(")를 문자열에 포함시키는 또 다른 방법은 백슬래시(\)를 이용하는 것이다. 백슬래시를 사용하면 백슬래시 뒤의 작은따옴표나 큰따옴표는 문자열을 둘러싸는
기호의 의미가 아니라 문자 ('), (") 그 자체를 뜻하게 된다.


"""
print("\n1111111111111111111111111111111111111111111111111111111111111\n")

#Example for #1

food = "Python's favorite food is perl"

print("\n1.", food)

print("\n222222222222222222222222222222222222222222222222222222222\n")

#Example for #2

say = '"Python is very easy." he says.'

print("\n2.", say)

print("\n3333333333333333333333333333333333333333333333333333333333333\n")

#Example for #3

food = 'Python\'s favorite food is perl'

say = "\"Python is very easy.\" he says."

print("\n3.", food)
print("\n3.", say)

print("--------------------------------------------------------------------------------------------------------------------")

"""
여러 줄인 문자열을 변수에 대입하고 싶을 때:
문자열이 항상 한 줄짜리만 있는 것은 아니다. 다음과 같이 여러줄의 문자열을 변수에 대입하려면 어떻게 처리해야할까?

Expected Output:
Life is too short
You need Python


1. 줄을 바꾸는 Escape Code '\n' 삽입하기.

하지만, 이 방법을 사용할 때는 읽기에 불편하고 줄이 길어지는 단점이 있다.


2. 연속된 작은 따옴표 3개(''') 또는 큰 따옴표 3개("*3) 사용하기

1번의 단점을 극복하기 위해 파이썬에서는 다음과 같이 작은 따옴표 3개 또는 큰 따옴표 3개를 사용한다.
"""

print("\n1111111111111111111111111111111111111111111111111111111111111111111111111")

#Example for #1

multiline1 = "Life is too short\n   You need Python"

print("\n1.", multiline1)


print("\n222222222222222222222222222222222222222222222222222222222222222222222222222")

#Example for #2

multiline2_1 = '''
Life is too short
You need Python
'''

multiline2_2 = """
Life is too short
You need Python
"""

print("\n2.1", multiline2_1)
print("\n2.2", multiline2_2)

"""
Types of Escape Code


    Code                Explanation

1. \n                   문자열 안에서 줄을 바꿀 때 사용
2. \t                   문자열 사이에 탭 간격을 줄 때 사용
3. \\                   문자 \를 그대로 표현할 때 사용
4. \'                   작은 따옴표(')를 그대로 표현할 때 사용
5. \"                   큰 따옴표(")를 그대로 표현할 때 사용
6. \r                   캐리지 리턴(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
7. \f                   폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
8. \a                   벨 소리(출력할 때 PC 스피커에서 '삑'소리가 난다)
9. \b                   백스페이스
10.\000                 Null 문자


**이 중에서 활용 빈도가 높은 것은 \n, \t, \\, \', \"이다. 나머지는 프로그램에서 잘 사용하지 않는다.
"""

print("\n문자열 연산하기")

"""
문자열 연산하기

파이썬에서는 문자열을 더하거나 곱할 수 있다. 다른 언어에서는 쉽게 찾아볼 수 없는 재미있는 기능으로, 우리 생각을 그대로 반영해 주는 파이썬만의 장점이라고 할 수 있다.

1. 문자열 더해서 연결하기 (Concatenation)

2. 문자열 곱하기

Line 186 ~ 192번을 보면 코드에서 *의 의미는 우리가 일반적으로 아는 곱하기가 아니다.
아래의 코드에서 a * 2는 a를 두 번 반복하라는 뜻이다.
즉, *는 문자열의 반복을 뜻하는 의미로 사용되었다.

3. 문자열 곱하기 응용

print("-" * 50)

4. 문자열 길이 구하기
문자열의 길이는 "len" 함수(length)를 사용하면 구할 수 있다. len 함수는 print 함수처럼
파이썬의 기본 내장 함수로 별다른 설정 없이 사용이 가능하다.

5. 문자열 인덱싱과 슬라이싱

인덱싱(Indexing)이란 무엇인가를 '가리킨다'는 의미이고, 슬라이싱(Slicing)은 무엇인가를 '잘라낸다'는 의미이다. 
Do it!점프 투 파이썬 - 전면 개정판 51쪽 참고

Ex) L i f e   i s   t o o   s h o r t ,   Y o u   n e e d   P y t h o n
    0                   1                   2                   3 
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3
    
    "Life is too short, You need Python" 문자열에서 L은 첫 번째 자리를 뜻하는 숫자 0,
    바로 다음인 i는 1 이런 식으로 계속 번호를 붙인 것이다. 중간에 있는 short의 s는 12가 된다.
"""


print("11111111111111111111111111111111111111111111111111111111")
#Example for #1

head = "Python"
tail = " is fun!"

print("\n", head + tail)


print("222222222222222222222222222222222222222222222222222222222222\n")
#Example for #2

a = "python"

b = a * 2

print(b)

print("333333333333333333333333333333333333333333333333333333333333333\n")
#Example for #3

print("=" * 50)
print("My Program")
print("=" * 50)

print("\n444444444444444444444444444444444444444444444444444444444444444444444\n")

a = "Life is too scary"

print(a, "<- length:", len(a))

#중간 실습
#'You need python'문장을 만들고 길이를 구해보자.

print("중간 실습 문제 답안")

a = "\'You need python\'"

print(a, len(a))


"""
1.문자열 인덱싱과 슬라이싱

인덱싱(Indexing)이란 무엇인가를 '가리킨다'는 의미이고,
슬라이싱(slicing)은 무엇인가를 '잘라낸다'는 의미이다.

문자열 인덱싱:

L i f e   i s   t o o   s h o r t ,   Y o u   n e e d   P y t h o n
0                 1                     2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3

"Life is too short, You need Python" 문자열에서 L은 첫 번쨰 자리를 뜻하는 숫자 0,
바로 다음인 i는 1 이런 식으로 계속 번호를 붙인 것이다. 중간에 있는 short의 s는 12가 된다.

a = "Life is too short, You need Python"

만약 a[5]의 값을 원하면,
output은 "i"를 출력한다.





1.1 문자열 인덱싱 활용하기

a[번호]에는 음수도 사용 가능하다.

음수를 쓰면 문자열 뒤에서부터 출력한다.


print(a[-5]) -> 문자열 뒤에서 5번째 자리를 가리킨다.
print(a[-11]) -> 문자열 뒤에서 11번째 자리를 가리킨다.




1.2 문자열 슬라이싱

문자열 슬라이싱이란 우리가 a에 저장한 문자열에서 "Life"나 "You" 같은 단어를 뽑아낼 수 있다.

아래에 있는 Example #3처럼 해도 무관하지만 더 좋은 방법이있다.
바로
a[0:4]

위의 코드에서 뜻하는 것은 a 문자열, "Life is too short, You need Python" 문장에서
자리 번호 0부터 4까지의 문자를 뽑아낸다는 것이다.

문자열의 인덱스를 보았을 때, a[0]은 L, a[1]은 i, a[2]는 f, a[3]은 e 이므로
a[0:3]으로도 Life라는 단어를 뽑아낼 수 있을까?

결론은 할 수 없다. Output에 "Lif"로만 출력이 된다.

그러한 이유는 슬라이싱 기법으로 a[시작번호:끝 번호]를 지정할 때 끝 번호에 해당하는 것은
포함하지 않기 때문이다. a[0:3]을 수식으로 나타내면 다음과 같다.

0 <= a < 3 -> a는 0과 같거나 크지만 3보다는 작다.

따라서 a[0:3]을 만족하는 것은 a[0], a[1], a[2]이다.

그러므로 "Life"를 출력하고 싶으면 a[0:4]가 정답이다.


******문자열을 슬라이싱할 때 항상 시작 번호가 0일 필요는 없다.****
ex) a[0:2] -> Output: Li
    
    a[5:7] -> Output: is
    
    a[12:17] -> Output: short
    
    
a[시작 번호:끝 번호]에서 끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지 뽑아낸다. Example #5참고 (Line 344)


a[시작 번호: 끝 번호]에서 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다. Example #6 참고 (Line 351)


a[시작 번호: 끝 번호]에서 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지를 뽑아낸다. Example #7 참고 (Line 357)

슬라이싱에서도 인덱싱과 마찬가지로 음수(-)를 사용할 수 있다. Example 8 참고 (Line 366)
"""

#Example #1 인덱싱
print("\nExample #1 인덱싱")
a = "Life is too short, You need Python"

print(a[3])
print(a[12])
print(a[0], a[1], a[2], a[3], a[4])


#Example #2 인덱싱 음수 ver.
print("\nExample #2 인덱싱 음수")
print(a[-1])
print(a[-2])


#Example #3 슬라이싱(인덱스를 활용한) ver.

print("\nExample #3 슬라이싱")
b = a[0] + a[1] + a[2] + a[3]

print(b)

#Example #4 슬라이싱
print("\nExample #4 슬라이싱")
print("a에 저장한 문자열에서 \"Life\"를 출력하라.\n")
print("오답: ", a[0:3])
print("정답: ", a[0:4])

#Example #5 슬라이싱 활용 (시작번호, 끝번호)
print("\nExample #5")
print(a[19:])
#a[시작 번호: 끝 번호]에서 끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지 뽑아낸다.

#Example #6 슬라이싱 활용 (시작번호, 끝번호)
print("\nExample #6")
print(a[:17])
print(a[:13])
#a[시작 번호: 끝 번호]에서 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다.

#Example #7 슬라이싱 활용 (시작번호, 끝번호)

print("\nExample #7")
print(a[:])
#a[시작 번호: 끝 번호]에서 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지를 뽑아낸다.

#Example #8 슬라이싱 활용 (시작번호, 끝번호)

print("\nExample #8")
print(a[19:-7])
#위 소스코드에서 a[19:7]이 뜻하는 것은 a[19]에서부터 a[-8]까지를 말한다. 이 역시 a[-7]은 포함이 되지 않는다.

hyphen = "-"
lline = hyphen * 70 + "\n"
print(lline)

"""
1.3 슬라이싱으로 문자열 나누기

다음은 자주 사용하게 되는 슬라이싱 기법 중 하나이다.

a = "20010331Rainy"
date = a[:8]
weather = a[8:]

date OUTPUT -> 20010331
weather OUTPUT -> Rainy

위 예는 문자열 a를 두 부분으로 나누는 기법이다. 숫자 8을 기준으로 문자열 a를 양쪽으로 한 번씩 슬라이싱했다. 
숫자 8을 기준으로 문자열 a를 양쪽으로 한번씩 슬라이싱했다. a[:8]이 포함되지 않고, a[8]을 포함하기 때문에
8을 기준으로 해서 두 부분으로 나눌 수 있는 것이다. 

위 예는 "20010331Rainy"문자열을 날짜를 나타내는 부분인 "20010331"과 날씨를 나타내는 부분인 "Rainy"로 
나누는 방법을 보여준다.

위 문자열 "20010331Rainy"를 연도 2001, 월과 일을 나타내는 0331, 날씨를 나타내는 Rainy의 세 부분으로 나누려면
다음과 같이 할 수 있다:


"""

a = "20010331Rainy"
date = a[:8]
weather = a[8:]

print(date)
print(weather)

print(lline)
#Example #8 문자열을 슬라이싱으로 나누기
print("20010331Rainy를 연도 2001, 월과 일을 나타내는 0331, 날씨를 나타내는 Rainy의 세 부분으로 나누어라.")

year = a[:4] #-> 처음부터 a[3]까지

month = a[4:8] #-> a[4]부터 a[7]까지

weather = a[8:] #-> a[8]부터 마지막까지

print("year:", year, "\nmonth:", month, "\nweather:", weather)


print(lline)
print("\n")

"""
2. 문자열 안에 있는 문자를 바꿔보기

Pithon 으로 저장된 문자열을 Python으로 바꾸려면 어떻게 해야 할까?


"""

a = "Pithon"

# a[1] = "y" -> 오류가 나온다. 이유는 문자열의 요소값은 바꿀 수 없기 때문이다. (문자열이 Immutable 자료형인 이유)

print(a[:1] + "y" + a[2:]) #-> 슬라이싱을 이용하면 "Pithon"문자열을 "P" 부분과 "thon" 부분으로 나눌 수 있기 때문에
#                              그 사이에 'y' 문자를 추가하여 "Python"이라는 새로운 문자열을 만들 수 있다.


print(lline)

"""
3. 문자열 포매팅

"현재 온도는 18도 입니다."

해당 문장이 출력된 후 시간이 지나고 다음 문장이 출력된다.

"현재 온도는 20도 입니다."

위 두 문자열은 문장은 같지만 20과 18이라는 숫자만 다른데, 
이렇게 특정한 값만 바꿔야할 경우가 있을 때 쓰는 방식이
문자열 포매팅 (Formatting)이다.

쉽게 말해 문자열 안에 어떤 값을 삽입하는 방법이다. 

3.1 숫자 바로 대입

print("I eat %d apples." %3)

Output: I eat 3 apples

위 코드는 문자열 안에 정수 3을 삽입한다.
문자열 안에 넣고 싶은 자리에 %d 문자를 넣어주고, 삽입할 숫자 3은 가장 뒤에 있는
%문자 다음에 써 넣었다. 여기에서 "%d"는 문자열 포맷 코드라고 부른다.


3.2 문자열 바로 대입

print("I eat %s apples." %"five")

Output: I eat five apples.

위의 코드에는 %d를 넣는 대신 %s를 삽입하였다. 

이를 통해 알 수 있는 점은, 
숫자는 %d, 문자열은 %s를 넣어야 한다.

3.3 숫자 값을 나타내는 변수로 대입
number = 3

print("I eat %d apples." %number)

Output: I eat 3 apples.

3.4 2개 이상의 값 넣기

문자열 안에 1개 이상의 값을 넣기 싶을 때는 아래의 코드처럼 하면 된다.

number = 10

day = "three"

print("I ate %d apples. so I was sick for %s days." %(number, day))
"""
print(lline)

#Example #9 숫자 대입
print("Example #9")
print("I eat %d apples." %3)

print(lline)
#Example #10 문자열 대입
print("Example #10")
print("I eat %s apples." %"five")

print(lline)
#Example #11 숫자 값을 나타내는 변수로 대입
print("Example #11")
number = 3

print("I eat %d apples." %number)

print(lline)

#Example #12 문자열 안에 2개 이상의 값을 넣기
print("Example #12")
number = 10

day = "three"

print("I ate %d apples. so I was sick for %s days." %(number, day))

print(lline)

#문자열 포맷 코드 표

"""
3.5 문자열 포맷 코드 표

코드           Explanation
%s            문자열(String)
%c            문자 1개 (Character)
%d            정수 (Integer)
%f            부동 소수 (Floating-Point)
%o            8진수
%x            16진수
%%            Literal % (문자 % 자체)
"""

"""
3.6 %s 포맷 코드
여기서 알아갈 점은 %s 포맷 코드인데, 이 코드는 어떤 형태의 값이든 변환해 넣을 수 있다.

print("I have %s apples." %3)
print("Rate is %s." %3.234)

Output: I have 3 apples.
Output: Rate is 3.234.

3.7 %를 문자열 안에 출력하고 싶을 때

위의 포맷 코드 표에 나온 것처럼, %%사용하면 문자열 안에 %를 출력할 수 있다.

print("Successful rate is %d%%." %99)
"""

#Example #13
print("Example #13")
print("I have %s apples." %3)
print("Rate is %s." %3.234)

print(lline)

#Example #14
print("Example #14")
print("Successful rate is %d%%." %99)

"""
3.7 포맷 코드와 숫자 함께 사용하기

위에서 보았듯이, %d, %s 등의 포맷 코드는 문자열 안에 어떤 값을 삽입하기 위해 사용한다.
하지만 포맷 코드를 숫자와 함께 사용하면 더 유용하게 사용할 수 있다. 

print("%10s" % "hi")
위의 코드는 %10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨두라는 의미이다.

Output: {        hi}

위의 소스코드를 인덱스열로 표현하면 이렇다.
0 1 2 3 4 5 6 7 h i

0부터 7까지는 공백, h는 8, i는 9에 들어간다


반대로 %뒤에 음수를 넣으면 'hi'가 어디로 가는 지 보자.
print("%-10jane" % 'hi')


Output: {hi        jane}
Output과 같이 hi를 왼쪽으로 정렬하고 나머지는 공백으로 채웠음을 볼 수 있다.

Index -> h i 2 3 4 5 6 7 8 9 j a n e
"""

print(lline)

#Example #15
print("Example #15")
print("%10s" % "hi")
#위의 소스코드를 인덱스열로 표현하면 이렇다.
#0 1 2 3 4 5 6 7 h i

#0부터 7까지는 공백, h는 8, i는 9에 들어간다

print(lline)
#Example #16
print("Example #16")
print("%-10sjane" % 'hi')


"""
3.8 소수점 표현하기

print("%0.4f" %3.4215555) -> 반올림을 해준다.

%0.4f 의 의미는 3.4215555를 소수점 4번째 자리까지만 나타내고 싶은 경우에 사용한다.

0.4의 "."은 소수점 포인트를 말하고 그 뒤의 숫자 "4"는 소수점 뒤에 나올 숫자의 개수를 말한다.

print("%10.4f" % 3.4215555)
Output: {    3.4216}

위의 코드는 3.4215555를 소수점 4번째 자리까지만 표시하고 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬하는 예를 보여준다.
Index: "0" "1" "2" "3" 3 . 4 2 1 6 (공백 4개, 전체 길이 10개)
"""

print(lline)
#Example #17
print("Example #17")
print("%0.4f" %3.4215555)

print(lline)
#Example #18
print("Example #18")
print("%10.4f" % 3.4215555)

"""
3.9 format 함수를 사용한 포매팅

문자열의 format 함수를 사용하면 좀 더 발전된 스타일로 문자열 포맷을 지정할 수 있다.

print("I eat {0} apples.".format(3))

Output: {I eat 3 apples.}
"I eat {0} apples" 문자열 중 {0} 부분이 숫자 3으로 바뀌었다.

----------------------------------------------------------------------------------------------------------------------


3.9.1 문자열 바로 대입하기
print("I eat {0} apples.".format("five"))

----------------------------------------------------------------------------------------------------------------------


3.9.2 숫자 값을 가진 변수로 대입하기
number = 3

print("I eat {0} apples.".format(number))

----------------------------------------------------------------------------------------------------------------------


3.9.3 2개 이상의 값 넣기

number = 10
day = "three"

print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

2개 이상의 값을 넣을 경우 문자열의 {0}, {1}과 같은 인덱스 항목이 format 함수의 입력값으로 순서에 맞게 바뀐다.
즉, 위 예에서 {0}은 format 함수의 첫 번째 입력값인 number로 바뀌고 {1}은 format 함수의 두 번쨰 입력값인 day로 바뀐다.

----------------------------------------------------------------------------------------------------------------------

3.9.4 이름으로 넣기

print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day = 3))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day = "three"))

위 코드와 같이{0}, {1}과 같은 인덱스 항목 대신 더 편리한 {name} 형태를 사용하는 방법도 있다. {name} 형태를 사용할 경우
format 함수에는 반드시 name = value 와 같은 형태의 입력값이 있어야 한다. 

예로 {number} 와 {day}가 format 함수의 입력값인 number = 10, day = "three' 값으로 바뀌는 것을 보여주고 있다.

----------------------------------------------------------------------------------------------------------------------

3.9.5 인덱스와 이름은 혼용해서 넣기

print("I ate {0} apples. so I was sick for {day} days.".format(10, day = 3))

#format(10, day = 3)에서 볼 수 있듯이, 인덱스와 함수 둘 다 활용하여 사용 가능하다.


3.9.6 왼쪽 & 오른쪽 & 가운데 정렬

왼쪽 정렬
print("{0:<10}".format("hi))

Output: {hi        }
#:<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.



오른쪽 정렬
print("{0:>10}".format("hi"))

Output: {        hi}
오른쪽 정렬은 :< 대신 :>을 사용하면 된다. 화살표 방향을 생각하면 어느 쪽으로 정렬되는지 바로 알 수 있을 것이다.

(왼쪽은 못난 놈, 오른쪽은 좋은 놈)

가운데 정렬
print("{0:^10}".format("hi"))

Output: {    hi    }
:^기호를 사용하면 가운데 정렬도 가능하다.

3.9.7 공백 채우기
print("{0:=^10}".format("hi")) -> Output: ====hi====
print("{0:!^10}".format("bro")) -> Output: !!!bro!!!
print("{0:!<10}".format("bro")) -> Output: bro!!!!!!!
print("{0:!>10}".format("bro")) -> Output: !!!!!!!bro
정렬할 때 공백 문자 대신에 지정한 문자 값으로 채워 넣는 것도 가능하다. 채워 넣을 문자 값은 정렬 문자 <, >, ^ 바로 앞에 넣어야 한다.


3.9.8 소수점 표현하기

y = 3.14159265

print("{0:0.4f}".format(y)) -> Output: 3.1416
print("{0:10.4f}".format(y)) -> Output: {    3.1416} -> 10개의 인덱스에서 오른쪽으로 3.1416

3.8에서 배웠던 것처럼 사용이 가능하다.

"""

print(lline)

#Example #19
print("Example #19")
print("I eat {0} apples.".format(3))

print(lline)
#Example #20
print("Example #20")
print("I eat {0} apples.".format("five"))


print(lline)

#Example #21
print("Example #21")

number = 12
print("I eat {0} apples.".format(number))

print(lline)

#Example #22
print("Example #22")

number = 10
day = "three"

print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

print(lline)
#Example #23
print("Example #23")

print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day = 3))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day = "three"))

print(lline)


#Example #24
print("Example #24")

print("I ate {0} apples. so I was sick for {day} days.".format(10, day = 3))
#format(10, day = 3)에서 볼 수 있듯이, 인덱스와 함수 둘 다 활용하여 사용 가능하다.

"""
왼쪽 정렬
print("{0:<10}".format("hi))

오른쪽 정렬
print("{0:>10}".format("hi"))

가운데 정렬
print("{0:^10}".format("hi"))

공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!^10}".format("bro"))
print("{0:!<10}".format("bro"))
print("{0:!>10}".format("bro"))
"""

print(lline)
#Example #25

print("Example #25")
#왼쪽 정렬
print("{0:<10}".format("hi"))
#:<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.


print(lline)
#Example #26
print("Example #26")
#오른쪽 정렬
print("{0:>10}".format("hi"))

print(lline)
#Example #27
print("Example #27")
#가운데 정렬
print("{0:^10}".format("hi"))

print(lline)

#Example #28
print("Example #28")
#공백채우기
print("1. {0:=^10}".format("hi"))
print("2. {0:!^10}".format("bro"))
print("3. {0:!<10}".format("bro"))
print("4. {0:!>10}".format("bro"))


print(lline)

#Example #29
print("Example #29")

y = 3.14159265

print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

"""
3.9.9 {또는} 문자 표현하기

print("{{and}}".format())
"""

print(lline)
#Example #30
print("Example #30")
print("{{and}}".format())
print("{{However}}".format())
print("{{Putting two Curly Brackets makes you print a curly bracket}}".format())

"""
3.10 f문자열 포매팅

파이썬 "3.6" 버전부터는 f문자열 포매팅 기능을 사용할 수 있다. (파이썬 3.6 미만에서는 불가.)


name = "Hunter"

Age = 22

print(f"My name is {name}, and I am {Age} years old.")
print(f"My name is {name}, and I am {Age + 1} years old in Korea")

위와 같이 변수들을 선언하고 "쓰고 싶은 문장들"의 Quotation 앞쪽에 "f"를 넣어준다.
"""
print(lline)

#Example #31
print("Example #31")
name = "Hunter"

Age = 22

print(f"My name is {name}, and I am {Age} years old.")
print(f"My name is {name}, and I am {Age + 1} years old in Korea")

"""
3.10.1 딕셔너리를 사용한 f 문자열 포매팅

dic = {'name':"Hunter", "age": 22}
print(f"My name is {d['name']}, and I am {d["age"]} years old.")
"""

print(lline)

#Example #31
print("Example #31")

dic = {'name':"Hunter", "age": 22}
print(f"My name is {dic['name']}, and I am {dic['age']} years old.")
print(f'My name is {dic["name"]}, and I am {dic["age"]} years old.')
#TIP: Make Sure to remember to use 'Single Quotation' when you are using "Double Quotation" with print function.
#     Make Sure to remember to use "Double Quotation" when you are using 'Single Quotation' with print function.

print(lline)

#총정리
"""
총정리:

print(f"{"hi":<10}")
"""
print("Review")
print(f".{'hi':<10}.   -> 왼쪽 정렬 (< 사용)")
print(f'.{"hi":>10}.   -> 오른쪽 정렬 (> 사용)')
print(f".{'hi':^10}.   -> 가운데 정렬 (^ 사용)")
print(f'.{"hi":=^10}.  -> 공백 채우기 (= 로 채움)')
print(f".{'hi':!^10}.  -> 공백 채우기 (! 로 채움)")
print("\n")
#소수점 표현하기
y = 3.14159265

print(f"pi is equal to .{y:0.4f}.  -> 소수점 4자리까지만 표현 (반올림 O)") 
print(f'pi is equal to .{y:10.4f}. -> 소수점 4자리 표현, 총 자릿수 10칸 맞춤')


print(lline)
#String_Quiz #2
print("String Formatting Quiz")
print("format 함수 또는 f 문자열 포매팅을 사용해 '!!!python!!!' 문자열을 출력해보자.")

#Answers
print(f"{'python':!^12}") #-> My answer

print("{0:!^12}".format('python')) #-> This is also correct

print(lline)
print("-" * 70)

"""
4. Functions Related to String 문자열 관련 함수

문자열 자료형은 자체적으로 함수를 가지고 있다. a.k.a 내장 함수라고 부른다.
내장 함수를 사용하려면 문자열 변수 이름 뒤에 '.'를 붙인 다음에 함수 이름을 써주면 된다.

문자열의 내장 함수 (아래 코드들)
"""

#1. 문자 개수 세기 (count)
print("1. 문자 개수 세기 {count}")
a = "hobby"
b = "ascertain"
print(a.count("b")) #-> a에 저장한 변수에서 'b'의 개수를 돌려준다.
print(b.count("a")) #-> b에 저장한 변수에서 'a'의 개수를 돌려준다.

print(enter)

#2. 위치 알려주기 1 (find)
print("2. 위치 알려주기 1 {find}")
a = "Python is the best choice"
print(a.find('b'))
#Output이 14로 나올텐데, 문자열에서 'b'가 처음 나온 위치이다.

print(a.find('k'))
#Output에 -1이 나올텐데, 이러한 이유는 찾는 문자나 문자열이 존재하지 않기 때문이다.
print(a.find('z'))

print(enter)

#3. 위치 알려주기 2 (index)
print("3. 위치 알려주기 2 {index}")

a = "Life is too short"

print(a.index('t'))
#find 함수와 같이 맨 처음으로 나온 위치를 반환한다.

#print(a.index('K'))
#982번 코드는 오류가 나는데, 그 이유는 "index"함수를 사용할 때
#찾는 문자나 문자열이 없으면 "오류"가 발생한다.

print(enter)

#4. 문자열 삽입 (join)
print("4. 문자열 삽입 {join}")

print(",".join('abcd'))

"""
abcd 문자열의 각각의 문자에 ','를 삽입한다.
join 함수를 문자열 뿐만 아니라 앞으로 배울 리스트나 튜플도 입력으로 사용할 수 있다.
join 함수의 입력으로 리스트를 사용하는 예는 아래 코드이다.
"""

print("\n4.1 문자열 삽입 (리스트를 사용한 join)")
print(",".join(['a', 'b', 'c', 'd']))


print(enter)

#5. 소문자를 대문자로 바꾸기 (upper)
print("5. 소문자를 대문자로 바꾸기 {upper}")

a = "bruh"
print(a.upper())
print("Output: BRUH")
print("upper 함수는 모든 소문자를 대문자로 바꾸어 준다.")
print("만약 문자열이 이미 대문자라면 아무 변화도 일어나지 않는다.")

print(enter)

#6. 대문자를 소문자로 바꾸기 (lower)
print("6. 대문자를 소문자로 바꾸기 (lower)")

a = "RNSEO WHWRKXEK"
print(a.lower())
print("Output: rnseo whwrkxek")
print("lower 함수는 모든 대문자를 소문자로 바꾸어준다")

print(enter)

#7. 왼쪽 공백 지우기 (lstrip)
print("7. 왼쪽 공백 지우기 (lstrip)")

a = "     python     "

print(a.lstrip())
print("Output: \"python     \"")
print("문자열 중 가장 왼쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다. lstrip에서 l은 'left'를 의미한다.")


print(enter)

#8. 오른쪽 공백 지우기 (rstrip)
print("8. 오른쪽 공백 지우기 (rstrip)")

a = "     python     "

print(a.rstrip())
print("Output: \"     python\"")
print("문자열 중 가장 오른쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다. rstrip에서 r는 'right'을 의미한다.")
      
print(enter)
      
#9. 양쪽 공백 지우기 (strip)
print("9. 양쪽 공백 지우기 (strip)")

a = "     python     "
print(a.strip())
print("Output: {python}")
print("문자열 양쪽에 있는 한 칸 이상의 연속된 공백을 모두 지운다.")

print(enter)

#10. 문자열 바꾸기 (replace)
print("10. 문자열 바꾸기 (replace)")

a = "21 Months are too short"

print("Original Sentence:", a)
print("Output: ", a.replace("short", "long"))
print(a.replace("short", "long"))
print("\nreplace(바뀌게 될 문자열, 바꿀 문자열)처럼 사용해서\n문자열 안의 특정한 값을 다른 값으로 치환해준다.")

print(enter)
#11. 문자열 나누기(split)
print("11. 문자열 나누기(split)")

a = "Life is too short"
print("Output: ", a.split())


b = "a:b:c:d"

print("Output: ", b.split(':'))

"""
split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어준다.
만약 b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어준다. 이렇게 나눈 값은 리스트에 하나씩 들어가게 된다. 

위 11개의 문자열 관련 함수는 문자열 처리에서 사용 빈도가 매우 높고 유용하다. 이 외의 함수가 더 있긴 하지만 자주 사용되지는 않는다. 
"""