# # # # # # # # # # # # # # # # # # # # # # # # # # # 변수선언
# # # # # # # # # # # # # # # # # # # # # # # # # # # 형 변환 int 정수형 float 실수형 str 문자형
# # # # # # # # # # # # # # # # # # # # # # # # # # # 불리안 = False, True 이해 (참 ,거짓 and 있다 ,없다 구분)
# # # # # # # # # # # # # # # # # # # # # # # # # # # 주석처리 이해
# # # # # # # # # # # # # # # # # # # # # # # # # # # 인덱스 = 몇 번째? 0부터 시작 - 활용 가능 (끝에서부터) lang을 통해 확인 가능 
# # # # # # # # # # # # # # # # # # # # # # # # # # # 슬라이싱 = : 을 통해 활용  :- 전체 0: 0번째부터 끝까지 0:2 0부터 2전까지(1까지)  :-1  끝에서 두번쨰까지 등
# # # # # # # # # # # # # # # # # # # # # # # # # # # 문자열 메소드

# # # # # # # # # # # # # # # # # # # # # # # # # # # lower() 소문자 
# # # # # # # # # # # # # # # # # # # # # # # # # # # upper() 대문자
# # # # # # # # # # # # # # # # # # # # # # # # # # # capitalize() 첫 글자만 대문자로
# # # # # # # # # # # # # # # # # # # # # # # # # # # title() 각 단어 capitalize
# # # # # # # # # # # # # # # # # # # # # # # # # # # swapcase() 대소문자 변환
# # # # # # # # # # # # # # # # # # # # # # # # # # # split() 문자형 분리 ex)how are you split 사용시 how, are, you
# # # # # # # # # # # # # # # # # # # # # # # # # # # count() 특정 단어 수 카운트

# # # # # # # # # # # # # # # # # # # # # # # # # # # 메소드=기능

# # # # # # # # # # # # # # # # # # # # # # # # # # # 문자열 메소드
# # # # # # # # # # # # # # # # # # # # # # # # # # # startswith(나도)  나도로 시작하는지?불리안 형태
# # # # # # # # # # # # # # # # # # # # # # # # # # # 반대 endswith 
# # # # # # # # # # # # # # # # # # # # # # # # # # # strip() 제거
# # # # # # # # # # # # # # # # # # # # # # # # # # # replace 변경
# # # # # # # # # # # # # # # # # # # # # # # # # # # find 문자 찾기
# # # # # # # # # # # # # # # # # # # # # # # # # # # center(10,'-') 

# # # # # # # # # # # # # # # # # # # # # # # # # # # 구글 파이썬 내장형 
# # # # # # # # # # # # # # # # # # # # # # # # # # # 문자열 출력
# # # # # # # # # # # # # # # # # # # # # # # # # # # print( , )
# # # # # # # # # # # # # # # # # # # # # # # # # # # 문자열 포맷
# # # # # # # # # # # # # # # # # # # # # # # # # # # {},{}등이 있어요'. format(,)
# # # # # # # # # # # # # # # # # # # # # # # # # # # f-string 
# # # # # # # # # # # # # # # # # # # # # # # # # # # 탈출 문자 \'' \''""
# # # # # # # # # # # # # # # # # # # # # # # # # # # \n 줄바꿈
# # # # # # # # # # # # # # # # # # # # # # # # # # # 리스트 = [ ]
# # # # # # # # # # # # # # # # # # # # # # # # # # #my_list[] 중복 허용함. 숫자 불리안 다 가능 
# # # # # # # # # # # # # # # # # # # # # # # # # # 인덱스 print(my_list[0]) 순서있는 비닐봉투 슬라이싱 가능
# # # # # # # # # # # # # # # # # # # # # # # # # #  in 쓰면 불리안 적용 len 몇개? 리스트 수정 가능 변수 지정
# # # # # # # # # # # # # # # # # # # # # # # # # #  append 값 추가, remove 삭제, 리스트 extend 합체 
# # # # # # # # # # # # # # # # # # # # # # # # # #  리스트 메소드 참고
 
