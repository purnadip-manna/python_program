a = [12, 'ab', 34, 'cd', 34]
b = []
b = list(filter(lambda x : True if type(x) is str else False, a))
print(b)
