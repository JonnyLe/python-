__author__ = 'Jonny'
__date__ = '2018.03.14'
__location__ = '西安'

'''给定序列实现选择排序：slist = [2,3,2,5,1,6,4,3,2,6,7,45]'''
'''选择排序的稳定性是不稳定的'''


def select_sort(slist):
    length = len(slist)
    for j in range(0,length-2):
        min = j
        for i in range(j+1,length-1):
            if slist[min] > slist[i]:
                min = i
        slist[min],slist[j] = slist[j],slist[min]
    return slist

if __name__ == '__main__':
    print(select_sort(slist = [2,3,2,5,1,6,4,3,2,6,7,45]))
