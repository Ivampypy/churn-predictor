import pandas as pd
from pathlib import Path
from src.utils.config import raw_data

def read_raw(path: Path = raw_data) ->pd.DataFrame:

    if not path.exists():
        raise FileExistsError("File does not exist!")

    return pd.read_csv(path,sep=",")    



if "__name__"=="__init__":
    dataset=read_raw()