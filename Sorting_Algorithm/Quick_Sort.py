class QuickSort():
    def partition(self,l,low,high):
        i= -1
        piv = l[high]
        for j in range(0, high):
            if l[j] < piv:
                i += 1
                # swap
                temp = l[j]
                l[j] = l[i]
                l[i] = temp
        i += 1
        # swap last
        temp = l[i]
        l[i] = l[high]
        l[high] = temp

        return i
    def quick_sort(self,l,low,high):
        if low <high:
            piv_index = self.partition(l,low,high)
            self.quick_sort(l,low,piv_index-1)
            self.quick_sort(l,piv_index+1,high)
        return l


l = [6,9,10,2,8,2.12 , -7]
QS = QuickSort()
n =len(l)
sorted_list = QS.quick_sort(l,0,n-1)
print(sorted_list)
