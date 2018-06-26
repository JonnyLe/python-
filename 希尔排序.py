__author__ = 'Jonny'
__date__ = '2018.03.14'
__location__ = '西安'

'''给定序列实现希尔排序：slist = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]'''
'''插入排序的稳定性是不稳定的'''


def shell_sort(slist):
    length = len(slist)
    gap  = length // 2
    while gap > 0:
        print('gap =',gap)
        for j in range(gap,length):
            i = j
            while i >= gap  :
                if slist[i] > slist[i-gap]:
                    slist[i],slist[i-gap] = slist[i-gap],slist[i]
                i = i - gap
        gap = gap // 2
    return slist

if __name__ == '__main__':
    print(shell_sort(slist = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]))
