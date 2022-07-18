
# def get_multiples(number=1, count=10):
#     next_num = number
#     for n in range(count, -1, -1):
#         yield next_num
#         next_num += number
    
def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num


gene = (num for num in range(1,10))
print(gene)
print(next(gene))
print(next(gene))
print(next(gene))

#  vs LIST

lst = [num for num in range(1,10)]

print(lst)