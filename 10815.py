# 풀이법 1
# 해쉬값을 이용하여 풀이

# from sys import stdin
#
# N = map(int, stdin.readline().split())
# own_cards = list(map(int, stdin.readline().split()))
# M = map(int, stdin.readline().split())
# card_list = list(map(int, stdin.readline().split()))
#
# dic = {}
#
# for n in own_cards:
#     if n not in dic:
#         dic[n] = 1
#
# # ans = []
# # for m in card_list:
# #     if m in dic:
# #         ans.append(dic[m])
# #     else:
# #         ans.append(0)
# # for i in ans:
# #     print(i, end=' ')
#
# print( ' '.join( str(dic[m]) if m in dic else '0' for m in card_list ))


#풀이법 2
#이진탐색을 이용하여 풀이
from sys import stdin

N = map(int, stdin.readline().split())
own_cards = sorted(map(int, stdin.readline().split()))
M = map(int, stdin.readline().split())
card_list = list(map(int, stdin.readline().split()))


def binary_search(card, start,end):

    mid = (start + end ) // 2
    if start > end:
        return 0

    if card == own_cards[mid]:
        return 1
    elif card < own_cards[mid]:
        return binary_search(card,start, mid-1)
    else:
        return binary_search(card,mid+1, end)


dic = {}

for card in card_list:
    start = 0
    end = len(own_cards)-1
    if card not in dic:
        dic[card] = binary_search(card,start,end)


print( ' '.join(str(dic[m]) if m in dic else '0' for m in card_list))
