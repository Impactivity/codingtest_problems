#
# n * n 문자열이 포함된 행렬과   ( 2 <= n <= 300)
# 최소 갯수 t 가 주어질 때
# k * k ( k < n ) 정사각형으로 n*n을 남기지 않고 모두 쪼갤 수 있어야한다.
# 예를들어, 6*6은 2*2 와 3*3 으로 쪼갤 수 있다.
# k * k 로 쪼갠 정사각형의 중복되지 않은 문자 갯수 중 최대값을 출력하시오
# 단, 최소 갯수 t를 넘지 않아야 한다.
# n > 2 일때 k는 2이상이지만 , n = 2일 떄는 k = 1로 허용된다.


# [ 'a','b','a','b','b','a']
# [ 'a','c','a','a','a','a']
# [ 'a','b','a','a','a','a']
# [ 'a','b','a','a','a','a']
# [ 'c','d','a','a','a','a']
# [ 'a','b','a','a','a','c']


# 정답 : 3

###### 주어진 입력 값 #######
graph = [[ 'a','b','a','b','b','a'], [ 'a','c','a','a','a','a'] ,[ 'a','b','a','a','a','a']
         ,['a','b','a','a','a','a'],['c','d','a','a','a','a'] , ['a','b','a','a','a','c'] ]
t = 3
##########################

n = len(graph)
# 문제에서 가능한 k값은 n의 약수 중에서 1 과 n 을 제외한 값이 된다.
# 1과 n을 제외한 약수를 구해보자
arr = []
if n == 2:
    print(1)
    exit(0)

for i in range(2,n):
    if n % i == 0 :
        arr.append(i)


st = ''
_max = 0

# 문제의 핵심아이디어는 다음과 같다.
# greedy하게 k*k배열을 하나의 문자열로 이어 붙여서
# set함수를 씌워 중복을 제거한 다음 len를 구하면 문자열의 개수가 나올테고
#


for k in arr: # k 배열
    for inx in range(0,n,k): # 0부터 n까지 k 값 만큼 증가한다.
        i = inx # 시작 행
        for j in range(0,n,k): # 0부터 n 까지 k 값 만큼 증가하며 graph 열 이동
            tmp = i + k
            st = ''
            while i < tmp :
                # 이부분에서 조각낸 k*k를 한줄 문자열로 만들어보자
                st += ''.join(graph[i][j:j+k])
                i += 1
            st_len = len(set(st))
            if t >= st_len:
                _max = max(_max, st_len)
            i = inx # 현재 행 변수를 원래 시작행으로 초기화하여 다음 번 k*k 행렬을 탐색할 수 있도록
print(_max)

# for k in arr:
#     for nx in range(0,n,k): # 0, 2, 4
#         for ny in range(0,n,k):
#             for i in range(k):
#                 for j in range(k):
#                     st += graph[nx + i][ny + j]
#             ar2= set(Counter(st))
#             count.append(len(ar2))
#             st = ''
#
# _max = 0
#
# for i in range(0,len(count)):
#     if count[i] <= t:
#         _max = max(_max, count[i])
#
# print(_max)

