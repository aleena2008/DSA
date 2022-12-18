
# Insertion at beginning

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.visited = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, new_data):
        print("inserting {} in front".format(new_data))
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev, new_data):
        print("inserting {} ".format(new_data))
        if prev==None:
            return
        else:
            new_node = Node(new_data)
            new_node.next = prev.next
            prev.next = new_node

    def insert_end(self, new_data):
        print("inserting {} at end".format(new_data))
        new_node = Node(new_data)
        
        if self.head==None:
            self.head=new_node
            return
        
        temp = self.head
        while(temp.next):
            temp=temp.next
        temp.next = new_node

    def print_llist(self):
        print("printing llist")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print("\n")

    def delete_first(self):
        if self.head==None or self.head.next==None:
            return
        temp = self.head
        self.head = temp.next
        temp = None

    def delete_node_at_pos(self, position):
        print("deleting node at pos {}".format(position))
        if self.head==None or self.head.next==None:
            return

        prev = self.head
        while prev:
            if(position==2):
                temp=prev.next
                prev.next = temp.next
                temp=None
                
            position-=1
            prev=prev.next

    def delete_node_by_key(self, key):
        print("deleting node with key {}".format(key))
        if self.head==None:
            self.head=None
            return
            
        temp = self.head
        prev = None

        if temp.data==key:
            self.head = temp.next
            temp=None
            return

        while temp:
            if temp.data==key:
                prev.next = temp.next
                temp=None
            else:
                prev=temp
                temp=temp.next


    def search_llist(self, key):
        temp = self.head
        position=1

        while temp:
            if temp.data==key:
                print("{} present at position {}".format(key, position))
                return
            else:
                temp=temp.next
                position+=1

        print("{} not present".format(key))

    def length_llist(self):
        length = 0
        temp = self.head
        while temp:
            length+=1
            temp=temp.next
        print("length of llist is ", length)

    def reverse_llist(self):
        print("reversing")
        prev = None
        curr = self.head
        next = curr.next

        while curr.next:
            curr.next = prev
            prev = curr
            curr = next
            next = curr.next

        self.head = curr
        self.head.next = prev

        return self.head

def merge_sorted(llist1, llist2):
    print("merging")
    llist1.print_llist()
    llist2.print_llist()
    t1 = llist1.head
    t2 = llist2.head

    pointer = Node(None)
    dummy = pointer

    while t1 and t2:
        if t1.data<t2.data:
            pointer.next = t1
            t1=t1.next
            pointer = pointer.next
        else:
            pointer.next = t2
            t2=t2.next
            pointer = pointer.next
    
    if t1:
        pointer.next = t1
    else:
        pointer.next = t2

    llist1.head = dummy.next
    llist.print_llist()
    return llist.head

# Reverse a Linked List in groups of given size 


def reverse_sub(llist, hd, k):
    prev = None
    curr = hd
    next = curr.next
    count=0


    while curr.next and count<k:
        print(count)
        curr.next = prev
        prev = curr
        curr = next
        next = curr.next
        count+=1

    if curr.next:
        print("curr", curr.data)
        hd.next = reverse_sub(llist, curr, k)


    return prev


def reverse_group(llist, k):
    llist.print_llist()
    llist.head = reverse_sub(llist, llist.head, k)
    llist.print_llist()



def detect_remove_loop(llist):
    print("detect and remove loop")
    pntr = llist.head
    prev = None

    while pntr:
        print(pntr.data)
        if pntr.visited:
            print("Loop present")
            prev.next = None
            break
        prev = pntr    
        pntr.visited = 1
        pntr = pntr.next
    llist.print_llist()



llist = LinkedList()
llist.insert_beginning(8)
llist.insert_beginning(7)
llist.insert_beginning(6)
llist.insert_beginning(4)
# llist.insert_beginning(7)
# llist.insert_beginning(8)
# llist.insert_beginning(9)
# llist.insert_end(10)
# llist.insert_end(20)
# llist.delete_first()
# llist.insert_after(llist.head.next, 7)
llist.print_llist()

# llist.delete_node_at_pos(3)
# llist.print_llist()
# llist.delete_node_by_key(4)
# llist.print_llist()
# llist.search_llist(7)
# llist.length_llist()
# llist.print_llist()
lilist = LinkedList()
lilist.insert_beginning(11)
lilist.insert_beginning(5)
lilist.insert_beginning(1)
# lilist.print_llist()
# lilist.reverse_llist()
lilist.print_llist()

llist.head = merge_sorted(llist, lilist)
# reverse_group(llist, 3)
llist.insert_beginning(5)
llist.insert_beginning(5)
llist.insert_end(5)
reverse_group(llist, 3)        

llist = LinkedList()
llist.insert_beginning(10)
llist.insert_beginning(4)
llist.insert_beginning(15)
llist.insert_beginning(20)
llist.insert_beginning(50)

llist.head.next.next.next.next.next = llist.head.next.next
detect_remove_loop(llist)