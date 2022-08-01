'''
This prpgram will sort the list first and then return the index of element u want to search in the list
'''
def sort_list(array_list):
    '''
    #Sort the list using insertion sort algorithm
    :param array_list: list
    :return: sorted list
    '''
    array_length =len(array_list)
    for i in range (1,array_length):
        key = array_list[i]
        j=i -1
        x=0
        while j>=0 and  key < array_list[j]:
            x=array_list[j]
            array_list[j]=key
            array_list[j+1]=x
            j-=1

    return array_list


def binary_search(array_list,x,low,high):
    '''

    :param array_list: list
    :param x: element which u want to search in the list
    :param low: lowest index in list
    :param high: highest index in list
    :return:it will return the index of element u want to search in the list
    '''
    sorted_list = sort_list(array_list)
    #from pdb import set_trace
    #set_trace()
    mid = int((low+high)/2)
    if x == array_list[mid]:
        return mid
    elif  x < array_list[mid]:
        return binary_search(array_list,x,low,mid -1)
    else:
        return binary_search(array_list,x,mid+1,high)

array_list = []
n = int(input("Enter the no. of element you want to add in the list: "))
for i in range(0,n):
    element =int(input("enter the {0} element:\n".format(i)))
    array_list.append(element)
print("Here is the Array_list: {0} ".format(array_list))
sorted_list = sort_list(array_list)
print("Soted array_list :{0} ".format(sorted_list))
element = int(input("Enter the no. you want to search "))
low = 0
high =len(array_list)-1
search_element_index = binary_search(array_list,element,low,high)
print("{0} is at index {1}".format(element,search_element_index))












