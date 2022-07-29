# it will serach the requested element by diving the array in to two equal halves
def sort_list(array_list):
    array_length =len(array_list)
    lowest = array_list[0]
    #highest = array_list[-1]
    for index in range (1,array_length - 1 ):
        if array_list[index] <= lowest :
            lowest =array_list[index]
            array_list[index -1] = lowest
            print(lowest)
            for j in range (index,array_length -1):
                continue

    return array_list









#def binary_search():
 #   return





array_list = [101,567,34,56,78,65,43]
print("Here is the Array_list: {0} ".format(array_list))
sorted_list = sort_list(array_list)
print("Soted array_list :{0} ".format(sorted_list))
#user_input = input("Enter no you want to search from the array_list ")
#search_element_index = binary_search(userinput,array)










