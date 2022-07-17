def calculation(a, b):
    return a+b,a-b

def tupleTostr(tup):
    return ', '.join([str(n) for n in res])
res = calculation(40, 10)
print(tupleTostr(res))