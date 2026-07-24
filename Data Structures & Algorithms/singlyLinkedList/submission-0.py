class LinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.value
            
            curr = curr.next
            i+=1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = LinkedList.Node(val)
        new_node.next = self.head

        self.head = new_node


       
    def insertTail(self, val: int) -> None:
        new_node = LinkedList.Node(val)

        if self.head == None:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new_node
        

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        curr = self.head
        i=0

        while curr and curr.next:
            if i + 1 == index:
                curr.next = curr.next.next
                return True

            curr = curr.next
            i+=1
        return False

    def getValues(self) -> List[int]:
        vals = []
        
        curr = self.head

        while curr:
            vals.append(curr.value)
            curr=curr.next

        return vals
