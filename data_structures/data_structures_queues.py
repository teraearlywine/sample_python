"""
QUEUE DATA STRUCTURE - FIRST IN FIRST OUT (FIFO)

Like stacks, we're going to practice creating a queue data structure.
The first item added is also the first item taken out. Basically it handles things one
at a time. Unlike a stack, where the first item put in is the last out, a queue is a 
first-in-first-out data structure. The first item added is also the first item taken out
"""


class DataQueue:
    """
    DataQueue
    =========
    QUEUE DATA STRUCTURE - FIRST IN FIRST OUT (FIFO)

    Note: The following method is not fast (because all of the other elements have to be shifted by one),
    the python documentation reccomends using collections, where inserts & pops are designed to be fast. 
    See data_types_lists.ipynb for implementation of a queue using collections

    The first item added is also the first item taken out. Basically it handles things one
    at a time. Unlike a stack, where the first item put in is the last out, a queue is a 
    first-in-first-out data structure. The first item added is also the first item taken out
    -----
    """
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        """
        .insert() items to the a given position in the list 
        If no position is specified, added to the top. ie. "first in" 
        """
        self.items.insert(0, data)
        
    def dequeue(self):
        """
        .remove() is a python method for removing the first item in a list
        For QUEUES, since they follow FIFO, we want to always remove the 'First' 
        of the top of the list
        """
        return self.items.remove()
        
        
