import time

name = 'alcatraz'

print(list(reversed(name)))
print(''.join(list(reversed(name))))

lst= [1,2,3]
print(len(lst)//2)

print(sum(lst))
print(sum(lst,4))

print(round(3.1362,2))
print(round(3.1332666,4))

max_lst1 = [300, 20 ,-900]
max_lst2 = [10,11,12]
max_lst3 = [-5,-1-89]

def max_magnitude(lst):
     return abs(max(lst, key=lambda n: abs(n)))

print(max_magnitude(max_lst1))
print(max_magnitude(max_lst2))
print(max_magnitude(max_lst3))
print("--------")
print(list(abs(n) for n in max_lst1))
def max_magnitude(lst):
    return max(abs(n) for n in lst)
print(max_magnitude(max_lst1))
print(max_magnitude(max_lst2))
print(max_magnitude(max_lst3))

print("-------------------")

def sum_even_values(*args):
    return sum([n for n in list(args) if n%2==0])

start = time.time()
print(sum_even_values(1,2,3,4,5,6))
print(sum_even_values(4,2,1,10))
print(sum_even_values(1))
for n in range(10000):
    sum_even_values(1,2,3,4,5,6)
    sum_even_values(4,2,1,10)
    sum_even_values(1)
end = time.time()
print(end- start)

def sum_even_values(*args):
    return sum((n for n in list(args) if n%2==0))
start2 = time.time()
print(sum_even_values(1,2,3,4,5,6))
print(sum_even_values(4,2,1,10))
print(sum_even_values(1))
for n in range(10000):
    sum_even_values(1,2,3,4,5,6)
    sum_even_values(4,2,1,10)
    sum_even_values(1)
end2 = time.time()
print(end2- start2)

def sum_floats(*args):
    return sum(n for n in args if type(n) == float)

print(sum_floats(1,2.2,3,4))