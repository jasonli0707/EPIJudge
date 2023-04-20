from list_node import ListNode


def append(L: ListNode, new_node: ListNode)->None:
    while L.next:
        L = L.next
    L.next = new_node

def insert_after(node: ListNode, new_node: ListNode)->None:
    new_node.next = node.next
    node.next = new_node

def delete_after(node: ListNode)->None:
    if node.next: # if not tail
        node.next = node.next.next  
        
def search_for(L: ListNode, key)->ListNode:
    while L and L.data == key: # while not None & key not match
        L = L.next
        
    return L # if key not present, will return None

if __name__ == "__main__":
    L1 = ListNode(data=0)
    L2 = ListNode(data=0)
    for i in range(1, 10):
        append(L1, ListNode(i))
        append(L2, ListNode(i))
    print(L1==L2)

    
