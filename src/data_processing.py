
# Use data collection class to process data
class DataCollection: 
    """ 
    Data Collection Class
    ---------------------

    This class uses add_record(record) method to 
    store data in a list whenever the class is initialized. 

    This enables reuse and streamlined iteration.

    Usage:::

    >>> projects = api.get_projects()
    >>> data_collection = DataCollection() # Initialize appending records to list
    >>> for project in projects: 
            data_collection.add_record(project.__dict__)
    >>> df = pd.DataFrame(data_collection.data) # Use the class attribute to create pandas dataframe
    """
    def __init__(self): 
        self.data = []

    def add_record(self, record):
        self.data.append(record)


if __name__ == "__main__":
    DataCollection()