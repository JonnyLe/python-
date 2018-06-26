__author__ = 'Jonny'
__date__ = '2018.03.14'
__location__ = '西安'
#利用python实现冒泡排序

'''冒泡排序的稳定是是稳定的'''

def maoPaoSort(list):
    n = len(list)
    for j in  range(0,n-1):#注意和负数下标作区别
        for  i in range(0,n-1-j):
            if list[i]>list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
    return list


if __name__ =='__main__':
    list = [1, 4, 2, 5, 3, 2, 5, 2, 7, 34, 23, 12, 43]
    print(list)
    list = maoPaoSort(list)
    print(list)