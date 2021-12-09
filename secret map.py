#-*- coding: utf-8 -*-
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

# array , commands[i,j,k]
def solution (array , commands):
    for array in commands


def function ():
    l = list(range(1,11))
    m = list(map(lambda n:n*n,  l))
    print(m)
    dic = {'cat' :[10 , 9]}
    dam = {'tiger':[1,3]}
    dic['lion'] = [1,2]
    ##print(dic.values())
    dic.update(dam)

    print(dic)


function()