class BottomUpMergeSort:
#Sort Function @prams the list of items to be sorted
    def sort1(self, listOfItems):
        N = len(listOfItems)
        aux = [0] * N

        sz = 1
        while sz < N:
            lo = 0
            while lo < N - sz:
                self.merge(listOfItems, aux, lo, lo + sz - 1, min(lo + 2 * sz - 1, N - 1))
                lo += sz + sz
            sz *= 2

    def merge(self, listOfItems, aux, lo, mid, hi):
        for _ in range(lo, hi+1):
            aux[_] = listOfItems[_]
        k = lo
        i = lo
        j = mid + 1

        while k <= hi:
            if i > mid:
                listOfItems[k] = aux[j]
                j+=1
            elif j > hi:
                listOfItems[k] = aux[i]
                i+=1
            elif self.less(aux[j], aux[i]):
                listOfItems[k] = aux[j]
                j +=1
            else:
                listOfItems[k] = aux[i]
                i+=1
            k+=1

    def less(self, item1, item2):
        try:
            return item1.compareTo(item2) < 0
        except:
            return item1 < item2


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
            DataFrame("Karim", "01273091969", 2),
            DataFrame("Aby", "01273091969", 2)]*n
    BottomUpMergeSort().sort1(data)
    for _ in data:
        print(_.name, _.phone, _.id)

main(1)