# # # # # # # # # # # # # # # # # # # # # # # # # 튜플! 내장 자료형  튜플은 소괄호 ()
# # # # # # # # # # # # # # # # # # # # # # # # # 튜플은 수정 불가함. 읽기 전용 리스트
# # # # # # # # # # # # # # # # # # # # # # # # # 순서도 보장 슬라이싱 가능 포함여부 가능in len길이 

# # # # # # # # # # # # # # # # # # # # # # # # 튜플 패킹?
# # # # # # # # # # # # # # # # # # # # # # # # 언패킹 >> 패킹 
# # # # # # # # # # # # # # # # # # # # # # # # numbers = (1,2,3,4,5)
# # # # # # # # # # # # # # # # # # # # # # # # (one,two,*others)=numbers 
# # # # # # # # # # # # # # # # # # # # # # # # 별을 통해 나머지를 넣을 수 있음.
# # # # # # # # # # # # # # # # # # # # # # # # 세트 순서X 중복X 
# # # # # # # # # # # # # # # # # # # # # # # # 세트 = { }
# # # # # # # # # # # # # # # # # # # # # # # # intersection 교집합
# # # # # # # # # # # # # # # # # # # # # # # # 합집합은? union  
# # # # # # # # # # # # # # # # # # # # # # # # 차집합 difference .

# # # # # # # # # # # # # # # # # # # # # # # # 세트는 슬라이싱이 안된다. 하지만 읽기 전용은 아니다.
# # # # # # # # # # # # # # # # # # # # # # # # add 를 통해 추가 remover 제거 가능 clear 로 싹 지울 수 있음.
# # # # # # # # # # # # # # # # # # # # # # # # del >시 완전 삭제
# # # # # # # # # # # # # # # # # # # # # # # # 세트 메소드 공부

# # # # # # # # # # # # # # # # # # # # # # # 딕셔너리 (사전)
# # # # # # # # # # # # # # # # # # # # # # # key, value 사전에 정의 
# # # # # # # # # # # # # # # # # # # # # # # 중복 불가, 
# # # # # # # # # # # # # # # # # # # # # # # 딕셔너리={key1:value1...}
# # # # # # # # # # # # # # # # # # # # # # # ex)
# # # # # # # # # # # # # # # # # # # # # # # person={'이름':'나귀욤',
# # # # # # # # # # # # # # # # # # # # # # #         '나이':7
# # # # # # # # # # # # # # # # # # # # # # #         '키':120
# # # # # # # # # # # # # # # # # # # # # # #         '몸무게':23}

# # # # # # # # # # # # # # # # # # # # # # # 딕셔너리 2
# # # # # # # # # # # # # # # # # # # # # # # get을 통해 None이 출력되게 함.
# # # # # # # # # # # # # # # # # # # # # # # 새로운 데이터 추가시 [ ] : 
# # # # # # # # # # # # # # # # # # # # # # #   [ ] 변경
# # # # # # # # # # # # # # # # # # # # # # #   update 로 변경 가능.
# # # # # # # # # # # # # # # # # # # # # # #   pop으로 특정 값 삭제
# # # # # # # # # # # # # # # # # # # # # # #   clear() 모든 값 삭제.
# # # # # # # # # # # # # # # # # # # # # # #   keys를 통해 어떤 ?
# # # # # # # # # # # # # # # # # # # # # # #   items() 모든 데이터 확인
  
# # # # # # # # # # # # # # # # # # # # # #   자료형 비교 
  
# # # # # # # # # # # # # # # # # # # # # #   여러값들을 순서대로 >리스트
# # # # # # # # # # # # # # # # # # # # # #   값이 바뀌면 안된다 > 튜플
# # # # # # # # # # # # # # # # # # # # # #   값의 존재여부가 중요하고 중복X >세트
# # # # # # # # # # # # # # # # # # # # # #   효율적인 데이터 > 딕셔너리
  
