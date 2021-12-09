import re


def solution(new_id):
    # 1단계 소문자변환
    new_id = list(new_id.lower())
    tmp_id = new_id
    answer = []

    # 2단계 특수문자 제거
    for i in range(0, len(new_id)):
        if new_id[i].isdigit():
            answer.append(new_id[i])
        elif str(new_id[i]).isalpha():
            answer.append(new_id[i])
        elif new_id[i] in ["-", "_", "."]:
            answer.append(new_id[i])

    # 3단계
    answer = "".join(answer)
    for i in range(len(answer)):
        answer = str(answer).replace("...", ".")
        answer = str(answer).replace("..", ".")

    # 4단계
    answer = list(answer)
    if answer[0] == ".":
        answer.pop(0)
    elif answer[-1] == ".":
        answer.pop()

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer.pop()

    # 5단계
    if answer == []:
        answer.append("a")
    # 7단계
    if len(answer) == 2:
        answer.append(answer[-1])
    elif len(answer) == 1:
        answer.append(answer[-1])
        answer.append(answer[-1])

    answer = "".join(answer)
    return answer


import re


def solution(new_id):
    # 1단계 소문자변환
    new_id = new_id.lower()
    tmp_id = new_id
    answer = ''

    # 2단계 특수문자 제거
    for i in new_id:
        if i.isdigit():
            answer += i
        elif i.isalpha():
            answer += i
        elif i in ["-", "_", "."]:
            answer += i

    # 3단계
    for i in range(len(answer)):
        answer = str(answer).replace("...", ".")
        answer = str(answer).replace("..", ".")

    # 4단계
    if answer[0] == ".":
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == ".":
        answer = answer[:-1]

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 5단계
    if answer == '':
        answer += "a"
    # 7단계
    if len(answer) == 2:
        answer += answer[-1]
    elif len(answer) == 1:
        answer += answer[-1]
        answer += answer[-1]

    return answer