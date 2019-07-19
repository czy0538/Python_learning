#_iter_():返回迭代器对象本身
#_next_():返回容器的下一个元素
#iter(迭代对象) 迭代器使用、
lst=[1,2,3,4,5]
it=iter(lst)
try:
    while True:
        val=it.__next__()
        print(val)
except StopIteration:
    print("over")
#
# 生成器
# fibonacci
def fibonacci():
    i=0
    a,b=0,1
    while True:
        yield (b)
        a,b=b,a+b

def main():
    for num in fibonacci():
        if num>100:
            break
        print(num,end=" ")
main()