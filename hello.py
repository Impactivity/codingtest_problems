# -*- coding: UTF-8 -*-
import collections

def solution3(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant) - 1]



def solution2(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer


def solution1(participant, completion):
    print(collections.Counter(participant))
    print(collections.Counter(completion))

    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

def solution(phone_book):
    phone_book.sort()
    q = len(phone_book)
    print(q)
    for i in range(0,q):
        for j in range(i+1,q):
            len1 = len(phone_book[i])
            print(len1)
            print(phone_book[i])
            print(phone_book[j][:len1])
            if phone_book[i] == phone_book[j][:len1]:
                return False
    return True

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True



phone_book = ["119", "97674223", "1195524421"]
phone_book2 = ["123","456","789"]
phone_book3 = [12,123,1235,567,88]

answer = solution(phone_book2)
print(answer)



def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

