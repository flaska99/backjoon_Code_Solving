#해당 함수는 첫세팅이다.
#시작되는곳에 제일 작은것을 끝기둥에 올리는 작업.
def hanoi(n, start, auxiliary, end) : 
    if n == 1 : #하나일떄 가장큰거 목적지로 올려버리는 연산
        print(start, end)
        return
    
    #재귀함수의 매개변수가 헷갈릴땐 
    # 원반이 4개일 때를 생각해보자.
    #해당 함수는 원반들을 보조기둥으로로 이동시키는 것
    hanoi(n-1, start, end, auxiliary)
    print(start, end)
    #해당 함수는 2번에 있는 원반들을 3번으로 이동시키는것것
    hanoi(n-1, auxiliary, start, end)

n = int(input())
print(2 ** n - 1)
if n <= 20 : hanoi(n, 1, 2, 3)


