"""Helper functions for project"""

import datetime as dt
import os, sys

def get_date(date):
    return dt.datetime.fromtimestamp(date)

def ensure_dir(file_path):
    """Makes a directory for path if it doesn't already exist"""

    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        return os.makedirs(directory)