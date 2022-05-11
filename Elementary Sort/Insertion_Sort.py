#Self programmed version of Insertion Sort
class InsertionSort:
#Sort Function @prams the list of items to be sorted
    def sort(self, listOfItems):
        length = len(listOfItems)
        for i in range(length):
            for j in range(i, 0, -1):
                if self.less(listOfItems[j], listOfItems[j-1]):
                    self.exchange(listOfItems, j, j-1)
                else:
                    break

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
            DataFrame("Karim", "01273091969", 2)]*n

    Insertion = InsertionSort()

    Insertion.sort(data)

    # for _ in data:
    #     print(_.name, _.phone, _.id)
    # print(Insertion.is_sorted(data))

# import time
# start_time = time.time()
# main()
# print(f"Insertion Sort takes\n--- {(time.time() - start_time)} seconds ---" )
