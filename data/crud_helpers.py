"""Helper methods for saving data"""
import os
import pandas as pd
import helpers.helpers as helpers

def pickle_df(df, name="test.pkl", folder="/"):
    """Pickles dataframe (df) to file (name) in (folder)"""

    base_folder = "data/saved_data"

    if not isinstance(df, pd.DataFrame):
        print("Error: {df.__str__} is not an instance of pd.DataFrame")
        return False
    
    if folder != "/":
        helpers.ensure_dir(f"{base_folder}{folder}")

    full_name = f"{base_folder}{folder}{name}"

    return df.to_pickle(path=full_name, compression="gzip", protocol=4)

def unpickle_df(file_path):
    """Unpickles dataframe from file (file_path)"""

    return pd.read_pickle(path=file_path, compression="gzip")

def delete_pickle(file_path):
    """Deletes a specific pickle file"""

    try:
        os.remove(file_path)
    except OSError as error:
        print(f"Cannot remove {file_path}, looks like it's a directory!\n{error}")
        return False
    else:
        return True

def update_pickle():
    """Find best way to merge DF objects if needed"""
    pass