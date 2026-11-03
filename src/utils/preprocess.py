import pandas as pd
from pathlib import Path

def read_raw(path: Path) ->pd.DataFrame:

    if not path.exists():
        raise FileExistsError("File does not exist!")

    return pd.read_csv(path,sep="|")    


#if "__name__"=="__init__":
