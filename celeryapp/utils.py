# this DSA we have implemented for order processing
'''
In the provided example, we have optimized the order processing workflow by introducing a queue data structure. Here's how the optimization works:

Efficient Order Processing:

By using a queue, we ensure that orders are processed in a first-in-first-out (FIFO) manner. When a new order is created (OrderList view), it is immediately added to the end of the queue (enqueue operation). This ensures that orders are processed in the order they are received, which is often a critical requirement in many applications.

Reduced Processing Time:

Using a queue allows us to efficiently manage the order processing workflow. When an order is created, it is added to the queue in constant time (O(1) complexity). Similarly, when an order is processed (ProcessOrder view), it is removed from the front of the queue (dequeue operation), also in constant time (O(1) complexity). This ensures that the overall processing time remains low and predictable, regardless of the number of orders in the system.

Improved Scalability:

By using a queue, we decouple the order creation and processing logic. This allows the system to scale more effectively, as it can handle a large number of orders without becoming overwhelmed. Orders are added to the queue as they arrive, and the processing logic can handle them at a pace that the system can sustain. This scalability is crucial for applications that experience fluctuations in order volume or need to handle bursts of orders during peak periods.

Overall, by integrating a queue data structure into the order processing workflow, we optimize the system for efficiency, reduced processing time, and improved scalability, resulting in a more robust and reliable application.
'''


# first-in-first-out (FIFO)
class Queue:
    def __init__(self):
        self.items = []
    
    # insert at the beginning of the list
    def insert(self,item):
        self.items.insert(0,item)
    
    def deque(self,item):
        if not self.is_empty():
            self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Each node key, value, prev, next
class ListNode:
    def __init__(self, key=None, value=None) :
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def remove_node(self,node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            if len(self.cache) == self.capacity:
                # Remove the least recently used node
                tail = self.tail.prev
                self._remove_node(tail)
                del self.cache[tail.key]

            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
