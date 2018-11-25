"""Helper methods for saving data"""
import pandas as pd
import helpers.helpers as helpers

def save_to_csv(df, name="test.csv", folder="/"):
    """Saves dataframe (df) to file (name) in (folder)"""

    base_folder = "data/saved_data"

    if not isinstance(df, pd.DataFrame):
        print("Error: {df.__str__} is not an instance of pd.DataFrame")
        return False
    
    if folder != "/":
        helpers.ensure_dir(f"{base_folder}{folder}")

    full_name = f"{base_folder}{folder}{name}"

    return df.to_csv(full_name, index=False)