import logging 
import os
import pandas as pd
# from data_processing.data_processing import DataCollection
from data_processing import data_processing as data
from todoist_api_python.api import TodoistAPI


logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d", format="%(levelname)s - %(asctime)s - %(message)s")

# Authenticate API 
creds = os.getenv("TODOIST_API_KEY")
api = TodoistAPI(creds)

def get_active_projects():
    """ 
    Get a list of currently active todoist projects.

    Usage::

        >>>  get_active_projects()
    """
    try:
        projects = api.get_projects()
        data_collection = data.DataCollection() # Initialize data collector class
        for project in projects: 
            data_collection.add_record(project.__dict__)
        df = pd.DataFrame(data_collection.data)
        logging.info(f"Data extracted from API and successfully added to pandas dataframe")
        return df
    except Exception as error:
        logging.info(f"Houston we have a problem: {error}")

get_active_projects()