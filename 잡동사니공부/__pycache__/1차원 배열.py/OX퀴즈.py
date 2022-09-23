a = int(input()) #케이스 개수
for i in range(a): #케이스 개수만큼 
    b = input() #OX출력 (a번)
    s = list(b) #OX출력을 list에 넣음
    sum = 0 #sum 값 부여.
    c = 1 #카운트 횟수 부여
    for i in s: #리스트 속 OX 안에서 반복문.
        if i == 'O': #i가 O일 경우 
            sum += c #sum에 카운트 추가
            c += 1 #카운트 1씩 증가
        else:
            c = 1 #X를 만나면 1로 돌아가게하는거구나.
    print(sum)