# solution 1  -> 실행시간 1020ms
# arr = []
# def d(n):
#     a = list(map(int, str(n).strip()))
#     return n + sum(a)
#
# for i in range(1, 10001):
#     num = d(i)
#     if num not in arr:
#         arr.append(num)
#
# for i in range(1, 10001):
#     if i not in arr:
#         print(i)


#solution2 -> 실행시간 84ms
# nat_num = set(range(1,10001))
# del_num = [ i+sum(list(map(int, str(i).strip()))) for i in nat_num ]
# self_num = sorted(nat_num - set(del_num))
# for i in self_num:
#     print(i)

#solution2 한 줄로 출력
print(*sorted(set(range(1,10001)) - set([ i+sum(list(map(int, str(i).strip()))) for i in range(1,10001)])) , sep='\n')