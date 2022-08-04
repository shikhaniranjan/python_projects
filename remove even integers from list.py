'''
Program to Remove even integers from list
owner: Shikha Niranjan
email-id :shikha.niranjan91@gmail.com
'''


def remove_even(user_list):
    """

    :param user_list: original list given by user
    :return: it will return list which has only odd numbers
    """
    for tup in enumerate(user_list):
        li = list(tup)
        if int(li[1] % 2) == 0:
            user_list.pop(li[0])

    return user_list



n = int(input("Enter the no of element you want to add in list : "))
user_list = []
for i in range(0,n):
    element = int(input())
    user_list.append(element)
print("Printing original user_list {0}".format(user_list))
odd_user_list = remove_even(user_list)
print("Printing new list which has only odd integers {0}".format(odd_user_list))


