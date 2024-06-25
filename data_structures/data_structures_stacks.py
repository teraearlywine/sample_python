"""
STACK DATA STRUCTURE - LAST IN FIRST OUT (LIFO)

Practicing creating the Stack data structure type
A stack is a kind of data structure that's similar to a list,
except that you can only operate on the last item in the stack.
"""


class DataStack:

    def __init__(self):
        self.records = []

    def add_record(self, data):
        """
        Pushes data to records stack.
        """

        self.records.append(data)

    def remove_record(self):
        """
        Removes the last record from records stack.
        """

        return self.records.pop()


"""
Next we're going to reverse a string using DataStack to mimic 
a common interview question. 
"""

if __name__ == "__main__":
    data_stack = DataStack()

    # Adds each char to the records attribute
    sample_str = "Hello Tera"
    for i in sample_str:
        data_stack.add_record(i)


    reverse = ""

    for i in range(len(data_stack.records)):
        # the += is like append for strings,
        # Iterate over each index string character and remove it
        reverse += data_stack.remove_record()

    print(reverse)
