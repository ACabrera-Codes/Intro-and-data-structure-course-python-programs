from random import randrange
import math  
from io import StringIO

class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.Size = 0

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.Size = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)
        while (i > 0):
            print(self.heapList, i)
            self.percDown(i)
            i = i - 1
        print(self.heapList,i)
                        
    def percDown(self,i):
        while (i * 2) <= self.Size:
            mc = self.minChild(i)
            print(mc) 
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.Size:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
               tmp = self.heapList[i // 2]
               self.heapList[i // 2] = self.heapList[i]
               self.heapList[i] = tmp
            i = i // 2
      
    def insert(self,k):
        self.heapList.append(k)
        self.Size = self.Size + 1
        self.percUp(self.Size)

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.Size]
        self.Size = self.Size - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
        
    def isEmpty(self):
        if self.Size == 0:  
            return True
        else:
            return False
        
    def printHeap(self):  
        print(self.heapList)

    def binaryHeapTree(self):
        tree = self.heapList
        total_width=30
        fill = ' '
        output = StringIO()
        last_row = -1
        for i, n in enumerate(tree[1:]): 
            if i:
                row = int(math.floor(math.log(i + 1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2 ** row
            col_width = int(math.floor(total_width / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print(output.getvalue())
        print()


def ListLen(listLength):
    list=[]
    i = 0
    for i in range(0, listLength):
        randomNum = randrange(1, 100)
        list.append(randomNum)
    
    return list


def main():
    randomIntList = ListLen(7)
      
    binaryHeap = BinaryHeap()
       
    for element in randomIntList:
        binaryHeap.insert(element)
        binaryHeap.printHeap()
        
    print("")
    
    print("Random list of integers: \n{0}".format(randomIntList))
    
    print("")
        
    print("Binary minimum heap list: ")
    binaryHeap.printHeap()
    
    print("")
    print("Binary minimum heap: ")
    
    binaryHeap.binaryHeapTree()
    

main()

    

