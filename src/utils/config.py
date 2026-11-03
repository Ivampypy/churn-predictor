import pathlib as pth

current_dir= pth.Path(__file__).resolve().parent


project_root = current_dir.parent.parent
raw_data=project_root/'data'/'raw'/'WA_Fn-UseC_-Telco-Customer-Churn.csv'

