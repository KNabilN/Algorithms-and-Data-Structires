#Self programmed version of Shell Sort
class ShellSort:
#Sort Function @prams the list of items to be sorted
    def sort(self, listOfItems):
        length = len(listOfItems)
        h = 1
        while h < length//3: h = 3 * h + 1
        while h >= 1:
            for i in range(h, length):
                for j in range(i, 0, -h):
                    if j >= h and self.less(listOfItems[j], listOfItems[j-h]):
                        self.exchange(listOfItems, j, j-h)
                    else:
                        break
            h //= 3

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

    Shell_Sort = ShellSort()
    Shell_Sort.sort(data)

    # for _ in data:
    #     print(_.name, _.phone, _.id)
    # print(Shell_Sort.is_sorted(data))

# import time
# start_time = time.time()
# main(100)
# print(f"Insertion Sort took\n--- {(time.time() - start_time)} seconds ---" )
