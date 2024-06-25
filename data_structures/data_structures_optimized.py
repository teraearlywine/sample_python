# https://docs.python.org/3/library/collections.html#collections.deque
# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues

from collections import deque


# Used AI to generate a list of 20 beers to practice iterating over
beers = [ 
    "Heineken", "Guinness", "Corona Extra", "Budweiser", "Stella Artois", "Blue Moon", 
    "Sierra Nevada Pale Ale", "Samuel Adams Boston Lager",
    "Coors Light", "Pabst Blue Ribbon", "Miller Lite", "New Belgium Fat Tire", 
    "Dos Equis", "Modelo Especial", "Beck's", "Hoegaarden", 
    "Lagunitas IPA", "Peroni", "Amstel Light", "Carlsberg"
]

queue = deque(beers)

queue.append("Hoffbrau")        # New beer is added to the list 
queue.append("Hen House IPA")   # Another new beer is added to the list

queue.popleft()                 # First beer in the list is removed
queue.popleft()                 # Second beer in the list is removed
sorted_queue = sorted(queue)    # Sort & assigned new variable

print(sorted_queue)             # Return results, you can see new beers added.

# Check to see if new queue is still 20 beers
assert len(sorted_queue) == len(queue), "New list must equal original list length" 
