def sum(a, b, *p):
    s = a + b
    for i in p:
        s = s + i
    return s
print(sum(1,2))
print(sum(1,2,3))
print(sum(1,2,3,4,5,6,))