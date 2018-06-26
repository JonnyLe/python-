__author__ = 'Jonny'
__date__ = '2018.03.14'
__location__ = '西安'

'''给定序列实现快速排序：slist = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
快速排序的稳定性是不稳定的
1. 不可变对象作为函数参数，相当于C系语言的值传递。
2. 可变对象作为函数参数，相当于C系语言的引用传递。
可变对象是（list,dict,set）不可变对象是（init,float,str,tuple）
'''

def fast_sort(slist,start,end):
    if start >= end:
        return
    low = start
    high = end
    mid_slist = slist[start]
    while low < high:
        while high > low and slist[high] >= mid_slist:
            high -= 1
        slist[low] = slist[high]
        while  high > low and  slist[low] < mid_slist:
            low += 1
        slist[high] = slist[low]
    slist[low] = mid_slist

    fast_sort(slist,start,low-1)
    fast_sort(slist,low+1,end)

if __name__ == '__main__':
    slist = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    fast_sort(slist, start=0, end=len(slist) - 1)
    print(slist)