# # # # # # # # # # # # # # # # # # # # # #   튜플도 수정법이 있다.
# # # # # # # # # # # # # # # # # # # # # #   my_tuple=
# # # # # # # # # # # # # # # # # # # # # #   my_list=list(my_tuple)
# # # # # # # # # # # # # # # # # # # # # #   이런식으로 변환해서 튜플 리스트를 변환하여 쓸 수 있음.
# # # # # # # # # # # # # # # # # # # # #   리스트는 중복이 허용되는데 제거 가능
# # # # # # # # # # # # # # # # # # # # #  세트로 바꾼다음 리스트로 바꿈
# # # # # # # # # # # # # # # # # # # # #  순서가 중요하다면 세트로 변환X 
# # # # # # # # # # # # # # # # # # # # #  딕셔너리로 dict.fromkeys(my_list)
# # # # # # # # # # # # # # # # # # # # #  유연하게 자료형 공부
 
# # # # # # # # # # # # # # # # # # # #  from re import X


# # # # # # # # # # # # # # # # # # # # 이문장 
# # # # # # # # # # # # # # # # # # # #  저문장
# # # # # # # # # # # # # # # # # # # #  그문장
 
# # # # # # # # # # # # # # # # # # # #  if 코딩
 
# # # # # # # # # # # # # # # # # # # #  조건이 True일 때 수행. False일 땐 실행 X
# # # # # # # # # # # # # # # # # # # #  if 조건:
# # # # # # # # # # # # # # # # # # # #    이 문장 (앞에 들여쓰기 필수,스페이스4또는 탭)
# # # # # # # # # # # # # # # # # # # #    다음 문장
# # # # # # # # # # # # # # # # # # # if else
# # # # # # # # # # # # # # # # # # # elif 
# # # # # # # # # # # # # # # # # # # if 중첩
# # # # # # # # # # # # # # # # # # # if 조건1:
# # # # # # # # # # # # # # # # # # #   이문장
# # # # # # # # # # # # # # # # # # #   if 조건2:
# # # # # # # # # # # # # # # # # # #     저 문장

# # # # # # # # # # # # # # # # # # for 반복문 *******
# # # # # # # # # # # # # # # # # # print('팔 벌려 뛰기 해')
# # # # # # # # # # # # # # # # # # 이 때 반복문. for
# # # # # # # # # # # # # # # # # # for 변수 in 반복범위:
# # # # # # # # # # # # # # # # # #   반복 수행 문장
  
# # # # # # # # # # # # # # # # # #   for x in range(10):
# # # # # # # # # # # # # # # # # #     print('팔 벌려 뛰기{x}회 해')
    
# # # # # # # # # # # # # # # # # for num in range(10):
# # # # # # # # # # # # # # # # #   print(f'죽,음료 쿠폰(입장 번호:{num+1})')

# # # # # # # # # # # # # # # # from distutils.command.build_scripts import first_line_re


# # # # # # # # # # # # # # # # range(10) 0이상 10 미만
# # # # # # # # # # # # # # # # range(1,10)
# # # # # # # # # # # # # # # # range(start,stop,step)
# # # # # # # # # # # # # # # # ex) 홀수 짝수 3의 배수
# # # # # # # # # # # # # # # # range(1,10,2)
# # # # # # # # # # # # # # # # 2만큼 증가 1 3 5 7 9
# # # # # # # # # # # # # # # # range(2,10,2) 2 4 6 8 10 
# # # # # # # # # # # # # # # # for 활용
# # # # # # # # # # # # # # # # for 변수 in 반복 범위 또는 대상:
  
# # # # # # # # # # # # # # # # 대상을 리스트 튜플 딕셔너리
# # # # # # # # # # # # # # # # my_list=[1,2,3]
# # # # # # # # # # # # # # # # for x in my_list:
# # # # # # # # # # # # # # # #   print(x)
# # # # # # # # # # # # # # # # person={'이름':'나귀욤'}
# # # # # # # # # # # # # # # # 문자열
# # # # # # # # # # # # # # # # fruit= 'apple'
# # # # # # # # # # # # # # # # for x in first_line_re
# # # # # # # # # # # # # # # from operator import itemgetter


# # # # # # # # # # # # # # # while ~하는 동안
# # # # # # # # # # # # # # # for while 
# # # # # # # # # # # # # # # while은 참인 동안 계속

