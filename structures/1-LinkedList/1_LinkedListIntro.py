# Simple implementation of a linked lists starts from creating a Node like this
class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
        
node1 = Node(4); # It stores the value 4
node2 = Node(5);
node3 = Node(18);

# Linking process
node1.next = node2;
node2.next = node3;

# Loop through the Linked list
currentNode = node1
while currentNode:
    print(currentNode.data, end=' -> ');
    currentNode = currentNode.next;
    
print('null');
    
        