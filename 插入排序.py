__author__ = 'Jonny'
__date__ = '2018.03.14'
__location__ = '西安'

'''给定序列实现插入排序：slist = [2,3,2,5,1,6,4,3,2,6,7,45]'''
'''插入排序的稳定性是稳定的'''


def insert_sort(slist):
    length = len(slist)
    for j in range(1,length):
        for i in range(j,0,-1):
            if slist[i] > slist[i-1]:
                slist[i],slist[i-1] = slist[i-1],slist[i]
    return slist

if __name__ =='__main__':
    print(insert_sort(slist = [2,3,2,5,1,6,4,3,2,6,7,45]))