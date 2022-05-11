import random

class QuickSort:
#Sort Function @prams the list of items to be sorted
    def partitioning(self, listOfItems, low, high):
        i = (low-1)         # index of smaller element
        pivot = listOfItems[high]     # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if self.less(listOfItems[j],pivot):

                # increment index of smaller element
                i = i+1
                listOfItems[i], listOfItems[j] = listOfItems[j], listOfItems[i]

        listOfItems[i+1], listOfItems[high] = listOfItems[high], listOfItems[i+1]
        return (i+1)

    def shuffle(self, listOfItems):
        N = len(listOfItems)
        for i in range(N):
            r = int(random.uniform(i+1, N-1))
            self.exchange(listOfItems, i, r)

    def sort1(self, listOfItems):
        self.shuffle(listOfItems)
        self.sort(listOfItems, 0, len(listOfItems) - 1)

    def sort(self, listOfItems, lo, hi):
        if hi <= lo:
            return
        j = self.partitioning(listOfItems, lo, hi)
        self.sort(listOfItems, lo, j - 1)
        self.sort(listOfItems, j + 1, hi)

    def less(self, item1, item2):
        return item1.compareTo(item2) < 0



    def exchange(self, listOfItems, i, mini):
        swap = listOfItems[i]
        listOfItems[i] = listOfItems[mini]
        listOfItems[mini] = swap

    def is_sorted(self, listOfItems):
        length = len(listOfItems)
        for i in range(1, length):
            if self.less(listOfItems[i], listOfItems[i - 1]):
                return False
        return True
class DataFrame:
    def __init__(self, name, phone, id):
        self.name = name
        self.phone = phone
        self.id = id

    def compareTo(self, that):
        #Compare on names first
        if self.name < that.name: return -1
        if self.name > that.name: return 1
        #If equal, compare on phones second
        if self.phone < that.phone: return -1
        if self.phone > that.phone: return 1
        #If equal, compare on id last
        if self.id < that.id: return -1
        if self.id > that.id: return 1
        #if equal return 0
        return 0

def main(n):
    #An example to be sorted using the rules we put
    data = [DataFrame("Karim", "01173091969", 4),
            DataFrame("Nabil", "01273091968", 1),
            DataFrame("Atiaa", "01178031367", 3),
            DataFrame("Karim", "01273091969", 2)]*n
    QuickSort().sort1(data)

    # for _ in data:
    #     print(_.name, _.phone, _.id)
# main(1000)
import sys
print(sys.getrecursionlimit())
