a = [1,2,3,4]
dict = {1,2,3,4}

dict2 = {1 : 'g',2 : 'h', 3 : 'q', 5 : 'lk'}

dict2 = sorted(dict2.items(), key=lambda k:k[1] , reverse=True)

print(dict2)