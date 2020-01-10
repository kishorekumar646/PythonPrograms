class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,ele):
        node = Node(ele)
        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
    
    def insertFirst(self,ele):
        node = Node(ele)
        node.next = self.head
        self.head = node

    def dispalyList(self):
        current = self.head
        while current:
            print(current.data," ----> ",end="")
            current = current.next
        print("None")

lst = LinkedList()
print("1.Insert Data\t2.Display List\t3.Insert First Place\t4.Terminate")
b = True
while b:
    n = int(input("Enter your choice : "))
    if n == 1:
        num = int(input("Enter the number : "))
        lst.insert(num)
    elif n == 2:
        lst.dispalyList()
    elif n == 3:
        num = int(input("Enter the number : "))
        lst.insertFirst(num)
    elif n == 4:
        b = False
        print("\n  ------ END -----\n")
    else:
        print("Wrong Iput......try again")