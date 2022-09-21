if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        l1 = []
        name = input()
        score = float(input())
        l1.append(name)
        l1.append(score)
        records.append(l1)
    l2 = []
    for i in records:
        l2.append(i[1])
    l2.sort()
    for item in l2:
        if item > l2[0]:
            break
    print(item)
    l3=[]

    for x in records:
        if x[1]== item:
            l3.append(x[0])

    l3.sort()
    for i in l3:
        print(i)
    #print(l2)
    #print("records {0}".format(records))
