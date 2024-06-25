# Sequential Search and Search Algorithm

def sequential_search(number_list, target):
    """ 
    Basic sequential search algorithm. 
    Iterates over a numbered list looking to match the provided target number
    The variable matched is set to True if found, then the loop is stopped and the 
    boolean result is returned
    """
    
    matched = False
    for num in number_list: 
        if num == target: 
            matched = True 
            break
    return matched
    
if __name__ == "__main__":
    
    number_list = range(1, 101) # list of numbers 1 to 100
    s1 = sequential_search(number_list, target=20)
    print(s1) # Prints true
    
    s2 = sequential_search(number_list, target=200)
    print(s2) # Prints false
