__author__ = 'Jonny'
__date__ = '2018.03.14'
__location__ = '西安'

'''给定序列实现归并排序：slist = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
归并排序的稳定性是稳定的
'''

def merge_sort(slist):
    if len(slist) <= 1:
        return slist

    mid = len(slist) // 2

    left_list = merge_sort(slist[:mid])
    right_list = merge_sort(slist[mid:])

    result_list = []
    left_flag,right_flag = 0,0

    while (left_flag < len(left_list)) and (right_flag < len(right_list)):
        if left_list[left_flag] < right_list[right_flag]:
            result_list.append(left_list[left_flag])
            left_flag += 1
        else:
            result_list.append(right_list[right_flag])
            right_flag += 1
    result_list +=left_list[left_flag:]
    result_list +=right_list[right_flag:]

    return result_list


if __name__ == '__main__':
    slist = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    print(merge_sort(slist))