# # # # # # # # # # # # # # # while 조건:
# # # # # # # # # # # # # # #   weight+ item <= max:
# # # # # # # # # # # # # # #     weight += item
# # # # # # # # # # # # # # #     print('짐을 추가합니다.')
# # # # # # # # # # # # # # #   print(어쩌고)
  
# # # # # # # # # # # # # # # break (비상 정지 장치) 반복문 탈출
# # # # # # # # # # # # # # # if와 같이 사용

# # # # # # # # # # # # # # continue를 적어주면 

# # # # # # # # # # # # # # 들여쓰기
# # # # # # # # # # # # # # indent     
# # # # # # # # # # # # # from ast import comprehension
# # # # # # # # # # # # # from multiprocessing.dummy import JoinableQueue


# # # # # # # # # # # # # SIRO JoinableQue

# # # # # # # # # # # # # List comprehension

# # # # # # # # # # # # # 리스트 컴프리헨션
# # # # # # # # # # # # new_list= [변수활용 for 변수 in 반복대상 if 조건]
# # # # # # # # # # # # my_list= [1,2,3,4,5]
# # # # # # # # # # # # new_list= [x for x in my_list if x > 3]
# # # # # # # # # # # # x에는 +1 *3 등 할 수 있음.
# # # # # # # # # # # 함수**

# # # # # # # # # # # customer1='나장발'

# # # # # # # # # # # def 함수명():
# # # # # # # # # # #   수행할 문장

# # # # # # # # # # # 전달값?
# # # # # # # # # # # 반환값
# # # # # # # # # # # return

# # # # # # # # # # #기본값 - 함수 사용 편리해짐 ..
# # # # # # # # # # def 함수명(전달값=기본값)

# # # # # # # # # # 키워드값 전달값의 대상을 전해줌


# # # # # # # # # def order(shot=2 ,size='Regular', takeout=True):
# # # # # # # # #   print(f'아메리카노{size}사이즈{shot}샷')
# # # # # # # # #   if takeout:
# # # # # # # # #     print('포장 완료')
# # # # # # # # #   else:
# # # # # # # # #     print('주문이 완료 되었습니다.')
    
# # # # # # # # # order('Regular',takeout=True)

# # # # # # # # # 가변인자.

# # # # # # # # # def visit(today,customer1,customer2,...): 이럴 때 가변인자 사용 (개수가 바뀔 수 있음.)
# # # # # # # # def visit(today,*customers):
# # # # # # # #   print(today)
# # # # # # # #   for customer in customers:
# # # # # # # #     print(customer)
    
# # # # # # # # visit('2022년 6월 10일', '나장발','ㅇ')
# # # # # # # # 주의사항: 전달값이 많으면 마지막에 한 번만.. 
# # # # # # # 지역변수
# # # # # # # 전역변수
# # # # # # # 전역변수사용 global
# # # # # # input.__annotations__

# # # # # name=input('예약자분 성함이 어떻게 되나요?')
# # # # # print(name)
# # # # # open(파일명,열기모드,encoding='인코딩')
# # # # # r,a,w 
# # # # # read append , write

# # # # f=open('list.txt','w',encoding='utf8')
# # # # f.write('정태훈')
# # # # f.close()

# # # with 함수

# # # 블럭 벗어나면 자동으로 닫음?
# # # with open('list.txt','w',encoding='utf8')as f:
# # #   f.write ~~~
  
  
# # name= '까망이'
# # resolution="FHD"
# # price= 200000
# # color = 'balck'
# # # 블랙박스 변수

# # # 딕셔너리.
# # class = 설계도 + 설명서

# # object 객체. instance . 인스턴스.

# #
#   #정의 
  
# class BlackBox:
#   pass

# b1 =BlackBox() #b1객체 생성 완료
# b1.name='까망이' #변수 선언
# print(b1.name)
# print(isinstance(b1,BlackBox))

# class BlackBox:
#   def __init__(self,name,price):
#     self.name=name
#     self.price=price
    
#   상속?

다중 상속
