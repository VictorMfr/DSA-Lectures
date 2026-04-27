class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
        
def traverseList(head):
    currentNode = head;
    while currentNode:
        print(currentNode.data, end=' -> ');
        currentNode = currentNode.next;
    print('null');
    
def insertNodeAtPosition(head, newNode, position):
    
    # If it's at position 1, then just add next to it returning the newNode as the new head
    if position == 1:
        newNode.next = head
        return newNode
    
    currentNode = head;
    
    # position yourself at two nodes before the position you want to add the new node
    for _ in range(position - 2):
        
        # Stop if the traversal is broken
        if currentNode.next is None:
            break
        
        # Keep traversing until the loop ends
        currentNode = currentNode.next
    
    # currentNode is now at 2 nodes before the target
    # Node -> Node -> Node (currentNode) -> Node -> Node (Target) -> Node
    
    # Node -> Node -> Node (currentNode) -> Node (newNode.next) -> Node (Target) -> Node
    newNode.next = currentNode.next
    
    # 
    currentNode.next = newNode
    
    return head
    
        
# Creating the list
node1 = Node(1);
node2 = Node(5);
node3 = Node(8);
node4 = Node(18);

# Linking
node1.next = node2;
node2.next = node3;
node3.next = node4;

# Operations

newNode = Node(2)
node1 = insertNodeAtPosition(node1, newNode, 1);

traverseList(node1);